---
type: system-workflow
graph-excluded: true
updated: 2026-10-27
---

# 文献检索与访问配置

## Web of Science

用户于 2026-10-24 授权接入 Web of Science。凭据保存在仓库内 `raw/personal/.env` 的 `WEB_OF_SCIENCE_API_KEY`，该文件由 Git 忽略。文档、回执和命令行参数只记录变量名，不记录值。

`system/scripts/run_paper_search_mcp.py` 在现有 Paper Search MCP 启动器之前运行，将该变量映射为插件读取的 `WOS_API_KEY`。优先使用已有非空 `WOS_API_KEY`，其次使用进程环境中的 `WEB_OF_SCIENCE_API_KEY`，最后读取上述文件。只解析下述白名单，不执行 `.env`。

同一包装器还按白名单读取 `ELSEVIER_API_KEY`，其它 dotenv 项不会加载。Springer 的两个变量分别映射为插件读取的 `SPRINGER_API_KEY` 与 `SPRINGER_OPENACCESS_API_KEY`。本地 MCP 配置的 `paper-search-nodejs` 使用以下结构（路径替换为实际安装位置）：

```toml
[mcp_servers.paper-search-nodejs]
command = "/usr/bin/python3"
args = ["<wiki>/system/scripts/run_paper_search_mcp.py", "<paper-search-install>/launch_mcp.py"]
```

已运行的 MCP 进程不会热加载；新会话或重启该 MCP 后生效。2026-10-24 实测 Starter 返回 HTTP 200，精确 DOI 查询取得 1 条记录；响应头限额为每日 50 次、每秒 1 次，本次请求后当天剩余 49 次。相同密钥请求 Expanded 返回 HTTP 403（`You cannot consume this service`），当前无该产品访问权限。去凭据回执见 [权限测试](../../outputs/literature-acquisition/20261024-webofscience-api-permissions-072448.json)。剩余额度只是查询时快照；测试为直接调用官方 API，未覆盖既有会话 MCP 的热加载。

## 检索路由

- 核结构文献仍先用 `nature-academic-search` 查询 Crossref/arXiv；需要 WoS 收录信息、引用计数或补充检索时，使用 `paper-search-nodejs.search_webofscience`，默认 `apiProduct: "starter"`。
- 示例参数：`{"query":"DO=10.1103/PhysRevC.100.024314","maxResults":1,"apiProduct":"starter","discoverAccess":false}`。不要把密钥放入工具参数。
- 引用计数记录数据库、查询时间和论文 DOI/UID；不同库计数不直接合并。Starter 的检索及计数不代表拥有完整引文关系权限。
- Expanded 必须另有明确的订阅授权与 `WOS_EXPANDED_API_KEY` 配置，才调用 Expanded 或 `get_webofscience_related_records`；不能由通用密钥存在推定已开通。
- 遇到 401/403，记录认证或权限失败并换用 Crossref、arXiv、OpenAlex 等可用入口；429 按服务限流退避，不反复消耗额度。

## Elsevier（2026-10-26）

用户提供的 `ELSEVIER_API_KEY` 位于仓库内 `raw/personal/.env`（不是根目录 `personal/.env`）。已接入三处：

- Paper Search MCP：由 `run_paper_search_mcp.py` 在启动时读取并传给 ScienceDirect/Scopus 适配器。
- `nature-downloader`：通过自带 `configure_credentials.py set elsevier --stdin` 写入本机 `~/.config/lit-dl/credentials.json`，权限 `0600`。
- Academic Search MCP：本机 `~/.config/pybliometrics.cfg` 已配置，权限 `0600`，补齐此前缺配置的 ScienceDirect/Scopus 路线。

后两者为私有配置副本，更换 dotenv 中的 key 后应同步更新；不得把密钥放入命令参数、Wiki 文档或 Git。2026-10-26 应用户要求实测：Larsson1978 的文章 META 返回 200，PDF 接口返回 200/application/pdf 且 `%PDF-` 文件头有效（仅探测开头，未重复下载全文）；Scopus DOI 检索返回 200、1 条结果。结果仅覆盖该论文和所测接口，不代表全部全文或其它 Scopus 产品权限；配额头当时报告 limit/remaining 均为 20000，不能解读成每日限额。详见 [权限回执](../../outputs/literature-acquisition/20261026-elsevier-api-permissions.json)。新启动 MCP 已实测识别密钥，pybliometrics 本地初始化通过；正在运行的每日学习进程未重启。

