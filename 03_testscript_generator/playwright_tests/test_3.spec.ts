import { test, expect } from '@playwright/test';

test('Signin with Correct Credentials', async ({ page }) => {
  await page.goto('https://recruter.ai/login');
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'SecurePass123');
  await page.click('#login-button');
});