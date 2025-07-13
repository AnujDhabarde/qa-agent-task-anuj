import { test, expect } from '@playwright/test';

test('Create Interview - Title Only', async ({ page }) => {
  await page.fill('#title', 'Frontend QA');
  await page.click('#create-button');
});