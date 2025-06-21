from app.agents.check_flight_agent import check_flight_availability
from app.agents.book_flight_agent import book_flight
from app.groq_agent import ask_deepseek

def process_user_request(message: str) -> str:
    # Let Groq classify the intent
    classify_prompt = f"""
You are a smart flight assistant.

Analyze the user message: "{message}"

If the message is about checking flights or availability, respond with: check  
If the message is about booking or reserving a flight, respond with: book  
Respond with only one word: check or book
"""
    intent = ask_deepseek(classify_prompt).strip().lower()

    if "check" in intent:
        result = check_flight_availability(message)
    elif "book" in intent:
        result = book_flight(message)
    else:
        result = "❌ Sorry, I couldn't understand your request. Please specify whether you're checking or booking a flight."

    final_response = f"✈️ FlightMate Agent Response:\n{result}"
    return final_response
