# 🤖 AI QA Agent for Recruter.ai — By Anuj Dhabarde

This is an AI-powered multi-agent QA automation framework designed to test the frontend of [Recruter.ai](https://recruter.ai). It automates:

- ✅ Test case generation using LLMs (GPT-4o)
- ✅ Playwright test script creation
- ✅ Test execution with video/screenshot capture
- ✅ Streamlit-based test reporting dashboard

---

## 🔍 What This Agent Can Do

| Phase | Function |
|-------|----------|
| ✅ 1. Transcription | Extract steps from Recruter.ai help video |
| ✅ 2. Test Case Generator | Generate test cases using OpenAI |
| ✅ 3. Script Generator | Convert JSON to Playwright tests |
| ✅ 4. Test Runner | Run tests with artifacts |
| ✅ 5. Reporter | Streamlit dashboard + HTML test report |

---

## 📁 Folder Structure

qa-agent-anuj/
├── 01_transcription/ # Transcript from video
├── 02_testcase_generator/ # LLM-based test case generator
├── 03_testscript_generator/ # Converts testcases.json to .spec.js
├── 04_test_runner/ # Executes all tests and saves results
├── 05_reporter/ # Streamlit reporting UI
├── playwright.config.js # Playwright config
├── .env # Your API key (excluded from repo)
└── README.md # You're here!

yaml
Copy
Edit

---

## 🧠 Behind the Scenes: Multi-Agent Flow

1. 📽️ Watch tutorial video (transcribed using YouTubeTranscript API)
2. 🧠 Feed into GPT-4o to generate structured test cases
3. 🧪 Convert test cases to Playwright `.spec.js` files
4. 🧼 Run Playwright tests → store logs, videos, screenshots
5. 📊 View results in Streamlit or HTML report

---

## 🧰 Technologies Used

- OpenAI GPT-4o
- Python (for transcription, LLMs, reporting)
- Playwright (JavaScript-based test automation)
- Streamlit (for test reporting UI)
- YouTubeTranscript API
- PowerShell automation scripts

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js v18+
- Git + VS Code

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/AnujDhabarde/qa-agent-task-anuj.git
cd qa-agent-task-anuj

# Python Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Node Setup
npm install
npx playwright install
▶️ Phase-by-Phase Usage
✅ Phase 1: Transcribe Video
bash
Copy
Edit
cd 01_transcription
python transcribe_video.py
Generates transcript.txt.

✅ Phase 2: Generate Test Cases (LLM)
bash
Copy
Edit
cd 02_testcase_generator
python generate_testcases.py
Outputs:

testcases.md (for reading)

testcases.json (for automation)

✅ Phase 3: Convert JSON → Playwright .spec.js
bash
Copy
Edit
cd 03_testscript_generator
python convert_to_playwright.py
Generates:

playwright_tests/test_*.spec.js

✅ Phase 4: Run Tests + Save Results
bash
Copy
Edit
cd 04_test_runner
.\run_tests.ps1
Artifacts:

playwright-report/ (HTML test report)

test-results/ (screenshots/videos)

results/results.json (for dashboard)

✅ Phase 5: Launch Reporting UI
bash
Copy
Edit
cd 05_reporter
streamlit run app.py
📝 Sample Test Case JSON
json
Copy
Edit
{
  "title": "Signup with Valid Email",
  "description": "Ensure user can register with valid credentials",
  "url": "https://recruter.ai/signup",
  "steps": [
    {"action": "goto", "selector": "https://recruter.ai/signup"},
    {"action": "fill", "selector": "#email", "value": "user@example.com"},
    {"action": "fill", "selector": "#password", "value": "SecurePass123"},
    {"action": "click", "selector": "#signup-button"}
  ]
}
📸 Reporting Output
📷 Screenshots in test-results/

🎥 Videos in test-results/

🧾 JSON summary in 04_test_runner/results/results.json

🌐 Full HTML report in playwright-report/index.html

📊 Live dashboard via Streamlit

👨‍💻 Author
Anuj Dhabarde
QA Engineer | LLM + Playwright Automation
🔗 https://www.linkedin.com/in/anuj-dhabarde-32b85114b/
📧 anujdhabarde05@gmail.com