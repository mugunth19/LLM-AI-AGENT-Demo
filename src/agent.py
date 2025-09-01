import chromadb
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import chainlit as cl

load_dotenv()

# Fitbit MCP Server Environment
os.environ["FITBIT_CLIENT_ID"] = os.getenv("FITBIT_CLIENT_ID")
os.environ["FITBIT_CLIENT_SECRET"] = os.getenv("FITBIT_CLIENT_SECRET")

# Setting the environment
DATA_PATH = os.path.abspath(os.path.join(os.getcwd(), '.', 'data'))
CHROMA_PATH = os.path.abspath(os.path.join(os.getcwd(), './notebooks/', 'chroma_db'))
# print(f"Mounted data folder at: {DATA_PATH}")
# print(f"Mounted data folder at: {CHROMA_PATH}")
# print("ChromaDB absolute path:", os.path.abspath(CHROMA_PATH))

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="RAG")
# print("Collection count:", collection.count())

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

# MCP Server Configuration
MCP_SERVER_COMMAND = ["mcp-fitbit"]

async def call_mcp_tool(tool_name: str, arguments: dict):
    """Call MCP server tool"""
    server_params = StdioServerParameters(command=MCP_SERVER_COMMAND[0], args=MCP_SERVER_COMMAND[1:])
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # List available tools
            tools = await session.list_tools()
            
            # Call the specific tool
            if any(tool.name == tool_name for tool in tools.tools):
                result = await session.call_tool(tool_name, arguments)
                return result.content[0].text if result.content else None
    return None

def should_use_mcp(query: str, rag_results: list) -> tuple[bool, str, dict]:
    """Determine if MCP server should be called based on query and RAG results"""
    decision_prompt = f"""
    You are an agent that decides whether to call a Fitbit MCP tool based on the user's query and available RAG results.
    If the query asks for Fitbit-specific data (like profile, weight, sleep, exercises, activity, heart rate, or food log), and RAG results do not answer it, you MUST call the appropriate MCP tool.
    Available Fitbit tools: get_weight, get_sleep_by_date_range, get_exercises, get_daily_activity_summary, get_heart_rate, get_food_log, get_profile.
    Query: {query}
    RAG Results Available: {len(rag_results) > 0}
    Respond with JSON: {{"use_mcp": true/false, "tool_name": "name", "arguments": {{}}}}
    """
    
    response = model.generate_content(decision_prompt)
    text = response.text.strip()
    # Remove code fences and any leading/trailing whitespace
    text = re.sub(r"^```json|^```|```$", "", text).strip()
    try:
        decision = json.loads(text)
        return decision.get("use_mcp", False), decision.get("tool_name", ""), decision.get("arguments", {})
    except Exception as e:
        # print("Decision parsing error:", e, text)
        return False, "", {}
@cl.on_message
async def main(message: cl.Message):
    # Get RAG results
    results = collection.query(query_texts=[message.content], n_results=20)
    #print("RAG Results:", results['documents'])
    
    # Check if MCP server should be called
    use_mcp, tool_name, arguments = should_use_mcp(message.content, results['documents'])
    # print(f"Decision: use_mcp={use_mcp}, tool_name={tool_name}, arguments={arguments}")
    
    mcp_data = ""
    if use_mcp and tool_name:
        # print(f"Calling MCP tool: {tool_name} with arguments: {arguments}")
        mcp_result = await call_mcp_tool(tool_name, arguments)
        # print(f"MCP result: {mcp_result}")
        mcp_data = f"\n\nAdditional tool data:\n{mcp_result}" if mcp_result else ""
    
    # Generate response
    system_prompt = f"""
    You are a health and wellness coach. Answer based on the provided knowledge only.
    If you don't know the answer, say: I don't know
    
    RAG Data: {results['documents']}{mcp_data}
    """
    
    response = model.generate_content([
        {"role":"user","parts":[{"text":system_prompt}]},
        {"role":"user","parts":[{"text":message.content}]}
    ])
    
    print("\n\n---------------------\n\n")
    print(response.text)
    #print("RAG Results:", results['documents'])
      # Send a response back to the user
    await cl.Message(
        content=f"Received: {response.text}",
    ).send()
    
if __name__ == "__main__":
    import asyncio
    query = input("What do you want to know about health and wellness?\n\n")
    asyncio.run(main(query))