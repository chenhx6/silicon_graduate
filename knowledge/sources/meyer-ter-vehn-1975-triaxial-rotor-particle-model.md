---
type: source
title: "Meyer-ter-Vehn1975(I)：单j芯—粒子模型及粒子—空穴等谱"
aliases: [Meyer ter Vehn1975 PartI, MTV75 single-j triaxial rotor particle]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: deep-read
title_original: "Collective model description of transitional odd-A nuclei (I). The triaxial-rotor-plus-particle model"
authors: [J. Meyer-ter-Vehn]
year: 1975
journal: Nuclear Physics A
volume: 249
pages: 111–140
doi: 10.1016/0375-9474(75)90095-0
canonical_source: https://doi.org/10.1016/0375-9474(75)90095-0
citation_key: ""
raw_file: raw/papers/1975_MeyerTerVehn_CollectiveOddANuclei_PartI.pdf
raw_sha256: 10cb7aca223dcbccb17ee7aa224a7a1c13fb9f1e6e58a04fcdd8ab1e4b888da9
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-wk22-particle-hole-symmetry-054/attachment-object-response.pdf
nuclei: []
models: [single-j-shell, triaxial-rotor-plus-quasiparticle, BCS, Davydov-rigid-core]
methods: [particle-hole-conjugation, angular-momentum-coupling, coherent-electromagnetic-matrix-elements]
observables: [energy-spectrum, B(E2), B(M1), spectroscopic-moment, mixing-ratio]
tags: [133Ce-method-blueprint, exact-model-symmetry, energy-zero, signed-EM]
---

# 等谱映射有完整合同，不能只改γ与λ两个数字

## Bibliographic Record

J. Meyer-ter-Vehn，Nuclear Physics A249(1975)111–140，DOI10.1016/0375-9474(75)90095-0。本文是[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]的Ref51，Ref52才是PartII。首页received1975-02-17；physicalPDF页+110=印刷页。出版商FULL XML/首页身份核准，实际30页、1365168bytes，SHA见frontmatter。

常规下载器先返回一页60529bytes预览，另以FULL XML实际返回的MAIN attachment EID经标准Object API取得完整30页；两者哈希/范围分开，不从工具downloaded状态推全文。si*.gif为ALTIMG/thumbnail，未识别scientific SI，不据文件名当补充数据。原件在tmp，raw未归档；完整PDF/XML/OCR/页图不进入本run公开发布。

## Scope and Reading Depth

054连续原读并视觉核PDF4–12的§2.1–2.6全部方法；055读PDF1–3引言与PDF12§3起至30全部结果/结论/参考，视觉核Figs1–13/Tables2–3/Eqs3.1–3.8；Table1/所有Ch2方程由054核。合并覆盖30页主线，未把任何单个worker的范围写成其独立全文。PartI没有逐核实验band数据表，系统实验比较明确留PartII，不能将引言/结论对它的预告当本篇新实验。

root另连续读PDF4–12方法、PDF1–3/13–15及20–30结果/结论关键文本，视觉核PDF4/5/7/8/10/11的single-j、对称、BCS近似和EM原式。不是作者数值求解重现或actual2022代码验证；未知程序和114均未运行。

## Summary

原文确有精确模型的particle–hole等谱关系，但连同single-j、壳能量零点、pairing/core与轴置换合同。它不由任意Nilsson多轨道H的轴置换自动成立，不把正λ取负就恢复负宇称输入。源还明确对应E2 RME变号、M1不变，故等谱也不能推出signedδ不变。适用域限定的数学点可闭合，实际133Ce参数/态/算符必须独立核。

## Experimental or Theoretical Setup

奇核子限一个完整j壳的1qp，β/γ固定的triaxial core，BCS ph二维空间与D2 good-I基；完整j取向/Coriolis混合不是冻结一条j方向。作者称1qp适用低激发E<2Δ，原intro承认实核softness可使谱整体压缩，rigid-core耦合较好是作者解释而非本篇已测γ刚性。

