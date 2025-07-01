from simulate_health import simulate_health_data
from prompt_builder import generate_prompt
from gemini_chatbot import get_response_from_gemini
from load_health import get_health_from_file


print("\n👵 Elder Care Chatbot (Gemini Edition) — Type 'exit' to quit.")

while True:
    user_input = input("\n👵 You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    health = get_health_from_file()  # ← always fetches the latest file values
    prompt = generate_prompt(user_input, health)
    response = get_response_from_gemini(prompt)
    print(f"\n🤖 Bot: {response}")
