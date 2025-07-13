import { test, expect } from '@playwright/test';

test('Signin with Wrong Password', async ({ page }) => {
  await page.goto('https://recruter.ai/login');
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'WrongPass');
  await page.click('#login-button');
});