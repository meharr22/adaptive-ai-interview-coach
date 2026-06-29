# test.py

from gemini_generator import generate_ai_questions

result = generate_ai_questions(
    "AI Engineer",
    ["python","tensorflow"],
    ["docker","pytorch"]
)

print(result)