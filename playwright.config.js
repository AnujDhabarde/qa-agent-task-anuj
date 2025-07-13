// playwright.config.js
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './03_testscript_generator/playwright_tests',
  timeout: 30000,
  retries: 0,
  workers: 2,
  reporter: [
    ['list'],
    ['json', { outputFile: '04_test_runner/results/results.json' }],
    ['html', { outputFolder: 'playwright-report', open: 'never' }]
  ],
  use: {
    headless: true,
    viewport: { width: 1280, height: 720 },
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    trace: 'on-first-retry'
  }
});
