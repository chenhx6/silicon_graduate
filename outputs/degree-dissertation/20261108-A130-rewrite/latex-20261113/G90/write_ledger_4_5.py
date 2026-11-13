import json, hashlib

tex_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-5.tex'
with open(tex_path, 'rb') as f:
    tex_sha = hashlib.sha256(f.read()).hexdigest()

ledger = {
  "section_id": "4.5",
  "title": "Br/As 与其它核区的反射---手征问题",
  "section_label": "sec:4-5",
  "type": "comparative_cross_region_study",
  "status": "audited_and_reconciled",
  "recorded_at": "2026-11-13T20:10:00Z",
  "output_tex": "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-5.tex",
  "output_tex_sha256": tex_sha,
  "staging_tex": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/sec-4-5.tex",
  "scope_boundary": "本节为博士论文第4章比较小节，系统建立 A ≈ 80 过渡核区 (78Br, 74As) 的反射-手征谱学证据、网络拓扑与测量反演链分析；深入核对刘晨 2016 博士论文与 PRL 2016、肖骁 2019 硕士论文与 PRC 2022 原件，严格区分 74As 2019 学位报告 (Band 4 作为候选赝自旋带) 与 2022 期刊聚焦 (Bands 1-3) 的版本差异；严格辨析实验室守恒宇称 P、时间反演 T 与手征复合操作 C=T R_y(pi) 的代数与表象，解剖 D0 提取对理论 Q0 输入的依赖，阐明 Myers-Swiatecki 质心反冲有效电荷与 Delta l = Delta j = 3 微观八极驱动机制，破除静态四重手征-八极简并带 (CPQ) 的假象，确立多重手征伴随八极软性关联 (MchiD with octupole correlations) 的物理实质。",
  "source_inputs": [
    {
      "source_id": "liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br",
      "citation_key": "liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br",
      "canonical_source": "C. Liu et al., Phys. Rev. Lett. 116, 112501 (2016)",
      "raw_file": "raw/papers/gpt/learning-daily/20261101-day29-78br-octupole/78br-prl-2016.pdf",
      "raw_sha256": "460051AED9AF9D84BBFA09A51339E4D671F8ABAAF511FF6B7E0A4FBC2A836AD4",
      "actual_read_pages": [1, 2, 3, 4],
      "text_anchor": "PDF pp. 1-4: reaction 70Zn(12C, p3n)78Br at 60 and 65 MeV; AFRODITE + DIAMANT; Bands 1-2 (pi g9/2 (x) nu g9/2, 8+ -> 16+ and 9+ -> 14+); Bands 3-4 (pi f5/2(p3/2) (x) nu g9/2, 6- -> 15- and 7- -> 13-); 8 E1 transitions strictly connecting Band 1 and Band 3; B(E1)/B(E2) ~ 10^-6 fm^-2; delta E != 0; MDC-CDFT PC-PK1 PES soft in beta30; interpreted as MchiD with octupole correlations.",
      "claims_supported": [
        "78Br 中观测到两对正负宇称双带，建立在不同的微观单粒子组态之上 (pi g9/2 (x) nu g9/2 与 pi f5/2 (x) nu g9/2)",
        "8 条实测 E1 跃迁严格仅连接正宇称 Band 1 与负宇称 Band 3，Band 2 与 Band 4 之间未见任何 E1 连接",
        "实测 B(E1)/B(E2) 比值约为 10^-6 fm^-2，比稳定八极核 224Th 小一个量级，且能量位移 delta E(I) != 0",
        "MDC-CDFT 给出 beta30=0 软势能面极小，支持八极软性与振动关联，而非静态八极形变",
        "结构本质属于多重手征双重带伴随八极关联 (MchiD with octupole correlations)，而非单一构型静态四重带 (CPQ)"
      ]
    },
    {
      "source_id": "liu-chen-2016-78br-chirality-reflection-symmetry-thesis",
      "citation_key": "liu-chen-2016-78br-chirality-reflection-symmetry-thesis",
      "canonical_source": "刘晨, 山东大学博士学位论文 (2016)",
      "raw_file": "raw/theses/degree-dissertation/刘晨_奇奇核~(78)Br中手征...间反射对称性的联立自发破缺.pdf",
      "raw_sha256": "5e00370aab205b689841cb58d65c7fad8829e3de74f084736a74f2d8658ab291",
      "actual_read_pages": [64, 78, 79, 80, 81, 82, 90],
      "text_anchor": "PDF pp. 78-79, Eqs. (5.1)-(5.2), Fig. 5.16: B(E1)/B(E2) formula; delta E formula; comparison with 125Ba and 224Th; PDF p. 90 (print p. 79) Ch. 7 summary: confirms 78Br has stable triaxiality but NO stable octupole deformation, exhibiting MchiD and octupole correlations; CPQ requires stable triaxial + stable octupole on same configuration, which remains an open research question.",
      "claims_supported": [
        "刘晨博士论文与 PRL 2016 属于同一次 iThemba LABS 实验数据分析，非独立重复测量",
        "正负宇称带间提取的 B(E1)/B(E2) 与 delta E 偏离稳定八极基准 224Th，属于八极软振动",
        "作者总结明确区分当前 78Br 的 MchiD/八极关联与未来『稳定三轴与稳定八极同时存在』的真正手征-宇称四重带 (CPQ)"
      ]
    },
    {
      "source_id": "xiao-2022-chirality-octupole-correlations-74as",
      "citation_key": "xiao-2022-chirality-octupole-correlations-74as",
      "canonical_source": "X. Xiao et al., Phys. Rev. C 106, 064302 (2022)",
      "raw_file": "raw/papers/2022_Xiao et al_Chirality and octupole correlations in As 74.pdf",
      "raw_sha256": "0B14112F23529B71930F546A8A9929313E940A9C7FED27FF25A0D1D4687E5C74",
      "actual_read_pages": [1, 2, 3, 5, 6, 7],
      "text_anchor": "PDF pp. 1-7: reaction 74Ge(4He, 1p3n)74As at 58.6 and 62.6 MeV at iThemba LABS; Table I: Band 1 (6+ -> 15+), Band 2 (7+ -> 14+), Band 3 (7- -> 14-); 3 E1 transitions linking Band 3 to Band 1: 372.4 keV (7- -> 6+), 919.4 keV (8- -> 7+), 1293.4 keV (9- -> 8+); B(E1)/B(E2) and delta E comparable to 78Br and 125Ba, distinct from 224Th; focused on Bands 1-3.",
      "claims_supported": [
        "74As 2022 期刊实验报道集中于正宇称手征双重带 Bands 1-2 与负宇称 Band 3",
        "观测到 3 条 E1 跃迁连接 Band 3 与 Band 1 (372.4, 919.4, 1293.4 keV)",
        "B(E1)/B(E2) 与 delta E 特征与 78Br 相似，偏离 224Th，指示八极软性关联而非静态八极形变",
        "无绝对能级寿命测量"
      ]
    },
    {
      "source_id": "xiao-xiao-2019-high-spin-74as-thesis",
      "citation_key": "xiao-xiao-2019-high-spin-74as-thesis",
      "canonical_source": "肖骁, 山东大学硕士学位论文 (2019)",
      "raw_file": "raw/theses/degree-dissertation/肖骁_奇奇核~(74)As的高自旋态研究.pdf",
      "raw_sha256": "bf0763004d98be5a540ab7802eb0baed7c11387224f1818426b891f5a3ef362b",
      "actual_read_pages": [32, 33, 35, 45, 46, 47],
      "text_anchor": "PDF pp. 32-35, Fig. 3.8: level scheme containing Band 1 (6+ -> 15+), Band 2 (7+ -> 14+), Band 3 (7- -> 14-), Band 4 (7- -> 13-); PDF pp. 45-47, Section 4.2: evaluated chiral criteria for Bands 3-4, found staggering S(I) and moments of inertia differed, concluded Bands 3-4 are NOT chiral doublets, proposed candidate pseudospin partner bands.",
      "claims_supported": [
        "74As 2019 硕士学位论文实测并报告了 Band 4 (7- -> 13-)，否定了『Band 4 从未被观测』的盲目断言",
        "作者明确检验手征判据并排除了 Bands 3-4 作为手征双重带的属性，提出其更可能为赝自旋伙伴带",
        "2019 学位论文与 2022 期刊论文代表了不同阶段的研究侧重，属于同一 iThemba 实验谱系"
      ]
    },
    {
      "source_id": "butler-1996-octupole-shapes",
      "citation_key": "butler-1996-octupole-shapes",
      "canonical_source": "P. A. Butler and W. Nazarewicz, Rev. Mod. Phys. 68, 349 (1996)",
      "raw_file": "knowledge/sources/butler-1996-octupole-shapes.md",
      "raw_sha256": "local-reference",
      "actual_read_pages": [350, 360, 375],
      "text_anchor": "Comprehensive review of intrinsic reflection asymmetry in atomic nuclei; Myers-Swiatecki droplet model for D0; microscopic Delta l = Delta j = 3 coupling; parity doublets and tunneling; CG rotational extraction formulas.",
      "claims_supported": [
        "宏观电偶极矩 Myers-Swiatecki 液滴模型 D0 = C_D A Z e beta2 beta3 与有效电荷 e N/A, -e Z/A",
        "微观 Delta l = Delta j = 3 轨道耦合驱动八极形变与软度",
        "轴对称强耦合下基于 Clebsch-Gordan 系数从 B(E1)/B(E2) 提取 D0 的代数公式与模型依赖边界"
      ]
    },
    {
      "source_id": "wang-2019-rat-prm-78br-octupole-correlations",
      "citation_key": "wang-2019-rat-prm-78br-octupole-correlations",
      "canonical_source": "K. Y. Wang, Q. B. Chen, and J. Meng, Phys. Rev. C 100, 064319 (2019)",
      "raw_file": "raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/wang-2019-rat-prm-78br-arxiv1902.00191v1.pdf",
      "raw_sha256": "local-reference",
      "actual_read_pages": [1, 2, 4, 7],
      "text_anchor": "RAT-PRM calculation for 78Br; octupole correlations and non-planar geometry.",
      "claims_supported": [
        "反射不对称三轴粒子--转子模型 (RAT-PRM) 描述 78Br 能带与电磁性质",
        "理论非平面转动几何与有效角模拟属于截断模型空间计算"
      ]
    }
  ],
  "notations_and_conventions": {
    "parity_operator": "空间反演算符 P 属于幺正算符，[H, P] = 0 在实验室系严格守恒，物理态有确定宇称 pi = +/- 1；内禀 beta3 != 0 导致内禀反射不对称，经宇称投影给出宇称双重态，隧穿间隙为 Delta E_parity(I)",
    "chiral_operator": "手征操作 C = T R_y(pi) 属于反幺正算符；三维非平面角动量破坏 C，经量子隧穿产生同宇称手征双重带，隧穿间隙为 Delta E_chiral(I)",
    "cpq_definition": "手征--宇称四重带 (CPQ) 严格要求同一微观组态同时在空间反演和手征变换下自发破缺，产生 4 个内禀简并态，经隧穿产生 4 条对称交织的近简并带；78Br 与 74As 均不满足此条件",
    "tensor_distinction": "四极三次标量不变量 q3 propto beta2^3 cos(3 gamma) 为宇称偶算符，描述三轴偏度，绝非八极算符 beta3 或 M(E3) (宇称奇算符)",
    "d0_extraction": "|D_0| = sqrt(5/12 [B(E1)/B(E2)] [<I K 2 0|I-2 K>^2 / <I K 1 0|I-1 K>^2] Q_0^2)；B(E1)/B(E2) 是相对比值，非绝对 B(E1)；D0 高度依赖外加采用的 Q0 模型参数与轴对称无 K 混合假定",
    "effective_charges": "质心反冲剔除后 E1 有效电荷为质子 e N/A，中子 -e Z/A",
    "octupole_selection_rule": "Delta l = Delta j = 3 驱动八极关联 (A ≈ 80 区为 g9/2 <-> p3/2, f5/2)"
  },
  "claims_and_derivations": [
    {
      "id": "CLAIM-4-5-1",
      "topic": "78Br 与 74As 实验第一手测量载荷与数据源依赖性",
      "tex_symbol_or_expr": "^{78}\\mathrm{Br}: \\text{Bands 1--2 } (\\pi g_{9/2} \\otimes \\nu g_{9/2}), \\text{Bands 3--4 } (\\pi f_{5/2} \\otimes \\nu g_{9/2}), 8\\ E1; ^{74}\\mathrm{As}: \\text{Bands 1--2 } (\\pi g_{9/2} \\otimes \\nu g_{9/2}), \\text{Band 3 } (\\pi(f_{5/2}/p_{3/2}) \\otimes \\nu g_{9/2}), 3\\ E1",
      "source_id": "liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br",
      "derivation_steps": [
        "严格核查 78Br (Liu 2016 PRL / 博士论文) 与 74As (Xiao 2019 硕士 / 2022 PRC) 原件数据",
        "明确学位论文与期刊论文共享相同的符合事件矩阵与实验刻度，属于同一实验谱系，不构成独立测量票",
        "澄清 74As 2019 硕士论文建立了包含 Band 4 的纲图并排除了手征属性 (倾向赝自旋)，2022 期刊聚焦于 Bands 1-3，纠正『未观测到第4带』的笼统断言",
        "明确两核均无直接绝对能级寿命测量"
      ]
    },
    {
      "id": "CLAIM-4-5-2",
      "topic": "实际跃迁网络拓扑解耦与非四重简并带判定",
      "tex_symbol_or_expr": "M\\chi D + \\text{Octupole Correlations} \\neq \\text{Static CPQ}",
      "source_id": "liu-chen-2016-78br-chirality-reflection-symmetry-thesis",
      "derivation_steps": [
        "梳理 78Br 实际网络拓扑：正负宇称双带涉及不同的未配对质子轨道 (pi g9/2 vs pi f5/2)",
        "证明实测的 8 条 E1 跃迁严格单侧局限于 Band 1 与 Band 3 之间，伴带 Band 2 与 Band 4 之间完全缺失 E1 连接",
        "证明 74As 在 2022 期刊呈现 2+1 结构，2019 学位论文中 Band 4 亦为单侧连接，不存在闭合四带对称 E1 网络",
        "严格确立 78Br 属于多重手征双重带伴随八极软性关联 (MchiD)，排除了单一构型静态四重带假说"
      ]
    },
    {
      "id": "CLAIM-4-5-3",
      "topic": "离散对称性算符理论与有限体系量子混合边界",
      "tex_symbol_or_expr": "[\\hat{H}, \\hat{\\mathcal{P}}] = 0; \\mathcal{C} = \\hat{\\mathcal{T}}\\hat{\\mathcal{R}}_y(\\pi); \\Delta E_{\\text{parity}} \\neq 0; \\Delta E_{\\text{chiral}} \\neq 0",
      "source_id": "butler-1996-octupole-shapes",
      "derivation_steps": [
        "阐明实验室好宇称态与内禀反射不对称的本质区别，说明内禀平均场破缺必须经角动量与宇称投影还原为好宇称态",
        "阐明反幺正手征算符 C 与幺正空间反演算符 P 的代数差异，指出同宇称手征双带与异宇称宇称双带源于不同自由度的量子隧穿",
        "证明四态近简并只是必要条件，有限多体系统的波函数混合不能作为同时静态自发破缺的确证",
        "严格证明标量不变量 q3 propto beta2^3 cos(3 gamma) (宇称偶) 属于四极张量，绝非奇多极八极算符 beta3 或 M(E3) (宇称奇)"
      ]
    },
    {
      "id": "CLAIM-4-5-4",
      "topic": "电偶极辐射微观驱动与宏观质心反冲机制",
      "tex_symbol_or_expr": "D_0^{\\text{macro}} = C_D A Z e \\beta_2 \\beta_3; e_{\\text{eff}}^{\\text{p}} = e N/A, e_{\\text{eff}}^{\\text{n}} = -e Z/A; \\Delta l = \\Delta j = 3",
      "source_id": "butler-1996-octupole-shapes",
      "derivation_steps": [
        "推导 Myers-Swiatecki 宏观液滴电荷中心与质量质心微观位移产生的电偶极矩公式",
        "给出剔除质心伪运动后的有效电荷质子 e N/A 与中子 -e Z/A",
        "阐明微观八极相互作用源于费米面附近的 Delta l = Delta j = 3 轨道对偶，指出 A ≈ 80 区 Z=33, 35 贴近八极驱动幻数 Z=34 (g9/2 <-> p3/2, f5/2 耦合)",
        "剖析 MDC-CDFT 沿 beta30 的软势阱与替代的赝自旋双重态机制"
      ]
    },
    {
      "id": "CLAIM-4-5-5",
      "topic": "内禀电偶极矩 D0 的测量反演链条与模型依赖性剖析",
      "tex_symbol_or_expr": "|D_0| = \\sqrt{\\frac{5}{12}\\,\\frac{B(E1)}{B(E2)}\\,\\frac{\\langle I K 2 0 | I-2 K \\rangle^2}{\\langle I K 1 0 | I-1 K \\rangle^2}\\,Q_0^2}; \\delta E(I) \\neq 0",
      "source_id": "liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br",
      "derivation_steps": [
        "给出由实验分支比提取 B(E1)/B(E2) 的精确公式，强调其为相对比值而非绝对 B(E1)",
        "给出轴对称强耦合 Clebsch-Gordan 几何投影公式提取 D0 的代数链条",
        "深入剖析提取 D0 对理论输入 Q0 的绝对依赖性，以及忽略三轴 K 混合的局限性",
        "对比稳定八极核 224Th (B(E1)/B(E2) ~ 10^-5 fm^-2, delta E -> 0) 与 78Br/74As (比值小一个数量级，delta E 剧烈偏离零)，论证其八极软性与振动关联本质"
      ]
    },
    {
      "id": "CLAIM-4-5-6",
      "topic": "跨核区物理迁移条件与可证伪前沿实验候选方案",
      "tex_symbol_or_expr": "\\text{Dual Driving Shells} + \\text{Potential Rigidity} + \\text{Strong Core Spin} (R \\gg 1)",
      "source_id": "butler-1996-octupole-shapes",
      "derivation_steps": [
        "提出手征与八极共存跨区迁移的物理条件：双重单粒子驱动轨道 (Delta l = Delta j = 3 且含高 j 粒子/空穴)、三轴与八极势能面刚度深度、强集体转动离心势",
        "提出利用反冲距离多普勒频移法 (RDM) 直接测量 78Br 与 74As 负宇称能级绝对寿命以脱离 Q0 依赖提取绝对 B(E1) 的实验方案",
        "提出在大立体角跟踪锗阵列上高灵敏搜寻 Band 2 与 Band 4 闭合交叉跃迁以排他性检验静态 CPQ 假说的方案",
        "提出利用放射性束流库仑激发直接测量内禀八极矩阵元 <M(E3)> 的直接物理测量方案"
      ]
    }
  ],
  "competing_explanations_and_boundaries": [
    {
      "case": "静态手征---宇称四重带 (CPQ) vs 多重手征伴随八极软性关联 (MchiD with Octupole Correlations)",
      "primary_claim": "部分文献早期探讨 78Br 可能属于手征与空间反射对称性同时自发破缺诱发的四重简并带",
      "counter_evidence": "正负宇称能带基于不同的单粒子组态 (pi g9/2 vs pi f5/2)；实测 8 条 E1 跃迁严格单侧局限于 Band 1 与 Band 3 之间，伴带间完全无 E1 连接；MDC-CDFT 计算给出 beta30=0 软势阱而非深双阱；B(E1)/B(E2) 与 delta E 严重偏离稳定八极基准 224Th",
      "competing_models": "多重手征双重带 (MchiD) 伴随八极振动与软性关联 (Liu et al. PRL 2016, 刘晨 2016 博士论文结论)",
      "status": "确立多重手征与八极软性关联模型，静态 CPQ 假说被实测组态与网络拓扑排他性否定"
    },
    {
      "case": "74As 负宇称伴带的手征双重带解释 vs 赝自旋伙伴带 / 能带混合",
      "primary_claim": "是否在 74As 中构成了两对正负宇称手征双重带",
      "counter_evidence": "肖骁 2019 硕士论文详细检验了负宇称 Bands 3-4 的手征判据，证实 S(I) 与惯量演化差异明显，排除了手征属性并归为赝自旋伙伴带；2022 期刊论文聚焦于 Bands 1-3，跨宇称 E1 仅有 3 条且单侧连接",
      "competing_models": "正宇称手征双重带 (Bands 1-2) + 负宇称赝自旋伙伴带 / 振动耦合带 (Xiao 2019 学位论文)",
      "status": "保留各版本原件报告，排除闭合四带手征网络解释"
    }
  ],
  "reader_checks": [
    {"check": "78Br 与 74As 实验原件数据核对", "result": "严格核对自旋范围、组态指派与跃迁网络；纠正旧稿中反应束流/靶核笔误与 74As CIAE 误传 (实际均为 iThemba LABS AFRODITE 实验)"},
    {"check": "74As 2019 学位与 2022 期刊版本差异核查", "result": "客观区分 2019 硕士论文报告 Band 4 (倾向赝自旋) 与 2022 期刊聚焦 Bands 1-3，彻底消除『Band 4 从未观测』的盲目断言"},
    {"check": "网络拓扑与 E1 连接检查", "result": "严格遵循实测跃迁绘制网络，78Br 仅 8 条 E1 (Band 1 <-> 3)，74As 仅 3 条 E1 (Band 3 -> 1: 372.4, 919.4, 1293.4 keV)，绝不按理论脑补未测边"},
    {"check": "对称性与算符代数区分检查", "result": "严格阐明守恒好宇称 P、时间反演 T 与反幺正手征操作 C 的物理区别；严格证明 q3 为四极三次标量不变量 (宇称偶)，绝非八极算符 beta3 或 M(E3) (宇称奇)"},
    {"check": "D0 反演链条与模型依赖性检查", "result": "明确 B(E1)/B(E2) 为相对比值非绝对 B(E1)，推导 CG 展开式指出对 Q0 输入与轴对称假定的绝对依赖，对比 224Th 明确八极软性特征"},
    {"check": "微观机制与可证伪实验检查", "result": "区分宏观质心反冲有效电荷与微观 Delta l = Delta j = 3 驱动力；提出 RDM 绝对寿命测量与大阵列闭合网络搜寻等可证伪前沿方案"}
  ],
  "prohibitions_strictly_obeyed": [
    "绝对禁止口号化用语（全篇剔除『彻底』、『金标准』、『铁证』、『毋庸置疑』等夸大词汇）",
    "严格区分独立实验与同源数据（明确 78Br 学位/期刊共享同次实验，74As 学位/期刊共享同次实验）",
    "禁止在能级图与网络图中绘制未测跨宇称连接线",
    "禁止将相对分支比 B(E1)/B(E2) 冒充绝对 B(E1) 跃迁几率",
    "禁止将四态近简并直接等同于证实静态手征--八极同时破缺"
  ],
  "open_issues": [
    "78Br 与 74As 关键负宇称能级目前完全缺乏直接绝对寿命测量 (DSAM/RDM)，无模型依赖的绝对 B(E1) 跃迁几率依然空缺",
    "Band 2 与 Band 4 之间是否存在极微弱的跨宇称连接，有待新一代极高探测效率跟踪锗阵列给出更严苛的实验上限"
  ]
}

ledger_json_str = json.dumps(ledger, indent=2, ensure_ascii=False)

staging_ledger = 'outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/section-4-5.json'
with open(staging_ledger, 'w', encoding='utf-8') as f:
    f.write(ledger_json_str)

canonical_ledger = 'raw/writing/gpt/A130/latex-evidence-ledger/section-4-5.json'
with open(canonical_ledger, 'w', encoding='utf-8') as f:
    f.write(ledger_json_str)

print('Ledger section-4-5.json written successfully to staging and canonical!')
