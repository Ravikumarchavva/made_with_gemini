from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient



# Load all the tools
try:
    toolbox = ToolboxSyncClient("http://127.0.0.1:5000")
    tools = toolbox.load_toolset('my_bq_toolset')
    print("Tools loaded successfully.")
    print(tools)
except Exception as e:
    print(f"Error loading tools: {e}")
    tools = []
    
root_agent = Agent(
    name="gcp_powered",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about Google Cloud Release notes."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the Google Cloud Release notes. Use the tools to answer the question"
    ),
    tools=list(tools),
)
