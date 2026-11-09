// Records a REAL VL code-generation run in VLCode on this Mac: open the Flow tab on the
// generation workflow, show the English request in the AI Assistant, then start the
// workflow through the IDE's own /api/workflow/execute route (the chat send is held on this
// Mac because the Core tray and the Matrix gateway are on different tenants). LLM steps run
// through the bound Matrix Task Brain (matrix-external). Watches the Flow canvas run, then
// opens the generated project in Preview.
const path = require('path'); const fs = require('fs');
const { chromium } = require(process.env.PW_DIR);
const URL = process.env.VLC_URL || 'http://127.0.0.1:4124';
const OUT = process.env.OUT || path.join(__dirname, 'run');
const MAX_MIN = Number(process.env.MAX_MIN || 35);
const WF_CARD = process.env.WF_CARD || 'Meta Direct';
const WF_NAME = process.env.WF_NAME || 'meta-direct-codegen';
const REQUEST = process.env.REQUEST || 'Build "Smart Campus Visitor Center", an English-language web app for a university: a Home dashboard with KPI cards (visitors today, pending appointments, checked-in now), a bar chart of visits by building, a Visitors table with search and status filter, an Appointment page with a registration form (visitor name, host, building, date, purpose) and a confirmation list. Use a clean light theme, realistic English seed data for 12 visitors and 6 buildings. All UI text in English.';
const cursorInit = () => { addEventListener('DOMContentLoaded', () => { const c = document.createElement('div');
  c.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24"><path d="M3 2l7 19 2.5-7.5L20 11z" fill="#fff" stroke="#000" stroke-width="1.4"/></svg>';
  Object.assign(c.style, { position: 'fixed', left: '0', top: '0', zIndex: 2147483647, pointerEvents: 'none', transform: 'translate(-50px,-50px)' }); document.documentElement.appendChild(c);
  addEventListener('mousemove', e => c.style.transform = `translate(${e.clientX - 3}px,${e.clientY - 2}px)`, true);
  addEventListener('mousedown', e => { const r = document.createElement('div'); Object.assign(r.style, { position: 'fixed', left: e.clientX - 22 + 'px', top: e.clientY - 22 + 'px', width: '44px', height: '44px', borderRadius: '50%', border: '3px solid #f5a524', zIndex: 2147483646, pointerEvents: 'none', transition: 'all .5s ease-out' }); document.documentElement.appendChild(r); requestAnimationFrame(() => { r.style.transform = 'scale(1.8)'; r.style.opacity = '0' }); setTimeout(() => r.remove(), 600) }, true); }); };
