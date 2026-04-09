# 组合镜像说明 FalkorDB + MCP Combined Image

该部署模式将 FalkorDB 与 Graphiti Custom MCP Server 打包到同一容器，适合本地开发、演示和单机部署。

---

## 目录 Contents

- [1. 服务组成 Architecture](#1-服务组成-architecture)
- [2. 快速启动 Quick Start](#2-快速启动-quick-start)
- [3. 构建镜像 Build](#3-构建镜像-build)
- [4. 关键配置 Configuration](#4-关键配置-configuration)
- [5. 健康检查 Health](#5-健康检查-health)
- [6. 常见问题 Troubleshooting](#6-常见问题-troubleshooting)

---

## 1. 服务组成 Architecture

单容器内包含三部分：

1. FalkorDB（端口 `6379`）
2. FalkorDB Browser（端口 `3000`，可关闭）
3. MCP Server（端口 `8000`）

适配场景：

- 快速验证功能
- 本地开发联调
- 单机轻量部署

---

## 2. 快速启动 Quick Start

### 2.1 Docker Compose

```bash
cd mcp_server
docker compose -f docker/docker-compose-falkordb-combined.yml up
```

### 2.2 docker run

```bash
docker run -d \
  -p 6379:6379 \
  -p 3000:3000 \
  -p 8000:8000 \
  -e OPENAI_API_KEY=ollama \
  -e OPENAI_API_URL=http://host.docker.internal:11434/v1 \
  -v falkordb_data:/var/lib/falkordb/data \
  your-org/your-repo-falkordb:latest
```

访问地址：

- MCP: `http://127.0.0.1:8000/mcp/`
- Health: `http://127.0.0.1:8000/health`
- Browser: `http://127.0.0.1:3000`

---

## 3. 构建镜像 Build

```bash
# 默认版本
docker compose -f docker/docker-compose-falkordb-combined.yml build

# 指定 graphiti-core 版本
GRAPHITI_CORE_VERSION=0.28.2 docker compose -f docker/docker-compose-falkordb-combined.yml build
```

常用 build args：

- `GRAPHITI_CORE_VERSION`
- `MCP_SERVER_VERSION`
- `BUILD_DATE`
- `VCS_REF`

---

## 4. 关键配置 Configuration

推荐环境变量：

```env
OPENAI_API_KEY=ollama
OPENAI_API_URL=http://host.docker.internal:11434/v1
GRAPHITI_GROUP_ID=main
SEMAPHORE_LIMIT=10
FALKORDB_PASSWORD=
FALKORDB_DATABASE=default_db
BROWSER=1
```

如果不需要 Browser，可设置：

```env
BROWSER=0
```

---

## 5. 健康检查 Health

组合镜像默认可通过以下命令校验：

```bash
docker compose -f docker/docker-compose-falkordb-combined.yml ps
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/ready
curl http://127.0.0.1:8000/metrics
```

---

## 6. 常见问题 Troubleshooting

1. MCP 启动失败：检查 `OPENAI_API_URL` 与密钥配置。  
2. Browser 无法访问：确认 `BROWSER=1` 且 `3000` 端口未被占用。  
3. 数据不持久：确认已挂载 `falkordb_data` volume。  
4. 端口冲突：修改 compose 端口映射。  
5. 并发过高导致限流：降低 `SEMAPHORE_LIMIT`。  
