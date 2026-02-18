# Vista AI（ADK App）

Vista AI 的 ADK 应用入口。当前为多 Agent 演示；后续将接入「自然语言 → SQL + 图表配置 → 看板 URL」的完整 pipeline。

## 运行方式

在**仓库根目录**执行（需已激活 venv 并配置 `GOOGLE_API_KEY` 或 `GEMINI_API_KEY`）：

- **Web：** `adk web agents --port 8010` → 选择 **vista_ai**
- **CLI：** `adk run agents/vista_ai`

## 目录与职责

| 路径 | 说明 |
|------|------|
| **agent.py** | 定义 `root_agent`（orchestrator）、sub_agents（math_agent、mcp_text_agent），并挂载 tools 与 `AgentTool(sub_agent)` |
| **tools/** | ADK tools：`safe_calc`（安全计算）、`orchestrator_stamp`、`finalize_report`；后续可在此增加 pipeline 相关 tools |
| **mcp/** | MCP 客户端配置：通过 stdio 启动 `mcp_server.py`，暴露 `reverse_text`、`slugify` 给 mcp_text_agent |
| **mcp_server.py** | MCP 服务进程入口（FastMCP），供 ADK 以子进程方式调用 |

## 当前 Agent 结构

- **root_agent（orchestrator_agent）**：按顺序调用 `orchestrator_stamp` → 将计算任务交给 math_agent → 将文本任务交给 mcp_text_agent → 调用 `finalize_report` 汇总结果。
- **math_agent**：使用 tool `safe_calc` 做数学表达式计算。
- **mcp_text_agent**：使用 MCP tools `reverse_text`、`slugify` 做文本变换。

## 依赖

与仓库根目录 `requirements.txt` 一致；需在根目录创建/激活 venv 并安装依赖后再运行本 app。
