import google.generativeai as genai

genai.configure(api_key="your_api_key_here")

model = genai.GenerativeModel("gemini-2.5-flash")
print(model.generate_content("Hello").text)