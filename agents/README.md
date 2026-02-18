# Agents 目录（ADK `agents_dir`）

本目录是 ADK 的 **agents_dir**：其下每个**子目录**对应一个可运行的 app（一个 agent 应用）。运行 `adk web agents` 时会列出所有子目录供选择。

## 当前应用

| 应用 | 说明 |
|------|------|
| **vista_ai** | Vista AI：自然语言 → 图表/看板（规划）。当前为演示：orchestrator + math agent + MCP text agent。详见 [vista_ai/README.md](vista_ai/README.md)。 |

## 如何运行（需在仓库根目录执行）

- **Web：** `adk web agents --port 8010` → 在页面中选择 **vista_ai**
- **CLI：** `adk run agents/vista_ai`

## 新增一个 app

在 `agents/` 下新建一个子目录，目录内至少包含：

- **agent.py** — 定义并导出 `root_agent`（`LlmAgent` 实例），或  
- **root_agent.yaml** — 用 YAML 定义 root agent

ADK 会将该子目录识别为一个新的 app 并加入 Web 列表、支持 `adk run agents/<子目录名>`。
