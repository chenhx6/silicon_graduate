---
type: l3-report
title: "L3 专题研学报告：同核异能态微观壳演化、天体物理 Astromer 与超重核转移反应机制（2026-11-07）"
project: "isomer-cross-region"
worker: "R4"
date: "2026-11-07"
status: complete
boundary_audit: passed
---

# L3 专题研学报告：同核异能态微观壳演化、天体物理 Astromer 与超重核转移反应机制

## 1. 任务边界与合规性审查（Boundary & Compliance）

本轮任务作为 Research Worker R4 独立执行，严格恪守 Wiki 架构契约与工作指令：
- **专有研读范围（Exclusive Scope）**：
  1. `raw/papers/isomer/isomer_application/nuclear_astrophysics/`（7 份物理原件，含版本对照与完全重复件）；
  2. `raw/papers/isomer/isomer_application/superheavy_nuclei/`（3 份物理原件，含经典理论与 Nature 实验原件）。
- **外部归属文献隔离（Ownership Boundary）**：
  - `2016_Review of metastable states in heavy nuclei.pdf`（Dracoulis, Walker, Kondev 2016 Rep. Prog. Phys.，47 页）归属于并行 Worker；本轮仅将其作为参考背景全文深读，**未在 `knowledge/sources/` 中创建或修改任何相关 source 页面**。
- **写入权限隔离（Write Sandbox）**：
  - 仅写入本次范围对应的 7 篇原创论文的新建源页 `knowledge/sources/*.md`；
  - 写入专题研究笔记 `knowledge/research-notes/isomer-shell-evolution-astrophysics-and-superheavy-transfer-20261107.md`；
  - 写入运行过程与成果目录 `tmp/runs/isomer-20261107/astro-she/` 与 `outputs/l3/20261107-isomer-cross-region/astro-she/`；
  - 严禁且无任何共享知识源、索引（index）、问题集（questions）、规则（system）、BibTeX 基线、或 raw 原始文件的修改；严禁且无任何 Git 提交（commit/push）或派生代理调用。

---

## 2. 原始文献全息对账与谱系关系（Corpus & Lineage）

全量 10 份物理原件已完成逐页精读、哈希校验与版本拓扑映射，详情见配套 `coverage_ledger.json`：
1. **Watanabe et al. (PRL 2013)**：
   - 原件：`2013_Watanabe et al_Isomers in Pd 128 and Pd 126  Evidence for a Robust Shell Closure at the Neutron Magic Number 82 in.pdf`（366,537 字节，5 页，SHA-256 `dc7d219a...`）
   - 知识落点：`knowledge/sources/watanabe-2013-128pd-126pd-isomers-n82.md`
2. **Taprogge et al. (PRL 2014)**：
   - 原件：`2014_Taprogge et al_1 p 3  2 Proton-Hole State in Sn 132 and the Shell Structure Along N = 82.pdf`（368,491 字节，6 页，SHA-256 `2be3b185...`）
   - 知识落点：`knowledge/sources/taprogge-2014-sn132-proton-hole-n82.md`
   - 重复件：同目录下 `... 1.pdf` 经 SHA-256 强校验确认是逐字节完全相同的物理副本（Byte-identical duplicate），已在源页元数据中登记为 `alternate_version_file`。
3. **Martin et al. (PRL 2016)**：
   - 原件 1（最终发表版）：`2016_Martin et al_Impact of Nuclear Mass Uncertainties on the r Process.pdf`（794,047 字节，6 页，SHA-256 `bcc1be25...`）
   - 原件 2（投稿录用清样版）：`... 1.pdf`（1,708,925 字节，7 页，SHA-256 `c9045474...`，CHORUS Accepted Manuscript）
   - 知识落点：`knowledge/sources/martin-2016-mass-uncertainties-r-process.md`（完整记录双版本对账）
4. **Yuan et al. (PLB 2016)**：
   - 原件：`2016_Yuan et al_Isomerism in the “south-east” of 132Sn and a predicted neutron-decaying isomer in 129Pd 1.pdf`（517,797 字节，6 页，SHA-256 `cf9c983d...`）
   - 知识落点：`knowledge/sources/yuan-2016-southeast-132sn-129pd-isomer.md`
5. **Yang et al. (PRL 2024)**：
   - 原件：`2024_Yang et al_Discovery of New Isotopes Os 160 and W 156  Revealing Enhanced Stability of the N = 82 Shell Closur.pdf`（626,952 字节，6 页，SHA-256 `24ab061d...`）
   - 知识落点：`knowledge/sources/yang-2024-os160-w156-n82-stability.md`
