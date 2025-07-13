import { test, expect } from '@playwright/test';

test('Create Interview - Missing Title', async ({ page }) => {
  await page.click('#create-button');
});