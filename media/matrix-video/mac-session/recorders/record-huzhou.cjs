// Records the Huzhou "教师发展数据看板" VL app (app-projects/huzhou/大屏应用复刻/06-vl)
// opened in VLCode (VL 4.3.0 editor) on this Mac: source → VL preview → interactions.
// Runs locally; only the resulting video leaves this machine. No secrets on screen:
// the project is aggregate statistics only (HuzhouTeachers.vdb has no person rows).
const path = require('path'); const fs = require('fs');
const PW = process.env.PW_DIR; // playwright package dir in the VLCode worktree
const { chromium } = require(PW);
const URL = process.env.VLC_URL || 'http://127.0.0.1:4123';
const OUT = process.env.OUT || path.join(__dirname, 'huzhou');
const cursorInit = () => { addEventListener('DOMContentLoaded', () => { const c = document.createElement('div');
  c.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24"><path d="M3 2l7 19 2.5-7.5L20 11z" fill="#fff" stroke="#000" stroke-width="1.4"/></svg>';
  Object.assign(c.style, { position: 'fixed', left: '0', top: '0', zIndex: 2147483647, pointerEvents: 'none', transform: 'translate(-50px,-50px)' }); document.documentElement.appendChild(c);
  addEventListener('mousemove', e => c.style.transform = `translate(${e.clientX - 3}px,${e.clientY - 2}px)`, true);
  addEventListener('mousedown', e => { const r = document.createElement('div'); Object.assign(r.style, { position: 'fixed', left: e.clientX - 22 + 'px', top: e.clientY - 22 + 'px', width: '44px', height: '44px', borderRadius: '50%', border: '3px solid #f5a524', zIndex: 2147483646, pointerEvents: 'none', transition: 'all .5s ease-out' }); document.documentElement.appendChild(r); requestAnimationFrame(() => { r.style.transform = 'scale(1.8)'; r.style.opacity = '0' }); setTimeout(() => r.remove(), 600) }, true); }); };
(async () => {
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(process.env.CHROME_BIN ? { executablePath: process.env.CHROME_BIN } : {}); const ctx = await b.newContext({ viewport: { width: 1600, height: 900 }, recordVideo: { dir: OUT, size: { width: 1600, height: 900 } } });
  await ctx.addInitScript(cursorInit); const p = await ctx.newPage(); const t0 = Date.now(); const marks = {}; const mark = k => { marks[k] = (Date.now() - t0) / 1000; console.log('MARK', k, marks[k].toFixed(1)); };
  let mx = 800, my = 450;
  const move = async (x, y, ms = 700) => { const n = Math.max(8, Math.round(ms / 16)); for (let i = 1; i <= n; i++) { const k = i / n, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; await p.mouse.move(mx + (x - mx) * e, my + (y - my) * e); await p.waitForTimeout(ms / n * .5) } mx = x; my = y };
  const to = async (loc, ms) => { await loc.waitFor({ state: 'visible', timeout: 15000 }); const bb = await loc.boundingBox(); await move(bb.x + bb.width / 2, bb.y + Math.min(bb.height / 2, 20), ms); return bb };
  const click = async (loc, ms) => { await to(loc, ms); await p.waitForTimeout(150); await loc.click({ timeout: 5000 }).catch(async () => { await p.mouse.down(); await p.mouse.up() }) };
  const wheel = async (dy, steps = 30) => { for (let i = 0; i < steps; i++) { await p.mouse.wheel(0, dy / steps); await p.waitForTimeout(30) } };
  const tab = n => p.locator('.mode-tab', { hasText: new RegExp(`^\\s*${n}\\s*$`) }).locator('visible=true').first();
  const file = n => p.getByText(n, { exact: true }).locator('visible=true').first();
  const dismiss = () => p.locator('#statusDismissBtn').click({ timeout: 800 }).catch(() => {});
  const chatOff = async () => { const bb = await p.locator('#chatPanel').boundingBox().catch(() => null); if (bb && bb.width > 300) await p.locator('.chat-collapse-btn:visible').first().click({ timeout: 4000 }).catch(() => {}); };
  await p.goto(URL, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(6000);
  await p.getByText('Maybe Later', { exact: true }).first().click({ timeout: 3000 }).catch(() => {}); await dismiss(); await chatOff(); mark('open');
  await p.screenshot({ path: path.join(OUT, '01-workbench.png') });
  // project map
  await click(tab('Map'), 700); await p.waitForTimeout(2500); await dismiss(); await move(700, 300, 900); await move(1000, 420, 900); mark('map'); await p.screenshot({ path: path.join(OUT, '02-map.png') });
  // VL source of the dashboard section
  await click(file('DashboardMain.sc'), 700); await p.waitForTimeout(900); await click(tab('Code'), 500); await p.waitForTimeout(1200); await dismiss(); await move(800, 500, 500); await wheel(1200, 60); mark('code'); await p.screenshot({ path: path.join(OUT, '03-code.png') });
  // preview = the VL app rendered by the VLCode preview runtime
  await click(tab('Preview'), 600); await p.waitForTimeout(6000); await dismiss(); mark('preview'); await p.screenshot({ path: path.join(OUT, '04-preview.png') });
  // interact: hover/scroll through the modules; click anything clickable in the preview frame
  const frame = p.frames().find(f => f !== p.mainFrame() && /preview|render|app/i.test(f.url())) || p.mainFrame();
  await move(600, 500, 800); await p.waitForTimeout(600); await move(1100, 450, 900); await p.waitForTimeout(600);
  for (let i = 0; i < 4; i++) { await wheel(350, 25); await p.waitForTimeout(1400); await p.screenshot({ path: path.join(OUT, `05-preview-scroll-${i}.png`) }); }
  const clickable = frame.locator('button, [role=tab], .tab, .btn, a').locator('visible=true');
  const n = Math.min(await clickable.count().catch(() => 0), 4);
  for (let i = 0; i < n; i++) { const el = clickable.nth(i); const bb = await el.boundingBox().catch(() => null); if (!bb) continue; await move(bb.x + bb.width / 2, bb.y + bb.height / 2, 600); await el.click({ timeout: 2000 }).catch(() => {}); await p.waitForTimeout(1500); await p.screenshot({ path: path.join(OUT, `06-interact-${i}.png`) }); }
  mark('interact');
  // ER of the data model and the theme
  await click(file('HuzhouTeachers.vdb'), 700); await p.waitForTimeout(1200); await click(tab('ER'), 500); await p.waitForTimeout(2500); await dismiss(); mark('er'); await p.screenshot({ path: path.join(OUT, '07-er.png') });
  await move(900, 600, 1500); await p.waitForTimeout(2500); mark('end');
  const video = await p.video().path(); await ctx.close(); await b.close();
  const final = path.join(OUT, 'huzhou-app.webm'); fs.renameSync(video, final);
  fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify({ video: final, marks }, null, 1)); console.log('done', final, JSON.stringify(marks));
})().catch(e => { console.error('FATAL', e.message); process.exit(1) });
