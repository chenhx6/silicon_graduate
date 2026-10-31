# Day25 无学分预习：135Nd 必须按两组 family 分行比较

**结论：** Lv2019 的新谱学对 D3/D4 正宇称候选伙伴有真实支持，也独立确认、扩展了 D5/D6 负宇称 family 的谱学。两组的电磁覆盖度不同：**D3/D4 在本文只有 D3 的一个 B(M1)/B(E2) 点，未给匹配的双 partner 绝对强度/寿命；D5/D6 的绝对 B 值明确来自 MU07，2019 年的新相对比与旧结果相似。本文没有重新分析 MU07 的寿命 fit 或逐线 branch normalizer。** 缺失输入不应抹去真实正支持。

本轮新增交付是 Day25 比较矩阵的 135Nd 双 family 行、最小 companion 组合及缺项降级规则，以及此前 source 未单列的正宇称连接局部歧义。其它原有事实仍使用既有 LV19 原 claims，不冒称新实验发现。

## 身份、原件和阅读范围

B. F. Lv et al., *Chirality of 135Nd reexamined: Evidence for multiple chiral doublet bands*, PRC **100**, 024314 (2019), DOI **10.1103/PhysRevC.100.024314**。

- 全文实际读本：`raw/papers/gpt/learning-daily/20260912-PREPLAN-135nd-crosswalk/lv-2019-135nd-reexamined-arxiv.pdf`，官方版本 URL `https://arxiv.org/pdf/1907.12809v1`，侧栏日期 30 July 2019。10 页、285508 bytes，SHA256 **97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303**。本轮读既有 raw，没有重新下载或改 raw。
- 定向 VoR：既有 `tmp/day21-checkpoint103/lv2019-vor.pdf`，原下载 URL `https://journals.aps.org/prc/pdf/10.1103/PhysRevC.100.024314`。9 页、548795 bytes，SHA256 **450a3032d7fecfdbc16f5a848be3d63842a536b0508dda73f3de55270fbf2066**。本轮只定向核 printed **024314-2/3/4/8**，不冒称新读完整 9 页 VoR。
- 当前阅读：raw 全 10 页文字；全部 **Figs.1–6**（PDF3–6）视觉；**Table I 全四页 PDF7–10** 视觉；Harris 参考、惯量、Q0/g 因子及各模型输入的未编号公式。正宇称 Fig.1 新放大核对。
- `active-recall.md` 在打开本轮正文前冻结，明确受 Wiki priming，不评分。不运行 114、历史物理脚本或作者 producer，不恢复正 P/机时排他认证。

## 新采集、旧身份、旧绝对 EM 与模型各是什么

| 层次 | 原件实际给出的信息 | Locator |
|---|---|---|
| 新采集 | 152 MeV 100Mo(40Ar,5n)，0.5 mg/cm² 自支撑富集靶，39 个 JUROGAM II Compton-suppressed Ge；与 MU07 的 175 MeV Gammasphere campaign 不同 | raw PDF2 Sec.II；VoR 024314-2 |
| 正宇称新/修订谱学 | D3 扩展且多条新线连 D2-3qp，parity 改 positive；D4 已知结构确认、spin 下调 1、新低位 19/2 态及连接；符合、RDCO/Rac、偏振支持总体修订 | raw PDF2，Figs.1/2 PDF3，Table I PDF8–9 |
| 偏振与宇称 | 830/1015/1161/1184-keV 的 IPDCO 为 .043(8)/.089(28)/.008(2)/.018(5)；作者据 electric character 及连向负宇称 D1 的关系建立 D2–D4 正宇称 | raw PDF2，Table I PDF8–9 |
| 负宇称新谱学 | D5/D6 旧 levels 确认；D5 两端扩展，旧 tentative links 确认/修订；新增 609/997/1071-keV D6→D5 links 及连 D1 的线 | raw PDF2，Fig.1，Table I PDF9–10 |
| 旧 band 身份 | D3/D4 包含旧已知结构而在此修订 Jπ；D5/D6 是早期负宇称 A/B family 的后期标签。组态是 alignment/模型支持的 assignment，并非直接测得 occupation | raw PDF1–2/4–6；Refs.10/35/36 |
| 当前相对 EM | Fig.5 的 B(M1)/B(E2) 比；Table I 的 Iγ 已效率修正、对 198.8-keV 线归一，来自 total projection 与 gated spectra 的组合 | raw PDF5 Fig.5；PDF10 footnote b |
| 旧绝对 EM | D5/D6 B(M1)、B(E2) 已发表于 **Ref.36=MU07**；作者称当前 B 比与旧值所得比相似。本文无新寿命技术、fit 或 τ 表 | raw PDF5 D5/D6 段；PDF7 Ref.36；VoR 024314-8 |
| 模型几何 | CDFT 提供形变、PRM 比较谱/比值并给 RMS 角动量；Fig.6 是模型输出，不是实测 signed orientation 或联合波函数 | raw PDF4–6，Figs.3/5/6 |

