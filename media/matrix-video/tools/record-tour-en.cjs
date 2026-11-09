// Cloud VLC tour (English project): Map, then for EVERY section (.sc): Code → Preview (hover +
// scroll) → Visual (object tree) → Logic; then the service (.vs) Code + Logic, ER, Theme, Flow
// (Parallel Codegen + Autotest graphs, fitted). Free-running with marks.
const path = require('path'); const fs = require('fs');
const { chromium } = require(process.env.PW_DIR || 'playwright');
const URL = process.env.VLC_URL || 'http://127.0.0.1:4000';
const PROJECT = process.env.PROJECT || 'SmartCampus';
const OUT = process.env.OUT || path.join(__dirname, 'rec', 'tour');
const MAX_SECTIONS = Number(process.env.MAX_SECTIONS || 3);
const cursorInit = () => { addEventListener('DOMContentLoaded', () => { const c = document.createElement('div');
  c.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24"><path d="M3 2l7 19 2.5-7.5L20 11z" fill="#fff" stroke="#000" stroke-width="1.4"/></svg>';
  Object.assign(c.style, { position: 'fixed', left: '0', top: '0', zIndex: 2147483647, pointerEvents: 'none', transform: 'translate(-50px,-50px)' }); document.documentElement.appendChild(c);
  addEventListener('mousemove', e => c.style.transform = `translate(${e.clientX - 3}px,${e.clientY - 2}px)`, true);
  addEventListener('mousedown', e => { const r = document.createElement('div'); Object.assign(r.style, { position: 'fixed', left: e.clientX - 22 + 'px', top: e.clientY - 22 + 'px', width: '44px', height: '44px', borderRadius: '50%', border: '3px solid #f5a524', zIndex: 2147483646, pointerEvents: 'none', transition: 'all .5s ease-out' }); document.documentElement.appendChild(r); requestAnimationFrame(() => { r.style.transform = 'scale(1.8)'; r.style.opacity = '0' }); setTimeout(() => r.remove(), 600) }, true); }); };
