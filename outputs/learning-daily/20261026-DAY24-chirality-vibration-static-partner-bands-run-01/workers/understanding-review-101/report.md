---
type: worker-review-report
task: /root/day24_understanding_101
target: outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/understanding-check-101.md
reviewer: day24_understanding_101
status: verified-no-op
created: 2026-10-27
scope: read-only-understanding-check
---

# Day24 理解核对 101 有界审查报告

## 审查范围与任务边界

本审查依据 `wiki-evidence-query` 技能与 Day24 运行约束执行：
1. 仅对 `outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/understanding-check-101.md` 中 root 预拟的 5 道读源后理解问题及回答进行严格证据对账；
2. 仅依据当前 canonical 知识页（`knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`、`knowledge/projects/133ce-thesis-analysis-blueprint.md`）、来源页（`knowledge/sources/tonev-2007-134pr-dynamic-chirality.md`、`wakudyanaye-2022-triaxiality-rotational-bands-133ce.md`、`mukhopadhyay-2007-135nd-chiral-vibration-static.md`、`frauendorf-meng-1997-tilted-rotation-chirality.md`）及本日已提取的原件图像/文本进行核对；
3. 不新开文献路线、不下载新文件、不增建 source/card、不修改 canonical/raw/PLAN/Bib/Git/课程状态，不派生子代理；
4. 检查重点涵盖：物理逻辑、物理量身份、相对相位与 $g_K$、约化矩阵元（RME）与初态统计因子、量词强度、以及文献重复计票。

---

## 逐题核对结论

### 答 1：左右手均场极小与有限核静态手征的区分

- **审查判定**：`supported`（原答成立；已采纳更精确的隧穿原始条目 locator）。
- **物理量与逻辑核验**：
  - 均场层面：TAC 在指定变形与转动输入下解出非平面（aplanar）解时，时间反演与空间旋转复合对称性（手征性）在内禀参考系破缺，出现左右手简并极小；
  - 量子系统层面：有限核量子 PRM（粒子-转子模型）中，左右手构型之间存在量子隧穿（tunneling），使得定态本征态出现能级劈裂（tunneling splitting），因而物理本征态并非永久固定于某一单侧内禀手性的定态；
  - 静态手征机制（static regime）物理上对应于势垒足够高、波函数在左/右手势阱中局域化（localization）且隧穿劈裂极小的渐进近似；
  - 量词与界限：清晰区分了 RPA 零频临界点、均场解分岔点、有限核能级劈裂以及实验中两带能级最近接近点，未将上述四个不同物理量等同为同一阈值。
- **现有精确 Locators**：
  - `knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md`：`FM97-4`（PDF pp. 11–12，说明 PRM 中隧穿劈裂使得双带在有限量子体系中仍非完全简并）；`FM97-D24P-001`（printed pp. 138–142 Sec. 3.1, Figs. 5–6 及最终 PRM 段落）；
  - `knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md`：`MU07-D24-002`（printed 172501-3/4，说明临界点比实验最近接近点高约 $1\hbar$）；
  - `knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`：第 54–67 行（内禀算符分量近似阶次展开与能隙物理对象分层）。

---

### 答 2：135Nd 两伙伴带总寿命不同与带内 B(E2) 相近的关系

- **审查判定**：`supported`。
- **物理量与逻辑核验**：
  - 物理量身份：能级总寿命 $\tau = 1/\Gamma_{\text{tot}}$ 对应母态向全退激网络所有可能通道（包括带内跃迁、带间跨带跃迁及可能存在的其它分支）的跃迁几率总和；而特定电磁跃迁几率 $B(\sigma L)$ 仅取决于初末态波函数与电磁多极算符矩阵元；
  - 速率依赖因子：跃迁分宽度 $\Gamma_\gamma \propto E_\gamma^{2L+1} B(\sigma L)$，不同伙伴带的退激分支比、末态能量分布及可能存在的微小能级差均会改变寿命与 $B$ 之间的比例系数；
  - 数值一致性对账（以 $I = 31/2^-$ 为例）：
    - 实验报告寿命：$\tau_A = 0.75(8)$ ps，$\tau_B = 1.46(2)$ ps，中央比 $\tau_B / \tau_A \approx 1.947$；
    - 实验推导带内强度：$B(E2)_A = 0.32(3)\ e^2b^2$，$B(E2)_B = 0.28(3)\ e^2b^2$，中央比 $B(E2)_B / B(E2)_A \approx 0.875$；
    - 图像与原文核对：`tmp/day24-originals/mukhopadhyay-2007-135nd-chiral-vibration-static-p2-001.png` Table I 原印数据与知识库完全一致；
  - 证据计票边界：上述寿命与推导 $B$ 来自同一条 Gammasphere DSAM / LINESHAPE 实验分析链，不得拆分为独立实验证据；在缺乏完整分支比、内转换系数（ICC）及误差协方差矩阵（Covariance）时，不凭高斯假设合成独立误差区间或人为构建置信度检验。