**MU07 normalizer 问题没有在本文闭合。** 新相对强度可提供新检验，但不能静默作为旧绝对强度分析的采用 branch。本文没有 DSAM time-response/side-feeding 重拟合、旧逐线输入账本或 joint Cov。此结论延续 LV19-R52/R103/R110，不声称这次首次发现。

## 模型输入、校准与支持

raw PDF4 明说 PRM 的 J0 按能谱趋势调整；采用 irrotational Jk=J0 sin²(γ−2kπ/3)。EM 使用经验 Q0=(3/√(5π)) R0² Zβ，R0=1.2 A^(1/3) fm，gR=Z/A，gs=.6 gfree。它们不是本文新测的 Q/g。Fig.4 的 Harris J0=11、J1=20 仅为 alignment 参考，与各 PRM J0 不是同一输入。

| Family | 原模型配置/参数 | 能支持什么、不能支持什么 |
|---|---|---|
| **D3/D4 正** | π[(h11/2)^1(g7/2)^−1]⊗ν(h11/2)^−1；β=.23，γ=21°，J0=28 hbar²/MeV，ξ=.94 | 谱再现、约 200 keV 分离、一个 D3 比值与模型在误差内相容。不是 D4 匹配绝对 EM 验证；ξ 是模型 attenuation，不是独立测量 |
| **D5/D6 负** | π(h11/2)^2⊗ν(h11/2)^−1；CDFT β=.24、γ22.2°；为再现 39/2 处 B 比突增，PRM 将 γ 调为 **20.2°**，J0=23.5，ξ=.98 | 谱/EM 的条件再现和已有绝对 B 的真实正支持保留；B 比特征参与选参，不能再作完全未用的参数无关 holdout |
| D2 背景，非第三组 chiral pair | D2-3qp 与 D2-5qp；D2-3qp 的 CDFT γ22.5° 改 17° 以再现 B 比，ξ=.92，J0=25/40 | 提供组态/交叉背景。D1/D2 不是本文的正宇称手征 pair；D3 与 D2 的比相近不独立测得 D3/D4 几何 |

Locator：raw PDF4–6；VoR 024314-8。D3 仅一个比的正文 spin 字面写 **I=29 hbar**，图/表是半整数；不静默改原句。D5/D6 被作者称为良好的 chiral-vibration 实例，合并谱/EM 证据支持配置。Fig.6 关于 D3/D4 更平衡的三轴 RMS 是 **PRM 比较**，不能因此把 EM 更稀疏的正 family 写成实验静态几何更确定。

## 本轮真正新增：正 family 的局部拓扑/能量歧义

既有 D3 334.4-keV parity tuple、D6 空 multipolarity、重复 934.9/966.3 行及 998.1/997 歧义全部保持。本轮另发现并在两版本实际图文核到：

