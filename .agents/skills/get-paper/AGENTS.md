# AGENTS.md — Wiki get-paper 技能目录

本目录实现 `get-paper`：围绕主任务跨 arXiv、OpenAlex、Crossref、Semantic Scholar
检索论文，并优先安全获取开放的 arXiv LaTeX 源码或 OA PDF。`SKILL.md` 是流程权威；
`scripts/get-paper.py` 是标准库 CLI，`scripts/test_get_paper.py` 覆盖标识符解析、
相关性排序、去重、主 TeX 识别、路径穿越拒绝、OA/HTTPS 边界、事务解包、缓存树哈希
和跨源故障隔离。

研究原件进入 `raw/papers/gpt/query/`，临时运行结果进入 `tmp/runs/get-paper/`；
归档必须附 `manifest.json` 并通过 `wiki_archive_gate.py`。不绕过付费墙，不执行下载
论文中的代码，不写入凭据或 Wiki 外部配置。来源、许可和适配记录见 `PROVENANCE.md`
与 `references/sources.md`。
