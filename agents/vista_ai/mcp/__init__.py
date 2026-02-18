"""MCP client config for ADK: toolset connecting to the stdio MCP server."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

_HERE = Path(__file__).resolve().parent
_SERVER_PATH = str(_HERE.parent / "mcp_server.py")

MCP_TOOL_NAMES = ["reverse_text", "slugify"]


def get_mcp_toolset() -> McpToolset:
    """Build McpToolset that runs mcp_server.py as a stdio subprocess."""
    return McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command=sys.executable,
                args=[_SERVER_PATH],
                env=os.environ.copy(),
            )
        ),
        tool_filter=MCP_TOOL_NAMES,
    )