### D4 段对 589/649-keV 的目标 family 前后不同

**raw PDF2 / VoR 024314-2** 同一段先说：

- 596/673/780/919-keV 新线连 **D4→D3**；
- 589/649/750-keV 连 **D4→D2-3qp**。

下一句却说 **589/649/780-keV between D4 and D3** 有 firm E2 character。两版本都如此。Fig.1 放大可见 589/649/750 的长连接朝 D2。Table I 的 D4 589.2/649.3 行分别标 23/2→19/2、25/2→21/2，不能不绑定具体 daughter 就直接复用为 D4↔D3 的绝对 branch。

### D2 的 2588.3-keV tuple 与三条相邻闭合路径不同

**raw PDF7–8 / VoR 024314-3**：D2 的 207.5 和 399.9 行均印 Ei=**2588.3 keV**，但其它实际行给：

- 2350.8+207.5 = **2558.3**；
- 2801.5−243.2 = **2558.3**；
- 2158.4+399.9 = **2558.3**。

D4 3207.6−649.3 也等于 2558.3；2940.0−589.2=2350.8（表中 D2 21/2 态），2940.0−596.5=2343.5（表中 D3 19/2 态）。`positive-link-boundary.json` 仅记录这些条件算术。**2558.3 不是新测/已更正能级，30 keV 不是本任务得到的 σ 或排除概率。** 没有原分析/勘误时，不指定应改哪个印刷字段。

**影响范围：** 隔离具体 target/tuple，不否定整体正宇称。1184 E1、D3 多条 E2、780.4 D4→D3 E2 及整体符合图仍提供真实支持。发现两个局部对象有歧义不等于全表不可信，更不是 chiral family 的排他反证。

## Day25 三核矩阵中的 135Nd 行：拆成两条

本轮只准备 Nd 行，不借用 Pr/Ce 的数字或其它核的模型阈值。

| 比较轴 | **135Nd D3/D4 positive family** | **135Nd D5/D6 negative family** |
|---|---|---|
| 身份 | 新/修订正 Jπ 和拓扑，旧 band 扩展、在此识别为候选 pair；与 D1/D2 分开 | 早期 A/B 负宇称 family，新采集确认并扩展 |
| 真实实验支持 | 新连接、符合、RDCO/Rac/偏振、近似相同 alignment、约 200-keV 分离；一个 D3 B 比 | 新谱学/relative B 比的独立 corroboration，加上更早 MU07 双 partner 寿命/绝对 EM；campaign 分开 |
| EM 完整度 | 未闭合匹配的 partner absolute EM，D4 缺 companion rate/τ | 已有较强 paired EM 历史，但本文不补 MU07 的 line/component/normalizer/response/Cov |
| 模型支持 | h11/2–g7/2 proton particle-hole 配置及 neutron hole，CDFT/PRM 与 RMS | 两个 h11/2 protons 加 neutron hole，PRM 条件再现；B 比突增参与 γ 选择 |
| 保留竞争解释 | 配置/交叉/混合/shape softness 不能由一个比或 RMS 箭头排尽；局部正连接须绑定 | 有限振动/静态窗口、高 spin reorientation/交叉及模型依赖仍保留；本源没有推翻旧 EM 正支持 |
| 可用表述 | **谱学与模型支持的正宇称 chiral-doublet candidate；partner 绝对 EM 检验不完整** | **有早期独立绝对 EM 支持的负宇称伙伴 family；静态几何与全部替代解释未被模型无关地固定** |
| 不应计数 | D3 比当 D4 rate；D2 当第三 pair；模型形状当新测量 | 2019 当独立 τ 复测；旧结果多次引用当多实验；新相对 Iγ 当旧 absolute branch |

## 最小 companion 组合及缺项降级

这是 **本任务 research design**，不是原文给出的普适识别定理。即使三块齐全，也不唯一测得 handedness。

