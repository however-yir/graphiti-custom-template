# 本地实体抽取示例 GLiNER2 Hybrid Client

该示例演示 GLiNER2 与通用 LLM 的混合模式：

- GLiNER2 本地执行实体抽取（NER）
- 通用 LLM 负责事实抽取、去重、摘要等推理任务

---

## 目录 Contents

- [1. 前置条件 Prerequisites](#1-前置条件-prerequisites)
- [2. 安装与配置 Setup](#2-安装与配置-setup)
- [3. 运行方式 Run](#3-运行方式-run)
- [4. 可调参数 Tunables](#4-可调参数-tunables)

---

## 1. 前置条件 Prerequisites

- Python 3.11+
- Neo4j 5.26+
- 任一 LLM 供应商 API Key（OpenAI/Gemini/Anthropic 等）

---

## 2. 安装与配置 Setup

```bash
pip install graphiti-core[gliner2]
cp .env.example .env
```

首次运行会自动下载 GLiNER2 模型权重。

---

## 3. 运行方式 Run

```bash
python gliner2_neo4j.py
```

---

## 4. 可调参数 Tunables

| 参数 | 说明 | 默认值 |
|---|---|---|
| `threshold` | GLiNER2 置信度阈值（越高越保守） | `0.5` |
| `GLINER2_MODEL` | HuggingFace 模型 ID | `fastino/gliner2-large-v1` |

参考：

- 论文: [GLiNER2](https://arxiv.org/abs/2507.18546)
- 模型: [fastino/gliner2-large-v1](https://huggingface.co/fastino/gliner2-large-v1)

