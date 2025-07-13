import { test, expect } from '@playwright/test';

test('Signin with Invalid Password', async ({ page }) => {
  await page.fill('#email', 'user@example.com');
  await page.fill('#password', 'WrongPass');
  await page.click('#login-button');
});