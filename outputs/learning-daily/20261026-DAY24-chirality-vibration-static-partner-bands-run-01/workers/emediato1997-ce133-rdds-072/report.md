# Emediato 1997：¹³³Ce RDDS 寿命原实验（072）

本单元取得并完整阅读 APS 正式4页正文，逐页查看全部图表。它是独立于 Gizon 1974 的新寿命实验，不能把 ENSDF 的 52.7 ps 入口数值冒充本文原始表值：本文 Table II 给的是 **平均寿命 τ=76(3) ps**，按标准 \(T_{1/2}=\ln2\,τ\) 换算为 52.68(2.08) ps，四舍五入为 52.7(2.1) ps。ENSDF 069 的“52.7 PS 21”是这个半衰期对应项，并不是本文把 52.7 写作 τ。

## 来源、获取和范围

L. G. R. Emediato et al., *Lifetime measurements in ¹³³Ce*, Physical Review C **55**(4), 2105–2108 (1997), DOI [10.1103/PhysRevC.55.2105](https://doi.org/10.1103/PhysRevC.55.2105)。Crossref、APS落地页和PDF首页均匹配12位作者、卷期页码和题名。PDF 4页、102,259 bytes，SHA256 `39f6d6a7bb4e2da109504aaab2c22c52fa8b1465b860c1dfd58937bc404869df`；物理页+2104=印刷页。原件及页文本、渲染图在本单元 `tmp/day24-emediato1997-ce133-rdds-072/`。开读前 primed recall 在 `primed-recall.md`，已知 ENSDF/父任务提示但非盲测、不计分。

APS的 `journals.aps.org/prc/pdf/...` 直接入口返回正式PDF；`link.aps.org/pdf`重定向到摘要HTML，harvest FULLTEXT 端点一次401后停止重复。OpenAlex/Unpaywall将文章标为closed且无仓储PDF；OA批次返回 `oa_not_found`，不将直接可访问的APS PDF改称开放许可。着陆页无补充材料链接，SI在所查文章入口和正文范围内记为未识别，不做全网不存在声明。各路由和边界见 `access-manifest.json`。

## 实验 setup 与 RDDS 拟合合同

¹³³Ce由 **¹²⁰Sn(¹⁶O,3n)**、70 MeV 激发。探测器是0°的BGO Compton-suppressed HPGe（22%效率、约2.1 keV分辨率），与反应面垂直平面内至少一个3''×3'' NaI(Tl)符合。富集120Sn靶约1.0 mg/cm²、薄Au背衬面向束流；平均反冲速度约0.008c，约20 mg/cm² Pb stopper停住全部反冲。13个 target–stopper 距离约20–250 μm，由电容法和精密千分尺测量；另有 `d0` 零点浮动项，本文得到真实零距离 **22.5(1.0) μm**。

不同距离谱用Au背衬 Coulomb 激发的279 keV线归一，来自无NaI符合条件的HPGe独立输出。作者不是只拟合 shifted/unshifted 比值，而用 LIFETIME 同时拟合两类强度随距离的曲线，并调寿命与初始布居；应用位置/速度依赖固角、飞行中取向衰减和 slowing-down 期间介于 shifted/unshifted 的发射修正。必要时采用一步 side feeding。14条transition curves一起拟合，340个数据点、22个初始布居/跃迁概率参数，整体 reduced χ²=2.1。MINOS以 profile χ²+1 给正负误差；数据点误差含峰拟合统计与拟合误差。

这套描述没有给出原始计数、逐线响应核、完整速度分布、ICC处理表、Cov矩阵或 producer/job；不能从文章表格重建新的B或CI。约1 ps及以下只作为全部移位的上限，不能写成精确中心寿命或“其余态都没有寿命”。

## 负宇称 νh₁₁/₂ yrast 带

Table II（PDF3/2107）明确以 **τ(ps)** 列出：

|跃迁|Eγ (keV)|τ (ps)|实验跃迁概率|
|---|---:|---:|---|
|11/2⁻→9/2⁻|170|76(3)|B(M1)=65(2) mW.u.|
|13/2⁻→9/2⁻|555|7.9(5)|B(E2)=17(3) W.u.|
|13/2⁻→11/2⁻|385|同一7.9(5)|B(M1)=45(4) mW.u.|
|15/2⁻→11/2⁻|619|3.8(8)|B(E2)=52(15) W.u.|
|15/2⁻→13/2⁻|235|同一3.8(8)|B(M1)=56(15) mW.u.|
|17/2⁻→13/2⁻|752|≤1|B(E2)≥65 W.u.|
|17/2⁻→15/2⁻|517|同一≤1|B(M1)≥40 mW.u.|
|19/2⁻→15/2⁻|763|≤1|B(E2)≥65 W.u.|

实验表中 385 和 235 keV 线都有 double placement；B(M1) 按纯 M1 假定提取，作者又说 PTR 预言 E2 admixture <10%。因此这些 M1 不能当独立、无成分混合影响的精确磁跃迁测量。15/2 的 619 与 235 共享同一 τ，17/2 的752/517共享同一上限；不要把每条线分配成独立时钟。

作者比较 triaxial-rotor-plus-quasiparticle（PTR）与 Donau–Frauendorf 几何模型：E2 结果总体相当，13/2 与 15/2 的计算 B(M1) 约为实验三倍；170 keV上 PTR偏大、几何模型偏小。IBFM虽然复现低能 signature splitting，但图读 B(E2) 约0.02–0.12 e²b²，低实验约2–3倍。这样的 E2 支持与 M1 失败须同时保留。

PTR使用本论文模型输入 Δ=.92 MeV、λ=50.6 MeV、ℏω₀=8.41 MeV、N=4/5壳，VMI J₀=6.9 MeV⁻¹、C=.0061 MeV³、ε₂=.165、ε₄=.019；小的有效 γ≈−5°改善能级而跃迁概率对精确 γ 不敏感，作者另提低自旋 signature splitting 约70–100 keV曾被解释为 γ≈−30°。这些是1997模型输入/解释，不是现代WK22 producer参数或刚性三轴测量。几何模型图文字为 νh₁₁/₂[541]9/2⁻、K=9/2、gₙ=−.24、对齐2ℏ、g_R=Z/A；不要静默将[541]改成现代[514]。

## 正宇称三准粒子带

Table III（PDF3/2107）给出：17/2⁺→15/2⁻ 1269 keV，τ=5.3(6) ps，B(E1)=23 μW.u.；19/2⁺→17/2⁻ 954 keV，τ=4.5(5) ps，B(E1)=42 μW.u.；19/2⁺→17/2⁺ 201 keV，B(M1)=0.5 W.u.；21/2⁺→19/2⁺ 159 keV，τ=5.3(6) ps，B(M1)=1.1 W.u.。15/2⁺带头因1305 keV interband线太弱没有寿命；负宇称三准粒子带的 M1 仅给 τ<1 ps，未展示在 Fig.2。

Table III 的 νh₁₁/₂⊗πh₁₁/₂⊗πg₇/₂ 组态是沿用 Ref.1 的先前指认；本实验的正宇称 M1量级与几何模型相符，但不构成一次新的组态独立证明。原文最后段将 23/42 μW.u. 的两个 E1 值按相反顺序叙述，和 Table III 不一致；两种 literal 版本都保留，未擅自选一项。

## 评估值转换、谱系和适用性

对 Table II 11/2⁻→9/2⁻：76(3) ps×ln2 = 52.6796(2.0794) ps，正好对应 ENSDF 069 的 207.4 keV、11/2⁻、T₁/₂=52.7(2.1) ps 项（该评估能级与本篇170 keV图示网络的现代绑定来自评估，不是原论文绝对 Eₓ表）。这一步是单位/定义核对，不是独立寿命测量，也不能将 ENSDF 的 T 列倒写成原文 τ。

Gizon1974 的历史谱给低负宇称网络和短 side-band clock；Emediato 是同反应不同年份的独立 RDDS 寿命采集，但相对强度和部分谱系引用 1987 年同反应工作。1997 论文只测了列出的低态/三准粒子 transition；没有“全 ¹³³Ce 没有寿命”的结论。现代 832.0/1409.8/1809.1 等母态不能只凭相同 Jπ 或近能量套用这些 τ。

原子化主张和表格文字见 `claim-ledger.json`；三张表逐行转录及文献内部冲突见 `original-table-ledger.json`；τ→T₁/₂与ENSDF对应核算见 `clock-and-table-crosscheck.json`。本单元没有运行作者模型、没有拟合新数据、没有修改 canonical/raw/Git 或 producer。来源自审不是 human-reviewed。
