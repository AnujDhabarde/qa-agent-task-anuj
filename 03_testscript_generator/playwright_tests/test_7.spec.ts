import { test, expect } from '@playwright/test';

test('Access Dashboard After Login', async ({ page }) => {
  await page.goto('https://recruter.ai/dashboard');
  // Unknown action: navigate
});