"""Vista AI ADK app: root agent + sub-agents (demo: orchestrator + math + MCP text)."""
from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Optional

try:
    from dotenv import load_dotenv
    _repo_root = Path(__file__).resolve().parent.parent.parent
    load_dotenv(_repo_root / ".env")
except ImportError:
    pass

from google import genai
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import AgentTool

from .mcp import get_mcp_toolset
from .tools import finalize_report, orchestrator_stamp, safe_calc

if TYPE_CHECKING:
    from google.genai import Client

DEFAULT_MODEL = "gemini-2.5-flash"


class GeminiWithClient(Gemini):
    """ADK Gemini backed by genai.Client."""
    client: Optional[Any] = None

    @property
    def api_client(self) -> "Client":
        if self.client is not None:
            return self.client
        from google.genai import Client
        api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
        return Client(api_key=api_key)


def _shared_model() -> GeminiWithClient:
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key) if api_key else None
    return GeminiWithClient(model=DEFAULT_MODEL, client=client)


_model = _shared_model()

math_agent = LlmAgent(
    name="math_agent",
    model=_model,
    description="Handles calculations precisely using a calculator tool.",
    instruction=(
        "You are a math helper. Always use the tool `safe_calc` to compute. "
        "Return ONLY the tool output as JSON."
    ),
    tools=[safe_calc],
)

mcp_text_agent = LlmAgent(
    name="mcp_text_agent",
    model=_model,
    description="Transforms text using MCP tools (reverse_text, slugify).",
    instruction=(
        "You are a text transformer. "
        "Use MCP tools when needed: reverse_text(text), slugify(text). "
        "Return ONLY the tool output."
    ),
    tools=[get_mcp_toolset()],
)

root_agent = LlmAgent(
    name="orchestrator_agent",
    model=_model,
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
