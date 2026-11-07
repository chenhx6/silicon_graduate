---
type: research-note
title: "Chen2026全文：核芯软度、费米面位置与摆动观测的条件比较"
aliases: [continuation-g16-soft-core-wobbling-20261107, Chen2026 soft-core CQPC]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [campaign-g06-chen-2026-triaxial-softness-wobbling]
created_from: "G16 full-text acquisition; parent primary-source integration"
promotion_target:
tags: [a100, a130, a160, wobbling, gamma-softness, cqpc, fermi-surface, competing-models]
---

# 核芯软度和费米面位置必须一起比较

## Grounded Evidence

[[campaign-g06-chen-2026-triaxial-softness-wobbling]]的实际21页出版PDF已取得，
`raw/papers/gpt/query/20261107-continuation-G16/chen-2026-triaxial-softness-wobbling-prc.pdf`，
7498113字节，SHA256 `f0b2f1ae994d79817c41a01fa5f69e8d07a11338e6c2c6a061eaa45aa9e44274`。
G16提取全文章节；总控重点回读PDF1、3、7、9、15、17–18，检查算符、参数、
带间跃迁与结论的适用范围。附录与全部图点未逐式/逐点复算，未恢复作者代码。
“正文可读”取代旧摘要边界，不等于全部微观实现已经重现。

## Model Contract

| 项目 | 来源实际内容 | locator | 迁移时要保留的条件 |
|---|---|---|---|
| 核芯 | γ=30°刚性TR；γ无关Wilets–Jean软核芯 | PDF5–7；PDF17总结 | 这是两个极限，不是所有现实软度的连续扫描 |
| 核芯谱尺度 | TR J0=30ℏ²/MeV；WJ C=.06MeV，使基带能量接近 | PDF7 SecIIID/Fig3 | TR∝R(R+4)，WJ∝R(R+6)，两谱并非严格相等 |
| 奇粒子 | h11/2单j、χ2=12.5MeV/b²、Δ=1.0MeV | PDF9 SecIV | β约.2是所用参数对应量级，不是各真实核形变测量 |
| 费米面 | λF=−2.5MeV代表low-shell粒子型；λF=0代表midshell粒子空穴混合型 | PDF9 SecIV | 不把这两个代表值当跨核区固定阈值，也不指定所有分量u²相同 |
| E2 | 忽略奇粒子电荷贡献，T(E2)=√(5/16π)Qcore | PDF3 Eqs14–16 | 比较E2须保留同波函数、核芯矩阵元与截断 |
| M1 | 先给含gR、gl、gs的完整角动量形式，再在单j跃迁中约化；所用h11/2质子gj=.7μN | PDF3 Eqs17–21 | 不把该gj搬成自由核子或普适中子值 |
| 近似 | CQPC采用KKDF/Dönau–Frauendorf的正能子空间投影 | PDF2–3 | 这是声明的模型近似，不是完整微观解认证 |

## What Changes the Interpretation

作者比较四个情景：两类核芯各耦合low-shell或midshell准粒子。
在本模型的low-shell+TR情景，低自旋TW随自旋转到LW；low-shell+WJ情景中
TW没有实现。midshell情景的LW与low-shell转到LW后的跃迁概率仍有明显差别
（PDF17）。所以只看到摆动能随I增加，不能指定费米面位置或唯一的LW结构。

作者在PDF9 Eq59定义与相邻favored-band能量平均之差。正文用其自旋趋势讨论
TW/LW，同时用角动量分布/SCS和电磁跃迁追踪模式。现实实验中能量趋势也可能
由组态交叉或其它激发产生；本任务不把单独的增/减趋势升级成充分判据。

## Two Interband Directions are Different Observations

PDF15 SecIVC2明确比较`w(I)→y(I−1)`与`y(I)→w(I−1)`两组ΔI=1支路。
它们连接不同的初末态，不是同一态对的正反过程，不能用详细平衡因子直接相互换算。
在所研究TR参数下，TW区后一组E2受抑；转到LW后两组变得接近。
作者用“become alike”，并指出另一个γ条件下接近程度不同，因而本页不称严格合并定理。

WJ情景的相关E2和M1支路与TR有可比较差别，但作者在PDF17仍说部分E2随自旋
相互接近；不能将有限算例写成“永不接近”。M1排序也有文中明确提到的
7.5→6.5例外（PDF17首段），不能写成所有自旋无例外。
这些条件比较把下一项实验需求具体化为两方向的绝对/相对E2与M1网络，
而不是只测一条大E2混合比。

## Cross-region Transfer and Competing Explanations

PDF17–18指出135Pr和105Pd等现实核的TW–LW解释与偶偶邻核软度间存在张力，
并明确认为直接使用未受扰动的偶偶邻核芯过于简单：奇准粒子会改变核芯性质，
如何在当前CQPC版本中加入这种改变仍是未来问题。作者转引TPSM共同参数解释
偶核软、奇核刚的结果；这是本篇对被引工作的陈述，不等于我们重新核验该TPSM运行。

可迁移到A100/A130/A160的是共同输入合同：比较占据/费米面、奇粒子极化、
核芯动力学、惯量、配对、波函数与电磁算符，再看何种观测能区分模型。
只按质量区、偶邻核γ软或某个固定势垒高低宣判TW可/不可出现，都超出本文证据。

## Failure Conditions and Next Step

若实际组态不是单h11/2、奇粒子电荷贡献不可忽略、邻核芯需明显重整化，
或者候选带是signature/γ振动/多准粒子激发，上述四情景的数值映射就需重新评估。
下一步是冻结核芯与占据输入，留出两方向跃迁作预测；本文作者生产数据/代码尚未归档，
所以不能声称已完成其21页模型的独立数值重放。

## Parent Self-audit

已收窄原worker的“严格合并”“软核永不合并”“M1排序无例外”“共同均值等于完全匹配”
及跨区排他性表述。正文获取真实；具体网络访问机构归属未由父代理独立认证，
不用于科学或权限结论。原获取manifest的UTC时间比文件写入时间偏移，
本轮另存父核验回执，保留原记录而不冒称其时间已验证。


## Research Trigger

核芯软度与费米面位置对摆动及两方向跃迁的共同作用。


## Provisional Reasoning

本页比较从原表/算符到条件结论的推断；这些推断与作者实验报告分别标注，不视作新的独立测量。


## Assumptions

采用本页声明的态对应、单位、多极/旋转规范和所用模型范围；未给的联合Cov、原始响应或作者实现不补造。


## Competing Explanations

所选机制须与组态混合、占据变化及实际实验/有效算符依赖比较；与名义数据相容不等于唯一解释。


## Transfer Conditions

迁移到另一核素/核区前，重新核对同态身份、占据/配对、形状动力学和探针算符；仅质量数或名词相同不满足合同。


## Failure Conditions

若原件/态映射/算符规范改变、或必要响应未恢复，重新计算并收窄结论；不得以缺失伴随信号代替有灵敏度的排除。


## Falsification or Reverse Tests

将TR/WJ与两占据代表值的未拟合支路作条件对照。 本页没有未执行的真实核模型排他认证。


## Open Questions

奇准粒子极化后的共同波函数和完整电磁网络。


## Human Review

本任务未发生用户逐项审核；记录的是Agent原件自审，未伪装human-reviewed。审核标注不作为检索或使用资格门。


## Promotion or Rejection History

本批根据直接原件与独立核查修订worker草案，撤回无源数值/普适断言；本页保持provisional。具体触发证据和仍存边界见正文，不以结构检查替代物理核验。
