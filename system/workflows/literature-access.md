---
type: system-workflow
graph-excluded: true
updated: 2026-10-24
---

# 文献检索与访问配置

## Web of Science

用户于 2026-10-24 授权接入 Web of Science。凭据保存在仓库内 `raw/personal/.env` 的 `WEB_OF_SCIENCE_API_KEY`，该文件由 Git 忽略。文档、回执和命令行参数只记录变量名，不记录值。

`system/scripts/run_paper_search_mcp.py` 在现有 Paper Search MCP 启动器之前运行，将该变量映射为插件读取的 `WOS_API_KEY`。优先使用已有非空 `WOS_API_KEY`，其次使用进程环境中的 `WEB_OF_SCIENCE_API_KEY`，最后读取上述文件。只解析这一项，不执行 `.env`，不加载其它凭据。

本地 MCP 配置的 `paper-search-nodejs` 使用以下结构（路径替换为实际安装位置）：

```toml
[mcp_servers.paper-search-nodejs]
command = "/usr/bin/python3"
args = ["<wiki>/system/scripts/run_paper_search_mcp.py", "<paper-search-install>/launch_mcp.py"]
```

已运行的 MCP 进程不会热加载；新会话或重启该 MCP 后生效。此轮仅完成配置接线，未发起联网检索，API 有效性、订阅权限和额度尚未验证。

## 检索路由

- 核结构文献仍先用 `nature-academic-search` 查询 Crossref/arXiv；需要 WoS 收录信息、引用计数或补充检索时，使用 `paper-search-nodejs.search_webofscience`，默认 `apiProduct: "starter"`。
- 示例参数：`{"query":"DO=10.1103/PhysRevC.100.024314","maxResults":1,"apiProduct":"starter","discoverAccess":false}`。不要把密钥放入工具参数。
- 引用计数记录数据库、查询时间和论文 DOI/UID；不同库计数不直接合并。Starter 的检索及计数不代表拥有完整引文关系权限。
- Expanded 必须另有明确的订阅授权与 `WOS_EXPANDED_API_KEY` 配置，才调用 Expanded 或 `get_webofscience_related_records`；不能由通用密钥存在推定已开通。
- 遇到 401/403，记录认证或权限失败并换用 Crossref、arXiv、OpenAlex 等可用入口；429 按服务限流退避，不反复消耗额度。

## 全文访问与归档

WoS 用于发现文献、书目核对和授权范围内的引文信息，不提供出版商全文访问授权。取得 DOI/出版商链接后按既有 Nature-first 流程补查 Scholar，使用 `nature-downloader` 获取公开或已有授权的全文。候选 PDF 在 `raw/papers/gpt/_incoming/<run-id>/` 核对身份与哈希后归档；去凭据获取记录保存到 `outputs/literature-acquisition/`。科学结论仍回到原文和 `knowledge/sources/`。
