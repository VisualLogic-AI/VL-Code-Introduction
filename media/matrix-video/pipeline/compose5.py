import json, subprocess, os
TL = json.load(open('timeline.json')); run = lambda a: subprocess.run(a, check=True)
FPS = 25; X264 = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p']
recs = {n: json.load(open(f'rec/{n}.json')) for n in ['prod1'] if os.path.exists(f'rec/{n}.json')}
P2 = json.load(open('rec/prod2.json')) if os.path.exists('rec/prod2.json') else None
HZ = json.load(open('rec/huzhou.json')) if os.path.exists('rec/huzhou.json') else None
HZ_PLAN = {'open': ('open', 'map'), 'map': ('map', 'code'), 'code': ('code', 'end')}
GEN = json.load(open('rec/gen.json')) if os.path.exists('rec/gen.json') else None
GEN_PLAN = {'open': ('open', 'workflow_selected'), 'request': ('workflow_selected', 'sent'), 'run1': ('sent', 'sent+40'), 'run2': ('sent+40', 'after_run'), 'preview': ('after_run', 'end')}
TOUR = json.load(open('rec/tour.json')) if os.path.exists('rec/tour.json') else None
FLOW = json.load(open('rec/flow.json')) if os.path.exists('rec/flow.json') else None
APPS = json.load(open('rec/apps.json')) if os.path.exists('rec/apps.json') else None
def apps_plan(M):
    navs = sorted([k for k in M if k.startswith('well_nav_')])
    det = 'well_detail' if 'well_detail' in M else (navs[len(navs) // 2] if navs else 'end')
    return {'dash': ('dash_open', 'dash_end'), 'login': ('well_open', 'well_home'), 'admin': ('well_home', det), 'detail': (det, 'end')}
FLOW_PLAN = {'open': ('open', 'sharded'), 'sharded': ('sharded', 'parallel'), 'parallel': ('parallel', 'enterprise'), 'enterprise': ('enterprise', 'mdcheck'),
             'mdcheck': ('mdcheck', 'run'), 'run': ('run-6', 'run_end+2'), 'report': ('run_end+2', 'end')}
def tour_plan(M):
    n = int(M.get('sections', 1) or 1); has_vs = 'service_code' in M
    after_first = 'code_1' if n > 1 else ('service_code' if has_vs else 'er')
    pages_end = 'service_code' if has_vs else 'er'
    return {'launch': ('launch', 'map'), 'map': ('map', 'code_0'), 'code': ('code_0', 'preview_0'), 'preview': ('preview_0', 'visual_0'),
            'visual': ('visual_0', 'logic_0'), 'logic': ('logic_0', after_first),
            'pages': ('code_1', pages_end) if n > 1 else ('preview_0', 'logic_0'),
            'service': ('service_code', 'er') if has_vs else ('er', 'theme'),
            'er': ('er', 'flow'), 'flow': ('flow', 'end')}
def marks_clip(seg, i, M, PLANX, video):
    out = []
    for k, l in enumerate(seg['lines']):
        ldur = (seg['lines'][k + 1]['start'] if k + 1 < len(seg['lines']) else seg['end']) - (seg['start'] if k == 0 else l['start'])
        a, b = PLANX[l['act']]; ws, we = mk(M, a), mk(M, b); win = max(we - ws, 1.0)
        speed = max(1.0, win / ldur); badge = None if speed < 1.5 else f'{speed:.0f}x' if speed >= 3 else f'{speed:.1f}x'
        o = f'parts/p{i:02d}_{k}.mp4'; clip(video, ws, ldur, o, speed=speed, badge=badge); out.append(o)
        print(seg['rec'], l['act'], f'win {win:.1f}s -> {ldur:.1f}s speed {speed:.1f}')
    return out
os.makedirs('parts', exist_ok=True)
SCALE = 'scale=1920:1080:flags=lanczos'

def clip(src, ss, dur, out, speed=1.0, badge=None):
    vf = [SCALE, f'fps={FPS}']
    if speed != 1.0: vf.insert(0, f'setpts=PTS/{speed}')
    if badge:
        vf.append(f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='{badge}':fontsize=40:fontcolor=white:box=1:boxcolor=0xf5a524@0.9:boxborderw=14:x=w-tw-60:y=60")
    vf.append(f'tpad=stop_mode=clone:stop_duration={dur:.3f}')
    vf.append('format=yuv420p')
    run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{ss:.3f}', '-i', src, '-t', f'{dur * speed:.3f}', '-vf', ','.join(vf), '-t', f'{dur:.3f}', *X264, out])

# live-task clip plan: narration line act -> (start mark, end mark). Window is fitted to the line's duration;
# if the window is longer than the line, it is played faster and labelled.
PLAN = {'select': ('start', 'selected'), 'goal': ('selected', 'goal_typed'), 'start': ('configured', 'sent+6'),
        'watch1': ('sent+6', 'worker_assigned+10'), 'watch2': ('worker_assigned+10', 'mid'), 'watch3': ('mid', 'terminal-5'),
        'done': ('terminal-5', 'end')}
def mk(m, key):
    if '+' in key: k, d = key.split('+'); return m[k] + float(d)
    if '-' in key and not key.startswith('-'): k, d = key.split('-'); return m[k] - float(d)
    return m[key]

parts = []
for i, seg in enumerate(TL):
    dur = seg['end'] - seg['start']
    if seg['type'] == 'slide':
        with open('l.txt', 'w') as f:
            for k, l in enumerate(seg['lines']):
                a = seg['start'] if k == 0 else l['start']; b = seg['end'] if k == len(seg['lines']) - 1 else seg['lines'][k + 1]['start']
                f.write(f"file 'slides/{seg['id']}_{k}.png'\nduration {b - a:.3f}\n")
            f.write(f"file 'slides/{seg['id']}_{len(seg['lines']) - 1}.png'\n")
        out = f'parts/p{i:02d}.mp4'; run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-i', 'l.txt', '-vf', f'fps={FPS},format=yuv420p', '-t', f'{dur:.3f}', *X264, out]); parts.append(out)
    elif seg['rec'] in recs:
        m = recs[seg['rec']]; ss = m['lead']; out = f'parts/p{i:02d}.mp4'; clip(m['video'], ss, dur, out); parts.append(out)
    elif seg['rec'] == 'gen' and GEN:
        parts += marks_clip(seg, i, dict(GEN['marks']), GEN_PLAN, GEN['video'])
    elif seg['rec'] == 'flow' and FLOW:
        parts += marks_clip(seg, i, dict(FLOW['marks']), FLOW_PLAN, FLOW['video'])
    elif seg['rec'] == 'apps' and APPS:
        parts += marks_clip(seg, i, dict(APPS['marks']), apps_plan(APPS['marks']), APPS['video'])
    elif seg['rec'] == 'vlc' and TOUR:
        parts += marks_clip(seg, i, dict(TOUR['marks']), tour_plan(TOUR['marks']), TOUR['video'])
    elif seg['rec'] == 'huzhou' and HZ:
        m = dict(HZ['marks'])
        for k, l in enumerate(seg['lines']):
            ldur = (seg['lines'][k + 1]['start'] if k + 1 < len(seg['lines']) else seg['end']) - (seg['start'] if k == 0 else l['start'])
            a, b = HZ_PLAN[l['act']]; ws, we = mk(m, a), mk(m, b); win = max(we - ws, 1.0)
            speed = max(1.0, win / ldur); badge = None if speed < 1.5 else f'{speed:.0f}x' if speed >= 3 else f'{speed:.1f}x'
            out = f'parts/p{i:02d}_{k}.mp4'; clip(HZ['video'], ws, ldur, out, speed=speed, badge=badge); parts.append(out)
            print('huzhou', l['act'], f'win {win:.1f}s -> {ldur:.1f}s speed {speed:.1f}')
    elif seg['rec'] == 'prod2' and P2:
        m = dict(P2['marks']); m['mid'] = (m['worker_assigned'] + 10 + m['terminal'] - 5) / 2 if 'worker_assigned' in m and 'terminal' in m else m.get('end', 0) / 2
        for k, l in enumerate(seg['lines']):
            ldur = (seg['lines'][k + 1]['start'] if k + 1 < len(seg['lines']) else seg['end']) - (seg['start'] if k == 0 else l['start'])
            a, b = PLAN[l['act']]; ws, we = mk(m, a), mk(m, b); win = max(we - ws, 1.0)
            speed = max(1.0, win / ldur); badge = None if speed < 1.5 else f'{speed:.0f}x' if speed >= 3 else f'{speed:.1f}x'
            out = f'parts/p{i:02d}_{k}.mp4'; clip(P2['video'], ws, ldur, out, speed=speed, badge=badge); parts.append(out)
            print('prod2', l['act'], f'win {win:.1f}s -> {ldur:.1f}s speed {speed:.1f}')
    else:
        out = f'parts/p{i:02d}.mp4'; run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'color=c=0x0b0f17:s=1920x1080:r={FPS}', '-t', f'{dur:.3f}', *X264, out]); parts.append(out)
open('parts.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-i', 'parts.txt', '-c', 'copy', 'bg.mp4'])
def at(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1920", "PlayResY: 1080", "WrapStyle: 0", "", "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Sub,DejaVu Sans,38,&H00FFFFFF,&H00FFFFFF,&H78000000,&H78000000,1,0,0,0,100,100,0,0,3,12,0,2,160,160,46,1", "", "[Events]",
       "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for s in TL:
    for l in s['lines']: ass.append(f"Dialogue: 0,{at(l['start'])},{at(l['end'])},Sub,,0,0,0,,{l.get('sub', l['t'])}")
open('subs.ass', 'w').write('\n'.join(ass) + '\n')
run(['ffmpeg', '-v', 'error', '-y', '-i', 'bg.mp4', '-i', 'narration.wav', '-filter_complex', "[0:v]ass=subs.ass[v]", '-map', '[v]', '-map', '1:a',
     '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', 'Matrix-Intro-EN-v5.mp4'])
print('ok')
