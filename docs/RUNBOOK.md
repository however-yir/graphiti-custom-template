# 运行手册 Runbook

## 1. 启动前检查

1. 确认图数据库可连接（Neo4j / FalkorDB）。
2. 确认模型服务可调用（OpenAI 或本地 Ollama）。
3. 检查 `.env` 是否包含必需变量。

## 2. 启动命令

### MCP Server

```bash
cd mcp_server
uv run main.py --transport http
```

### Graph Service

```bash
cd server
uv run uvicorn graph_service.main:app --host 0.0.0.0 --port 8000
```

## 3. 健康检查

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/live
curl http://127.0.0.1:8000/ready
curl http://127.0.0.1:8000/metrics
```

## 4. 常见故障与处理

1. `not_ready`：优先检查数据库连通性。
2. `429`：降低 `SEMAPHORE_LIMIT`。
3. MCP 工具返回空：检查 `group_id` 与 episode 是否写入成功。
4. 本地 Ollama 调用失败：确认 `OPENAI_API_URL` 与模型名。

## 5. 发布前检查

1. 更新 `CHANGELOG.md`。
2. 使用 `scripts/generate_release_notes.sh` 生成发布草稿。
3. 运行关键测试（至少兼容性单测 + 集成冒烟）。
