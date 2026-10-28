---
type: research-note
title: "Day26：定量主张纠错与准粒子单体算符反例"
aliases: [Day26 quantitative claim corrections]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, bernard-2016-144ba-sccm-octupole, garg-2015-135pr-magnetic-rotation, roy-2011-cd110-systematics-antimagnetic]
created_from: Day26 source rereading and algebraic counterexamples
promotion_target: shears-mechanism
tags: [evidence-boundary, octupole, shears, correction]
---

# 定量主张的纠错与可复用反例

## Research Trigger

Day26 的后续工件与早先直接原件记录发生冲突。规范检查只检查文件结构，不能认证物理事实。013–015 中混合了自设参数、未定位的“实验”表和过强定理；其科学认证撤回，旧字节保存在 Git 历史。此页是 Codex self-audit，不改变已有人工审核和课程学分。

## Grounded Evidence

| 原主张 | 实际支持与修订 | 原件定位 |
| --- | --- | --- |
| 144Ba 的误差为 −29/+21，146Ba 为 −34/+25 | 原报告恰好相反：144Ba 为 48(−34/+25)，146Ba 为 48(−29/+21) W.u. | [[bucher-2016-144ba-direct-octupole]] Table I；[[bucher-2017-146ba-direct-octupole]] PDF3 |
| 97.1% 相消、逐核素质子/中子分项与 148Ba 实测负符号 | 015 的权重与宏观系数是自设值；BU17 仅支持模型中占据驱动的近相消和计算符号变化。数据对 E1/E3 相对符号不敏感。 | BU17 PDF3–5、Fig5 |
| 015 生产 HWG 给 E3=48 W.u.，E1 与实验完满吻合 | 实际保存的 JSON 将两核矩阵元和 E3 强度均舍入为 0.0。人为设定偶极核比例产生约89.9倍比值，不是生产 SCCM 预言。模型 H、N、算符核未来自原作者；删除低范数态后嵌回全空间的求解方式还可能引入伪零模。 | 015 Python 的 solve_hwg 与 JSON；方法比较见 [[bernard-2016-144ba-sccm-octupole]] Eqs3–5 |
| 两核坐标密度实测/原模型重叠85.9% | 原文只定性描述 very large overlap；85.9%来自自设高斯网格，不是数字化原图或生产核。 | BU17 PDF4 Fig4 |
| SCCM 绝对 E1 已得到精确验证 | 146Ba Table I 给实验0.000223与SCCM 0.00474 e b^(1/2)，打印幅度比21.26，强度比451.8。应保留绝对偏差与解释的定性成功两层。 | BU17 PDF3 Table I |
| 区间交叠84.8%意味着形状概率/模型排他判决 | 50/59只是两报告区间的 Jaccard 几何量；没有 likelihood、协方差或先验，不能恢复后验重叠系数、排他概率或统计显著性。 | BU16/BU17原报告区间 |
| 平衡点 D0≈0 蕴含整个非对角 E1 核处处为零 | 局部对角值不能限定所有 q,q′ 的非局域核；需要完整 f*O(q,q′)f 相干和。 | BE16 Eq4；BU17 PDF4 |
| 所有振动模型都只有8 W.u.且被排除 | 8是015自设值；振动图像没有普适固定强度。强E3支持集体关联，不能凭该值排除所有动态振动解释。 | BE16 Table I 的2D模型25 W.u.；BU16讨论 |

## One-body operator in a quasiparticle basis

数守恒的单体算符 T=Σtᵢⱼcᵢ†cⱼ，在 Bogoliubov 变换 c=Uβ+V*β† 后，通常含 T00、T11β†β、T20β†β† 与 T02ββ。因此“3qp与5qp相差两个准粒子，所以单体E2必为零”不成立。固定粒子 Slater 行列式的选则不能直接搬到准粒子数。

可复算反例：一个时间反演配对轨道的 BCS 因子为 |Φ⟩=u|0⟩+v|pair⟩；其两准粒子伴态为 −v|0⟩+u|pair⟩。三颗不受算符作用的旁观准粒子把两态分别变成3qp与5qp。对该时间偶单体分量在配对轨道上的限制 T=q(n₁+n₂)，两态正交，但矩阵元为2quv；u=0.8、v=0.6时为0.96q。这是反驳普适零定理的代数例，不是对135Pr实际约化E2的计算；角动量、宇称和具体波函数仍可使特定跃迁为零。

[[garg-2015-135pr-magnetic-rotation]] 在2015原文报告相对B(M1)/B(E2)，未测本带绝对强度。比值上升既可能来自分子，也可能来自分母；不能单凭比值认证B(M1)增强、E2塌缩或两个峰严格重合。27/2−为带低端身份，作者交叉约33/2−，保留2019勘误正文尚缺的版本边界。

## Parity displacement and rotor control

