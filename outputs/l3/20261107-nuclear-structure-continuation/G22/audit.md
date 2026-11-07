# G19产出窄事实校验与纠错审计报告 (Worker G22)

- **审计对象**：
  - `knowledge/sources/continuation-g19-dunlop-2016-cd-halflives.md`
  - `knowledge/sources/continuation-g19-saito-2020-129cd-spectroscopy.md`
  - `knowledge/sources/continuation-g19-taprogge-2014-129cd-isomer.md`
  - `knowledge/research-notes/continuation-g19-cd-in-common-weak-operator-20261107.md`
  - `outputs/l3/20261107-nuclear-structure-continuation/G19/table_129cd_feeding_comparison.csv`
  - `outputs/l3/20261107-nuclear-structure-continuation/G19/table_130in_isomers_energetics.csv`
- **核验原件**：
  1. `Saito_2020_PRC_102_024337_129Cd_decay.pdf` (arXiv:2008.02959v1)
  2. `Dunlop_2016_PRC_93_062801_128-130Cd_halflives.pdf` (arXiv:1711.05621v1)
  3. `Taprogge_2014_PLB_738_223_129Cd_isomer.pdf` (Elsevier OA)
  4. `Taprogge_2015_PRC_91_054324_AAM.pdf` (PRC 91, 054324)
  5. `Nesterenko_2020_PLB_808_135642_128In_130In_isomers.pdf` (arXiv:2005.09398v1)

---

## 逐项原文核验清单（8项）

### 1. NA-14与jj45pna相互作用及作者是否当同一个
- **核验结论**：不支持（原作者从未当成同一个相互作用）。
- **确切PDF页/表**：
  - `Saito 2020` 第 10 页左栏；`Taprogge 2015` 第 9 页右栏；`Taprogge 2014` 第 225 页右栏；
  - `Nesterenko 2020` 第 3 页左栏、第 5 页及参考文献 [45],[47]。
- **原文短句实际内容**：
  - `NA-14`：基于 CD-Bonn 势经 $V_{\text{low}-k}$ 截断重整化，并在双闭芯 $^{132}\text{Sn}$ 的空穴空间由 Coraggio 等针对 $46 \le Z \le 50, N \le 82$ 进行经验多极修正，在 `OXBASH` 运行。
  - `jj45pna`：基于 CD-Bonn 势经微扰 $G$ 矩阵方法重整化（Machleidt 2001 PRC 63, 024001），由 B. A. Brown 整合入 `NuShellX@MSU`，未包含局部经验多极修正。
  - 判定：两者重整化理论、有效矩阵元与计算程序均不同，原作者未当同一个。
- **纠错动作**：已在相关 source 与 research note 中彻底解耦，明确指明两者属于不同模型相互作用。

### 2. Dunlop $q=0.66 \to 0.75$ 的针对模型
- **核验结论**：不支持（针对大尺度壳模型，不能套用于 DF3/RHB）。
- **确切PDF页/表**：
  - `Dunlop 2016` 第 1-2 页、第 4 页右栏及参考文献 [9,10,12]。
- **原文短句实际内容**：
  - “Increasing the GT quenching factor from $q = 0.66$ to $q = 0.75$ in order to reproduce the shorter half-life of 130Cd... resolves this discrepancy”明确源自大尺度壳模型（LSSM, Zhi 2013 PRC 87, 025803; Cuenca-Garcia 2007; Lorusso 2015 PRL 114, 192501）针对 $N=82$ 等待点核的经验标度拟合。
  - DF3+CQRPA（Borzov 2008）与 RHB+RQRPA（Marketin 2016）为全局泛函/QRPA 模型，在 Fig. 7 中作为系统对比并略微高估绝对半衰期，但未在本文中被调参至 $q=0.75$。
- **纠错动作**：已更正 `continuation-g19-dunlop-2016-cd-halflives.md` 与 research note，删去“DF3/RHB 将淬灭因子调高至 0.75”的混淆表述。

### 3. Saito Table II 半衰期 147(3) 与 157(8) 来源及独立性
- **核验结论**：支持（来源指认明确，数据采集关系明确）。
- **确切PDF页/表**：
  - `Saito 2020` 第 2 页右栏、第 6 页右栏（Section IV B）及参考文献 [14, 15]。
- **原文短句实际内容**：
  - Saito 2020 明确指出：“using the same data set as used in this work, Dunlop et al. [15] confirmed the EURICA results with half-lives of 147(3) ms for the 11/2- state and 157(8) ms for the 3/2+ state.”
  - 判定：Saito 2020 与 Dunlop 2016 共享 TRIUMF-ISAC GRIFFIN 同一实验数据集，非独立采集；而两者与 Taprogge 2015（RIKEN RIBF EURICA）为完全独立的实验装置与数据采集。
- **纠错动作**：在 source 中补充明确说明 Saito 2020 直接采纳 Dunlop 2016 的同数据集分析值，不可当作重复测量。

