---
type: research-note
title: "N=75 的 3D-TAC 来源对读：Starosta 2001 与 Olbratowski 2002 v1"
aliases: [N75 3D TAC source contrast, Day26 TAC source audit 024]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [starosta-2001-n75-chiral-vibrations, olbratowski-2002-critical-frequency-preprint]
created_from: Day26 source audit 024 and uncredited Day27 preview
promotion_target: tilted-axis-cranking
tags: [chirality, n75, three-dimensional-tac, source-audit, model-boundary]
---

# N=75 的 3D-TAC 来源对读

## Research Trigger

对照同一 $^{132}\mathrm{La}$ 的手征候选与两个不同时代的三维推转计算，辨认原件中的实验能带、均场解、经典分岔和量子伙伴能隙。此笔记为 Day26 独立来源审计；相关 Day27 知识仅作**无学分预习**，不推进 Day27、不打开 Day28。数值明细见 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/tac-starosta-olbratowski-comparison-024.json`。

## Grounded Evidence

| 主题 | Starosta et al. 2001 | Olbratowski et al. 2002 v1 |
|---|---|---|
| 原件/身份 | [[starosta-2001-n75-chiral-vibrations]]，PRL **86**, 971–974，原 PDF 四页；`raw/` 文件 `%PDF-1.3`、135709 bytes、SHA256 `9082c1e8ced3fbfeb2248f5b18c1b646f4dc1adc77af5c27c6a988855583cbf4`。 | [[olbratowski-2002-critical-frequency-preprint]]，arXiv:nucl-th/0211075v1 三作者稿四页；已归档为 `raw/papers/gpt/day26-20261028/olbratowski-2002-critical-frequency-arxiv-v1.pdf`（原读本 `tmp/day24-critical-tac-007/arxiv-0211075v1.response`）；两者均 `%PDF-1.4`、252547 bytes、4 页、SHA256 `3cc0000405bb8360d0b7112fbd6d6a3811546091dee182da2b44be071c8bbffb`。归档的是三作者 arXiv v1；2004 四作者 VoR 未由此取得。 |
| 实验输入 | 新 sideband 的同宇称/相对自旋由 mixed M1/E2 连接及 angular correlations 支持；$^{132}\mathrm{La}$ 双带约 0.37 MeV 位移，共同 $I=9$ 带头属系统学选择。PDF pp.2–3，Figs.2–3。 | 重用 Starosta 等的实验候选谱作比较，没有新采集。PDF p.4 Fig.6、Ref.2；原稿说其 HF 起始频率显著高于实验候选带出现频率。 |
| 微观/唯象输入 | Hybrid spherical Woods–Saxon 加 deformed modified harmonic oscillator；配对 gap 取奇偶质量差的 80%。固定 $\hbar\omega=0.35$ MeV 作形变/倾角自洽，再用该形变扫频；Table I 的 Cs/Eu 点分别在 0.30/0.20 MeV。PDF p.3 方法段、p.4 Table I。 | Skyrme-HF、SKM*、14 spherical oscillator shells、无 pairing、关闭 time-odd mean fields、仅保 parity；先作非自洽单粒子探针，再找平面和非平面 HF 解。PDF pp.1–2，Fig.1、p.4 Ref.6。 |
| $^{132}\mathrm{La}$ 形变及枝 | Table I 在 $\hbar\omega=0.35$ MeV 给 $\epsilon=0.175,\gamma=32^\circ,\vartheta=65^\circ,\varphi=36^\circ,E_b=12$ keV、$J=11.3\hbar$。这是 3D-TAC 的内禀解/鞍点势垒，不是实测形变或 0.37 MeV 能隙的量子计算。PDF p.4 Table I。 | 选定近似内的 HF 解约 $\beta=0.25,\gamma=45^\circ$；非平面 HF 分支自 $\hbar\omega=0.6$ MeV 出现。PDF p.1 末、p.3 Eq.7 后。两篇形变约定/模型不同，不能把两点放在同一固定形变曲线上。 |
| 解析临界与谱的边界 | Table I 给浅势垒；作者把非简并 pair 解释为软手征振动，但没有算出量子振动本征频率或 tunnelling splitting。PDF pp.3–4，Fig.1、Table I。 | 冻结 gyro 模型由 $I=\mathcal J\omega+s$、$\omega\times I=0$、$\omega_m(\mu-\mathcal J_m)=0$ 得 $\omega_c=[(s_s/(\mathcal J_m-\mathcal J_s))^2+(s_l/(\mathcal J_m-\mathcal J_l))^2]^{1/2}$。所列 HF 导出参数给 **模型算术** $\hbar\omega_c=0.514639$ MeV（原稿四舍五入 0.51），并非实际 HF 搜索的 0.6 MeV。PDF pp.2–3 Eqs.2–7、Fig.4。 |
| 竞争解释 | 原文以 0.75 MeV qp routhian 差与区域 $\gamma$ 振动能作论证，仍承认小混合；共同组态由选择规则推断。PDF p.3 两栏。 | Fig.6 明示 planar/axial-long 两带也可近似再现约 350 keV 分离；作者将其列为暂定替代。PDF p.4 Fig.6、左栏末。 |

## Provisional Reasoning

$^{132}\mathrm{La}$ 的 12 keV 是 Starosta **内禀 Routhian 势垒**，约 0.37 MeV 是实验两带 **能量位移**，0.514639 MeV 是 Olbratowski **冻结参数经典临界频率**，0.6 MeV 是其 **HF 分支出现频率**。四量维度/对象不同；数值接近、差异或大小次序均不直接给有限核的手征双带量子劈裂。Starosta 的 $\epsilon,\gamma$ 与 Olbratowski 的 $\beta,\gamma$ 也来自不同势与约定，不组成一条已测 $\gamma\to\omega_c$ 曲线。Olbratowski v1 PDF p.4 关于惯量差缩小令临界频率降低的文字，与其 Eq.7 在固定非零 gyro 下的代数方向有张力；保留源中文字歧义，不把它当普适 γ 单调律。

## Assumptions

只对实际读到的 Starosta 2001 PRL 四页与 Olbratowski 2002 arXiv v1 四页作对照。两份 PDF 经签名、页数、字节数与 SHA256 核验；文本逐页读取，Starosta p.4 Table I、Olbratowski pp.3–4 Eqs.5–7/Figs.4–6 另作图像核读。未取得原实验矩阵、完整 HFODD 运行、Starosta 的 3D-TAC 代码或 2004 VoR。Olbratowski v1 归档恢复只改变存储路径，不改变版本和阅读覆盖。

## Competing Explanations

同宇称双带的能隙可由手征振动/隧穿、不同平面/轴向 HF 枝、准粒子激发或形状/组态混合产生。Starosta PDF p.3 讨论了前两种竞争中的 qp/γ 振动尺度；Olbratowski PDF p.4 Fig.6 给出 planar/axial-long 具体替代。二者比较的是不同模型假设，不能按“两个独立实验支持手征”计票。

## Transfer Conditions

对下一核迁移 3D-TAC 时，先对齐势/EDF、配对与 time-odd 耦合、占据、$\epsilon$ 对 $\beta$ 的定义、频率与自旋映射，再区分均场极小、集体质量/势垒与量子跃迁算符。只用同一组输入的完整计算与实测绝对强度/连接，才可逐带比较模式；不能移植这里的 0.514639 或 0.6 MeV 作为跨核阈值。

## Failure Conditions

若缺少可重算的集体质量、左右手波函数相干与实际带内/带间跃迁网络，TAC 双极小不能给隧穿能隙或手征振动谱。Starosta p.4 Table I 的 `10B(E2)` 栏须除以 10 才是所列单位下的 $B(E2)$；原 Table I 注释用 $+\to+$ / $+\to-$ 标签描述两类跃迁，不能脱离原图与其定义重排成实验带内/带间量。两篇的源文件存储身份须保持分开。

## Falsification or Reverse Tests

对 $^{132}\mathrm{La}$，在相同组态与惯量/配对输入下计算 planar、axial-long、aplanar 三类量子化能谱及绝对 M1/E2 连接，再在不使用候选带标签调参的条件下比较实验带位移、$S(I)$ 和跃迁比。若平面/轴向分支同样解释能谱而电磁矩更符合实验，则能谱近合不足以认证手征。当前两篇均未交付这一完整对照；这里是下一步设计，不是已执行证伪。

## Open Questions

Starosta 的浅 Routhian 势垒在加入集体质量、配对与涨落后产生多大隧穿或振动能？Olbratowski 的 time-odd 耦合/配对打开后，HF 起始频率和 planar/axial-long 竞争如何变化？原 Starosta 同一实验谱是否提供足够绝对寿命与分支来做逐带保留检验？

## Human Review

本轮是 Codex 直接原件对读和条件代数核算，新增结论 `needs_review: true`，未提升 `human-reviewed`。2002 v1 不替代未读的 2004 VoR；某项论文措辞需按原版、图表 locator 与实验依赖定向复核。

## Promotion or Rejection History

2026-10-28：将 132La 的实验约 0.37 MeV 位移、Starosta 12 keV 势垒、Olbratowski 冻结 gyro 0.514639 MeV 和 HF 0.6 MeV 分成四种物理量；撤回将 017 示例频率当实核相界或将两个不同 3D-TAC 参数点合并的推断。同期将 Olbratowski v1 从 tmp 恢复到 raw，逐字节 SHA/页数复核；不改变版本与 review 边界。Day27 仅无学分预习，不更新课程索引。
