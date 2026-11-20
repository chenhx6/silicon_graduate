---
type: source
title: "PyPA、PyPI 与 Qt 元数据：PDM 的 Python 包分发依据"
title_original: "Packaging Python Projects; Entry Points Specification; PyPI Upload API and Project Metadata"
year: 2026
aliases: [PDM PyPI packaging]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: technical-documentation
reading_depth: skimmed
canonical_source: "PyPA packaging tutorial and entry-point specification; PyPI upload documentation and public project metadata, retrieved 2026-11-20"
raw_file: "raw/papers/gpt/query/20261120-pdm-pypi-packaging/manifest.json"
raw_sha256: "2241ec74fd9046dda087c26c12aac407c6abb785622c74f28480979869d4a867"
archive_required: true
tags: [python, packaging, pypi, pdm-software]
---

# PDM 的 Python 包分发依据

## Bibliographic Record

- PyPA, Packaging Python Projects: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- PyPA, Entry Points Specification: https://packaging.python.org/en/latest/specifications/entry-points/
- PyPI, Upload API: https://docs.pypi.org/api/upload/
- PyPI public JSON metadata: https://pypi.org/pypi/pdm/json , https://pypi.org/pypi/PySide6/json , https://pypi.org/pypi/PySide6-Essentials/json .
- 名称探测 https://pypi.org/pypi/multipolePDM/json 在本次返回404；仅保存状态记录，不把它称为已取得项目元数据或已保留名称。

## Scope and Reading Depth

本页保留实施前技术预查的原件范围。定向核对 wheel/sdist、GUI entry point、上传接口和依赖元数据。此预查阶段未上传PDM、未验证账号发布权限、未进行Windows/macOS运行测试。技术网页和JSON原件按主题留档；本页不包含任何API key。

## Key Results

本节官方接口说明的 `claim_kind=technical-specification`、`evidence_level=official-documentation`；`locator` 为各条明确列出的教程章节或JSON字段。平台方案属于本任务设计推断，不是跨平台实测。

- PyPA教程“Generating distribution archives”示例说明：兼容各平台的纯Python项目可只提供一个 `py3-none-any.whl`，另配sdist；这不意味着其依赖也是纯Python，也不意味着所有系统已实际验证。
- Entry Points的“Entry points for scripts”规定 `console_scripts` / `gui_scripts` 安装后生成启动入口；二者的区别主要在Windows控制台行为。PDM可使用 `pdm-gui`，不必自己制作四套原生安装包。
- `pdm-project.json` 的 `info.name`/`info.summary` 显示 `pdm` 已是一个Python项目/依赖管理工具；不能将该PyPI名称用于本研究的新项目。
- `multipolePDM` 本次JSON查询404只说明查询时未找到；正式发布前仍要复查，PyPI可保留或拒绝某些名称，404不是占名成功。
- PySide6项目JSON列出平台wheel及多个二进制相关依赖。自己的PDM wheel可为纯Python，但Qt、NumPy、SciPy等依赖仍需pip选择兼容版本/平台wheel。只使用QtCore/QtGui/QtWidgets时，可评估直接依赖PySide6-Essentials，避免不需要的WebEngine等组件；这是本任务的软件设计建议，不是已测兼容结论。
- 上传API是发布操作；读取公开元数据不验证上传token权限。发布测试应针对验收合格的真实制品，不上传无意义占位包。TestPyPI与生产PyPI的账号/token和入口不能混用。

## Summary

一套通用Python wheel、明确的GUI入口和由pip解析的平台依赖，可以减少PDM自行制作原生安装包的工作。发布仍需真实制品、权限与安装验证，名称404查询和本地token存在性都不能代替发布成功的证据。

## Competing Interpretations and Limitations

PyPI分发减少自建原生包负担，但需要用户拥有支持的Python并进行一次安装；它不是“不安装Python即可解压双击”的同义词。平台兼容性仍受Qt、科学库和系统库限制。已下载元数据不等于下载/安装/运行了其中任何发行档。

## Extracted Pages

PDM执行合同见 [[pdm-three-mode-execution-contract-20261120]]。原始文件、请求URL、文件大小、获取时间和哈希见归档manifest；本次没有向外部发送私有凭据。