若 E(I)=A I(I+1)，简单邻点平均给 δE=E(I)−[E(I−1)+E(I+1)]/2=−A，理想同一转子也非零。需要消去该曲率时，可明确定义自旋加权插值：

δEw(I)=E(I)−{(I+1)E(I−1)+I E(I+1)}/(2I+1)。

它对上述理想转子为零。不同论文可能采用不同交错定义，必须先声明约定，再谈随自旋收敛。小宇称间隔还受组态、配对、隧穿与Coriolis作用影响，不能当静态梨形刚度的普适充要条件。010的逐核能量与“>340keV平台”未经原表逐点定位，不作为认证数据。

## AMR and direct data

理想对称两刃有 μ⊥=0，但纵向 μ∥=2gₕjₕcosθ+gₚjₚ 一般不为零；转动状态的非零角动量/电流也不能因此称时间反演不破缺。两个同种 g9/2 空穴的量子最大耦合为8ℏ，不能将经典2j=9ℏ当严格Pauli极限。

[[roy-2011-cd110-systematics-antimagnetic]] 原 Table1 的110Cd B(E2)=0.14(1)、0.12(2)、0.11(2)、0.09(3)、0.06(2) e²b²。原作者解释为AMR与core耦合，同时在p326说明最高28+不由AMR产生。013模型打印B(E2)约0.116→0.011，与0.14→0.06不能称“完满再现”；18%–26%分担是该工件条件输出而非实测比例。J^(2)/B(E2)带单位，大比值只作支持证据，无普适≥100排他门槛。Roy表的1323→1314keV还给出负有限差分；忽略这个点会造成选择偏差。频率中心、寿命条件换算与表列偏差在RO11-D26C-003–006逐项记录。

## Natural-basis zero-mode diagnostic

对015假定的41点高斯范数核与相同H进行026定向数值诊断。保留正范数本征模后应在r维自然基底中求解Hn=B†HB，B=Ur nr^(−1/2)，再令f=Bc，满足f†Nf=1。若把N^(−1/2) H N^(−1/2)嵌回41维再取最低本征态，弃掉的范数零空间也进入候选谱；其0附近本征值可以低于真正的正能量态。

本次原41点、绝对范数截断10^(−4)的实际复算中，旧路径选态的f†Nf接近零，而自然基底态为1；详情保存在026 JSON的legacy_input_diagnostic，不再仅是风险猜测。另比较41/61点与相对截断10^(−8)、10^(−6)、10^(−4)：自然基底偶态最低能约0.312–0.320、奇态约1.110–1.140（纯示例能量单位），保留截断依赖，不认证收敛到真实核。原E1核被人为缩放所给89.9倍比值，即使算术保留，也不能恢复实验或生产SCCM证据。

此处是离散非正交基的系数约定，矩阵积f†Nf及f†Of中不另乘网格步长；连续积分若采用求积权重，N、H、O与系数必须一起变换。数学实现遵循 [[bernard-2016-144ba-sccm-octupole]] Eq3–5的方法结构，但没有good-J/N/Z投影、HFB态或EDF，所以不输出物理E1/E3与W.u.。

## Knowledge Impact and Learning Decision

`revises` 013–015的来源身份与推导；`supports` E1与E3需要各自算符核、MR需要相对和绝对强度分层、AMR需要条件对称几何。下一步获取生产算符核/协方差及Pr勘误，而非用自设参数补齐。参见 [[octupole-mr-amr-evidence-gradient]]、[[shears-mechanism]] 与 [[antimagnetic-rotation]]。

## Provisional Reasoning

区分规范通过、算术复算、原文支持与独立实验证明四种状态；上文反例属于条件代数，原表核对属于直接文献记录。

## Assumptions

BCS例采用一对时间反演轨道与三个旁观态；位移例采用恒定惯量；磁矩例采用等长等g因子双刃。它们不含实际Pr/Cd生产波函数。

## Competing Explanations

交叉处可能有M1变化、E2变化或两者；Ba小E1可来自相消而大E3保留，但不同EDF和核配置还需比较。

## Transfer Conditions

只有算符定义、初末态自旋、对称性、模型空间与数据谱系一致时才可迁移公式；源值与自设参数分开。

## Failure Conditions

若原件不支持数字、缺生产核或模型不能再现表列结果，停止该数字的认证；文件可运行和lint通过不足以豁免。

## Falsification or Reverse Tests

019用非零3qp–5qp单体矩阵元反驳零定理，用理想转子−A残差检出未经修正的位移判据，并演示横向磁矩为零而纵向非零。

## Open Questions

尚缺Pr2019勘误正文、Ba有符号生产核和真实联合协方差；013多核数表需逐篇定位，不能作为已核系统学。

## Human Review

本轮是Codex self-audit；review_status保持unreviewed，未产生human-reviewed记录。

## Promotion or Rejection History

2026-10-28：撤回007–015的过强科学认证与未定位数值，将有原件支持的结果与条件反例分层。未改旧日学分与人审边界。
