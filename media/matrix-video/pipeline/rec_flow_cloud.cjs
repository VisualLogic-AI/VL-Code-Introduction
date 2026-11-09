// Cloud VLC (http://127.0.0.1:4000 by default): the Flow tab in detail. Generation graphs
// (Meta Sharded, Parallel Codegen, an Enterprise cascade) with node hovers and pans, then a
// REAL run of the read-only "metadata-check" DAG (tool nodes only, no model) so the canvas
// animates nodes running -> done, then the written report. Free-running with marks.
const path = require('path'); const fs = require('fs');
const { chromium } = require('playwright');
const URL = process.env.VLC_URL || 'http://127.0.0.1:4000';
const PROJECT = process.env.PROJECT || 'HuzhouDashboard';
const OUT = process.env.OUT || path.join(__dirname, 'rec', 'flow');
const cursorInit = () => { addEventListener('DOMContentLoaded', () => { const c = document.createElement('div');
  c.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24"><path d="M3 2l7 19 2.5-7.5L20 11z" fill="#fff" stroke="#000" stroke-width="1.4"/></svg>';
  Object.assign(c.style, { position: 'fixed', left: '0', top: '0', zIndex: 2147483647, pointerEvents: 'none', transform: 'translate(-50px,-50px)' }); document.documentElement.appendChild(c);
  addEventListener('mousemove', e => c.style.transform = `translate(${e.clientX - 3}px,${e.clientY - 2}px)`, true);
  addEventListener('mousedown', e => { const r = document.createElement('div'); Object.assign(r.style, { position: 'fixed', left: e.clientX - 22 + 'px', top: e.clientY - 22 + 'px', width: '44px', height: '44px', borderRadius: '50%', border: '3px solid #f5a524', zIndex: 2147483646, pointerEvents: 'none', transition: 'all .5s ease-out' }); document.documentElement.appendChild(r); requestAnimationFrame(() => { r.style.transform = 'scale(1.8)'; r.style.opacity = '0' }); setTimeout(() => r.remove(), 600) }, true); }); };
