# Google ADK Multi-Agent Demo (Orchestrator + 2 Sub Agents + MCP Tool)

## What you get
- 1 orchestrator agent (root_agent)
- 2 sub agents
- all 3 agents call tools
- 1 sub agent calls an MCP server via ADK McpToolset (stdio)

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install google-adk mcp
```

## Configure
Copy `.env.example` to `.env` and fill your key:
```bash
cp .env.example .env
```

## Run (CLI)
From this repo root:
```bash
adk run adk_multi_agent_demo
```

Example prompt:
- 计算 ((3+5)*2)/4，然后把文本 'Hello ADK MCP' 做 slugify 并 reverse，最后合并结果。

## Run (Web)
```bash
adk web --port 8000
```
Then open http://localhost:8000

## Notes
- MCP server runs as a child process over stdio; do not print to stdout inside `mcp_server.py`.
