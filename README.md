# ✈️ FlightMate Backend

FlightMate is an AI-powered flight assistant backend built using **FastAPI**. It supports natural language queries to **check flight availability** and **book flights**, using powerful LLMs like **DeepSeek**, **Gemini**, and **Groq**.

---

## 🚀 Features

- Natural language flight query understanding
- Flight check and booking agents using AI
- CLI interface for terminal-based interaction
- Modular architecture for future expansion
- LLM integration via `.env` keys

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Farid-Bytes/flightmate_backend.git
cd flightmate_backend

------------------------------------------------------------------------
------------------------------------------------------------------------

Install dependencies
poetry install

------------------------------------------------------------------------
------------------------------------------------------------------------

Set up environment variables
Create a .env file:
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key

------------------------------------------------------------------------
------------------------------------------------------------------------

🔄 Run the Server
poetry run uvicorn app.main:app --reload

------------------------------------------------------------------------
------------------------------------------------------------------------

💬 Run in CLI (Chat Mode)
poetry run python app/cli_agent.py

Type natural questions like:

"Check flights from Lahore to Karachi"

"Book a flight for tomorrow from Islamabad to Dubai"

