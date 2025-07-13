import { test, expect } from '@playwright/test';

test('Signup with Invalid Email', async ({ page }) => {
  await page.goto('https://recruter.ai/signup');
  await page.fill('#email', 'invalidemail');
  await page.fill('#password', 'SecurePass123');
  await page.click('#signup-button');
});