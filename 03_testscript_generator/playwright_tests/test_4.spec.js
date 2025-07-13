import { test, expect } from '@playwright/test';

test('Signin with Valid Credentials', async ({ page }) => {
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'SecurePass123');
  await page.click('#login-button');
});