### 4. 129Cd $E_x = 343(8)\,\text{keV}$ 与 $Q_\beta = 9780(17)\,\text{keV}$ 的质量版一致性及 $Q$ 误差
- **核验结论**：不支持（非相同质量版本，绝不能不查协方差直接合成 $Q$ 误差）。
- **确切PDF页/表**：
  - `Saito 2020` 第 2 页左栏 Ref. [12]（Manea et al. PRL 124, 092502 (2020)）；第 6 页右栏 Ref. [32]（AME2016, CPC 41, 030002 (2017)）。
- **原文短句实际内容**：
  - $Q_\beta = 9780(17)\,\text{keV}$ 采纳自 AME2016，而 $E_x(3/2^+) = 343(8)\,\text{keV}$ 采纳自 2020 年发表的 CERN-ISOLTRAP 质谱实验（Manea 2020），两者属于跨越 3 年的不同质量评估版本。
  - 判定：原文献未提供两者间的实验协方差；G19 擅自按方和根计算 $Q_\beta(3/2^+) = 10123(19)\,\text{keV}$（$\sqrt{17^2+8^2} \approx 19$）违背误差传播基本原则。
- **纠错动作**：已在 source 与 research note 中撤回合成误差 $10123(19)\,\text{keV}$，设立协方差缺失的明确不完备边界。

### 5. "Pn 10–15%" 与 "valence GT 2–5 损失 95%" 是否原文给出
- **核验结论**：不支持（原文均未给出）。
- **确切PDF页/表**：
  - `Saito 2020` 全文；`Taprogge 2015` 第 6 页右栏；`Taprogge 2014` 全文。
- **原文短句实际内容**：
  - Saito 2020 与 Taprogge 2015 原文均未报告或测定 $^{129}\text{Cd}$ 的 $P_n$ 实验值。Taprogge 2015 仅给出未观测到的跃迁强度上限（$9/2^+$ 路径 $11(3)\%$、$1/2^-$ 路径 $6(3)\%$，包含基态直馈、高能微弱 $\gamma$ 及延迟中子）。“$P_n \approx 10-15\%$”系 G19 擅自主观推断。
  - 原文在价空间内仅计算 $\nu 0g_{7/2} \to \pi 0g_{9/2}$ 跃迁，未计算更未提及 Ikeda 求和规则 $3(N-Z)=99$，“valence GT 2-5 损失 95%”系 G19 臆测。
- **纠错动作**：已在 research note 中彻底删除“$P_n \approx 10-15\%$”与“损失 95%”无源断言，修正为客观记录未报告边界。

### 6. TAGS 能否称“完全无偏/根本消除全部 Pandemonium”
- **核验结论**：不支持（属于夸大实验技术的非物理断言）。
- **确切实验原理与文献依据**：
  - 全吸收谱学（TAGS）依赖基于能级密度与强度函数模型的谱反解（Response matrix unfolding），引入模型依赖；且面临延迟中子反应本底及子体衰变干扰。
  - $^{129}\text{Cd}$ 拥有两近等寿命（$147\,\text{ms}$ vs $157\,\text{ms}$）母态，若缺乏前级质量/异能态纯化分离，TAGS 无法单独解开重叠的衰变强度。
- **纠错动作**：已撤回“从根本上定量消除全部 Pandemonium”措辞，修改为客观陈述其在统计能区减小漏计但受反解与异能态混合限制的物理边界。

### 7. FF 算符是否真正采用共同处理，还是仅从 $\log ft$ 推断
- **核验结论**：不支持“共同算符处理”（原文仅从经验 $\log ft$ 与选择定则推断）。
- **确切PDF页/表**：
  - `Saito 2020` 第 6 页、第 10 页左栏及 Fig. 8；`Taprogge 2015` 第 9 页右栏。
- **原文短句实际内容**：
  - 壳模型 NA-14 在 OXBASH 中仅计算了 $\nu 0g_{7/2} \to \pi 0g_{9/2}$ 的允许 GT 跃迁；对一阶禁戒跃迁未进行任何微观张量算符或相对论形状因子动力学计算。
  - 原文全部禁戒跃迁归属均由标准 NNDC 允许程序 `logft` 算出的比较半衰期（$\log ft > 5.5$）结合宇称改变选择定则进行定性推断。
- **纠错动作**：将 research note 标题由“共同弱衰变算符合同”缩窄为“弱衰变分析的原件核验与模型不完备边界合同”，明确指出目前不存在包含微观一阶禁戒算符的共同闭合求解。

### 8. 40 行 CSV 是否错配不同母态 feeding 列/上限/缺失值
- **核验结论**：支持（G19 CSV 存在严重错配、臆造上限、列互换与漏行）。
- **确切PDF页/表**：
  - `Saito 2020` 第 10 页 Table II。