- **现有精确 Locators**：
  - `knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md`：Table I（printed 172501-2）、`MU07-D20-F01`、`MU07-7`；
  - `knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`：第 29–38 行（Table I 账本及衍生比）。

---

### 答 3：Tonev 2007 长文对形状涨落与静态手征/共存的证据地位

- **审查判定**：`supported`。
- **物理量与逻辑核验**：
  - 核心物理结论：Tonev 等人在 PRC 76, 044313 (2007) 详细报道了 $^{134}\text{Pr}$ 的 Euroball IV 实验，并对比了 TQPTR 与 IBFFM 两个模型：
    - TQPTR 模型：基于固定三轴形变与取向动力学，能较好描述能级能谱与 $I=15$ 处尖锐能带交叉，但在电磁跃迁几率（尤其是交错交替的跃迁分支）上与实验数据存在显著失配；
    - IBFFM 模型：引入玻色子核芯形变涨落自由度，在带内 $B(E2)$ 趋势上改善了与实验的一致性，但带间能隙过大，且在合理参数空间内无法重现 $I=15$ 的能级交叉；
  - 量词与作者结论严格性：作者在结论（Sec. VI, physical PDF25）中使用了有边界的表述：`"The present study suggests that the existence of the two crossing ΔI=1 bands with the same parity in 134Pr should be attributed to a weak fluctuation dominated chirality combined with an intrinsic symmetry yet to be revealed."` 原文明确指出存在“尚待揭示的内禀对称性”，并未宣称该核已排他性地否定了所有静态手征或形状共存机制；
  - 谱系与证据计票：
    - Tonev 2006 (PRL 96, 052501) 与 Tonev 2007 (PRC 76, 044313) 属于同一次 Euroball IV 实验数据的短报与长文报告，不可作为两套独立实验采集计票；
    - IBFFM 计算根据本次实验数据调整了相互作用与电磁算符参数（如 $e_{\text{vib}}=1.2$、$g_R=0.15$），故而 EM 吻合并非无参盲预测验证（independent holdout）；
    - $I > 16$ 处带 1 的曲率改变被作者解释为两个额外准粒子解对齐，属于作者的组态配置解释，非已直接数出核子数；
    - 不能将 $^{134}\text{Pr}$ 拟合所得的唯象参数直接迁移至 $^{135}\text{Nd}$ 或 $^{133}\text{Ce}$。
- **现有精确 Locators**：
  - `knowledge/sources/tonev-2007-134pr-dynamic-chirality.md`：`TO07-D24-001` 至 `TO07-D24-010`、physical PDF pp. 11, 17, 18, 23, 25；
  - 物理原件抽取文本：`tmp/day24-tonev2007-134pr-long-095/10.1103_PhysRevC.76.044313.pdf`。

---

### 答 4：未知伙伴带 g 因子的补齐边界与电磁矩阵元关系

- **审查判定**：`supported`（原答成立；采纳补充初态统计因子的措辞修订）。
- **物理量与逻辑核验**：
  - 实验报告状态：在 $^{135}\text{Nd}$ 的原始测量（MU07）中，并未逐能级测量伙伴带的 $g$ 因子，在知识库与证据矩阵中必须记录为 `unknown`，不可因未测补写为零；
  - 模型极限边界：纯单粒子 $j$ 极限的 $g_j$（如单 $\nu h_{11/2}$ 在截断自由值下的标量值）或轴对称形变下的渐近 Nilsson 内禀 $g_K$ 均属于特定极限；三轴混合态通常不存在无条件的单一好 $K$（good-$K$）量子数，不能直接用轴对称公式将角动量投影作为普适跃迁算符；
  - 跨核与跨态移植边界：$^{128}\text{Cs}$ 的 $g$ 因子测量针对的是 $9^+$、半衰期 $T_{1/2}=56$ ns 的带头同质异能态（采用 TDPAD 进动法），与高自旋皮秒（ps）量级的伙伴能级在核素、组态、自旋及寿命时钟尺度上均完全不同，不得跨核套用；
  - 电磁约化矩阵元（RME）与 $B$ 值的精确关系（本次采纳修订）：
    - 跃迁几率标准定义为 $B(\sigma L; I_i \to I_f) = \frac{1}{2I_i + 1} |\langle I_f || \hat{\mathcal{M}}(\sigma L) || I_i \rangle|^2$（见 WK22 Eq. 3.21 / PDF p. 48）；必须包含初态统计权重 $1/(2I_i+1)$ 与算符张量归一，不可将 $B$ 直接等同于裸 RME 模平方；
    - 混合比 $\delta$ 的符号由 $E2$ 与 $M1$ 的相对振幅与相位共同决定（$\delta \propto \frac{\langle I_f || \mathcal{M}(E2) || I_i \rangle}{\langle I_f || \mathcal{M}(M1) || I_i \rangle}$）；不能把单态内禀期望值或 $g_K$ 混同为具有跨带跃迁相位的有符号 RME。
