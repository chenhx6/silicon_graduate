# G17产出窄事实校验与纠错审计报告 (Worker G25)

- **审计对象**：
  - `knowledge/research-notes/continuation-g17-mo98-absolute-constraints-20261107.md`
  - `knowledge/sources/continuation-g17-chen-singh-2020-nds-98mo.md`
  - `knowledge/sources/continuation-g17-thomas-2016-96-98mo-coexistence.md`
- **核验原件**：
  1. `raw/papers/gpt/query/20261107-continuation-G17/nds-2020-chen-singh-98mo-adopted.pdf`（NDS 164, 1 (2020) 官方 Adopted Levels, Gammas 98Mo 评价底本，51页）
  2. `raw/papers/gpt/query/20261107-continuation-G17/thomas-2016-96-98mo-coexistence.xml` 及 `.pdf`（Thomas et al., NPA 947 (2016) 203–233 全文）
  3. `raw/papers/⁹⁸Mo A possible candidate for octupole collectivity in A ≈ 100 region.pdf`（Karmakar et al., NPA 1066 (2026) 123265 出版全文，8页）
- **纠错与对照参照**：
  1. `knowledge/sources/campaign-g13-iskra-2019-96zr-revised-e3.md`（Iskra et al., PLB 788 (2019) 396–400）
  2. `knowledge/research-notes/octupole-orbital-eligibility-and-collectivity-boundary-20261107.md`（Suhonen 微观 Racah 代数与三阶张量三角不等式精确解）
  3. `knowledge/research-notes/mo98-ru100-same-parent-e1-e3-constraints-20261107.md`（同母态 E1/E3 分母消除与相对区分力分析）
- **备份目录**：`tmp/runs/20261107-nuclear-continuation/G25/drafts/`

---

## 四项核心核验与纠错事实

### A. Chen & Singh 2020 评价原件核验（98Mo覆盖、寿命、B(E3)方向与虚构数据清除）
- **核验结论**：
  - **覆盖真实性**：确实直接覆盖 $^{98}\text{Mo}$，底本即为 NNDC ENSDF 官方截取的 $^{98}\text{Mo}$ Adopted Levels, Gammas 出版件（51 物理页），文献截止 2020-02-15（含 2021-05-06 修改批注），作者 Jun Chen, Balraj Singh，DOI: 10.1016/j.nds.2020.01.001。
  - **3- 寿命性质**：原件第 3 页明确列出 2017.53(3) keV $3^-_1$ 态的 $T_{1/2} = 65(7)\text{ ps}$（半衰期，对应平均寿命 $\tau = 93.8(101)\text{ ps}$）。
  - **B(E3) 方向与数值**：原件第 15 页针对 2017.46(10) keV $\gamma$ 退激基态跃迁（$3^-_1 \to 0^+_1$）直接给出 $[E3]$ 向下跃迁几率 $B(E3\downarrow) = 30^{+7}_{-5}\text{ W.u.}$（量纲值 $0.0171(35)\text{ }e^2\text{b}^3$）。向上基态库仑激发跃迁 $B(E3\uparrow; 0^+_1 \to 3^-_1)$ 含有初态自旋统计权重 $2J+1=7$，量纲值为 $7 \times B(E3\downarrow) \approx 0.120\text{ }e^2\text{b}^3$；两者定义不可混淆。
  - **虚构数值与文件清除**：G17 在 source CS20-F1 中声称“库仑激发数据集为 37(6) W.u.”并标注 locator 为 `coulex.pdf p.2`。经原件全文检索，51 页底本中根本不存在该数值，且归档目录中无任何名为 `coulex.pdf` 的文件。此项属无证据推断，已彻底删除并修正 locator 为 `p.3, p.15`。