Hp=(εj−λF)τz+Vpτz+Δτx，unique-j常数εj设0。Vp限该壳quadrupole field。HR=hR·1ph，hR=Σ(Ik−jk)²/(2𝒥k)，假定particle/hole写法的core相同；𝒥k=(4/3)𝒥0 sin²(γ−2πk/3)。β/γ/λ为可选参数，质量标度k/𝒥0/Δ为本方法经验选择，不填WK22 actual卡。

## Key Results

所有新claims needs_review:true，严格原模型/数值近似/任务推广/实际边界分层。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MTV75-D24-001 | 空间限制为single-j完整壳的1qp、固定βγ芯；εj为同壳常数并设0，不等多轨道h0的全部spherical spacings可抹去。 | explicit-model-domain-and-zero | direct-original | PDF3–5 printed113–115; Eqs2.6–2.7 | true |
| MTV75-D24-002 | 精确模型映射Γ同时变(γ,λF,Δ)→(60°−γ,−λF,−Δ)，轴(1,2,3)→(3,1,2)；再以ph σy组合得到等谱，core也须协变。不是两实核不同组态必degenerate。 | original-full-symmetry-contract | direct-original | PDF5–7 Eqs2.11–2.22 | true |
| MTV75-D24-003 | Eq2.28保qp/qh间hη，实际Eq2.30另将其略去；作者在远离壳/弱形变邻近耦合情形论证近似。模型内对称精确不等其数值近似已被全面验证。 | original-approximation-boundary | direct-original | PDF8–9 Eqs2.25–2.33 | true |
| MTV75-D24-004 | 若absolute能量壳中心E0非0，ph反射应为E′=2E0−E、Λ′=2E0−Λ；只在共同E0=0约定才写−λ。这是原εj0的任务坐标推广，不把50.6盲负，也不等negative-parity λ。 | task-energy-reference-contract | original-zero-premise-plus-algebra | PDF5 Eq2.6及其后句; PDF7 Eq2.19 | true |
| MTV75-D24-005 | 多轨道精确迁移的充分条件是存在封闭空间的U/E0，使h′−E0=−U(h−E0)U†并配对/core/轴惯量/截断协变；quadrupole轴负关系不自动覆盖不同h0、spin-orbit/l²、ε4。不是证明多轨道必不可能等谱。 | explicit-task-sufficient-contract | source-symmetry-plus-operator-inference | PDF5–7 Eqs2.6–2.22; WK22 physicalPDF46/48 | true |
| MTV75-D24-006 | 源定义下S†QS=−Q、S†MS=M，对应态E2 RME变号/M1不变，Qsp和δ反号、各B不变；限匹配态/同算符相位与辐射约定，非任意statephase效应或actualCeδ预测。 | original-EM-duality-and-scope | direct-original | PDF10–11 Eqs2.40–2.51及其后段 | true |
| MTV75-D24-007 | β/γ/λ free参数与k=206/A^(1/3)、ℏ²/(2𝒥0)=204/(β²A^(7/3))、Δ=135/A的标度为本模型经验处方，保b=βA^(2/3)尺度不等actual参数已定。 | direct-parameter-calibration-scope | direct-original | PDF11–12 Eqs2.52–2.58 | true |
| MTV75-D24-008 | γ30°偶芯有两个惯量相等、kinetic H关于轴对称，但形状不因此轴对称；n=I−α的wobbling标记是本rigid-core解，不等实验任意band已是声子。 | direct-core-symmetry-and-label-boundary | direct-original | PDF13–15 Eqs3.1–3.6/Figs1–3 | true |
| MTV75-D24-009 | Fig11改用rigid-body-like惯量后可保decoupledlevelorder而失irrotational Fig6的多crossings；原稿明确实验比较联合检验shape与惯量，不能从谱独立测唯一γ。 | actual-model-sensitivity-and-inference | direct-original | PDF24–26 §3.4/Fig11 | true |
| MTV75-D24-010 | Fig10画去Eγ、有量纲的δ′=R_E2/R_M1，不是直接δ；Table2 sign rule仅低激发/sizable分支、b>3和λ≤e₂（第二单粒子能）范围的数值规律，作者说general justification未给。不能据此定WK22三跨带线实际sign。 | printed-observable-and-rule-domain | direct-original | PDF22–24 Figs8–10/Table2 | true |
| MTV75-D24-011 | K/Ω是approximate averaged分类，Table3只有最底态dominant分量可>50%；higher band assignment tentative。Fig13最大B带内不保证最大partialwidth，原作者保band leaking，缺branch/phase不能由权重补。 | state-classification-and-EM-network-boundary | direct-original | PDF27–29 §3.5/Table3/Fig13 | true |
| MTV75-D24-012 | 引言承认rigid-core忽略softness造成谱压缩，PartI只给模型图谱，具体A135/A190实验比较在PartII；不能将预告/结论作者评价记成本篇新独立实验。 | source-lineage-and-validity-boundary | direct-original | PDF2–3 Introduction; PDF29–30 Conclusion | true |