- **现有精确 Locators**：
  - `knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`：第 45 行、第 194–208 行（$^{128}\text{Cs}$ TDPAD 测量与高自旋寿命尺度差异分析）；
  - `knowledge/projects/133ce-thesis-analysis-blueprint.md`：第 266 行（单粒子 $g_j$ 与渐近 $g_K$ 极限）、第 460–484 行（PROBMO 算符定义、相位与字典）；
  - `knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md`：PDF p. 48 Eq. 2.31 / Eq. 3.21。

---

### 答 5：133Ce 候选能差与同母分母/跨带跃迁误读审查

- **审查判定**：`supported`。
- **物理量与逻辑核验**：
  - 能差与实验跃迁边界：
    - 能级能量差 $1409.8 - 592.1 = 817.7$ keV 仅为算术候选能差（母态 Band 4 $17/2^-$ 到 Band 1 $13/2^-$）；
    - 查对 WK22 Table 5.2（实验跃迁表）与 Fig. 5.1（能级纲图），均未收录 817.7 keV 跃迁，无光子强度、DCO 比值或分支比记录；
    - Gizon 1974 Table 4 中列出的未指认弱线 817.3 keV 无符合门谱证据绑定到 1409.8 keV 能级，不能借此将 817.7 keV 升级为已观测跃迁或作为 582.7 keV 的同母态 out/out 参考分母；
  - 正宇称近邻 $13/2^+$ 态及其衰变连接：
    - 正宇称存在两个相距仅 14.1 keV 的近邻态：$1459.9$ keV（Band 2 $13/2^+$）与 $1445.8$ keV（Band 3 $13/2^+$）；
    - 查对 WK22 Table 5.4（`tmp/day24-wk22-table54-098.png` / PDF p. 71）：两条跨带连接 412.4 keV（到 $1033.4\ \text{keV}, 11/2^+$，$I_\gamma = 0.20(9)$）和 767.7 keV（到 $678.1\ \text{keV}, 9/2^+$，$I_\gamma = 0.58(7)$）**均出自同一个 $1445.8$ keV 母态**；
    - 属于 Band 2 的 $1459.9$ keV 态在 Table 5.3 中的退激跃迁为 426.4 keV 和 781.8 keV；并非由两个 $13/2^+$ 态分别发射 412.4 与 767.7 keV；
    - 两个近邻能级能差小仅构成同自旋节点身份区分练习，并不等同于实验上测得了转动交叉频率 $\omega_c$ 或能带混合矩阵元。
- **现有精确 Locators**：
  - `knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md`：`WK22-20`（Table 6.11 out/out 分母缺口）、`WK22-34`（近邻 $13/2^+$ 能差与跨带连接）、`WK22-44`（817.3 历史线与 817.7 能差边界）、`WK22-46`（Table 5.4 母末态归属修正）；
  - `knowledge/projects/133ce-thesis-analysis-blueprint.md`：第 61–63 行、第 273 行、第 372 行、第 615 行。

---

## 审查小结与状态判定

1. **事实增量判定**：`verified-no-op`。
   本审查未引入任何新的科学假设、未向 canonical 知识库添加未经核实的新事实，未修改任何 Git 跟踪文件，未触碰 raw/PLAN/Bib 目录，未宣布 `human-reviewed`，亦未变更课程学分状态。
2. **文本采纳闭环**：
   root 在 `outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/understanding-check-101.md` 中已完全采纳代理建议：
   - 在第 1 答中补全了 `FM97-4` 隧穿原件依据；
   - 在第 4 答中补充了初态统计因子 $1/(2I_i+1)$ 与算符张量归一说明，修正了将 $B$ 值简化为裸 RME 模平方的表述漏洞。
3. **时限合规**：
   全审查于 15 分钟内严格收束于只读和本地报告生成，符合不足 90 分钟不新开 source/card 的有界审计契约。