(async () => {
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(process.env.CHROME_BIN ? { executablePath: process.env.CHROME_BIN } : {}); const ctx = await b.newContext({ viewport: { width: 1600, height: 900 }, recordVideo: { dir: OUT, size: { width: 1600, height: 900 } } });
  await ctx.addInitScript(cursorInit); const p = await ctx.newPage(); const t0 = Date.now(); const marks = {};
  const log = (...a) => { const s = `[${((Date.now() - t0) / 1000).toFixed(1)}s] ` + a.join(' '); console.log(s); fs.appendFileSync(path.join(OUT, 'log.txt'), s + '\n'); };
  const mark = k => { marks[k] = (Date.now() - t0) / 1000; log('MARK', k); fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify(marks, null, 1)); };
  let mx = 800, my = 450;
  const move = async (x, y, ms = 700) => { const n = Math.max(8, Math.round(ms / 16)); for (let i = 1; i <= n; i++) { const k = i / n, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; await p.mouse.move(mx + (x - mx) * e, my + (y - my) * e); await p.waitForTimeout(ms / n * .5) } mx = x; my = y };
  const to = async (loc, ms) => { await loc.waitFor({ state: 'visible', timeout: 15000 }); const bb = await loc.boundingBox(); await move(bb.x + bb.width / 2, bb.y + Math.min(bb.height / 2, 20), ms); return bb };
  const click = async (loc, ms) => { await to(loc, ms); await p.waitForTimeout(150); await loc.click({ timeout: 5000 }).catch(async () => { await p.mouse.down(); await p.mouse.up() }) };
  const wheel = async (dy, steps = 30) => { for (let i = 0; i < steps; i++) { await p.mouse.wheel(0, dy / steps); await p.waitForTimeout(30) } };
  const tab = n => p.locator('.mode-tab', { hasText: new RegExp(`^\\s*${n}\\s*$`) }).locator('visible=true').first();
  const files = re => p.locator('#sidebar, body').getByText(re).locator('visible=true');
  const dismiss = () => p.locator('#statusDismissBtn').click({ timeout: 800 }).catch(() => {});
  const shot = n => p.screenshot({ path: path.join(OUT, n + '.png') });
  const chat = async (open) => { const bb = await p.locator('#chatPanel').boundingBox().catch(() => null); const ex = !!bb && bb.width > 300; if (open !== ex) await p.locator('.chat-collapse-btn:visible').first().click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(500); };
  const V = (t, ex = true) => p.getByText(t, { exact: ex }).locator('visible=true').first();
  const wf = () => p.frameLocator('iframe[src*="workflow-editor.html"]').first();
  const safeTab = async (n, wait) => { const t = tab(n); if (await t.count()) { const dis = await t.evaluate(e => e.classList.contains('disabled') || e.getAttribute('aria-disabled') === 'true').catch(() => false); if (!dis) { await click(t, 600); await p.waitForTimeout(wait); await dismiss(); return true; } } return false; };
  const visualTree = async () => { const ot = p.getByText('Object Tree', { exact: true }).locator('visible=true').first(); const bb = await ot.boundingBox().catch(() => null); if (bb) { for (const dy of [40, 70, 100, 130, 160]) await move(bb.x + 90, bb.y + dy, 400); } else { await move(500, 400, 800); await move(1100, 450, 800); } };
  const fitGraph = async () => { const fit = wf().getByText('Fit', { exact: true }).first(); if (await fit.count()) { await to(fit, 500); await fit.click({ timeout: 3000 }).catch(() => {}); await p.waitForTimeout(1000); } };
  await p.goto(URL, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(4000);
  await p.getByText('Maybe Later', { exact: true }).first().click({ timeout: 2000 }).catch(() => {}); await dismiss();
  const cur = p.locator('.ws-current'); if (await cur.count()) { await cur.click(); await p.waitForTimeout(700); const row = p.locator(`text=${PROJECT}`).locator('xpath=..').getByText('Open', { exact: true }); if (await row.count()) { await row.click(); await p.waitForTimeout(3000); } else { await p.keyboard.press('Escape'); } }
  await p.getByText('Maybe Later', { exact: true }).first().click({ timeout: 800 }).catch(() => {}); await dismiss(); await chat(false); mark('launch'); await shot('01-launch');
  await move(200, 350, 900); await move(900, 300, 900);
  await safeTab('Map', 2500); await move(700, 300, 900); await move(1000, 420, 900); mark('map'); await shot('02-map');
  const names = (await files(/\.sc$/).allInnerTexts().catch(() => [])).map(s => s.trim()); log('sections', JSON.stringify(names));
  const count = Math.min(names.length, MAX_SECTIONS);
  for (let k = 0; k < count; k++) {
    const sc = files(/\.sc$/).nth(k); await click(sc, 600); await p.waitForTimeout(900); log('section', k, names[k]);
    await safeTab('Code', 1200); await move(800, 500, 500); await wheel(700, 40); mark(`code_${k}`); await shot(`10-code-${k}`);
    await safeTab('Preview', 6500); mark(`preview_${k}`); await shot(`11-preview-${k}`);
    for (const [x, y] of [[700, 420], [1000, 480], [600, 650]]) { await move(x, y, 800); await p.waitForTimeout(700); }
    await wheel(450, 30); await p.waitForTimeout(1200); await shot(`12-preview-scroll-${k}`); await wheel(-450, 30);
    if (await safeTab('Visual', 9000)) { await visualTree(); } mark(`visual_${k}`); await shot(`13-visual-${k}`);
    // Logic needs a method/event node: expand this section in the tree and pick its first child
    { const row = files(/\.sc$/).nth(k); const caret = row.locator('xpath=ancestor::*[contains(@class,"tree") or contains(@class,"file") or contains(@class,"row")][1]//*[contains(@class,"caret") or contains(@class,"chevron") or contains(@class,"toggle") or contains(@class,"arrow")]').first();
      if (await caret.count()) { await click(caret, 400); } else { const bb = await row.boundingBox(); if (bb) { await move(bb.x - 22, bb.y + bb.height / 2, 400); await p.mouse.down(); await p.mouse.up(); } }
      await p.waitForTimeout(800); const child = p.locator('#sidebar, body').getByText(/\(\)|^on[A-Z]\w+|init|load/).locator('visible=true').first(); if (await child.count()) { await click(child, 500); await p.waitForTimeout(600); log('logic node', (await child.innerText().catch(() => '')).slice(0, 60)); } }
    if (await safeTab('Logic', 4000)) { await move(800, 450, 900); await move(1100, 520, 900); await wheel(300, 20); } mark(`logic_${k}`); await shot(`14-logic-${k}`);
  }
  if (count === 0) { await safeTab('Code', 1200); mark('code_0'); await shot('10-code-0'); await safeTab('Preview', 6500); mark('preview_0'); await shot('11-preview-0'); if (await safeTab('Visual', 5000)) await visualTree(); mark('visual_0'); await shot('13-visual-0'); await safeTab('Logic', 4000); mark('logic_0'); await shot('14-logic-0'); }
  marks.sections = count;
  const vs = files(/\.vs$/).first(); if (await vs.count()) { await click(vs, 600); await p.waitForTimeout(900); await safeTab('Code', 1200); await wheel(600, 40); mark('service_code'); await shot('20-service-code');
    { const bb = await vs.boundingBox(); if (bb) { await move(bb.x - 22, bb.y + bb.height / 2, 400); await p.mouse.down(); await p.mouse.up(); await p.waitForTimeout(800); } const m = p.locator('#sidebar, body').getByText(/\w+\(\)/).locator('visible=true').first(); if (await m.count()) { await click(m, 500); await p.waitForTimeout(600); log('service node', (await m.innerText().catch(() => '')).slice(0, 60)); } }
    if (await safeTab('Logic', 4000)) { await move(800, 450, 900); await move(1150, 540, 900); } mark('service_logic'); await shot('21-service-logic'); }
  const vdb = files(/\.vdb$/).first(); if (await vdb.count()) { await click(vdb, 600); await p.waitForTimeout(900); }
  await safeTab('ER', 2500); await move(900, 500, 900); mark('er'); await shot('30-er');
  const vth = files(/\.vth$/).first(); if (await vth.count()) { await click(vth, 600); await p.waitForTimeout(900); }
  await safeTab('THEME', 2500); await move(1350, 520, 900); mark('theme'); await shot('31-theme');
  await click(p.locator('.mode-tab-flow'), 700); await p.waitForTimeout(2500); await dismiss(); await click(V('Autotest'), 600).catch(() => {}); await p.waitForTimeout(900); mark('flow'); await shot('40-flow');
  const at = p.getByText(/AutoTest Pipeline/i).locator('visible=true').first(); if (await at.count()) { await click(at, 700); await p.waitForTimeout(2000); await fitGraph(); await move(1000, 560, 1000); mark('flow_autotest'); await shot('41-flow-autotest'); }
  await move(700, 600, 1200); await p.waitForTimeout(1200); mark('end');
  const video = await p.video().path(); await ctx.close(); await b.close();
  const final = path.join(OUT, 'tour.webm'); fs.renameSync(video, final);
  fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify({ video: final, marks }, null, 1)); console.log('done', final, JSON.stringify(marks));
})().catch(e => { console.error('FATAL', e.message); process.exit(1) });
