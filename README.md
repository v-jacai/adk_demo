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
pip install -r requirements.txt
```

Requirements pin **google-genai==1.63.0** for the custom model integration; `google-adk` and `mcp` are also included.

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

## Custom model (google-genai 1.63.0)

All agents use one **custom model** built with google-genai 1.63.0 and ADK’s Gemini integration:

- **Default**: base model `gemini-2.5-flash` with retry options (see `GeminiWithClient` in `adk_multi_agent_demo/agent.py`).
- **Override**: set `ADK_CUSTOM_MODEL` in `.env` to a different model ID (e.g. a tuned model name).
- **Create a tuned model**: run the script (requires `GOOGLE_API_KEY`), then set `ADK_CUSTOM_MODEL` to the printed model name:

```bash
export GOOGLE_API_KEY=your_key
python scripts/create_custom_tuned_model.py
# Then add ADK_CUSTOM_MODEL=tunedModels/... to .env
```

## Notes
- MCP server runs as a child process over stdio; do not print to stdout inside `mcp_server.py`.
