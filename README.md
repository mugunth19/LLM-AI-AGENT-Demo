🧑⚕️ AI Health & Wellness Coach (Demo)

Welcome! 👋  
This project is a beginner-friendly demo AI agent that acts as a Health & Wellness Coach. It helps users ask questions about fitness, nutrition, mindfulness, and lifestyle in a safe and educational way.

The agent uses:
- **Chainlit** for the interactive web UI
- **ChromaDB** for document retrieval (RAG)
- **Gemini LLM** for generating answers
- **MCP tools** (via submodule) for API integrations (e.g., Fitbit)
- **Python** and **submodules** for modularity and extensibility

⚠️ Disclaimer: This demo is for educational purposes only. It is not medical advice. Always consult a qualified professional for health decisions.

🚀 Features
- Chatbot-like interaction: Ask natural questions and get structured responses.
- RAG-enabled: The agent can pull answers from curated health/wellness PDFs or notes.
- Modular tools: Easily plug in MCP-enabled services (like Fitbit API, via submodule).

🏗 Project Structure
```
LLM-AI-AGENT-Demo/
│
├── data/                 # Local documents for RAG (e.g., nutrition guides, fitness tips)
├── notebooks/            # Experimentation, demos
│   └── chroma_db/        # ChromaDB persistent storage
├── src/
│   ├── agent.py          # Core AI agent definition (Chainlit entrypoint)
│   ├── rag.py            # RAG pipeline (embedding & retrieval)
│   ├── tools.py          # Optional MCP tools
│   └── server.py         # (Legacy) Web/CLI interface
├── mcp/                  # MCP tool integration (added as a git submodule)
├── requirements.txt      # Python dependencies
├── .env                  # API keys and secrets (not tracked in git)
└── README.md             # This file
```

> **Note:**  
> Fitbit MCP integration is included as a git submodule.  
> Original submodule repository: [https://github.com/TheDigitalNinja/mcp-fitbit](https://github.com/TheDigitalNinja/mcp-fitbit)  
> Always run `git submodule update --init --recursive` after cloning to ensure all submodule code is available.

**Credits:**  
- MCP Fitbit tool by [TheDigitalNinja](https://github.com/TheDigitalNinja/mcp-fitbit)
- Chainlit UI by [Chainlit](https://github.com/Chainlit/chainlit)
- ChromaDB by [Chroma](https://github.com/chroma-core/chroma)
- Gemini LLM by Google Generative AI

⚙️ Installation & Setup
1. Clone the repo
    ```sh
    git clone https://github.com/your-username/LLM-AI-AGENT-Demo.git
    cd LLM-AI-AGENT-Demo
    ```
2. **Pull in submodules (Fitbit MCP is added as a submodule):**
    ```sh
    git submodule update --init --recursive
    ```
3. Create a virtual environment
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate   # (Linux/macOS)
    .venv\Scripts\activate      # (Windows)
    ```
4. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
    Dependencies include:
    - chromadb – vector database for retrieval
    - google-generativeai – Gemini LLM API
    - python-dotenv – for environment variables
    - requests – for HTTP APIs
    - mcp – for MCP tool integration
    - chainlit – for the web UI

5. Add your API keys and secrets to a `.env` file:
    ```
    GOOGLE_API_KEY=your_gemini_api_key
    FITBIT_CLIENT_ID=your_fitbit_client_id
    FITBIT_CLIENT_SECRET=your_fitbit_client_secret
    ```

🧠 How It Works
- **User Query:** You ask a health/wellness question.
- **RAG:** The agent checks local docs in `data/` (like a “Wellness Basics” guide).
- **MCP Tool:** For Fitbit or other API queries, the agent can call MCP tools.
- **Response:** The agent combines the grounded answer into a friendly explanation.

🔌 Running the Demo

🖥️ **Run with Chainlit UI**
```sh
chainlit run src/agent.py -w
```
- This will start the Chainlit web server.
- Open the provided URL in your browser to chat with the agent.

📚 Adding Custom Knowledge (RAG)
You can ground the AI in your own knowledge files:

- Drop PDFs or text files into the `data/` folder.
- Re-run the indexing script:
    ```sh
    python src/rag.py --build-index
    ```
- Now the agent will answer using your docs + the model.

🔧 MCP Integration (Fitbit Example)
The project supports MCP (Model Context Protocol) for advanced users:

- Connect to APIs like Fitbit for personalized health data.
- Make sure your `.env` file contains valid Fitbit credentials.
- When running in a dev container, the MCP server will prompt you to authorize Fitbit access. Open the provided URL:
    ```sh
    "$BROWSER" <authorization_url>
    ```
- Complete the OAuth flow in your browser. After authorization, rerun your agent script.

🧪 Example Interaction
You: “What are 3 beginner-friendly workouts I can do at home?”  
AI Coach: Suggests bodyweight squats, push-ups, planks with clear explanations.

You: “What is my Fitbit profile information?”  
AI Coach: Retrieves your profile data from Fitbit via MCP tool.

You: "Calculate my BMI index"
AI Coach: Pull height and weight from Fitbit profile and calculates the BMI index and shows the result.

** TO-DOs **
1. Deploy in a cloud infra and access via a public URL
2. Add a Action button and prompt user to connect to own fitbit account
3. Add in-memory for the chats

** Furture Imrpovements **
1. Add User login
2. Add profile/user fitbit token restoring in a database
3. SSL for the deployments
4. Long Term memory
5. Add feature to upload user's own Health related PDF document and provide answers based on it.