## Springer Nature（2026-10-27）

用户提供了 `SPRINGER_META_API_KEY` 与 `SPRINGER_OPEN_ACCESS_API_KEY`，已接入 Paper Search MCP；`nature-downloader` 私有凭据按服务写入 `~/.config/lit-dl/credentials.json` 的 `springer_nature.metadata_api_key` 与 `springer_nature.openaccess_api_key`，权限 0600。旧的通用 `springer_nature.api_key` 已移除，避免把 Meta key 当成 Full Text 授权。两把 key 不写入 Wiki。

实测 `https://api.springernature.com/meta/v2/json` 与 `https://api.springernature.com/openaccess/json` 各一次，均 HTTP 200，分别返回 1 条记录；查询词为 `keyword:nuclear`。本次响应没有账户额度头。用户提供的账户配额为 **500 hits/day、100 hits/min**；这条配额信息来自用户，不是响应头推断。Paper Search 代码内置约 3 次/分钟和 5000/日的本地保护计数，属于客户端保护，实际调用仍应遵守账户的 100/min、500/day。权限回执见 [Springer 测试](../../outputs/literature-acquisition/20261027-springer-api-permissions.json)。

Meta/OA 检索成功不等于任意 Springer 论文均有 PDF 权限；全文仍需文章级 OA、JATS/API 返回或合法机构访问。Nature downloader 的 metadata/openaccess 校验均返回 HTTP 200；没有 `fulltext_api_key`，因此不宣称 Springer Full Text API 已开通。新 MCP 进程加载配置，旧进程不热加载。

## Paper Search 下载目录（2026-10-26 修正）

该插件的路径校验使用相对当前工作目录的 `./downloads`，仅设置 `DEFAULT_DOWNLOAD_PATH` 不生效。原启动器切换到安装目录，导致 Wiki 内的 `savePath` 被判越界。

本机 `launch_mcp.py` 现从包装器的 `WIKI_PAPER_SEARCH_WORKDIR` 读取工作目录（本项目为 `raw/papers/gpt/_incoming`），创建其 `downloads` 子目录，并将 `DEFAULT_DOWNLOAD_PATH` 同步为该绝对路径；Node 入口仍用安装目录的绝对路径。恢复安装时须同时保留这项启动器配置。

调用时使用 `savePath: "/workspace/wiki/raw/papers/gpt/_incoming/downloads/<run-id>"`，或相对于该 downloads 根的 run 子目录。`tmp/day23-originals/...` 和仓库外路径仍不属于允许目录，需改用上述入口；路径及符号链接越界检查保留。每次使用独立 run 子目录，核验后再归档，避免覆盖已有原件。当前会话的旧 MCP 不热加载，下一会话生效；本轮未发起实际下载。已用插件实际路径校验函数核对：绝对/相对隔离区子路径允许，旧 tmp 路径、仓库外路径和目录穿越拒绝，详见 [路径回执](../../outputs/literature-acquisition/20261026-download-path-check.json)。

## 全文访问与归档

`daily-learning` 的用户长期授权已包含应读正文、SI和必要附件/数据/代码等资源；默认自主获取并核验，不再询问是否下载或是否需要SI。下载器要求SI flag时直接用 `--si`；这是已重申的每日学习规则，见 [continuous learning](continuous-learning.md#每日学习的资源获取默认) 与 `system/memory.md`，覆盖外部skill的通用SI询问步骤。

WoS 用于发现文献、书目核对和授权范围内的引文信息，不提供出版商全文访问授权。取得 DOI/出版商链接后按既有 Nature-first 流程补查 Scholar，使用 `nature-downloader` 获取公开或已有授权的全文。候选 PDF 在 `raw/papers/gpt/_incoming/<run-id>/` 核对身份与哈希后归档；去凭据获取记录保存到 `outputs/literature-acquisition/`。科学结论仍回到原文和 `knowledge/sources/`。
