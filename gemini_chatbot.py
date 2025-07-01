import google.generativeai as genai
import os

# 1. Set your Gemini API key here
os.environ["GOOGLE_API_KEY"] = "AIzaSyBYTphb7PMr0lJe-BT01qs-0TqK0x8KxW4"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 2. Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

def get_response_from_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error from Gemini API: {str(e)}"
