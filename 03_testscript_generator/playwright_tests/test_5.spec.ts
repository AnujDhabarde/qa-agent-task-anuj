import { test, expect } from '@playwright/test';

test('Create Interview with Title Only', async ({ page }) => {
  await page.goto('https://recruter.ai/dashboard/interviews/new');
  await page.fill('#title', 'Frontend QA');
  await page.click('#create-button');
});