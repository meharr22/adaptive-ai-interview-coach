import google.generativeai as genai

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
      api_key="your_api_key_here"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash-lite"
)


def evaluate_answer(
    question,
    answer
):

    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Evaluate:

1. Score out of 10
2. Strengths
3. Weaknesses
4. Improvement Suggestions

Return concise feedback.
"""

    response = model.generate_content(
        prompt
    )

    return response.text