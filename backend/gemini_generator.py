import google.generativeai as genai
from company_profiles import COMPANY_CONTEXT
import os
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_ai_questions(
    target_role,
    skills,
    missing,
    difficulty,
    company
):

    company_context = COMPANY_CONTEXT.get(
        company,
        ""
    )

    prompt = f"""
Generate exactly 5  interview questions.

Role: {target_role}

Difficulty: {difficulty}

Existing Skills:
{skills}

Missing Skills:
{missing}

Company:
{company}

Company Context:
{company_context}

IMPORTANT RULES:

1. Return ONLY a JSON array.
2. No explanation.
3. No markdown.
4. No numbering.
5. No headings.
6. Output format must be exactly:

[
"Question 1",
"Question 2",
"Question 3",
"Question 4",
"Question 5"
]
"""

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)

    except Exception:
        return [
            q.strip()
            for q in response.text.split("\n")
            if q.strip()
        ]