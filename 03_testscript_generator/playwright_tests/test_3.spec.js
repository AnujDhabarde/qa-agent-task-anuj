import { test, expect } from '@playwright/test';

test('Signup Missing Password', async ({ page }) => {
  await page.fill('#email', 'user@example.com');
  await page.click('#signup-button');
});