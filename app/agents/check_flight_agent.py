from app.groq_agent import ask_deepseek

def check_flight_availability(request: str) -> str:
    prompt = f"""
You are a flight availability assistant.

Task: Check available flights and seat availability based on the user's request below.

User request: "{request}"

Respond with a short and clear summary of available flights, times, and seat info.
"""
    return ask_deepseek(prompt).strip()
# This function checks flight availability based on the user's request.