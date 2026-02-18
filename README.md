# Vista AI

Google [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) 项目：用自然语言生成图表/看板（规划中）。当前为多 Agent 演示：orchestrator + math agent + MCP text agent。

## 目录结构

```
vista-ai/
├── agents/                    # ADK agents_dir，每个子目录一个 app
│   ├── README.md
│   └── vista_ai/              # Vista AI 应用
│       ├── __init__.py
│       ├── agent.py           # root_agent、sub_agents、tools 挂载
│       ├── tools/             # 计算器、orchestrator 等 ADK tools
│       ├── mcp/                # MCP 客户端配置（stdio）
│       └── mcp_server.py      # MCP 服务（reverse_text, slugify）
├── config.py                  # 环境变量与调参常量
├── services/                  # 共享业务逻辑（占位）
├── storage/                   # 文档库 + 向量库（占位）
├── data_sources/              # 数据源抽象（占位）
├── models/                    # 共享 DTO（占位）
├── schema_cache/             # Vista JSON schema（占位）
├── requirements.txt
├── .env.example               # 可选：环境变量示例
└── README.md
```

## 环境与运行

### 1. 创建虚拟环境并安装依赖

```bash
cd vista-ai
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 配置 API Key

在项目根目录创建 `.env`，或导出环境变量：

```bash
# 二选一即可
export GOOGLE_API_KEY="your-key"
# 或
export GEMINI_API_KEY="your-key"
```

### 3. 启动方式

| 方式 | 命令 | 说明 |
|------|------|------|
| Web | `adk web agents --port 8010` | 浏览器打开 http://127.0.0.1:8010，选择 **vista_ai** |
| CLI | `adk run agents/vista_ai` | 终端内与 agent 对话 |

端口默认可用 8000；若被占用可改为 `--port 8010` 等。

## 依赖概览

- **google-adk** — Google Agent Development Kit  
- **google-genai** — Gemini API 客户端  
- **mcp** — MCP 服务/客户端  
- **python-dotenv** — 加载 `.env`

更多说明见 `agents/README.md`（agents 目录约定）与 `agents/vista_ai/README.md`（vista_ai 应用说明）。