6. **Xu et al. (PRL 2004)**：
   - 原件：`2004_Xu et al_Enhanced Stability of Superheavy Nuclei Due to High-Spin Isomerism.pdf`（174,665 字节，4 页，SHA-256 `9e6cdfecc...`）
   - 知识落点：`knowledge/sources/xu-2004-superheavy-high-spin-isomer-stability.md`
7. **Herzberg et al. (Nature 2006)**：
   - 原件：`2006_Herzberg et al_Nuclear isomers in superheavy elements as stepping stones towards the island of stability.pdf`（321,125 字节，4 页，SHA-256 `a18026ab...`）
   - 知识落点：`knowledge/sources/herzberg-2006-superheavy-isomers-stepping-stones.md`
8. **Dracoulis et al. (Rep. Prog. Phys. 2016)**：
   - 原件：`2016_Review of metastable states in heavy nuclei.pdf`（4,744,441 字节，47 页，SHA-256 `2cd8ce21...`）
   - 遵循所有权隔离，只读吸收，不建新源。

---

## 3. 关键跨区科学焦点决议摘要

### 3.1 $^{129}\text{Pd}$ 中子放射性：模型预言性质与精确动理学阈值
- **模型推导性质**：Yuan 2016 基于 `jj46` 壳模型计算，预言 $^{129}\text{Pd}$ 存在高自旋异能态 $J^\pi = 19/2^-$（$E_x = 1.903\text{ MeV}$）。算得 $S_n = 1.524\text{ MeV}$，高出 $^{128}\text{Pd}(0^+) + n$ 阈值 $Q_n = 0.379\text{ MeV}$（FRDM 为 $0.442\text{ MeV}$；AME2012 外推为 $0.123\text{ MeV}$）。
- **子核能级限制与衰变通道**：子核 $^{128}\text{Pd}$ 的第一激发态 $2^+$ 位于 $1.311\text{ MeV}$（Watanabe 2013），衰变到 $2^+$ 态需要 $Q_n > 1.311\text{ MeV}$，在能量上被严格禁戒。因此中子发射只能走向 $0^+$ 基态，受角动量与宇称守恒限制必须为 $\ell = 9\hbar$ 离心穿透，算得部分半衰期 $T_{1/2}(n) \approx 0.3–10\ \mu\text{s}$，与电磁 $E2$ 退激寿命（$\tau_{E2} = 0.955\ \mu\text{s}$）直接竞争。
- **阈值敏感性与边界澄清**：中子衰变通道完全闭合要求 $S_n \ge 1.903\text{ MeV}$（比 `jj46` 计算值高出 $\ge 379\text{ keV}$）。若 $S_n$ 仅增加 $200\text{ keV}$，$Q_n$ 减为 $\sim 0.18\text{ MeV}$，离心势垒穿透大幅放缓，但通道尚未严格关闭。袁岑溪等（2016）在原文中明确指出中子放射性属于“尚未被发现的衰变模式”，该成果属于理论模型预言，不能在文献中表述为已证实的物理发现。

### 3.2 $^{132}\text{Sn}$ 单质子空穴态身份与天体物理外推机制
- **空穴参考基准**：Taprogge 2014 测定的质子空穴态严格相对于**双满壳 $^{132}_{50}\text{Sn}_{82}$ 核心**。在被测核 $^{131}_{49}\text{In}_{82}$ 中，通过 $^{131}\text{Cd}$ $\beta$ 衰变与 $^{132}\text{Cd}$ $\beta n$ 衰变观测到 $988\text{ keV}$ $\gamma$ 跃迁，衰变至已知的 $365(8)\text{ keV}$ 的 $(1/2^-)$ $\beta$ 异能态（$\pi 1p_{1/2}^{-1}$），确立 $1353\text{ keV}$ 能级为 $\pi 1p_{3/2}^{-1}$ 单质子空穴态。
- **研究对象与外推前提区分**：测得的 $\pi 1p_{3/2} - 1p_{1/2}$ 劈裂（$988\text{ keV}$）显著小于 $N=50$ 区，壳模型表明 $Z=38$ 和 $Z=40$ 的质子次壳闭合在 $N=82$ 链上彻底消失。作者基于“相互支持的幻数效应”推论缺乏质子次壳闭合将导致 $N=82$ 壳隙向更低质子数（$Z=38, 40$ 的 Sr, Zr）演化时发生淬灭，从而建议 $r$ 过程采用 HFB-24 等具有壳淬灭效应的模型。这与 Watanabe 2013 在 $Z=46$（$^{128}\text{Pd}$）实验测定的局域稳定性属于不同质子数对象与不同层次的论断（$Z=46$ 实验测量 vs $Z \le 40$ 模型外推），并非相同核素上的直接实验矛盾。

