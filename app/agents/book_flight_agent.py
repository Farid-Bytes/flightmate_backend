from app.groq_agent import ask_deepseek

def book_flight(request: str) -> str:
    prompt = f"""
You are a flight booking assistant.

Task: Book a flight based on the user's request below.

User request: "{request}"

Respond with confirmation, including flight details, seat info, and a success message.
"""
    return ask_deepseek(prompt).strip()
