// Records the two hosted Huzhou University VL applications (production preview host):
// 1) Faculty development dashboard (data-rich big screen), 2) Teacher recuperation service
// portal: demo login shown on its own login page (demo data), admin side, route list, detail.
const path = require('path'); const fs = require('fs');
const { chromium } = require(process.env.PW_DIR);
const OUT = process.env.OUT || path.join(__dirname, 'apps');
const DASH = 'https://pre.dev.h5app.com/play/Wyqvuc5U'; const WELL = 'https://pre.dev.h5app.com/play/3jlwzSyj/route/entry';
const cursorInit = () => { addEventListener('DOMContentLoaded', () => { const c = document.createElement('div');
  c.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24"><path d="M3 2l7 19 2.5-7.5L20 11z" fill="#fff" stroke="#000" stroke-width="1.4"/></svg>';
  Object.assign(c.style, { position: 'fixed', left: '0', top: '0', zIndex: 2147483647, pointerEvents: 'none', transform: 'translate(-50px,-50px)' }); document.documentElement.appendChild(c);
  addEventListener('mousemove', e => c.style.transform = `translate(${e.clientX - 3}px,${e.clientY - 2}px)`, true);
  addEventListener('mousedown', e => { const r = document.createElement('div'); Object.assign(r.style, { position: 'fixed', left: e.clientX - 22 + 'px', top: e.clientY - 22 + 'px', width: '44px', height: '44px', borderRadius: '50%', border: '3px solid #f5a524', zIndex: 2147483646, pointerEvents: 'none', transition: 'all .5s ease-out' }); document.documentElement.appendChild(r); requestAnimationFrame(() => { r.style.transform = 'scale(1.8)'; r.style.opacity = '0' }); setTimeout(() => r.remove(), 600) }, true); }); };
(async () => {
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch({ executablePath: process.env.CHROME_BIN }); const ctx = await b.newContext({ viewport: { width: 1600, height: 900 }, recordVideo: { dir: OUT, size: { width: 1600, height: 900 } } });
  await ctx.addInitScript(cursorInit); const p = await ctx.newPage(); const t0 = Date.now(); const marks = {};
  const log = (...a) => { const s = `[${((Date.now() - t0) / 1000).toFixed(1)}s] ` + a.join(' '); console.log(s); fs.appendFileSync(path.join(OUT, 'log.txt'), s + '\n'); };
  const mark = k => { marks[k] = (Date.now() - t0) / 1000; log('MARK', k); fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify(marks, null, 1)); };
  let mx = 800, my = 450;
  const move = async (x, y, ms = 700) => { const n = Math.max(8, Math.round(ms / 16)); for (let i = 1; i <= n; i++) { const k = i / n, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; await p.mouse.move(mx + (x - mx) * e, my + (y - my) * e); await p.waitForTimeout(ms / n * .5) } mx = x; my = y };
  const to = async (loc, ms) => { await loc.waitFor({ state: 'visible', timeout: 15000 }); const bb = await loc.boundingBox(); await move(bb.x + bb.width / 2, bb.y + bb.height / 2, ms); return bb };
  const click = async (loc, ms) => { await to(loc, ms); await p.waitForTimeout(150); await loc.click({ timeout: 5000 }).catch(async () => { await p.mouse.down(); await p.mouse.up() }) };
  const wheel = async (dy, steps = 30) => { for (let i = 0; i < steps; i++) { await p.mouse.wheel(0, dy / steps); await p.waitForTimeout(30) } };
  const shot = n => p.screenshot({ path: path.join(OUT, n + '.png') });
  const V = (t) => p.getByText(t, { exact: true }).locator('visible=true').first();
  // 1) dashboard
  await p.goto(DASH, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(9000); mark('dash_open'); await shot('01-dash');
  for (const [x, y] of [[300, 350], [820, 420], [1300, 380], [600, 700], [1100, 720]]) { await move(x, y, 900); await p.waitForTimeout(900); }
  mark('dash_hover'); await shot('02-dash-hover');
  await wheel(500, 40); await p.waitForTimeout(1500); await shot('03-dash-scroll'); await move(900, 500, 800); await p.waitForTimeout(800); await wheel(-500, 40); await p.waitForTimeout(800);
  mark('dash_end');
  // 2) recuperation service: demo login (credentials printed on the page itself), admin side
  await p.goto(WELL, { waitUntil: 'domcontentloaded', timeout: 60000 }); await p.waitForTimeout(6000); mark('well_open'); await shot('10-well-login');
  const admin = V('管理端'); if (await admin.count()) await click(admin, 700); await p.waitForTimeout(800);
  const user = p.getByPlaceholder('请输入账号').first(); const pass = p.getByPlaceholder('请输入密码').first();
  await click(user, 600); await p.keyboard.type('demo.admin', { delay: 70 }); await click(pass, 500); await p.keyboard.type('123456', { delay: 70 }); await p.waitForTimeout(400);
  await click(V('登录'), 700); await p.waitForTimeout(6000); mark('well_home'); await shot('11-well-home'); log('url', p.url());
  const body = (await p.locator('body').innerText().catch(() => '')).replace(/\s+/g, ' '); log('home text', body.slice(0, 500));
  // explore: visible menu items (left nav / tabs); click up to 4 different ones and screenshot
  const navTexts = await p.locator('a, [role=menuitem], .el-menu-item, .ant-menu-item, li, .nav-item, button').evaluateAll(els => els.filter(e => e.offsetParent && (e.textContent || '').trim().length > 1 && (e.textContent || '').trim().length < 12).map(e => (e.textContent || '').trim())).catch(() => []);
  const uniq = [...new Set(navTexts)].filter(t => !/登录|退出|关闭|取消/.test(t)); log('nav', JSON.stringify(uniq.slice(0, 30)));
  let n = 0;
  for (const t of uniq) { if (n >= 4) break; const loc = p.getByText(t, { exact: true }).locator('visible=true').first(); if (!(await loc.count())) continue; try { await click(loc, 700); await p.waitForTimeout(3500); n++; mark(`well_nav_${n}`); await shot(`12-well-nav-${n}`); log('nav clicked', t, p.url()); await move(900, 500, 700); await wheel(300, 20); await p.waitForTimeout(900); await wheel(-300, 20); } catch (e) { log('nav fail', t, e.message.slice(0, 60)); } }
  // detail: first table row / detail button
  const detail = p.getByText(/详情|查看|编辑/).locator('visible=true').first(); if (await detail.count()) { await click(detail, 700); await p.waitForTimeout(3500); mark('well_detail'); await shot('13-well-detail'); await move(900, 600, 800); await wheel(400, 25); await p.waitForTimeout(1200); await shot('14-well-detail-scroll'); }
  await p.waitForTimeout(1000); mark('end');
  const video = await p.video().path(); await ctx.close(); await b.close();
  const final = path.join(OUT, 'apps.webm'); fs.renameSync(video, final);
  fs.writeFileSync(path.join(OUT, 'marks.json'), JSON.stringify({ video: final, marks }, null, 1)); console.log('done', final, JSON.stringify(marks));
})().catch(e => { console.error('FATAL', e.message); process.exit(1) });
