# 快速入门示例 Graphiti Quickstart

本示例展示如何使用 Graphiti 完成从“连接数据库 -> 写入 Episode -> 检索事实/节点”的完整最小链路。

---

## 目录 Contents

- [1. 示例覆盖能力 Scope](#1-示例覆盖能力-scope)
- [2. 环境要求 Prerequisites](#2-环境要求-prerequisites)
- [3. 运行步骤 Run Steps](#3-运行步骤-run-steps)
- [4. 输出解读 Output](#4-输出解读-output)
- [5. 常见问题 Troubleshooting](#5-常见问题-troubleshooting)

---

## 1. 示例覆盖能力 Scope

- 连接 Neo4j / FalkorDB / Neptune
- 初始化图索引与约束
- 写入文本 episode
- 混合检索（语义 + 关键词）
- 基于中心节点的图距离重排
- 节点检索 recipe 示例

---

## 2. 环境要求 Prerequisites

- Python `3.10+`
- 可用图数据库（Neo4j 或 FalkorDB）
- OpenAI 兼容 API（本地 Ollama 或云模型）

---

## 3. 运行步骤 Run Steps

```bash
# 安装依赖
pip install graphiti-core

# 基础环境变量
export OPENAI_API_KEY=ollama
export OPENAI_API_URL=http://127.0.0.1:11434/v1

# Neo4j
export NEO4J_URI=bolt://localhost:7687
export NEO4J_USER=neo4j
export NEO4J_PASSWORD=change-me

# FalkorDB（可选）
export FALKORDB_URI=redis://localhost:6379
```

执行示例：

```bash
python quickstart_neo4j.py
# or
python quickstart_falkordb.py
# or
python quickstart_neptune.py
```

---

## 4. 输出解读 Output

检索结果通常包含：

- `fact`：抽取出的事实文本
- `uuid`：边或节点的唯一标识
- `valid_at/invalid_at`：事实时序窗口
- `source/target node`：实体关系方向

---

## 5. 常见问题 Troubleshooting

1. `Graph not found`：检查 Neo4j database 名称。  
2. 检索为空：确认已成功写入 episode 且 embedding 服务可用。  
3. 本地模型调用失败：检查 `OPENAI_API_URL` 与模型名。  
4. Neptune 参数错误：确认 host 协议前缀与端口。  

