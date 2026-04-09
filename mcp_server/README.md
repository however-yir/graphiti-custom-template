<p align="center">
  <img src="../images/graphiti-custom-logo.svg" width="132" alt="Graphiti Custom MCP" />
</p>

# 记忆图服务网关 Graphiti Custom MCP Server

面向 MCP 客户端的时序记忆图服务层（HTTP / stdio），用于把 AI 对话与业务事件写入图数据库并检索。

---

## 目录 Contents

- [1. 服务定位 Service Positioning](#1-服务定位-service-positioning)
- [2. 本版本改造点 What Changed](#2-本版本改造点-what-changed)
- [3. 功能清单 Features](#3-功能清单-features)
- [4. 快速开始 Quick Start](#4-快速开始-quick-start)
- [5. 配置与环境变量 Configuration](#5-配置与环境变量-configuration)
- [6. 客户端接入 Client Integration](#6-客户端接入-client-integration)
- [7. Docker 部署 Docker Deployment](#7-docker-部署-docker-deployment)
- [8. 测试与排错 Testing & Troubleshooting](#8-测试与排错-testing--troubleshooting)

---

## 1. 服务定位 Service Positioning

`Graphiti Custom MCP Server` 提供一组 MCP 工具，把时序记忆图能力封装成标准接口，方便在 Claude、Cursor、自动化 Agent 平台中复用。

核心作用：

1. 把文本/消息/JSON 数据作为 Episode 持续写入图。
2. 查询节点（entities）与事实（facts）。
3. 按 `group_id` 隔离不同业务域或租户。
4. 执行图维护（清理、索引重建）。

---

## 2. 本版本改造点 What Changed

1. 项目包名调整为 `graphiti-custom-mcp-server`。
2. 依赖补齐 `python-dotenv`，避免运行时缺依赖。
3. 新增 `.env.example`，统一本地启动变量模板。
4. `config.yaml` 改为环境变量优先，默认走本地地址。
5. OpenAI 兼容端点支持增强：自动标准化 `/v1`。
6. 支持本地 OpenAI 兼容服务（如 Ollama）无 key 回退。
7. LLM 与 Embedder 均支持 `organization_id` 透传。
8. 新增工厂单测 `tests/test_openai_compatibility.py`。

---

## 3. 功能清单 Features

- Episode 管理：新增、查询、删除
- 节点检索：按语义查询实体
- 事实检索：按关系查询事实
- 队列状态：查询各 `group_id` 的排队与 worker 状态（`get_queue_status`）
- 图维护：清理图、重建索引
- 多数据库：FalkorDB / Neo4j
- 多模型供应商：OpenAI / Azure OpenAI / Anthropic / Gemini / Groq
- 双传输协议：`http`（默认）与 `stdio`

---

## 4. 快速开始 Quick Start

### 4.1 进入目录

```bash
cd mcp_server
```

### 4.2 安装依赖

```bash
uv sync
```

### 4.3 复制环境变量

```bash
cp .env.example .env
```

### 4.4 启动服务

```bash
uv run main.py --transport http
```

默认 MCP endpoint：`http://127.0.0.1:8000/mcp/`

---

## 5. 配置与环境变量 Configuration

配置优先级：

1. CLI 参数
2. 环境变量
3. `config/config.yaml`
4. 代码默认值

### 5.1 Ollama 本地示例

```bash
OPENAI_API_KEY=ollama
OPENAI_API_URL=http://127.0.0.1:11434/v1
LLM_PROVIDER=openai
LLM_MODEL=gpt-oss:20b
```

### 5.2 FalkorDB 示例

```bash
DATABASE_PROVIDER=falkordb
FALKORDB_URI=redis://127.0.0.1:6379
```

### 5.3 Neo4j 示例

```bash
DATABASE_PROVIDER=neo4j
NEO4J_URI=bolt://127.0.0.1:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=change-me
```

---

## 6. 客户端接入 Client Integration

### 6.1 HTTP 客户端

将 MCP 服务器地址配置为：

```text
http://127.0.0.1:8000/mcp/
```

运维探针：

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/live
http://127.0.0.1:8000/ready
http://127.0.0.1:8000/metrics
```

### 6.2 仅支持 stdio 的客户端

```bash
uv run main.py --transport stdio
```

---

## 7. Docker 部署 Docker Deployment

默认（FalkorDB + MCP）：

```bash
docker compose up
```

Neo4j 版本：

```bash
docker compose -f docker/docker-compose-neo4j.yml up
```

---

## 8. 测试与排错 Testing & Troubleshooting

### 8.1 运行关键测试

```bash
uv run pytest tests/test_openai_compatibility.py
```

### 8.2 常见问题

1. 连接失败：先检查数据库是否启动。
2. 429 限流：降低 `SEMAPHORE_LIMIT`。
3. 本地 Ollama 报鉴权错误：确认 `OPENAI_API_KEY=ollama`。
4. 路径问题：确认 `CONFIG_PATH` 指向有效 YAML。
