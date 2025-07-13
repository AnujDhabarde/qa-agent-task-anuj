import os
import json
import traceback
from dotenv import load_dotenv
from openai import OpenAI  # ✅ Correct import for new SDK

# Load your API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Create a new OpenAI client (new syntax)
client = OpenAI(api_key=OPENAI_API_KEY)

# ✅ Read transcript safely
try:
    with open("../01_transcription/transcript.txt", "rb") as f:
        raw_bytes = f.read()
    transcript = raw_bytes.decode("utf-8", errors="ignore")
    print("✅ Transcript loaded. Length:", len(transcript))
except Exception as e:
    print("❌ Failed to read transcript:", e)
    exit(1)

# ✅ Define your prompt
prompt = f"""
Generate exactly 10 frontend test cases for Recruter.ai using the following transcript.

Each test case must include:
- title
- description
- url (use 'https://recruter.ai' as base)
- steps (array of steps: each with action, selector, and value if needed)

Return response ONLY in JSON format. No markdown, no headings, no explanations.

Transcript:
\"\"\"{transcript}\"\"\"
"""

# ✅ New OpenAI call (correct syntax)
try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    output = response.choices[0].message.content
except Exception as e:
    print("❌ Error calling OpenAI API:", e)
    exit(1)

# ✅ Debug GPT output
print("\n🔍 GPT raw output (first 20 lines):\n")
print("\n".join(output.splitlines()[:20]))

# ✅ Save as .md
with open("testcases.md", "w", encoding="utf-8") as f:
    f.write(output)

# ✅ Try saving as JSON
try:
    testcases = json.loads(output)
    with open("testcases.json", "w", encoding="utf-8") as f:
        json.dump(testcases, f, indent=2)
    print("✅ testcases.json created successfully.")
except Exception as e:
    print("⚠️ Failed to parse output as JSON.")
    traceback.print_exc()