(async () => {
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true });
  const t0 = Date.now();
  const log = (...a) => { const s = `[${((Date.now() - t0) / 1000).toFixed(1)}s] ` + a.join(' '); console.log(s); fs.appendFileSync(path.join(OUT, 'log.txt'), s + '\n'); };
  const b = await chromium.launch(process.env.CHROME_BIN ? { executablePath: process.env.CHROME_BIN } : {});
  const ctx = await b.newContext({ viewport: { width: 1600, height: 900 }, recordVideo: { dir: OUT, size: { width: 1600, height: 900 } } });
  await ctx.addInitScript(cursorInit); const p = await ctx.newPage(); const marks = {}; const mark = k => { marks[k] = (Date.now() - t0) / 1000; log('MARK', k); fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify(marks, null, 1)); };
  let mx = 800, my = 450;
  const move = async (x, y, ms = 700) => { const n = Math.max(8, Math.round(ms / 16)); for (let i = 1; i <= n; i++) { const k = i / n, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; await p.mouse.move(mx + (x - mx) * e, my + (y - my) * e); await p.waitForTimeout(ms / n * .5) } mx = x; my = y };
  const to = async (loc, ms) => { await loc.waitFor({ state: 'visible', timeout: 20000 }); const bb = await loc.boundingBox(); await move(bb.x + bb.width / 2, bb.y + Math.min(bb.height / 2, 20), ms); return bb };
  const click = async (loc, ms) => { await to(loc, ms); await p.waitForTimeout(150); await loc.click({ timeout: 5000 }).catch(async () => { await p.mouse.down(); await p.mouse.up() }) };
  const wheel = async (dy, steps = 30) => { for (let i = 0; i < steps; i++) { await p.mouse.wheel(0, dy / steps); await p.waitForTimeout(30) } };
  const tab = n => p.locator('.mode-tab', { hasText: new RegExp(`^\\s*${n}\\s*$`) }).locator('visible=true').first();
  const dismiss = () => p.locator('#statusDismissBtn').click({ timeout: 800 }).catch(() => {});
  const shot = n => p.screenshot({ path: path.join(OUT, n + '.png') });
  const chat = async (open) => { const bb = await p.locator('#chatPanel').boundingBox().catch(() => null); const ex = !!bb && bb.width > 300; if (open !== ex) await p.locator('.chat-collapse-btn:visible').first().click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(500); };
  const state = async () => { try { return await p.evaluate(async () => { const r = await fetch('/api/workflow/current-state'); return await r.json(); }); } catch { return null; } };
  await p.goto(URL, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(6000);
  await p.getByText('Maybe Later', { exact: true }).first().click({ timeout: 2000 }).catch(() => {}); await dismiss(); mark('open'); await shot('01-open');
  // Flow tab → Generate → show the workflow card
  await chat(false); await click(p.locator('.mode-tab-flow'), 700); await p.waitForTimeout(2500); await dismiss();
  const card = p.getByText(WF_CARD, { exact: true }).locator('visible=true').first(); await to(card, 900);
  await click(card, 300).catch(() => {}); await p.waitForTimeout(1500); mark('workflow_selected'); await shot('02-workflow-selected');
  // AI Assistant → Build intent → show the request (typed, not sent: the run starts through the IDE route below)
  await chat(true); await click(p.locator('#chatPanel .intent-opt', { hasText: 'Build' }).first(), 600).catch(() => {});
  await click(p.locator('#chatInput'), 500); await p.keyboard.type(REQUEST, { delay: 6 }); await p.waitForTimeout(900); await shot('03-request');
  await p.locator('#chatInput').fill('').catch(() => {}); await chat(false); await p.waitForTimeout(400);
  // Start the workflow through the IDE's own route; the Flow canvas animates the run.
  const started = await p.evaluate(async ({ WF_NAME, REQUEST }) => {
    const body = { workflowName: WF_NAME, projectDir: '', clientRunToken: 'video-' + Date.now(), params: { userRequest: REQUEST, projectName: 'SmartCampus', targetLang: 'en' } };
    const r = await fetch('/api/workflow/execute', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) });
    // keep the SSE stream alive in the page
    (async () => { try { const rd = r.body.getReader(); while (true) { const { done } = await rd.read(); if (done) break; } } catch {} })();
    return { status: r.status, ct: r.headers.get('content-type') };
  }, { WF_NAME, REQUEST });
  log('execute', JSON.stringify(started)); mark('sent');
  // watch the run on the Flow canvas
  const t1 = Date.now(); let last = ''; let i = 0; let done = false; let sawActive = false;
  while (Date.now() - t1 < MAX_MIN * 60000 && !done) {
    await p.waitForTimeout(5000); i++;
    const s = await state();
    if (s) {
      const ns = s.nodeStatuses || {}; const summary = Object.entries(ns).map(([k, v]) => `${k}:${typeof v === 'string' ? v : (v && (v.status || v.state)) || '?'}`).join(' ');
      const line = `active=${s.active} step=${s.currentStepID} err=${s.lastError ? String(s.lastError).slice(0, 80) : ''} ${summary}`.slice(0, 400);
      if (line !== last) { last = line; log('STATE', line); }
      if (s.active) sawActive = true;
      if (sawActive && !s.active) { done = true; mark('run_end'); log('finished', s.finishedAt, 'stopped', s.stopped, s.stopReason || ''); }
      if (!sawActive && i >= 12 && !s.active) { log('never became active'); done = true; mark('run_end'); }
    }
    if (i % 6 === 0) { await shot(`04-run-${String(i).padStart(3, '0')}`); }
    if (i % 4 === 2) { await move(900 + (i % 3) * 40, 520 + (i % 5) * 20, 800); }
    if (i % 12 === 6) { await wheel(200, 20); } else if (i % 12 === 0) { await wheel(-200, 20); }
  }
  await shot('05-run-final'); mark('after_run');
  // results: files list, then Preview of the main section/app
  await p.waitForTimeout(1500);
  const files = await p.locator('#sidebar, body').getByText(/\.(sc|vx)$/).locator('visible=true').allInnerTexts().catch(() => []); log('files', JSON.stringify(files.slice(0, 20)));
  const vx = p.locator('#sidebar, body').getByText(/\.vx$/).locator('visible=true').first();
  if (await vx.count()) { await click(vx, 600); await p.waitForTimeout(1000); }
  await click(tab('Preview'), 600); await p.waitForTimeout(8000); await dismiss(); mark('preview'); await shot('06-preview');
  await move(800, 450, 900); await p.waitForTimeout(800); await wheel(400, 30); await p.waitForTimeout(1500); await shot('07-preview-scroll'); await wheel(-400, 30);
  const sc = p.locator('#sidebar, body').getByText(/\.sc$/).locator('visible=true');
  const n = Math.min(await sc.count().catch(() => 0), 3);
  for (let k = 0; k < n; k++) { await click(sc.nth(k), 600); await p.waitForTimeout(1000); await click(tab('Preview'), 500); await p.waitForTimeout(6000); await dismiss(); await shot(`08-preview-${k}`); await move(800, 500, 800); await wheel(300, 20); await p.waitForTimeout(1200); await wheel(-300, 20); }
  mark('end');
  const video = await p.video().path(); await ctx.close(); await b.close();
  const final = path.join(OUT, 'gen-run.webm'); fs.renameSync(video, final);
  fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify({ video: final, marks }, null, 1)); console.log('done', final, JSON.stringify(marks));
})().catch(e => { console.error('FATAL', e.message); process.exit(1) });
