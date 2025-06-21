# app/groq_agent.py
import os
from dotenv import load_dotenv
from groq import Groq  # Make sure this is installed: poetry add groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_deepseek(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # or any other model you want from Groq
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"
