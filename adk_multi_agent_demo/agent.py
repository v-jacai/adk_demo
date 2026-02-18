from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Dict, Any

from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from .tools_local import safe_calc, orchestrator_stamp


def finalize_report(run_id: str, math_result: Dict[str, Any], text_result: Dict[str, Any]) -> Dict[str, Any]:
    """Orchestrator tool: merge sub-agent outputs into a single result."""
    return {
        "status": "ok",
        "run_id": run_id,
        "math": math_result,
        "text": text_result,
    }


# -------- Sub-agent 1: math agent (calls local tool safe_calc) --------
math_agent = LlmAgent(
    name="math_agent",
    model="gemini-3-flash-preview",
    description="Handles calculations precisely using a calculator tool.",
    instruction=(
        "You are a math helper. Always use the tool `safe_calc` to compute. "
        "Return ONLY the tool output as JSON."
    ),
    tools=[safe_calc],
)

# -------- Sub-agent 2: mcp text agent (calls MCP tools via McpToolset) --------
HERE = Path(__file__).resolve().parent
MCP_SERVER_PATH = str(HERE / "mcp_server.py")

mcp_text_agent = LlmAgent(
    name="mcp_text_agent",
    model="gemini-3-flash-preview",
    description="Transforms text using MCP tools (reverse_text, slugify).",
    instruction=(
        "You are a text transformer. "
        "Use MCP tools when needed: reverse_text(text), slugify(text). "
        "Return ONLY the tool output."
    ),
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command=sys.executable,
                    args=[MCP_SERVER_PATH],
                    env=os.environ.copy(),
                )
            ),
            tool_filter=["reverse_text", "slugify"],
        )
    ],
)

# -------- Orchestrator (root_agent): delegates + calls its own tools --------
root_agent = LlmAgent(
    name="orchestrator_agent",
    model="gemini-3-flash-preview",
    description="Orchestrates tasks across math_agent and mcp_text_agent, then finalizes a report.",
    instruction=(
        "You are the orchestrator. Goal: produce a final JSON report.\n"
        "Process (strict):\n"
        "1) Call tool `orchestrator_stamp` to create a run_id.\n"
        "2) Delegate calculation work to `math_agent`.\n"
        "3) Delegate text work to `mcp_text_agent` (this one uses MCP tools).\n"
        "4) Call `finalize_report(run_id, math_result, text_result)` and return that.\n\n"
        "Rules: Use tools; do not handwave. Final answer must be finalize_report JSON."
    ),
    sub_agents=[math_agent, mcp_text_agent],
    tools=[
        orchestrator_stamp,
        finalize_report,
        AgentTool(math_agent),
        AgentTool(mcp_text_agent),
    ],
)
