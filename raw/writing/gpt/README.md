# GPT 辅助学术手稿库

这里保存论文工作包、可复现分析、图件和数据 provenance。目录中的文件按
论文证据门维护；本地编译通过不等于作者已经批准投稿。

## 当前主线

[`pado-alignment-response-dependence/`](pado-alignment-response-dependence/) 是
当前最成熟的单点论文候选，主题是公开 \(^{67}\mathrm{Ga}\) 表格上的
P-ADO alignment-response transfer 与 profile-preserving coverage audit。
它目前是 EPJ A Regular Article 的 `partial/not-ready` 候选，结论严格限于
声明的 independent-row Gaussian、固定边际误差和 common-\(\rho\) 合同。
文章不提供 event-level likelihood、实验 p-value、真实 feeding fraction 或
A≈130 某个核素的模式裁决。

[`133ce-response-aware-collective-mode-identifiability/`](133ce-response-aware-collective-mode-identifiability/)
是第二条核结构路线。它依赖私有 iThemba 数据、producer lineage、响应协方差
和独立 holdout，当前保持 local-only、partial-L4，不能把私有数据写成公开数据。

## 历史失败案例

[`a130-triaxial/`](a130-triaxial/) 是已撤回的 omnibus 草稿，只用于保存失败
模式、来源谱系和审计记录。它把多个核素、模型输出、toy calculation 和私有
workbook-derived 数值混在一篇稿件中；其中的“证明”“彻底排除”“\(>10\sigma\)”
等旧表述不属于当前证据库，不能作为事实源、投稿稿件或新图的输入。

对应的长期说明见
[`knowledge/projects/triaxial-collective-excitations-a130-manuscript.md`](../../knowledge/projects/triaxial-collective-excitations-a130-manuscript.md)
和
[`knowledge/research-notes/a130-triaxial-writing-package-audit-20261105.md`](../../knowledge/research-notes/a130-triaxial-writing-package-audit-20261105.md)。

## 文件规则

- 文章直接可公开的数据放在各主题目录的 `data/`；
- 绘图及中间缓存放在 `figures/made/data/` 或分析结果目录，并注明其派生性质；
- 原始论文、来源页、哈希和权限边界按 Wiki 的 research-archive 工作流维护；
- `main.pdf` 只表示本地编译产物；作者信息、许可证、永久 DOI 和最终措辞仍须
  通过论文级证据门。
