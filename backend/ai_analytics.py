import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key="your_api_key_here"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_ai_report(report):

    prompt = f"""
    Analyze this interview report:

    {report}

    Give:

    1. Strengths
    2. Weaknesses
    3. Final Verdict

    Keep it concise.
    """

    response = model.generate_content(
        prompt
    )

    return response.text