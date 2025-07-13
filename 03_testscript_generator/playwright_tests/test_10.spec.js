import { test, expect } from '@playwright/test';

test('Password Field Hidden Characters', async ({ page }) => {
  await page.fill('#password', 'Secret123!');
});