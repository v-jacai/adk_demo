# Vista AI (ADK app)

Orchestrator + math agent + MCP text agent (demo). Future: natural language → SQL + chart config → dashboard URL.

## Run

From repo root:

- **CLI:** `adk run agents/vista_ai`
- **Web:** `adk web agents` → select **vista_ai**

## Layout

- `agent.py` — root_agent, sub_agents (math_agent, mcp_text_agent), tools
- `tools/` — safe_calc, orchestrator_stamp, finalize_report (pipeline tools TBD)
- `mcp/` — MCP client config (stdio to mcp_server.py)
- `mcp_server.py` — MCP server (reverse_text, slugify)