## Exact Model Symmetry and Actual Input

Γ把quadrupole potential反号而core不变，σy再把ph Hp反号，合成S=σyΓ使H的对应参数表示等谱。Δ号单独是本BCS势的gauge自由度，不能据此略掉pairing幅度/相位合同。这里是参数对偶的模型谱关系，不是仅重命名同核band，也不证明两实验带具有相同组态。

设e=E−E0、ℓ=Λ−E0，所需e′=−e/ℓ′=−ℓ给E′=2E0−E、Λ′=2E0−Λ。共同平移E/Λ保持E−Λ，但不能令未经核验的两列自动共零点。WK22 ε约5–6MeV与λ50.6仍需实际header，负πλ仍unknown；ph反射不改变所选轨道空间宇称。

多轨道迁移需要实际算符等式，而非只看γ反射。若h=h0+V2且h0为不同spherical energies的旋转scalar，纯轴置换保h0，却需h0−E0反号；只有同常数或另有成对谱映射才能满足。full Nilsson spin-orbit/l²跨l/j差和rank4场也须变换，不由单j V2关系包办。R-dependent core函数若在同R/同轴映射下相同可保对称，不是所有Harris处方自动破坏或自动保持。

BCS逐态若εν′=−εν、λ′=−λ、absΔ′=absΔ，则eν′=eν、u′²=v²；只改λ而保持原εν不动不满足。Eq2.30忽略hη是另一个实际求解近似；blocking、空间或近似只改一边时不沿用等谱认证。

## Signed EM and Band Classification

源用core+particle Q和ph-even的M，并明确Q odd/M even。对应初末态的共同重相位使E2/M1同时乘同phase，比值不变；参数对偶时两算符有相对odd/even行为才使δ变号。限同正Eγ/radiation定义、M1非零，不能将该模型sign规则当actualCe结果。

须保本源literal归一：Eq2.49给5/(16π)abs(R_Q)²/(2I+1)，Eq2.50给abs(R_M)²/(2I+1)，Eq2.51含√.7 Eγ√(5/16π)R_Q/R_M。本页只按原定义讨论相对变换；与[[larsson-1978-nuclear-core-quasiparticle-coupling]]或实际PROBMO作absolute比较前须对齐M/Q与单位，不能凭磁算符同名字补/删系数。

Fig10 δ′去掉Eγ、仍有单位与所用磁尺度，不能作本核直接δ曲线。K/Ω近似分类不由一个dominant权重变严格守恒；源虽可有大带内B，却因能量因子/其它出口发生band leaking。low1qp解的高态不自动给实际3qp crossing。

## Competing Interpretations and Limitations

完整j壳允许Coriolis使j重新取向，因此不是F14式单方向冻结j；形状βγ仍冻结，1qp/weak-deformation/no-qp-qh-mixing边界分别保。Fig11显示能谱对形状和惯量联合敏感，与[[larsson-1978-nuclear-core-quasiparticle-coupling]]的软/刚芯比较互补，不由一个参数拟合证明γrigid。本文未做133Ce实际数据、寿命、signedRME或135Nd四替代fit。

supports的是历史对称和完整合同可原核；limits的是把WK22对Eq3.14的概述无条件迁到Eq3.16多轨道Nilsson/ε4/BCS job。能谱等价、模型参数对偶和观测不变分别判断，不恢复既有撤回或擅改review。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：等谱、零点与actual配置/EM判别的边界。
- [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]：Ref51原读范围与原简述的适用条件。
- [[135nd-chiral-partner-resolved-evidence-map]]：模型对称不能替代partner-resolved实验。
