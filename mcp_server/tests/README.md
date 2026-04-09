# 测试套件说明 MCP Server Tests

本目录用于验证 `Graphiti Custom MCP Server` 的配置加载、协议兼容、并发行为与压力表现。

---

## 目录 Contents

- [1. 测试结构 Test Modules](#1-测试结构-test-modules)
- [2. 运行前准备 Prerequisites](#2-运行前准备-prerequisites)
- [3. 运行方式 How to Run](#3-运行方式-how-to-run)
- [4. 常用测试组合 Common Suites](#4-常用测试组合-common-suites)
- [5. 环境变量 Environment](#5-环境变量-environment)

---

## 1. 测试结构 Test Modules

核心文件：

- `test_openai_compatibility.py`：OpenAI 兼容端点与本地回退单测
- `test_configuration.py`：配置加载与工厂构造测试
- `test_mcp_integration.py`：MCP 工具集成测试
- `test_async_operations.py`：异步并发行为验证
- `test_stress_load.py`：压力与负载测试
- `run_tests.py`：测试入口脚本

---

## 2. 运行前准备 Prerequisites

```bash
cd mcp_server
uv sync
```

如需真实模型调用，请配置 `.env` 或环境变量中的 API Key。

---

## 3. 运行方式 How to Run

### 3.1 快速验证

```bash
uv run pytest -q tests/test_openai_compatibility.py
```

### 3.2 按套件执行

```bash
python tests/run_tests.py smoke
python tests/run_tests.py integration
python tests/run_tests.py stress --parallel 4
```

### 3.3 全量执行

```bash
python tests/run_tests.py all
```

---

## 4. 常用测试组合 Common Suites

1. 本地开发最小回归：
   - `test_openai_compatibility.py`
   - `test_configuration.py`
2. 数据库联调回归：
   - `integration --database neo4j`
3. 压测前检查：
   - `smoke` + `async`

---

## 5. 环境变量 Environment

```bash
# Database
export DATABASE_PROVIDER=falkordb
export FALKORDB_URI=redis://localhost:6379
# or
export DATABASE_PROVIDER=neo4j
export NEO4J_URI=bolt://localhost:7687
export NEO4J_USER=neo4j
export NEO4J_PASSWORD=change-me

# LLM
export OPENAI_API_KEY=ollama
export OPENAI_API_URL=http://localhost:11434/v1
```

提示：压力测试会产生较多调用，建议先设置低并发验证。