| 必须绑定的块 | 目的 | 缺一项时如何降级 |
|---|---|---|
| **A. 身份合同**：共同 I/Jπ、明确 parent→daughter/family、intra/inter links；按需有符合/角分布/偏振和 δ/component，局部歧义单列 | 先保证比的是同一对象。D4 的 589/649 问题是实际例子 | 保留谱学 candidacy；不把未定 branch 当匹配 EM 点；隔离行而非拒绝整组 |
| **B. 匹配绝对 EM**：两 partner 共同自旋处 τ、完整 branches/IC/δ、门谱/响应/normalizer，得到 B(M1)、B(E2) 与 joint uncertainty；可得时加 interband rates/limits | 区分 ratio 与电荷/磁性绝对尺度；检查 τ 差是否由能量或 branch 补偿 | 无 τ：relative EM only。缺 branch/δ/normalizer：旧发表 B 的支持保留，但新的重构/精确跨 campaign 成分比较仍条件化 |
| **C. 独立组态/形状 companion 与 holdout**：例如 matched partner g 加形状敏感 E2/Q 量或另一配置约束；冻结 model/EM inputs，留未用于选 J0/γ/ξ 的量/自旋段 | g 与 charge collectivity 约束不同部分，但任何单标量都不等完整 3D 几何 | 无 companion：配置/形状解释仍模型依赖。无真正 holdout：称 conditional fit，不称独立预测或排他证伪 |

**Nd 行优先级不同：** D3/D4 首先缺 B 块的双 partner EM 覆盖；D5/D6 优先追回已有正支持的实际 line/component/normalizer，并增加 C 块独立伴随量。更多同形谱 fit 或假设的正偏振/机时都不能替代。只补一个实验块时，要写清改善哪组 family，而非宣称“135Nd 完整手征测试”。

## 给 leader 的 atomic candidates

所有新候选保留 `needs_review:true`，不改既有 LV19 flags、人审或撤回。前两项是本轮新 literal nodes，后三项是 Day25 综合/设计，不是新增测量。

| ID | 草稿 | 类型 / locator |
|---|---|---|
| LV19-D25P-001 | D4 段在两版本先把 589/649/750 分给 D2-3qp，后又称 589/649/780 是 D4↔D3 E2；target/表中 spin tuple 须保留歧义，整体正 family 支持不撤销 | direct literal topology boundary；raw PDF2/Fig.1 PDF3，VoR 024314-2/4 |
| LV19-D25P-002 | D2 Ei=2588.3 的 207.5/399.9 行与三个相邻闭合路径及 D4 649.3 链都给 2558.3 不符；不自行更正 table 或创造新测量 | literal tuple + conditional arithmetic；raw PDF7–9，VoR 024314-3/4，positive-link-boundary.json |
| LV19-D25P-003 | 135Nd 矩阵应区分正 D3/D4 的新拓扑/一个 D3 比与负 D5/D6 的早期 paired absolute EM/新相对 corroboration；缺项不抹去支持 | cross-source synthesis；raw PDF2/5–6，既有 R52/R103 |
| LV19-D25P-004 | LV19 没有重分析 MU07 τ/branch normalizer；独立 relative 比与经 γ 校准的 PRM 有不同于独立 absolute B 复测的验证角色 | source lineage/calibration；raw PDF5，VoR 024314-8，Ref.36 |
| LV19-D25P-005 | 最小有界比较包含身份、匹配绝对 EM、独立组态/形状 companion 与冻结 holdout；缺项具体降级，不作普适 chiral rejection | task research design；上表及原件缺口，不是 paper fact |

## 收束与写入边界

本单元是 **Day25 preview、credit 0**；same Day24 run。未创建 session/run，未修改课程状态，未读 Day26。只写指定 worker 与 `tmp/day24-day25-preview-nd135-018/`；canonical/raw/PLAN/Bib/Git 保持只读。长期知识由 leader 审核写回 knowledge，outputs 不作第二事实库。
