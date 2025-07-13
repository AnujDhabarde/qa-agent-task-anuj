const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  // Folder where your .spec.js test files live
  testDir: './03_testscript_generator/playwright_tests',

  // Reporters for test results
  reporter: [
    ['html', { open: 'never' }], // Saves HTML report in playwright-report/
    ['json', { outputFile: '04_test_runner/results/results.json' }] // Saves test results for Streamlit
  ],

  // Playwright default settings
  use: {
    trace: 'on',                  // Save trace.zip for each test
    video: 'on',                  // Save videos for all tests
    screenshot: 'only-on-failure', // Capture screenshot only if test fails
  },

  // Optional: run tests in headless mode
  // headless: true,

  // Timeout settings (optional)
  timeout: 30 * 1000, // 30 seconds per test
});
