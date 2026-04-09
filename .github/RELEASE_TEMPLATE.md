# 发布说明模板 Release Notes Template

## 版本信息 Version

- 版本号: `vX.Y.Z`
- 发布日期: `YYYY-MM-DD`
- 发布类型: `Major / Minor / Patch`

## 一句话概述 Summary

本版本聚焦于：`一句话描述本次发版目标`。

## 重点改动 Highlights

1. `关键能力点 1`
2. `关键能力点 2`
3. `关键能力点 3`

## 详细变更 Details

### Added
- 

### Changed
- 

### Fixed
- 

### Security
- 

## 升级说明 Upgrade Guide

1. 配置变更：
   - `需要新增/修改的环境变量`
2. 依赖变更：
   - `需要升级/替换的依赖`
3. 数据变更：
   - `数据库迁移或索引重建步骤`

## 兼容性 Compatibility

- Python: `>=3.10`
- Graph DB: `Neo4j / FalkorDB`
- MCP Transport: `http / stdio`

## 验证清单 Validation Checklist

- [ ] 单元测试通过
- [ ] 集成测试通过
- [ ] 关键接口冒烟通过
- [ ] 文档已同步更新
- [ ] 无敏感信息泄露

## 相关链接 Links

- Changelog: `./CHANGELOG.md`
- Compare: `https://github.com/<owner>/<repo>/compare/<prev>...<new>`
- Docker Image: `<image>:<tag>`
