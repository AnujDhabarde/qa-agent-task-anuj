import os
import json

# Paths
INPUT_FILE = "../02_testcase_generator/testcases.json"
OUTPUT_DIR = "playwright_tests"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load test cases
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    testcases = json.load(f)

# Template to generate each .spec.js file
def generate_test_script(testcase, index):
    title = testcase["title"]
    steps = testcase["steps"]
    lines = [
        "import { test, expect } from '@playwright/test';",
        "",
        f"test('{title}', async ({'{'} page {'}'}) => {{"
    ]

    for step in steps:
        action = step["action"]
        selector = step.get("selector", "")
        value = step.get("value", "")

        if action == "goto":
            lines.append(f"  await page.goto('{value}');")
        elif action == "fill":
            lines.append(f"  await page.fill('{selector}', '{value}');")
        elif action == "click":
            lines.append(f"  await page.click('{selector}');")
        elif action == "check":
            lines.append(f"  await page.check('{selector}');")
        elif action == "uncheck":
            lines.append(f"  await page.uncheck('{selector}');")
        elif action == "select":
            lines.append(f"  await page.selectOption('{selector}', '{value}');")
        else:
            lines.append(f"  // Unknown action: {action}")

    lines.append("});")
    return "\n".join(lines)

# Generate .spec.js files
for i, testcase in enumerate(testcases, start=1):
    script = generate_test_script(testcase, i)
    filename = f"test_{i}.spec.js"
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(script)

print(f"✅ {len(testcases)} test scripts generated in {OUTPUT_DIR}")
