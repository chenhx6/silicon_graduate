---
type: research-note
title: "Eu152源响应重放：事件单位、几何顺序与有限MC统计"
aliases: [Eu152 source response replay, GRETINA finite MC calibration contract]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [ucgretina-2024-geant4-11-source-replay, ucgretina-2012-eu152-public-calibration-data, riley-2021-ucgretina-energy-response]
created_from: Day16 independent run, uncredited Day17 response preview
promotion_target: compton-polarimetry
tags: [source-calibration, covariance, GRETINA, simulation-readiness, geometry]
---

# Eu152：先定义模型的输入和事件单位，再比较能谱

## Research Trigger

公开七quad源/背景hist能核背景归一，却缺历史MC模板与eventΣ。Day16的DCO双解需要matching偏振companion；在尝试把公开模拟当Q校准之前，先检查实际可用代码能支撑哪一层response。

## Grounded Evidence

[[ucgretina-2012-eu152-public-calibration-data]] UE12-1–8：真实2012 NSCL七quad源/背景egam；1800–3000的共享归一a=.456739181，条件σ=.00468656。原件没有TTree/Comptonξ/历史MC模板，真实实验eventΣ尚未恢复。

[[ucgretina-2024-geant4-11-source-replay]] UG24-1–12：固定G411/11.4.2已实际编译、运行并native解码。原all-empty decay truth、仅改process名后的26空槽、新source-only append和逐位CRYS对照分别保留，不能将第三个版本的通过覆盖前两个失败。仅记录层改动的相同种子183/349条core/IP不变；sourceframe改动则物理history会变。

源框对照的必要companion是**实际导航volume和有效材料**。原decay宏虽含命令且exit0，单event Eu152实际从Target出发；另名postinitialize recipe从euTape出发。不能用参数报告中的“including frame”替代这个检查。1000event新recipe为367条CRYS/287探测history，仍不是实验效率。

### Riley2021原件补齐的实际参数身份

[[riley-2021-ucgretina-energy-response]] R21-1/7/11–18完整原读26页及12图后，限定其主线为十二quad/flood和单晶pencil数据。当前100k模拟的asolid两shape，经format doc、parser及usePassive核，实际coax/back/outer=1.5/2.5/.9mm，数值对应论文Table2 II；输入hash保持，不将此数值相同写成七quad2012与十二quad2019–2020的响应一致。

Table2 I/II只改变采用的同组效率能区，outer optimum由.4变.9mm，coax/back也随之变；图7/8有参数valley。作者指出一组有效参数无法同时复现低能效率和continuum，模型stat intervals不代表真实层厚度精度。当前源MC已具输入身份和模型Σ，仍缺原实验的matched response与联合Σ。

R21的continuum为1172/1173target、upstream LaBr1332gate；[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] L25-30为1333target/1173gate，不能只以60Co或约1.3MeV叫同一个reference。约210keV背散射的Compton公式检查解释了邻接/后方材料为何影响continuum，不能从能谱0阶响应推出偏振cos2 harmonic灵敏度Q。

## Assumptions

本模型只用非偏振source能量。无POL、无Q、无实验δ fit；coreE/timestamp/IP读取排除未初始化trig_time/unused tail及未认证beta。默认没有外加能量分辨率、门阈值或addback；若后来引入，须冻结另一命名response，不能倒填为历史producer。

单primaryγ/event与decay/history分母不同。真实级联、电子与sum-in/out可改变能谱，不能把两组同N的hist裸相减解释为独立物理效率差。相同种子在改变几何后会改变后续RNG消耗，也不作逐eventpaired检验。

## Provisional Reasoning

### source-calibration可复用关口

| 层次 | 本run已获得的证据 | 保留的边界 |
| --- | --- | --- |
| 源码/依赖 | 724blob对Git tree、11.4.2官方header与安装副本一致 | 不等历史实验actualproducer |
| 构建 | headless无POL、原source不动、publicsha明确 | 编译通过不认证偏振EM |
| truth记录 | 两次原失败＋另名source-only append通过 | 不推广beta/boost或任意in-beam |
| 探测器核心字段 | 183/349同种子逐位相同、能量和/容量检查 | 仅所选1000history |
| 几何 | pre/post实际Target/euTape trace、有效POLY差别 | 全阵列solid warning与response未闭合 |
| 源能谱/有限MC | 1000控制＋各100000history实际区域计数/矩阵检查 | 历史模板、真实source-free与全响应精度未认证 |
| 实验偏振 | 尚无匹配Compton事件/response/Q | 不从无偏振source谱提Q或δ |

### 以独立history保留有限MC误差

对事前定义的互不重叠能区，令`c_e`为第e个完整history在各区的**晶体singles次数向量**，不是只取该history是否被探测。令`S=Σ_e c_e`、`H=Σ_e c_e c_e^T`、N为总模拟history数（包含未探测history）。

在固定N、history独立同分布的条件模型下，样本总数向量的协方差估计为：

`Cov_fixedN(S)=N/(N−1) × [H−SS^T/N]`。

若改成独立history到达数为Poisson，compound-Poisson插件估计为`Cov_Poisson(S)=H`。二者只因所条件化的N不同而不同，不能根据哪一个误差小就挑选。对于每history最多一个互斥类别的特例，前式回到multinomial负交叉项；对于一个history有多个晶体singles时，H包含真实模拟的跨晶体/跨区共享贡献。直接以hist bin counts作对角Poisson会漏掉这些项。

这是本任务明确推导的统计设计，尚未冒充实验Σ。真实ROOT没有history索引，不能把模拟H迁回实验数据。未来若把模板乘scale s，先有`s² Cov(S)`；若s由同一峰/背景估计，还须包含其方差与交叉Cov，不能固定s后宣称fullfit精度。

