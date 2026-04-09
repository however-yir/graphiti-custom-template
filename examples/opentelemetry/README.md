# 可观测性示例 OpenTelemetry Tracing

该示例用于演示 Graphiti 与 OpenTelemetry 集成，将 trace span 直接输出到 stdout。

---

## 目录 Contents

- [1. 使用场景 Use Cases](#1-使用场景-use-cases)
- [2. 运行步骤 Run](#2-运行步骤-run)
- [3. 关键代码 Key Snippet](#3-关键代码-key-snippet)

---

## 1. 使用场景 Use Cases

- 本地调试链路耗时
- 验证 episode 写入与检索路径
- 快速接入可观测性体系前的预演

---

## 2. 运行步骤 Run

```bash
cd examples/opentelemetry
uv sync
export OPENAI_API_KEY=ollama
export OPENAI_API_URL=http://127.0.0.1:11434/v1
uv run otel_stdout_example.py
```

---

## 3. 关键代码 Key Snippet

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)
```