### 3.3 $^{160}\text{Os} / {}^{156}\text{W}$ 壳增强与同核异能态缺失之本质辨析
- **壳增强事实**：Yang 2024 通过近物所 SHANS 合成新同位素 $^{160}_{76}\text{Os}_{84}$ 与 $^{156}_{74}\text{W}_{82}$，测得折合 $\alpha$ 衰变宽度 $\delta^2$ 在 $Z > 68$ 持续单调下挫，证明 $N=82$ 中子满壳核心的结构刚性在缺中子极区得到保持与增强，压低了表面四体 $\alpha$ 预形成几率。
- **异能态缺失的原件事实与定位**：原文第 3 页左栏明确指出：依据 $N=84$ 同中子异位素能级系统学（引证文献 [23]：D. T. Joss et al., Phys. Lett. B 772, 703 (2017) Fig. 6），预期 $^{160}\text{Os}$ 中存在 $\nu(f_{7/2} \otimes h_{9/2})8^+$ Yrast Trap 异能态。但杨华彬等在 SHANS 实验中**未发现任何该异能态存在的证据**（no evidence for the isomer was found in the present work），所有事件均归属于基态衰变。
- **物理机制辨析**：平均场壳隙决定全局基态束缚能与稳定性；同核异能态的形成则高度敏感于特定多粒子态的微观能级相对次序。随质子数增加，组态相互作用的演化可能引起多重态能级微调或退激分支改变，使其寿命缩短脱离电子学测量窗口或受限于反应布居几率。壳闭合强化并不自动保证同核异能态的存在。

### 3.4 $^{254}\text{No}$ 实验结果对徐甫荣高自旋稳定性假说的检验与模型边界
- **能级与半衰期单位核验**：Xu 2004 预言形变超重核 $^{254}\text{No}$ 存在低激发双准粒子高 $K$ 异能态（双准中子 $8^-$ 在 $1.12\text{ MeV}$，双准质子 $8^-$ 在 $1.48\text{ MeV}$）。Herzberg 2006（Nature）实验测得基态带之上的长寿命异能态为 $T_{1/2} = 266(2)\text{ ms}$（$E_x = 1293\text{ keV}$）。高位异能态的半衰期为 **$T_{1/2} = 184(3)\ \mu\text{s}$（微秒，原文印刷为 $\mu\text{s}$，不可与毫秒混淆）**，量热电子分析给出其自旋下限 $J \ge 14$，四准粒子 $(16^+)$ 构型归属被作者明确标注为在实验层面上仍具有高度暂定性（highly tentative on experimental grounds alone）。
- **视觉核验强制校正（Explicit Visual Audit Override）**：针对 Nature 原版第 897 页正文、图 2b 插图及图注进行直接视觉高分辨率核查，确证该短寿命态半衰期为 $184 \pm 3\ \mu\text{s}$（微秒），而非提取工具 `pdftotext` 错误字符映射得到的 `184 ms`。微秒（$\mu\text{s}$）与毫秒（$\text{ms}$）异能态处于完全不同时间尺度，不可合并。
- **中间带带头与 $g_K$ 归属性质**：根据 Nature 442, 898 原文图 3，中间过渡的 $K^\pi = 3^+$ 转动带带头位于约 $988\text{ keV}$（$987.9\text{ keV}$）；$841\text{ keV}$ 与 $943\text{ keV}$ 为该带头退激至基态带 $4^+$ 与 $2^+$ 能级的 $M1$ $\gamma$ 射线能量，旧过程回执中误将 $943\text{ keV}$ 标为带头的断言在此正式纠正与撤回。实验测得的 $g_K = 0.87(14)$ 严格源自该中间 $3^+$ 带的带内分支跃迁比率，在转动模型框架下支持双准质子构型 $\{1/2^-[521]_p \otimes 7/2^-[514]_p\}3^+$，对应球形 $2f_{5/2}$ 质子能级。对于 $T_{1/2} = 266(2)\text{ ms}$ 的 $8^-$ 异能态，作者讨论了双准质子单质子跃迁退激优势与双准中子理论计算两类可能性，其两准粒子构型归属在文献中并非唯一确定。同时，该 $266\text{ ms}$ $8^-$ 态与高位 $184(3)\ \mu\text{s}$ 暂定 $(16^+)$ 态在寿命时间尺度（毫秒 vs 微秒）与构型复杂度上严格区分。