事前统计合同冻结四区`[120,128)`、`[1404,1412)`、`[1540,1800)`、`[1800,3000)`keV，及与8000×1keV→Rebin4相同的能谱轴。它们对应UE12的grossROI/高区问题，不预设高区source-free。单γ表max1408.022给能量守恒control；decay级联/电子模式则须实际查看，不能从单γ表的cutoff外推。

### 实际1000history统计控制

UG24-13/14的新计算已实际执行，不是虚构counts：

| 源模型（均N1000） | 两个低区S1/S2 | H12 | fixedN总数Cov12/counts² |
| --- | --- | --- | --- |
| 单primaryγ，原postinit frame | 27/5 | 0 | −.135135 |
| 完整decay，另名postinit frame | 38/14 | 3 | +2.470470 |

fixedN矩阵均PSD，8000-bin计数与四区history向量求和一致，另一NumPy样本Cov路线到2.14×10^-14counts²内闭合，输入hash保持。decay另有同history同bin多singles使Hdiag比裸counts多2。这是源事件分母/级联与条件化方式能改变协方差的实际模型示例；不把两个模型当独立实验。

两个高区在小样本均为0；该模型的单侧95%history-hit概率上限约.00299125。它的分母是全部1000history，不是被探测的160/287；该界也不直接限制每history平均singles或真实实验源污染。零插件方差不表示已知无源贡献。随后按原冻结合同执行100000history，结果见下一节。

### 100000history的实际增量

UG24-15–17：两个新种子run、native decode和history脚本均exit0，γ/decay有20431/32976条core singles，四区计数依次`(2364,555,0,0)`与`(3611,850,3,0)`。fixedN的低区Cov12=−13.120331/+7.306573counts²，若把history数Poisson化则为H12=0/38。hist/history求和、两种Cov算法、PSD和读后hash全部通过；这份模型Σ已有实际输入与失败检查，实验Σ仍缺。

3条1540–1800记录回到histories52586/60023/81372。其中history60023的core1643.411621keV大于各单γ，却与记录1299.133057+344.278595之和在3.06×10^-5keV内相符；这是保留级联sum-in解释的具体对象，不仅说“可能有级联”，也不按能量相符就认证逐track起源。

1800–3000仍零观测，模型内history-hit概率的单侧95%界降至2.9956874×10^-5。该界不包含几何、源框、nuclear packages、历史event窗口或实验背景漂移，不能直接修UE12的alpha，更不能成为Compton Q标定。单γ模式的结构上界与decay模型的有限样本上界也须分开。

## Competing Explanations

原程序exit0、参数日志含frame、仅修process名、两个同种子文件SHA不同，都不足以独自证明模型有效或无效。实际empty truth、核态/光子索引区分、剔除未初始化字节后的逐位core比较及Target/euTape导航分别约束不同对象。

Morse pureE2偏振校准的成功控制仍保留于[[ucgretina-2021-polarized-emission-code]] UC21-8；本source兼容/几何问题不反驳那个原实验。NSCL2012七quad与Morse六quad、L26十二quad/47crystals的response不同，源能谱再吻合也不自动使Q可迁移。

## Failure Conditions

- CConvexPolyhedron的BoundingLimits、微小wall-plane提示与源框preinit指针顺序未被全几何认证；精确允许warning只保障可追踪继续，不证明无偏。
- radioactive-decay/PhotonEvaporation包不同历史版；level文件虽固定，不能据此称完整历史nuclide-decay输入相同。
- 电子贡献、cascade angular correlations、探测分辨率/threshold、背景漂移、原simulation sorting与fitCov尚未全部闭合。
- 当前各100000history的高区/有限MC结果已写回；未拟历史p1或Q。极长decay时间阈值下完整history与实际触发/积分窗口是否匹配仍需原件核查，虚拟timestamp不能直接当DAQ物理时间。

## Transfer Conditions

可迁移的是source identity→实际geometry→有效binary字段→history统计的核验方法。迁移到另一阵列、interaction ordering或偏振分析时，须重新给matching response、reference/门、Compton角与Q合同，不能仅改核素标签复用本模型。

## Falsification or Reverse Tests

单γ模式出现超出1408.022keV上界且超出浮点门的core deposit、相同记录层副本的已初始化CRYS改变、或postinitialize primary未进入euTape，均可反驳本页相应局部判断。有限MC矩阵若非PSD或遗漏未探测history，也应停止其误差传播；不能用clip消去。

## Open Questions

各100000history检查及Riley2021原件主线/图表、5733点网格、实际II参数和Compton机制核验已通过。原back-fraction计数分母/归一ledger、联合误差与exact response仍缺；需要新的原producer/实验方法输入来决定可重放的空间子类或门控校准，而非盲加统计或调source geometry、α/Q追印刷值。此路线仍是Day16下partial17，不开Day18。

## Human Review

本页是Codex self-audit，所有支撑source新claim均needs_review；没有新增human-reviewed或实验事实。常规科学边界留作具体claim追踪，不自动转成用户待办。

## Promotion or Rejection History

2026-10-19：新增source-replay合同与各100000history实际模型统计；接受有效字段/源框导航/条件Cov证据，拒绝将程序exit0、无偏振谱或source-only patch提升为实验P/Q/δ认证。

## Reproducibility

原版本、完整724blob校验、两次truth失败、source-only overlay diff与pre/post导航log索引见[[ucgretina-2024-geant4-11-source-replay]] UG24-1–12。源文件、MC与SDK不被此note修改；100k输入/种子/后处理四区与协方差定义先冻结在本run的`ucgretina-g411-eu152-100k-contract.json`及freeze，输出另记，不将receipt metadata当科学证据。
