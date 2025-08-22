🧑⚕️ AI Health & Wellness Coach (Demo)
Welcome! 👋
This project is a beginner-friendly demo AI agent that acts as a Health & Wellness Coach. It helps users ask questions about fitness, nutrition, mindfulness, and lifestyle in a safe and educational way.

The project is designed with explorability in mind for those new to AI but curious about:

✅ Conversational AI Agents

✅ Retrieval-Augmented Generation (RAG) for grounding answers in reliable documents

✅ Web Search Tools to fetch up-to-date health news or wellness tips

✅ (Optional) MCP Integration – for connecting the agent to other tools or APIs

⚠️ Disclaimer: This demo is for educational purposes only. It is not medical advice. Always consult a qualified professional for health decisions.

🚀 Features
Chatbot-like interaction: Ask natural questions and get structured responses.

RAG-enabled: The agent can pull answers from curated health/wellness PDFs or notes.

Web Search: If it doesn’t know something, it can search the web (via a search API).

Modular tools: Easily plug in MCP-enabled services (like custom APIs or apps).

🏗 Project Structure
bash
ai-health-coach/
│
├── data/                 # Local documents for RAG (e.g., nutrition guides, fitness tips)
├── notebooks/            # Experimentation, demos
├── src/
│   ├── agent.py          # Core AI agent definition
│   ├── rag.py            # RAG pipeline (embedding & retrieval)
│   ├── tools.py          # Web Search + optional MCP tools
│   └── server.py         # Web/CLI interface
├── requirements.txt      # Python dependencies
└── README.md             # This file
⚙️ Installation & Setup
1. Clone the repo
bash
git clone https://github.com/your-username/ai-health-coach.git
cd ai-health-coach
2. Create a virtual environment
bash
python3 -m venv .venv
source .venv/bin/activate   # (Linux/macOS)
.venv\Scripts\activate      # (Windows)
3. Install dependencies
bash
pip install -r requirements.txt
Dependencies include:

langchain – for agent & RAG chain.

faiss-cpu – vector database for retrieval.

openai or groq – LLM APIs.

duckduckgo-search (or SerpAPI) – web search.

fastapi + uvicorn – web server.

🧠 How It Works
User Query → You ask:
“What are some simple daily mindfulness exercises?”

RAG → The agent checks local docs in data/ (like a “Wellness Basics” guide).

Web Search → If needed, it searches the web for new, up-to-date tips.

Response → The agent combines the grounded answer into a friendly explanation.

🔌 Running the Demo
🖥️ Run in CLI
bash
python src/agent.py
Type your health/wellness questions directly in the terminal.

🌐 Run as a Web App
bash
uvicorn src.server:app --reload
Visit: http://localhost:8000

📚 Adding Custom Knowledge (RAG)
You can ground the AI in your own knowledge files:

Drop PDFs or text files into the data/ folder.

Re-run the indexing script:

bash
python src/rag.py --build-index
Now the agent will answer using your docs + the model.

🌍 Web Search Tool
By default, the agent uses DuckDuckGo Search API to fetch live results.

Replace with SerpAPI or another search tool if you prefer.

API keys (if needed) go in a .env file:

bash
OPENAI_API_KEY=your_openai_key
SERPAPI_KEY=your_serpapi_key
🔧 (Optional) MCP Integration
The project supports MCP (Model Context Protocol) for advanced users:

Connect to APIs like:

A calorie-tracking app

Your step counter

Personalized health planner

Example:

bash
python src/mcp_connector.py --tool calories_api
🧪 Example Interaction
You: “What are 3 beginner-friendly workouts I can do at home?”
AI Coach: Suggests bodyweight squats, push-ups, planks with clear explanations.

You: “What does recent research say about intermittent fasting?”
AI Coach: Retrieves a summary from your docs + searches the web for updates.
