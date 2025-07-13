# Run tests
npx playwright test

# Generate HTML report
npx playwright show-report

# Save JSON results
npx playwright test --reporter=json > 04_test_runner/results.json

# Save videos and screenshots
# Already configured via playwright.config.js if set properly
# Overwrite existing results.json
if (Test-Path "results/results.json") {
    Remove-Item "results/results.json"
}
Move-Item "results.json" "results/"