(async () => {
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true });
  const t0 = Date.now(); const marks = {};
  const log = (...a) => { const s = `[${((Date.now() - t0) / 1000).toFixed(1)}s] ` + a.join(' '); console.log(s); fs.appendFileSync(path.join(OUT, 'log.txt'), s + '\n'); };
  const mark = k => { marks[k] = (Date.now() - t0) / 1000; log('MARK', k); fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify(marks, null, 1)); };
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 1600, height: 900 }, recordVideo: { dir: OUT, size: { width: 1600, height: 900 } } });
  await ctx.addInitScript(cursorInit); const p = await ctx.newPage();
  let mx = 800, my = 450;
  const move = async (x, y, ms = 700) => { const n = Math.max(8, Math.round(ms / 16)); for (let i = 1; i <= n; i++) { const k = i / n, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; await p.mouse.move(mx + (x - mx) * e, my + (y - my) * e); await p.waitForTimeout(ms / n * .5) } mx = x; my = y };
  const to = async (loc, ms) => { await loc.waitFor({ state: 'visible', timeout: 15000 }); const bb = await loc.boundingBox(); await move(bb.x + bb.width / 2, bb.y + Math.min(bb.height / 2, 20), ms); return bb };
  const click = async (loc, ms) => { await to(loc, ms); await p.waitForTimeout(150); await loc.click({ timeout: 5000 }).catch(async () => { await p.mouse.down(); await p.mouse.up() }) };
  const wheel = async (dy, steps = 30) => { for (let i = 0; i < steps; i++) { await p.mouse.wheel(0, dy / steps); await p.waitForTimeout(30) } };
  const dismiss = () => p.locator('#statusDismissBtn').click({ timeout: 800 }).catch(() => {});
  const shot = n => p.screenshot({ path: path.join(OUT, n + '.png') });
  const chat = async (open) => { const bb = await p.locator('#chatPanel').boundingBox().catch(() => null); const ex = !!bb && bb.width > 300; if (open !== ex) await p.locator('.chat-collapse-btn:visible').first().click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(500); };
  const V = (t, ex = true) => p.getByText(t, { exact: ex }).locator('visible=true').first();
  const wf = () => p.frameLocator('iframe[src*="workflow-editor.html"]').first();
  const state = async () => { try { return await p.evaluate(async () => (await fetch('/api/workflow/current-state')).json()); } catch { return null; } };
  // hover a few nodes of the current graph, pan a little
  const tourGraph = async (tag) => {
    await p.waitForTimeout(1500); await dismiss();
    const fit = wf().getByText('Fit', { exact: true }).first(); if (await fit.count()) { await to(fit, 600); await fit.click({ timeout: 3000 }).catch(() => {}); await p.waitForTimeout(1200); }
    const nodes = wf().locator('.node-body'); const n = Math.min(await nodes.count().catch(() => 0), 6); log(tag, 'nodes', n);
    for (let i = 0; i < n; i++) { const bb = await nodes.nth(i).boundingBox().catch(() => null); if (bb && bb.x > 380 && bb.x < 1500 && bb.y > 300 && bb.y < 880) { await move(bb.x + Math.min(60, bb.width / 2), bb.y + 14, 650); await p.waitForTimeout(450); } }
    await shot(`g-${tag}`);
    // pan right by dragging empty canvas
    await move(1300, 820, 500); await p.mouse.down(); await move(900, 760, 1400); await p.mouse.up(); await p.waitForTimeout(600);
    await shot(`g-${tag}-pan`);
  };
  await p.goto(URL, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(4000);
  await p.getByText('Maybe Later', { exact: true }).first().click({ timeout: 2000 }).catch(() => {}); await dismiss();
  // open the project
  const cur = p.locator('.ws-current'); if (await cur.count()) { await cur.click(); await p.waitForTimeout(700); const row = p.locator(`text=${PROJECT}`).locator('xpath=..').getByText('Open', { exact: true }); if (await row.count()) { await row.click(); await p.waitForTimeout(3000); } else { await p.keyboard.press('Escape'); } }
  await p.getByText('Maybe Later', { exact: true }).first().click({ timeout: 800 }).catch(() => {}); await dismiss(); await chat(false);
  mark('open'); await shot('01-open');
  // Flow tab → Generate → Meta Sharded
  await click(p.locator('.mode-tab-flow'), 700); await p.waitForTimeout(2500); await dismiss();
  await click(V('Generate'), 500).catch(() => {}); await p.waitForTimeout(800);
  await click(V('Meta Sharded'), 800); mark('sharded'); await tourGraph('sharded');
  // Parallel Codegen
  await click(V('Parallel Codegen'), 800); mark('parallel'); await tourGraph('parallel');
  // Enterprise cascade (biggest graphs): first card of the Enterprise sub-tab
  await click(V('Enterprise'), 600); await p.waitForTimeout(900); await shot('02-enterprise-cards');
  const grand = p.getByText(/EnterpriseGrand|Enterprise Grand/).locator('visible=true').first();
  if (await grand.count()) { await click(grand, 800); } else { await click(V('Enterprise Design Parallel'), 800).catch(() => log('no enterprise card')); }
  mark('enterprise'); await tourGraph('enterprise');
  // MetaData → metadata-check: a real tool-only run
  await click(V('MetaData'), 600); await p.waitForTimeout(900); await shot('03-metadata-cards');
  const mdCard = p.getByText(/Meta\s?Data\s?Check/i).locator('visible=true').first();
  if (await mdCard.count()) { await click(mdCard, 700); } else { log('metadata-check card not found by text'); }
  await p.waitForTimeout(1800); await dismiss(); mark('mdcheck'); await shot('04-mdcheck-graph');
  const before = await state(); const prevRun = before?.runID || before?.lastRun?.runID || null; log('prev run', prevRun);
  const runBtn = wf().locator('#runBtn'); await to(runBtn, 700); await p.waitForTimeout(300); await runBtn.click({ timeout: 5000 }).catch(() => log('runBtn click failed'));
  // the IDE asks for the requirement first: type it and confirm
  const dlgInput = p.locator('textarea:visible').last(); if (await dlgInput.count()) { await click(dlgInput, 600); await p.keyboard.type(process.env.RUN_REQ || 'Health-check the Smart Campus project metadata: pages, sections, services, tables and their relations. Report what is missing.', { delay: 14 }); await p.waitForTimeout(500); await shot('04b-run-dialog'); const go = p.getByText('Run workflow', { exact: true }).locator('visible=true').last(); await click(go, 600); }
  mark('run'); let last = ''; let done = false; let saw = false;
  for (let i = 0; i < 120 && !done; i++) { await p.waitForTimeout(250); const s = await state(); if (!s) continue; const rid = s.runID || s.lastRun?.runID || null; const ns = Object.entries(s.nodeStatuses || {}).map(([k, v]) => `${k.split('_').pop()}:${typeof v === 'string' ? v : v?.status}`).join(' '); if (ns !== last) { last = ns; log('STATE', s.active, rid, ns); } if (s.active || (rid && rid !== prevRun)) saw = true; if (saw && !s.active) done = true; }
  log('run detected', saw);
  await p.waitForTimeout(1500); mark('run_end'); await shot('05-run-end');
  // hover the finished nodes, then open the written report if the file tree shows it
  await tourGraph('mdcheck-done');
  const rep = p.locator('#sidebar, body').getByText(/MetaData|Report|report/).locator('visible=true').first(); if (await rep.count()) { await click(rep, 700).catch(() => {}); await p.waitForTimeout(1500); }
  mark('report'); await shot('06-report'); await move(900, 500, 900); await p.waitForTimeout(1500); mark('end');
  const video = await p.video().path(); await ctx.close(); await b.close();
  const final = path.join(OUT, 'flow.webm'); fs.renameSync(video, final);
  fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify({ video: final, marks }, null, 1)); console.log('done', final, JSON.stringify(marks));
})().catch(e => { console.error('FATAL', e.message); process.exit(1) });
