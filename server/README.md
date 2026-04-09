# 图服务接口层 Graphiti Custom Service

面向 HTTP API 的图记忆服务封装层，基于 FastAPI 对 `graphiti-core` 提供写入、检索与管理接口。

---

## 目录 Contents

- [1. 服务定位 Service Scope](#1-服务定位-service-scope)
- [2. 功能清单 Features](#2-功能清单-features)
- [3. 快速开始 Quick Start](#3-快速开始-quick-start)
- [4. 配置说明 Configuration](#4-配置说明-configuration)
- [5. 接口与探针 API & Probes](#5-接口与探针-api--probes)
- [6. Docker 部署 Deployment](#6-docker-部署-deployment)

---

## 1. 服务定位 Service Scope

`server/` 是对图能力的 REST 化封装，适用于：

1. 非 MCP 场景的业务系统调用。
2. 传统后端服务通过 HTTP 接入图记忆。
3. 内部网关/中台统一接入图检索能力。

---

## 2. 功能清单 Features

- 写入消息为 Episode（异步队列）
- 新增实体节点
- 查询事实、边、历史 episode
- 清理分组数据与全量图数据
- 服务探针：`/healthcheck`、`/live`、`/ready`、`/metrics`

---

## 3. 快速开始 Quick Start

```bash
cd server
cp .env.example .env
uv sync
uv run uvicorn graph_service.main:app --host 0.0.0.0 --port 8000
```

启动后访问：

- OpenAPI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 4. 配置说明 Configuration

`.env` 示例（本地 Ollama + Neo4j）：

```env
OPENAI_API_KEY=ollama
OPENAI_BASE_URL=http://127.0.0.1:11434/v1
MODEL_NAME=gpt-oss:20b
EMBEDDING_MODEL_NAME=text-embedding-3-small

NEO4J_URI=bolt://127.0.0.1:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=change-me
```

建议：

1. 生产环境通过 Secret Manager 注入密钥。
2. 将 `NEO4J_PASSWORD` 改为强密码并定期轮换。

---

## 5. 接口与探针 API & Probes

### 5.1 核心接口

- `POST /messages`
- `POST /entity-node`
- `POST /search`
- `POST /get-memory`
- `GET /episodes/{group_id}`

### 5.2 运行探针

- `GET /healthcheck`：基础健康检查
- `GET /live`：进程存活探针
- `GET /ready`：数据库可用性探针
- `GET /metrics`：Prometheus 风格基础指标

---

## 6. Docker 部署 Deployment

建议与 Neo4j 一起编排，示例：

```yaml
services:
  graph-service:
    build: ./server
    ports:
      - "8000:8000"
    env_file:
      - ./server/.env

  neo4j:
    image: neo4j:5.22.0
    environment:
      - NEO4J_AUTH=neo4j/change-me
    ports:
      - "7474:7474"
      - "7687:7687"
```
