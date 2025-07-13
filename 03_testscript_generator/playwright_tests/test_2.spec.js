import { test, expect } from '@playwright/test';

test('Signup with Invalid Email', async ({ page }) => {
  await page.fill('#email', 'invalidemail');
  await page.fill('#password', 'Password123');
  await page.click('#signup-button');
});