### B. 能级对应性、寿命空白范围与 Thomas 2016 测生态核验
- **核验结论**：
  - **能级一一对应**：
    - $5^-_1$：ENSDF 2620.78(5) keV $\leftrightarrow$ Thomas 2016 2620.56(17) keV $\leftrightarrow$ Karmakar 2026 2620.4(3) keV。
    - $7^-_1$：ENSDF 3096.26(16) keV $\leftrightarrow$ Thomas 2016 3095.74(19) keV $\leftrightarrow$ Karmakar 2026 3095.4(4) keV。
    - $9^-_1$（Band 2）：ENSDF 3656.7(3) keV $\leftrightarrow$ Karmakar 2026 3655.7(4) keV（Thomas 2016 实验入射能 16 MeV 未布居该态）。
    - $9^-_2$（Band 3）：ENSDF 3768.7(6) keV $\leftrightarrow$ Karmakar 2026 3767.5(4) keV（属侧带伴带，退激仅观测到 672.4 keV，无带间 E1，严格与八极主带 $9^-_1$ 隔离）。
  - **评价寿命空白**：Chen & Singh 2020 Adopted Levels 中，2620.78、3096.26、3656.7 与 3768.7 keV 四个负宇称能级的半衰期列全部留空，未给出任何测量值、上限或下限。
  - **Thomas 2016 寿命性质**：Thomas 2016 Table 2 提取有效寿命上限（$\tau_{\text{eff}} < 0.1\sim 0.6\text{ ps}$）的能级全部为偶宇称态（2206, 2333, 2525, 2700, 2871, 2905, 2916, 2976, 3050, 3228, 3556 keV 等）；2620.56 keV $5^-$ 与 3095.74 keV $7^-$ 在 Table 2 中的寿命列明确留空，正文第 2.2 节亦明确未提取负宇称态线形。
  - **不夸大历史从未**：将 G17 原 note 中“全部文献穷尽”、“世上无文献”等过度概括表述，收窄为“在本次取得并核验的 NDS 2020 评价底本与 Thomas 2016、Karmakar 2026 谱学文献中，目标负宇称态未见直接能级寿命或同态绝对跃迁几率数据”。

### C. 理论 ICC 剥离与 Citation Key 纯净化
- **核验结论**：
  - **ICC 剥离**：Karmakar 2026 Table 1 与 NDS 2020 Adopted Gammas 原始实验数据表仅报道 $\gamma$ 光子相对强度 $I_\gamma$；G17 在 Ledger 表中插入的 $\alpha = 2.77\times 10^{-3}$、$\alpha = 4.8\times 10^{-4}$ 等为未声明出处的理论 BrIcc 转换系数，易使读者误以为是实验直接测量值。已从 Ledger 表中剥离，仅保留实验报告的纯多极指认与混合比 $\delta$。
  - **Citation Key**：两篇新 source 的 `citation_key` 均核实为空字符串 `""`，未捏造未证实的 BibTeX 键值。

### D. 核心物理机制纠错与泛化论断收窄
- **核验结论**：
  - **纠错 1（96Zr 寿命冲突）**：G17 将 Mach 1990 的 $T_{1/2} = 50(7)\text{ ps}$ 与 Iskra 2019 修订的 $B(E3) = 42(3)\text{ W.u.}$ 拼合。经核查 Iskra 2019 原文（PLB 788, 396 [[campaign-g13-iskra-2019-96zr-revised-e3]]），Iskra 明确采用 Horen 1993 的 $T_{1/2} = 67.8(43)\text{ ps}$（并指出加权平均值 66.2(40) ps 相容），结合 12.8(3):100（1897.2/1750.4-keV光子相对强度，不是总支路12.8%） 分支比得出 42(3) W.u.；Mach 1990 的 50(7) ps 对应的是旧的 65(10) W.u. 评价。已在 note 中纠正此引用因果。
  - **纠错 2（微观八极驱动轨道三角关系破坏）**：G17 称“八极激发以 $\pi 1p_{1/2}^{-1} 0g_{9/2} \otimes \nu 2d_{5/2}^{-1} 1h_{11/2}$ 为主”。对秩为 3 的球谐算符 $Y_3$，$\pi 1p_{1/2} \leftrightarrow 0g_{9/2}$ 跃迁角动量变化 $\Delta j = |1/2 - 9/2| = 4 > 3$，严格违反三角不等式 $|j_1 - j_2| \le 3 \le j_1 + j_2$，其约化矩阵元与角向因子在数学上严格为 0（参见 [[octupole-orbital-eligibility-and-collectivity-boundary-20261107]]）。真正满足 $\Delta l = \Delta j = 3$ 且角向非零的质子驱动对是 $\pi 1p_{3/2} \leftrightarrow 0g_{9/2}$。已在 note 中予以根本订正。
  - **纠错 3（无源 1–50 ps 测量范围清除）**：G17 在“最有信息量下一测量”中指定目标态真实寿命在“皮秒区间（1~50 ps）”，缺乏文献或模型依据。已将其修正为技术视界表述（针对 Thomas 2016 薄靶 DSAM 亚皮秒上限未测出寿命的情况，通过拓展时间窗口的厚靶低能反冲 DSAM 或 RDM/Plunger 进行测量）。
  - **纠错 4（偏振测量局限性明确）**：G17 称通过康普顿偏振“以实验方式直接验证其纯 E3 多极性”。线偏振度（$\Delta_{i\text{PDCO}}$ 或 $P$）仅能辅助判别电/磁特征（宇称改变），不能单独确证为纯 E3。已在 note 中明确说明需结合自旋序列、混合比界限及单粒子跃迁速率上限综合判定。
  - **纠错 5（相对观测并非毫无区分力）**：G17 原 note 断言缺乏绝对寿命时一切观测均无法提供物理区分。父任务新研究 [[mo98-ru100-same-parent-e1-e3-constraints-20261107]] 证明，同母态 $B(E1)/B(E3)$ 比值消去了共同的 $B(E2)$ 分母与能级寿命，构建了无分母直接比值 $S_i$。$^{98}\text{Mo}$ 的 $S_7/S_5 \approx 0.31$ 与 $^{100}\text{Ru}$ 的 $S_7/S_5 \approx 1.56$ 存在明确差异，证明相对测量依然具有区分核结构模型演化的物理辨识力。已将此重要结论与链接回填入 note。
  - **纠错 6（竞争态严格隔离）**：在 Ledger 表中将 Band 3 的 3767.5 keV $9^-_2$ 态与八极候选带 Band 2 的 3655.7 keV $9^-_1$ 态做物理带归属隔离，杜绝跨带混淆。

