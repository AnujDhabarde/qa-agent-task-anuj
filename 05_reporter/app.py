import streamlit as st
import json
import os
from pathlib import Path

# --- Paths ---
RESULTS_PATH = Path("../04_test_runner/results/results.json")
SCREENSHOTS_PATH = Path("../test-results/")
REPORT_LINK = "../playwright-report/index.html"

# --- Page Config ---
st.set_page_config(page_title="QA Agent Test Report", layout="wide")
st.title("📊 QA Agent – Automated Test Results")

# --- Load Results ---
if not RESULTS_PATH.exists():
    st.error("❌ No results.json found in 04_test_runner/results/. Please run tests first.")
    st.stop()

with open(RESULTS_PATH, "r", encoding="utf-8") as f:
    results_json = json.load(f)

# --- Parse Tests ---
tests = []
for suite in results_json.get("suites", []):
    for spec in suite.get("specs", []):
        for test in spec.get("tests", []):
            title = spec["title"]
            status = test["results"][0]["status"]
            duration = test["results"][0].get("duration", 0)
            tests.append({
                "title": title,
                "status": status,
                "duration": duration
            })

# --- Summary Metrics ---
passed = len([t for t in tests if t["status"] == "passed"])
failed = len([t for t in tests if t["status"] == "failed" or t["status"] == "timedOut"])
total = len(tests)

col1, col2, col3 = st.columns(3)
col1.metric("✅ Passed", passed)
col2.metric("❌ Failed", failed)
col3.metric("🧪 Total Tests", total)

st.markdown("---")

# --- Individual Test Results ---
for test in tests:
    emoji = "✅" if test["status"] == "passed" else "❌"
    with st.expander(f"{emoji} {test['title']}"):
        st.write(f"**Status**: `{test['status']}`")
        st.write(f"**Duration**: {test['duration']} ms")

# --- Optional Screenshots Section ---
st.markdown("## 📸 Failure Screenshots")
screenshot_files = list(SCREENSHOTS_PATH.rglob("test-failed-1.png"))

if screenshot_files:
    for img_path in screenshot_files:
        st.image(str(img_path), caption=img_path.name, use_column_width=True)
else:
    st.info("No screenshots found in /test-results/")

# --- Link to HTML Report ---
st.markdown("## 🌐 Full HTML Report")
st.markdown(f"[Click here to open Playwright HTML report]({REPORT_LINK})")
