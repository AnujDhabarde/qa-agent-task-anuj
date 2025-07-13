import { test, expect } from '@playwright/test';

test('Logout Functionality', async ({ page }) => {
  await page.goto('https://recruter.ai/dashboard');
  await page.click('#user-menu');
  await page.click('#logout-button');
});