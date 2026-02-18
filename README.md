# Vista AI

Google ADK project: natural language → chart/dashboard (future). Current: multi-agent demo (orchestrator + math + MCP text).

## Directory layout (best practice)

```
vista-ai/
├── agents/                    # ADK agents_dir (one app per subdir)
│   ├── README.md
│   └── vista_ai/              # Vista AI app
│       ├── __init__.py
│       ├── agent.py           # root_agent + sub_agents
│       ├── tools/             # ADK tools
│       ├── mcp/               # MCP client config
│       └── mcp_server.py
├── config.py                  # Env and tuning
├── services/                  # Shared logic (placeholder)
├── storage/                   # Document + vector (placeholder)
├── data_sources/              # Data source abstraction (placeholder)
├── models/                    # DTOs (placeholder)
├── schema_cache/             # Vista schema (placeholder)
├── requirements.txt
└── README.md
```

## Run (from repo root)

- **Web:** `adk web agents --port 8000` → choose **vista_ai**
- **CLI:** `adk run agents/vista_ai`

## Setup

```bash
pip install -r requirements.txt
# Set GOOGLE_API_KEY or GEMINI_API_KEY in .env
```
