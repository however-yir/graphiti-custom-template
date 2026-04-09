# 容器化部署指南 Docker Deployment Guide

本目录提供 `Graphiti Custom MCP Server` 的 Docker 编排方案，支持两种后端：

1. FalkorDB（默认，组合镜像）
2. Neo4j（分容器部署）

---

## 目录 Contents

- [1. 快速开始 Quick Start](#1-快速开始-quick-start)
- [2. 环境变量 Environment](#2-环境变量-environment)
- [3. 数据库模式 Database Modes](#3-数据库模式-database-modes)
- [4. 运维命令 Operations](#4-运维命令-operations)
- [5. 故障排查 Troubleshooting](#5-故障排查-troubleshooting)
- [6. 生产建议 Production Notes](#6-生产建议-production-notes)

---

## 1. 快速开始 Quick Start

```bash
# 默认：FalkorDB 组合镜像
docker compose up

# Neo4j 分容器

docker compose -f docker-compose-neo4j.yml up
```

默认地址：

- MCP Endpoint: `http://127.0.0.1:8000/mcp/`
- 健康检查: `http://127.0.0.1:8000/health`
- 就绪检查: `http://127.0.0.1:8000/ready`
- 指标输出: `http://127.0.0.1:8000/metrics`

---

## 2. 环境变量 Environment

建议在本目录创建 `.env`：

```env
OPENAI_API_KEY=ollama
OPENAI_API_URL=http://host.docker.internal:11434/v1
GRAPHITI_GROUP_ID=main
SEMAPHORE_LIMIT=10
```

如使用云模型，将 `OPENAI_API_KEY` 替换为真实 key，并将 `OPENAI_API_URL` 指向云服务地址。

---

## 3. 数据库模式 Database Modes

### 3.1 FalkorDB（默认）

- Compose 文件：`docker-compose.yml`
- 特点：部署简单、单容器整合、适合本地与中小规模场景

示例变量：

```env
DATABASE_PROVIDER=falkordb
FALKORDB_URI=redis://localhost:6379
FALKORDB_PASSWORD=
FALKORDB_DATABASE=default_db
```

### 3.2 Neo4j（独立容器）

- Compose 文件：`docker-compose-neo4j.yml`
- 特点：更完整图数据库能力，适合生产化治理

示例变量：

```env
DATABASE_PROVIDER=neo4j
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=change-me
NEO4J_DATABASE=neo4j
```

---

## 4. 运维命令 Operations

### 4.1 查看日志

```bash
docker compose logs -f graphiti-mcp
```

### 4.2 查看容器健康状态

```bash
docker compose ps
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/ready
```

### 4.3 切换数据库后端

```bash
# 关闭当前
docker compose down

# 启动目标后端
docker compose up
# or
docker compose -f docker-compose-neo4j.yml up
```

---

## 5. 故障排查 Troubleshooting

1. `8000` 端口冲突：修改 compose 端口映射。  
2. MCP 无法连接数据库：检查 `DATABASE_PROVIDER` 与连接 URI。  
3. `429` 限流：降低 `SEMAPHORE_LIMIT`。  
4. Neo4j 启动慢：等待健康检查通过再发请求。  
5. 本地 Ollama 容器不可达：确认 `OPENAI_API_URL` 使用 `host.docker.internal`。  

---

## 6. 生产建议 Production Notes

1. 开启持久卷并制定备份策略。  
2. 对 `OPENAI_API_KEY`、`NEO4J_PASSWORD` 做密钥托管。  
3. 将 `/metrics` 接入监控系统。  
4. 设置资源限额（CPU/内存）与重启策略。  
5. 发布前执行 `CHANGELOG` 与发布清单校验。  

