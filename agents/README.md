# Agents directory (ADK `agents_dir`)

Each **subdirectory** here is one ADK app. `adk web agents` lists all of them.

## Apps

- **vista_ai** — Vista AI: natural language → chart/dashboard (demo: orchestrator + math + MCP text).

## Run (from repo root)

- **Web:** `adk web agents --port 8000` → choose **vista_ai**
- **CLI:** `adk run agents/vista_ai`

To add a new app, create a subdirectory under `agents/` with at least `agent.py` defining `root_agent` (or `root_agent.yaml`).