---

## 修正文件与变更清单

1. `knowledge/sources/continuation-g17-chen-singh-2020-nds-98mo.md`
   - CS20-F1 删除无依据的“库仑激发数据集为 37(6) W.u.”及非物理 locator `coulex.pdf p.2`，澄清向下 $B(E3\downarrow)$ 与向上 $B(E3\uparrow)$ 定义关系；
   - CS20-F6 locator pp.3-5 扩展为 pp.3-7（3557 keV 态位于第 7 页）；
   - 修正“Competing Interpretations and Scientific Impact”中绝对否定性语调，回链 [[mo98-ru100-same-parent-e1-e3-constraints-20261107]]。
2. `knowledge/sources/continuation-g17-thomas-2016-96-98mo-coexistence.md`
   - 修正“Competing Interpretations and Scientific Impact”，说明 Thomas 2016 未提取负宇称寿命与薄靶 DSAM 阻止时间窗口的关系，不将本实验未报夸大为历史从未；回链同母态 E1/E3 结构约束。
3. `knowledge/research-notes/continuation-g17-mo98-absolute-constraints-20261107.md`
   - frontmatter 单行数组完善，补全 `mo98-ru100-same-parent-e1-e3-constraints-20261107` 与 `octupole-orbital-eligibility-and-collectivity-boundary-20261107`；
   - 态身份 Ledger 表：移除未标明理论来源的 ICC 数值；保留原件实测光子比与多极性；明确同母态分母消除相对约束；明确 Band 2 $9^-_1$ 与 Band 3 $9^-_2$ 的带结构隔离；
   - 纠正 $^{96}\text{Zr}$ 寿命引用因果（Iskra 2019 采用 Horen 1993 67.8(43) ps 而非 Mach 1990 50(7) ps）；
   - 纠正微观八极驱动轨道，指出 $\pi 1p_{1/2} \leftrightarrow 0g_{9/2}$ 因 $\Delta j = 4$ 矩阵元严格为 0，真正驱动轨为 $\pi 1p_{3/2} \leftrightarrow 0g_{9/2}$；
   - 剔除“1~50 ps”无依据寿命范围；
   - 纠正“偏振直接确证纯 E3”的不严谨表述，明确偏振仅辅助判别 E/M（宇称改变）；
   - 收窄“全部文献穷尽”、“形状必然导致 B(E2) 减小”等绝对化词句；补充说明仅测量 $\tau$ 依然不够，必须配合完整分支比与内转换系数。

---

## 边界与未核范围声明

- 本次纠错严格限定在 G17 提交的 3 个文件（1 note + 2 sources），未改动任何 raw、shared source、index、project、handoff、PLAN 或日常调度文件；
- 未运行全库 lint，未执行 git commit/push；
- 98Mo 领域是否存在冷门轻离子反应在非知名刊物上测得过负宇称态皮秒级寿命，未在本次已查评价与核心期刊之外进行无边界文献穷尽搜索。


父代理最终范围：上述审计中的方法/模型局限仅适用于本批材料；原文未报告不等于全球无模型或测量。
具体保留/撤回内容以当前canonical知识页为准；未报绝对量/空白不自动给寿命上下界。
