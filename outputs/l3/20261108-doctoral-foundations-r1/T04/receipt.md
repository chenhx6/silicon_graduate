# T04 独立原件核查回执

- 日期：2026-11-08；任务类型：phase 1、独立复杂理论审核。无委派、无 Git 操作、无大规模模拟或文献下载。
- 顺序：先读 README、索引及相关 profile/skill，再从原始 PDF 和静态 LaTeX 核公式、能量、表格及数值；完成独立判断后读取既有 G34 source 的元数据并链接。未读取 G34 研究草稿结论，未修改 G34 文件。
- 原件：`raw/papers/gpt/query/20261108-foundations-G34/Zhi_2013_PRC_87_025803_SM_halflives_first_forbidden.pdf`；PDF 14 页、440775 bytes，SHA-256 `eaedbd4539854e3d1f0e7860ef7ab9c647d4fa44cd8144b4989ba220ec639333`；首页显示 arXiv:1301.5225v1，2013-01-22。首页另外印 Dated 2021-01-12，不能据此改写版本日期。PDF 与既有 source 的 11 页表述不符；未核期刊排版页数。
- 精读定位：pp.2–6 Eqs.1–16、Table I、Figs.1–2 和相关文字；pp.6–10 Table II–III、Figs.3、8–10 及相关文字；pp.13–14 的图文仅作页数/文献延续确认。静态对照 `tmp/runs/20261108-doctoral-foundations/G34/get-paper/arxiv-1301-5225/source/rp.tex`；没有执行源代码。未逐项核完整论文其余图与参考文献。
- 自主代数：原子/核质量换算；\(ft=K\) 和 \(\log f_0t\)；Table I 自洽控制。使用 \(\lambda_e=386.15926764\) fm：65.8 fm→5.3257，85.4 fm→5.0992；18.9 fm→6.4092（表列理论 7.26），10.3 fm→6.9365（表列理论 6.32）。PDF 与 LaTeX 表项一致；未查最终出版版/勘误，原因未定。
- 关键数据关联：Table I 共 20 行，不自动等同 20 独立输入；131mIn 属作者明确 FF 拟合系列；130Cd 半衰期用于校准 \(q_{GT}\)；129Ag 是相对已披露 q 拟合的比较候选，严格独立性未证。
- 交付：`knowledge/research-notes/doctoral-r1-t04-first-forbidden-operator-audit-20261108.md`；过程文件仅本回执。未写 source、G34、系统交接、计划或其他路径。
- 既有工作树存在多个并行任务的未提交修改；任务开始前检查了 `git status --short --branch`，未触碰这些修改。
- 停止条件：指定原件的算符、约定、拟合与实际表格审计已覆盖；对期刊版、实验原件、拟合目标的未知细节，以及 G34 草稿之间的差异明确保留，不扩充下载或跨来源研究。
- 交付检查：11 个指定顺序的英文 H2、单行 YAML 数组、正文行尾空白、PDF SHA-256 及四个独立数值点均通过；未做全库测试。