- **实测核对证据**：
  - **4 个强态核对**：
    1. `3150 keV ((13/2)-)`：原表 $I_\beta(11/2^-) = 45(10)\%$，$3/2^+$ 馈送列为空白。G19 擅自在 $3/2^+$ 列填充无源上限 `<1, <1`。
    2. `3184 keV ((5/2)+)`：原表 $I_\beta(3/2^+) = 22(6)\%$，$11/2^-$ 馈送列为空白。G19 擅自在 $11/2^-$ 列填充 `<2, <2`。
    3. `3347 keV ((5/2)+)`：原表 $I_\beta(3/2^+) = 13(3)\%$，$11/2^-$ 馈送列为空白。G19 擅自在 $11/2^-$ 列填充 `<2, <2`，且漏掉了同名次能级 `(3347) keV`（$I_\beta(11/2^-) = 0.4(2)\%$）。
    4. `995 keV (11/2+)`：原表 $I_\beta(11/2^-) = 9.4(38)\%$，$3/2^+$ 馈送列为空白。G19 擅自在 $3/2^+$ 列填充 `<0.7, <0.7`。
  - **上限行与错配核对**：
    1. `1354 keV (13/2+)`：原表实测上限为 $I_\beta(11/2^-) < 6.3\%$。G19 错写成确定值 `5.7(2)`，并将 $3/2^+$ 填为 `<2, <2`。
    2. `1761 keV`：原表实测上限为 $I_\beta(3/2^+) < 2.6\%$。G19 严重错配将 3150 keV 的主跃迁强度 `45(10)` 填入该能级当前 $3/2^+$ 馈送列。
    3. `1688 keV (17/2-)`：原表 $I_\beta(11/2^-) < 2.5\%$。G19 错写为 `<1`。
    4. `1693 keV`：原表 $I_\beta(11/2^-) < 1.7\%$，$3/2^+$ 为空白。G19 错写为 $11/2^-$ 为 `<1`，且将原本属于其它能级的数据 `1.4(6), 0.4(4)` 错填入 $3/2^+$ 列。
    5. `2015 keV` 与 `2058 keV`：原表 2015 归 $11/2^-$（$1.7(8)\%$），2058 归 $3/2^+$（$1.5(8)\%$）。G19 将两者馈送列完全颠倒互换。
- **纠错动作**：已使用 `pdftotext -layout` 准确定位 Table II 各列字符边界，完整重构生成包含全部 40 个能级（补齐 `(3347)` keV）的全新 `table_129cd_feeding_comparison.csv`，空白单元格真实保留为空，彻底剔除臆造上限与错配值。

---

## 修正文件与残留边界总结

### 实际修正的文件清单 (changed_files)
1. `outputs/l3/20261107-nuclear-structure-continuation/G19/table_129cd_feeding_comparison.csv`（完全重构，对齐 Saito 2020 Table II 全部 40 个能级）
2. `outputs/l3/20261107-nuclear-structure-continuation/G19/table_130in_isomers_energetics.csv`（澄清外来 AME 130Sn 质量输入与 jj45pna 偏离）
3. `knowledge/sources/continuation-g19-dunlop-2016-cd-halflives.md`（修正 $q=0.66 \to 0.75$ 模型范围至大尺度壳模型）
4. `knowledge/sources/continuation-g19-saito-2020-129cd-spectroscopy.md`（修正数据采集同源性、质量评估跨版本及弱算符边界）
5. `knowledge/sources/continuation-g19-taprogge-2014-129cd-isomer.md`（区分 NA-14 与 jj45pna）
6. `knowledge/research-notes/continuation-g19-cd-in-common-weak-operator-20261107.md`（缩窄为简洁原件合同与不完备边界，清除所有无源数字）
7. `outputs/l3/20261107-nuclear-structure-continuation/G22/audit.md`（本审计报告）
8. `outputs/l3/20261107-nuclear-structure-continuation/G22/receipt.json`（回执文件）

### 原始草稿备份路径
`tmp/runs/20261107-nuclear-continuation/G22/drafts/`

### 必须由父代理审阅的少数残留
1. **AME2020 协方差未开放**：AME2020 中 $^{129}\text{Cd}$ 基态与异能态的精确质量差与协方差矩阵未在正文中解析，建议后续若需计算精密异能态 $\beta$ 能窗，应直接查阅 AME2020 原始输入数据或使用最新 JYFLTRAP/ISOLTRAP 频率比。
2. **3150 keV 分支归一化定义区分**：Table II 中 $24.1(9)\%$ 为相对于全部 $^{129}\text{Cd}$ 衰变事件的宏观强度（全注入），而 $45(10)\%$ 为仅相对于 $11/2^-$ 母态自身衰变事件的归一化强度，引用时需严格声明分母基准，避免混用。由父代理统一收窄。
3. **算符局限性严格限本批论文**：关于未自洽计算微观一阶禁戒算符的结论仅严格限于本批所读文献（Saito 2020, Taprogge 2014/2015, Dunlop 2016），不外推为全理论界缺失。由父代理接管表述。
4. **有效力评价边界**：$^{130}\text{In}(10^-)$ 的单点能量偏离（$200\,\text{keV}$）属于局部多极力或组态截断效应，不构成对 jj45pna 整套有效相互作用的全局证伪。由父代理接管评述。


父代理最终范围：上述审计中的方法/模型局限仅适用于本批材料；原文未报告不等于全球无模型或测量。
具体保留/撤回内容以当前canonical知识页为准；未报绝对量/空白不自动给寿命上下界。
