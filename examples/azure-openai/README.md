# Azure OpenAI 示例 Azure OpenAI + Neo4j

该示例演示在 Graphiti 中使用 Azure OpenAI（OpenAI v1 兼容接口）与 Neo4j 构建时序图记忆。

---

## 目录 Contents

- [1. 前置条件 Prerequisites](#1-前置条件-prerequisites)
- [2. 环境配置 Setup](#2-环境配置-setup)
- [3. 运行示例 Run](#3-运行示例-run)
- [4. 示例流程 Workflow](#4-示例流程-workflow)
- [5. 常见问题 Troubleshooting](#5-常见问题-troubleshooting)

---

## 1. 前置条件 Prerequisites

- Python 3.10+
- Neo4j 可用实例
- Azure OpenAI 已部署 Chat 模型与 Embedding 模型

---

## 2. 环境配置 Setup

```bash
cd examples/azure-openai
cp .env.example .env
```

`.env` 关键项：

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=change-me

AZURE_OPENAI_ENDPOINT=https://<resource>.openai.azure.com
AZURE_OPENAI_API_KEY=<your-key>
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

---

## 3. 运行示例 Run

```bash
uv sync
uv run azure_openai_neo4j.py
```

---

## 4. 示例流程 Workflow

1. 初始化 Neo4j 与 Azure OpenAI 客户端。  
2. 写入文本与 JSON episode。  
3. 执行混合检索与中心节点重排。  
4. 输出检索结果并关闭连接。  

---

## 5. 常见问题 Troubleshooting

1. 401/403：检查 Azure API Key 与 endpoint。  
2. deployment not found：确认 deployment 名称与模型已发布。  
3. Neo4j 连接失败：确认 URI 与认证信息。  
4. v1 接口异常：确认 endpoint 最终为 `/openai/v1/`。  

