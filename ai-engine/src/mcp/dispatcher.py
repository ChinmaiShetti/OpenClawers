"""
src/mcp/dispatcher.py — Routes LLM tool_use responses to the right MCP client.
"""

async def dispatch(tool_name: str, tool_input: dict) -> dict:
    """
    Dispatches an LLM tool call to the appropriate MCP client.
    tool_name: e.g. "notion_create_page", "slack_send_message"
    """
    if tool_name.startswith("notion_"):
        from src.mcp.notion.tools import handle
        return await handle(tool_name, tool_input)
    elif tool_name.startswith("slack_"):
        from src.mcp.slack.tools import handle
        return await handle(tool_name, tool_input)
    elif tool_name.startswith("github_"):
        from src.mcp.github.tools import handle
        return await handle(tool_name, tool_input)
    elif tool_name.startswith("calendar_"):
        from src.mcp.calendar.tools import handle
        return await handle(tool_name, tool_input)
    else:
        return {"error": f"Unknown tool: {tool_name}"}
