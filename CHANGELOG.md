# 更新日志 Changelog

本项目遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 规范，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added
- 新增 `PROJECT_TERMS.md` 项目使用协议。
- 新增仓库元数据模板 `.github/settings.yml`（名称、描述、topics）。
- 新增主项目 Logo：`images/graphiti-custom-logo.svg`。
- 新增 `mcp_server/.env.example` 与统一环境变量模板。
- 新增 OpenAI 兼容端点单测：`mcp_server/tests/test_openai_compatibility.py`。
- 新增 MCP 服务运维端点：`/live`、`/ready`、`/metrics`。
- 新增 server 服务运维端点：`/live`、`/ready`、`/metrics`。
- 新增发布说明模板：`.github/RELEASE_TEMPLATE.md`。
- 新增版本发布草稿脚本：`scripts/generate_release_notes.sh`。

### Changed
- 根 `README.md` 重写为中文主导、中英结合风格，并补充改造说明。
- `mcp_server/README.md` 重写为中文主导风格。
- `server/README.md`、`mcp_server/docker/README*.md`、`mcp_server/tests/README.md` 与 examples 子目录 README 统一为中文风格。
- 包名与项目元数据品牌化：
  - `graphiti-core` -> `graphiti-custom-core`
  - `mcp-server` -> `graphiti-custom-mcp-server`
  - `graph-service` -> `graphiti-custom-server`
- `mcp_server` OpenAI/Embedder 工厂增强：
  - 自动标准化 OpenAI 兼容 `base_url`（补全 `/v1`）
  - 本地端点支持无 key 回退（默认 `ollama`）
  - 透传 `organization_id`
- `mcp_server/config/config.yaml` 与根 `.env.example` 全面改为本地优先模板。
- `mcp_server` 依赖补齐 `python-dotenv`。
- server 代码命名去 `Zep` 化，统一为 `CustomGraphiti` 语义。

### Fixed
- 修复本地运行 `mcp_server/main.py` 时根目录模块导入路径兼容问题（自动注入 repo root 到 `sys.path`）。

### Security
- 移除文档中的硬编码敏感配置示例，统一改为环境变量占位符。
