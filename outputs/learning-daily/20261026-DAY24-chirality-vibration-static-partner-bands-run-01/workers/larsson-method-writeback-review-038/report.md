# 038：Larsson方法写回的短read-only review

结论：**受检新增文字未发现实质P0/P1误转录或过强认证。** 有一项可选的literal措辞微调；无需为审查另造科学问题。本worker未改canonical/raw/Git，也未运行新代码或原producer。

受检对象：新source `knowledge/sources/larsson-1978-nuclear-core-quasiparticle-coupling.md` 的LLR78-D24-001–012、133Ce blueprint“1978原方法”节、WK22-39、main135Nd替代scope及index入口。原件沿用032同一SHA108c29bed9de467d99f330c0b8cef47be82a290263a85e398ba3b4f2e97d77eb；本轮只定向回看原页PDF6/9/10/32/33的既有render，不重读35页。

## 核对结果

| 项目 | 原件定位与复核 | 判断 |
|---|---|---|
| 六矩阵bar/index | printed197/PDF9 Eqs11–16；前两项⟨χμ\|j±\|barχν⟩，后四项为unbarred ket；d=j²−j3²、e=j+²+j−²、Ω=j3、Ω²=j3² | source列表与对应(a+b)/c/d/e/Ω/Ω²一致，未丢bar或把j3²写成截断j3平方 |
| recoil与惯量 | 032已核printed191–192 Eqs6–7；新文保particle-H已含相应recoil才可删、constantcore的(4/3)J0 sin²(γ+2πk/3) | 正确，未把constant历史惯量当WK22 Harris/coreR实际值 |
| BCS两处方 | printed198/PDF10的standardBCS段与下一段schematic Δ12/√A/λoddorbital并列；原文ignoredblocking/recoil特殊性 | 新文正确保语境与忽略项，也没有给整个core+particle E2统一套plus factor |
| real signed / complex | printed220/PDF32 A3/A4 literal a_final a_initial，没有共轭星号 | 新文明确a_f* a_i只是通用复幅推广，signed coherent sum保留，未冒literal |
| A2方向/符号/单位 | printed220 A2为⟨I∥M∥I−1⟩，同页favoured/unfavoured sign rule限定decoupledband | RME顺序与WE/单位/emission/符号待actualoutput核的边界正确 |
| Table1→B比 | printed194/PDF6 γ4→ground4为127/102/70，ground4→2为−165/−164/−158；A1printed220 | source数值/分母相消条件正确，见下方精确分数 |
| 下游量词 | blueprint/WK22-39/main135Nd/index均保历史formalism已读与actual2022input/output缺口 | 没有把source/参数名字相同当actualproducer，也未把A193toy结论写成133Ce/135Nd实测或预测 |

### Table1算术核验

两组各自的跨模型比较都有相同Ii=4，A1的2Ii+1=9消去；共用reference标尺也在表中明确。因此：

- γ4→ground4，软/刚B比 = 127²/70² = **16129/4900 = 3.29163265…**；打印3.29163正确。
- 同支动态/刚 = 102²/70² = **10404/4900 = 2.12326531…**；打印2.12327正确。
- ground4→2，软/刚 = (−165)²/(−158)² = **27225/24964 = 1.09057042…**；打印1.09057正确。

负号在B中平方，不给signedRME/phase额外裁决；模型RME归一不是实测eb。新文已明确这些不是photon-rate/计数比、精度、功效或机时认证。没有Eγ与实验response时不补Eγ⁵或CI。

## 唯一可选微调，不作为实质阻断

LLR78-D24-007目前写“favoured→unfavoured负δ规则”。原printed220用的是**between a favoured state and an unfavoured state**，不写单向箭头。若追求literal精确，最小改为：

> favoured/unfavoured态之间的负δ规则限其decoupled-band语境。

这只是避免箭头多带一个方向含义，不重定任何δ convention或物理归属；其余A2上下文可原样保留。

## Scope与完成状态

032 worker实际方法scope仍为PDF1–11、31–34的15页范围，本review不将其改为35页全读。root另完成的036应用单元及后续scope合并由root统一记录；本review不抢写那段覆盖。

未改原review_status、needs_review或旧withdrawal；本报告是限定新增文字的self-audit，不是整篇/整库科学认证。无需新模型、全篇重读、网络或测试程序。
