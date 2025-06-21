# app/cli_agent.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from app.agents.main_agent import process_user_request

def main():
    print("🛫 Welcome to FlightMate Terminal Agent!")
    print("Type your message (type 'exit' to quit):")

    chat_history = []

    while True:
        user_input = input("🧑 You: ").strip()
        if user_input.lower() == "exit":
            print("👋 Exiting FlightMate. Goodbye!")
            break

        chat_history.append({"role": "user", "content": user_input})

        response = process_user_request(user_input)

        chat_history.append({"role": "agent", "content": response})

        print(f"🤖 FlightMate: {response}\n")

if __name__ == "__main__":
    main()
