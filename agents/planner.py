from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

async def run_domain_task(user_prompt):
    # Connect to the local domain MCP server
    client = MultiServerMCPClient({
        "legal": {
            "transport": "stdio",
            "command": "python",
            "args": ["infra/mcp-server/server.py"]
        }
    })
    
    tools = await client.get_tools()
    
    # Initialize the reasoning agent (2026 model standard)
    agent = create_agent("claude-3-5-sonnet-20241022", tools)
    
    # Execute the task with domain-specific reasoning
    response = await agent.ainvoke({"messages": [{"role": "user", "content": user_prompt}]})
    return response
  
