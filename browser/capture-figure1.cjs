// Figure 1 capture for paper 19: the corrected component-nma page (branch commit f7a78dc) in Microsoft Edge via Playwright.
// node cap19.cjs <port> <inputs.json> <playwright-module-dir> <outdir>
const fs = require('fs'), path = require('path');
const [port, inputsFile, pwDir, outDir] = process.argv.slice(2);
const { chromium } = require(path.join(pwDir, 'playwright'));
const inp = JSON.parse(fs.readFileSync(inputsFile, 'utf8'));
const URL = `http://127.0.0.1:${port}/component-nma/index.html`;
const SCALE = 5;
const out = p => path.join(outDir, p);
(async () => {
  const b = await chromium.launch({ channel: 'msedge' });
  const log = { url: URL, scale: SCALE, browser: b.version(), runs: {}, console: [] };
  const ctx = await b.newContext({ viewport: { width: 1000, height: 1000 }, deviceScaleFactor: SCALE, colorScheme: 'light' });
  const pg = await ctx.newPage();
  pg.on('console', m => log.console.push(m.type() + ': ' + m.text()));
  pg.on('response', r => { if (r.status() >= 400) log.console.push('HTTP ' + r.status() + ' ' + r.url()); });
  await pg.goto(URL); await pg.waitForLoadState('networkidle');
  await pg.addStyleTag({ content: '#hub-back{display:none!important}' });
  async function run(name) {
    await pg.evaluate(() => document.querySelectorAll('.toast-item').forEach(t => t.remove()));
    await pg.fill('#src', inp[name].text); await pg.click('#btn-run'); await pg.waitForTimeout(800);
    const state = JSON.parse(await pg.evaluate(() => JSON.stringify({
      result: window._almLastCnma(),
      componentTable: Array.from(document.querySelectorAll('#comp-body tr'), r => Array.from(r.querySelectorAll('td'), x => x.textContent)),
      combinationTable: Array.from(document.querySelectorAll('#int-body tr'), r => Array.from(r.querySelectorAll('td'), x => x.textContent)),
      toasts: Array.from(document.querySelectorAll('.toast-item'), x => x.textContent),
    })));
    log.runs[name] = Object.assign({ key: inp[name].key }, state);
    return state;
  }
  const panels = await pg.locator('section.panel').count();
  log.panel_count = panels;
  await run('main');
  await pg.locator('section.panel').nth(0).screenshot({ path: out('p19_A_input.png') });
  await pg.locator('#comp-tbl').screenshot({ path: out('p19_B_components.png') });
  await pg.locator('#int-tbl').screenshot({ path: out('p19_C_combinations.png') });
  await pg.locator('#forest').screenshot({ path: out('p19_D_forest.png') });
  const exbar = pg.locator('[data-action="json"]').first().locator('xpath=..');
  log.export_bar_html = (await exbar.evaluate(e => e.outerHTML)).slice(0, 3000);
  await exbar.screenshot({ path: out('p19_F_exports.png') });
  await run('refused');
  await pg.waitForSelector('.toast-item');
  log.refusal_toast = await pg.locator('.toast-item').first().textContent();
  await pg.locator('.toast-item').first().screenshot({ path: out('p19_E_refusal_message.png') });
  await pg.locator('section.panel').nth(1).screenshot({ path: out('p19_E_refusal_cleared.png') });
  log.cleared = { comp: await pg.locator('#comp-body tr').count(), comb: await pg.locator('#int-body tr').count(), forest: await pg.locator('#forest').evaluate(e => e.innerHTML) };
  await b.close();
  fs.writeFileSync(out('p19_shots_log.json'), JSON.stringify(log, null, 1));
  console.log('ok', log.browser, Object.keys(log.runs));
})().catch(e => { console.error(e); process.exit(1); });