### 3.5 异能态冷态寿命演化与重离子反应截面的物理区分
- **冷核态寿命（Decay Phase）**：对于已形成的冷异能态，专属性势垒（Specialization Energy）以及配对减弱引起的推转惯量增大，确实能显著延长其自发裂变半衰期。
- **反应截面动力学（Production Phase）**：重离子完全熔合蒸发剩余核截面由各分波的俘获、复合核形成以及粒子蒸发生存几率卷积决定。在高温高激发复合核阶段，配对削弱，高态密度混沌破坏 $K$ 守恒，且旋转离心力降低裂变势垒，使得高角动量分波的存活几率显著降低。剩余核对特定异能态的布居取决于退激末端的 Yrast 馈送动力学。冷异能态的寿命延长不直接等同于其在熔合反应中具有更高的产生截面。

### 3.6 Seniority 方案代数相消边界与半满壳机械外推防范
- 在单 $j=9/2$ 质子壳层中，$^{128}_{46}\text{Pd}$（$n=4$ 空穴相对于 $Z=50$）接近理论半满壳（$n=5$），其实验测得的 $B(E2; 8^+ \to 6^+) = 0.22(3)\text{ W.u.}$ 受到显著阻碍（相比 $^{130}\text{Cd}$ $n=2$ 的 $1.3\text{ W.u.}$ 压低约 6 倍）。
- **防范误推声明**：严格相消点仅存在于单一轨道 $j$ 的精确半满壳 $n=(2j+1)/2$。严禁将单轨道相消机制机械外推至存在跨壳组态混合或非半满壳状态的核素（如 $^{130}\text{Sn}$ 或 $^{210}\text{Po}$）。

---

## 4. 可证伪天体物理 Astromer 与核反应转移方案设计

本研究在定性物理与细致平衡原理基础上提出四项方案：
1. **$^{131}\text{In}$ 双核素解耦 Astromer 天体物理模型**：针对 $9/2^+$ 基态与 $1/2^-$ 异能态，热平衡依赖于通过高位共振门态（如 $1353\text{ keV}$ 的 $3/2^-$ 态）的光激发。细致平衡需结合门态跃迁矩阵元、普朗克光子密度谱与流体膨胀时标。可证伪标准：若热平衡时标远大于膨胀与衰变时标，两态必须作为解耦核素追踪；反之则服从玻尔兹曼平衡。
2. **$^{128}\text{Pd}$ $8^+$ 异能态快速退激动力学**：基于 $\tau_{E2} = 5.8\ \mu\text{s} \ll \tau_\beta \sim 35\text{ ms}$，理论表明在缺乏持续高强度谐振光泵浦时，该态将迅速落回基态。
3. **$^{129}\text{Pd}$ $19/2^-$ 假想中子放射性检验**：需实验高精度测量单中子分离能 $S_n$ 与异能态能级 $E_x$。可证伪标准：若实际测得 $E_x \le S_n$（$Q_n \le 0$），则中子放射性衰变道在能动量守恒上完全关闭。
4. **深部非弹性多核子转移反应（MNT）合成形变超重核高 $K$ 异能态**：探索近垒重离子深部非弹性碰撞在适度激发能下布居形变超重核异能态的可行性。可证伪标准：若大角动量转移主要耗散为碎片的深部非弹性断裂内能与中子多重蒸发，导致目标形变带产额未能达到谱学测量信噪比阈值，则表明低能 MNT 无法有效规避超重核合成中的裂变竞争瓶颈。

---

## 5. 变更文件清单与最终状态检查

1. **新建知识源文件（NEW `knowledge/sources/`）**：
   - `knowledge/sources/watanabe-2013-128pd-126pd-isomers-n82.md`
   - `knowledge/sources/taprogge-2014-sn132-proton-hole-n82.md`
   - `knowledge/sources/martin-2016-mass-uncertainties-r-process.md`
   - `knowledge/sources/yuan-2016-southeast-132sn-129pd-isomer.md`
   - `knowledge/sources/yang-2024-os160-w156-n82-stability.md`
   - `knowledge/sources/xu-2004-superheavy-high-spin-isomer-stability.md`
   - `knowledge/sources/herzberg-2006-superheavy-isomers-stepping-stones.md`
2. **新建专题研究笔记（NEW `knowledge/research-notes/`）**：
   - `knowledge/research-notes/isomer-shell-evolution-astrophysics-and-superheavy-transfer-20261107.md`
3. **交付成果与过程文件（Outputs & Tmp）**：
   - `outputs/l3/20261107-isomer-cross-region/astro-she/coverage_ledger.json`
   - `outputs/l3/20261107-isomer-cross-region/astro-she/l3_report.md`
   - `tmp/runs/isomer-20261107/astro-she/coverage_ledger.json`
4. **质量与控制字符扫描（QA Scan）**：
   - 经 Python 二进制全量字节扫描，所有新建 Markdown 文件与 JSON 文件中完全杜绝了 `\a` (0x07)、`\f` (0x0c)、`\v` (0x0b) 及未预期的 TAB 等 Python 转义污染，TeX 公式语法全部严密闭合。
