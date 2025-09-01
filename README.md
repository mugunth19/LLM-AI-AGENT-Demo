🧑⚕️ AI Health & Wellness Coach (Demo)
Welcome! 👋
This project is a beginner-friendly demo AI agent that acts as a Health & Wellness Coach. It helps users ask questions about fitness, nutrition, mindfulness, and lifestyle in a safe and educational way.

The project is designed with explorability in mind for those new to AI but curious about:

✅ Conversational AI Agents  
✅ Retrieval-Augmented Generation (RAG) for grounding answers in reliable documents  
✅ Web Search Tools to fetch up-to-date health news or wellness tips  
✅ (Optional) MCP Integration – for connecting the agent to other tools or APIs (e.g., Fitbit)

⚠️ Disclaimer: This demo is for educational purposes only. It is not medical advice. Always consult a qualified professional for health decisions.

🚀 Features
- Chatbot-like interaction: Ask natural questions and get structured responses.
- RAG-enabled: The agent can pull answers from curated health/wellness PDFs or notes.
- Web Search: If it doesn’t know something, it can search the web (via a search API).
- Modular tools: Easily plug in MCP-enabled services (like Fitbit API).

🏗 Project Structure
```
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
```

⚙️ Installation & Setup
1. Clone the repo
    ```sh
    git clone https://github.com/your-username/ai-health-coach.git
    cd ai-health-coach
    ```
2. Create a virtual environment
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate   # (Linux/macOS)
    .venv\Scripts\activate      # (Windows)
    ```
3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
    Dependencies include:
    - chromadb – vector database for retrieval
    - google-generativeai – Gemini LLM API
    - python-dotenv – for environment variables
    - requests – for HTTP APIs
    - mcp – for MCP tool integration

4. Add your API keys and secrets to a `.env` file:
    ```
    GOOGLE_API_KEY=your_gemini_api_key
    FITBIT_CLIENT_ID=your_fitbit_client_id
    FITBIT_CLIENT_SECRET=your_fitbit_client_secret
    ```

🧠 How It Works
- **User Query:** You ask a health/wellness question.
- **RAG:** The agent checks local docs in `data/` (like a “Wellness Basics” guide).
- **Web Search:** If needed, it searches the web for new, up-to-date tips.
- **MCP Tool:** For Fitbit or other API queries, the agent can call MCP tools.
- **Response:** The agent combines the grounded answer into a friendly explanation.

🔌 Running the Demo
🖥️ Run in CLI
```sh
python3 src/agent.py
```
Type your health/wellness questions directly in the terminal.

🌐 Run as a Web App
```sh
uvicorn src.server:app --reload
```
Visit: http://localhost:8000

📚 Adding Custom Knowledge (RAG)
You can ground the AI in your own knowledge files:

- Drop PDFs or text files into the `data/` folder.
- Re-run the indexing script:
    ```sh
    python src/rag.py --build-index
    ```
- Now the agent will answer using your docs + the model.

🌍 Web Search Tool
By default, the agent uses DuckDuckGo Search API to fetch live results.

Replace with SerpAPI or another search tool if you prefer.

API keys (if needed) go in a `.env` file:
```
OPENAI_API_KEY=your_openai_key
SERPAPI_KEY=your_serpapi_key
```

🔧 MCP Integration (Fitbit Example)
The project supports MCP (Model Context Protocol) for advanced users:

- Connect to APIs like Fitbit for personalized health data.
- Make sure your `.env` file contains valid Fitbit credentials.
- When running in a dev container, the MCP server will prompt you to authorize Fitbit access. Open the provided URL using:
    ```sh
    "$BROWSER" <authorization_url>
    ```
- Complete the OAuth flow in your browser. After authorization, rerun your agent script.

🧪 Example Interaction
You: “What are 3 beginner-friendly workouts I can do at home?”  
AI Coach: Suggests bodyweight squats, push-ups, planks with clear explanations.

You: “What is my Fitbit profile information?”  
AI Coach: Retrieves your profile data from Fitbit via MCP tool.

You: “What does recent research say about intermittent fasting?”  
AI Coach: Retrieves a summary from your docs + searches the web
