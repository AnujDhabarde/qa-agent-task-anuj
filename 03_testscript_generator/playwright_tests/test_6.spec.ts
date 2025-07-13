import { test, expect } from '@playwright/test';

test('Create Interview Missing Title', async ({ page }) => {
  await page.goto('https://recruter.ai/dashboard/interviews/new');
  await page.click('#create-button');
});