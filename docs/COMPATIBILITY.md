# 兼容矩阵 Compatibility Matrix

## 运行时兼容性

| 组件 | 支持版本 | 备注 |
|---|---|---|
| Python | 3.10+ | 推荐 3.11 |
| Neo4j | 5.26+ | `bolt://` 连接 |
| FalkorDB | 1.1.2+ | 默认后端 |
| MCP Transport | `http` / `stdio` | `sse` 已标注 deprecated |

## LLM 与 Embedding

| 类型 | 支持供应商 | 说明 |
|---|---|---|
| LLM | OpenAI / Azure OpenAI / Anthropic / Gemini / Groq | OpenAI 兼容端点支持自动 `/v1` 补全 |
| Embedder | OpenAI / Azure OpenAI / Gemini / Voyage | 支持本地 OpenAI 兼容接口 |

## 部署模式

| 模式 | 推荐场景 | 备注 |
|---|---|---|
| 本地进程 | 开发调试 | 配合 `.env` |
| Docker 组合镜像 | 单机演示 | FalkorDB + MCP |
| Docker 分容器 | 生产预备 | Neo4j 可独立扩缩 |
