import { test, expect } from '@playwright/test';

test('Valid Signup Flow', async ({ page }) => {
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'SecurePass123');
  await page.click('#signup-button');
});