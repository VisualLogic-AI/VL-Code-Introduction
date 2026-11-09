import json, os, subprocess, asyncio, numpy as np, soundfile as sf, edge_tts
S = json.load(open("script.json")); SR=24000; GAP=0.5; SEGGAP=1.1; LEAD=0.8
os.makedirs("audio", exist_ok=True)
PROXY=os.environ["HTTPS_PROXY"]
async def tts(text, path):
    for i in range(4):
        try:
            await edge_tts.Communicate(text, "en-US-AndrewNeural", rate="+30%", proxy=PROXY).save(path); return
        except Exception as e: print("retry", e); await asyncio.sleep(2**i)
    raise SystemExit("tts failed")
def load(mp3):
    raw=subprocess.run(["ffmpeg","-v","error","-i",mp3,"-f","f32le","-ac","1","-ar",str(SR),"-"],capture_output=True,check=True).stdout
    a=np.frombuffer(raw,dtype=np.float32)
    nz=np.where(np.abs(a)>0.01)[0]; return a[max(0,nz[0]-240):nz[-1]+480] if len(nz) else a
full=[np.zeros(int(LEAD*SR),np.float32)]; t=LEAD
for si,seg in enumerate(S):
    seg["start"]=t-(LEAD if si==0 else SEGGAP/2)
    for li,l in enumerate(seg["lines"]):
        p=f"audio/{seg['id']}_{li}.mp3"
        if not os.path.exists(p): asyncio.run(tts(l["t"],p))
        a=load(p); l["start"]=t; l["end"]=t+len(a)/SR; full.append(a); t=l["end"]
        g=GAP if li<len(seg["lines"])-1 else SEGGAP; full.append(np.zeros(int(g*SR),np.float32)); t+=g
    seg["end"]=t-(SEGGAP/2 if si<len(S)-1 else 0)
full.append(np.zeros(SR,np.float32)); t+=1; S[-1]["end"]=t
audio=np.concatenate(full); sf.write("narration.wav",audio,SR)
fps=25; env=[float(np.sqrt(np.mean(audio[int(i/fps*SR):int((i+1)/fps*SR)]**2) or 0)) for i in range(int(len(audio)/SR*fps)+1)]
json.dump(env,open("envelope.json","w")); json.dump(S,open("timeline.json","w"),indent=1)
def ts(x): return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int((x%1)*1000):03d}"
with open("subs.srt","w") as f:
    i=1
    for seg in S:
        for l in seg["lines"]: f.write(f"{i}\n{ts(l['start'])} --> {ts(l['end'])}\n{l.get('sub',l['t'])}\n\n"); i+=1
print("total",round(t,1)); [print(s["id"],round(s["start"],1),round(s["end"],1)) for s in S]
