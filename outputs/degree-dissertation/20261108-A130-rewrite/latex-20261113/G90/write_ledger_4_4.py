import json, hashlib

tex_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex'
with open(tex_path, 'rb') as f:
    tex_sha = hashlib.sha256(f.read()).hexdigest()

ledger = {
  "section_id": "4.4",
  "title": "$A\\approx 130$、稀土与重区的取向对照",
  "section_label": "sec:4-4",
  "type": "comparative_cross_region_study",
  "status": "audited_and_reconciled",
  "recorded_at": "2026-11-13T19:40:00Z",
  "output_tex": "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex",
  "output_tex_sha256": tex_sha,
  "staging_tex": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/sec-4-4.tex",
  "scope_boundary": "本节为博士论文第4章比较小节，系统建立跨越稀土超形变区 (163Lu)、中重核区 (135Pr) 与重核过渡区 (178W, 187Au, 190Hg) 的非轴对称取向动力学对照基准；严格推导电荷空间半轴与惯量主轴排序，落实第3章关于摆动能量非单调性、实根稳定性与倾斜边界的判据，核实 163Lu 原表与采用量依赖，剖析 135Pr 极化双根与 IBFM/QTR 竞争解释，澄清 Shimizu 轴对称高 K 进动的参考系与能标微商，明确跨区迁移的物理充要条件与失效反例。",
  "source_inputs": [
    {
      "source_id": "campaign-g07-gorgen-2004-163lu-quadrupole-moments",
      "citation_key": "campaign-g07-gorgen-2004-163lu-quadrupole-moments",
      "canonical_source": "A. Görgen et al., Phys. Rev. C 69, 031301(R) (2004)",
      "raw_file": "raw/papers/gpt/query/20261107-continuation-G23/gorgen-2004-163lu-quadrupole-moments-prc.pdf",
      "raw_sha256": "5dbf88f286183ac22cd762e4f22a69e778d64f59e78f4cbc7533c85589ed992e",
      "actual_read_pages": [1, 2, 3],
      "text_anchor": "PDF pp. 2-3, Table I (15 in-band transitions: TSD1 with Qt = 7.37-9.93 b, TSD2 with Qt = 6.66-8.88 b, overall range ~ 6.7-9.9 b); Table II (5 interband TSD2 -> TSD1 transitions with B(E2) = 0.54-0.70 e^2b^2, B(M1) = 0.017-0.024 mu_N^2, using adopted average delta = -3.10).",
      "claims_supported": [
        "163Lu TSD1 (nw=0) 与 TSD2 (nw=1) 在全部测量自旋区间呈现高度一致的跃迁四极矩 Qt ≈ 6.7–9.9 b (Table I)",
        "TSD2 向 TSD1 的带间 Delta I = 1 连接跃迁测得强烈的集体 E2 增强 B(E2)_out ≈ 0.54–0.70 e^2b^2 (Table II)",
        "基于标准单粒子估计 B_W(E2) ≈ 0.05940 A^(4/3) e^2fm^4 ≈ 0.00530 e^2b^2 (A=163, R0=1.2 fm) 严格换算，对应 B(E2)_out ≈ 100–132 W.u.",
        "Table II 中的 B(E2) 与 B(M1) 提取依赖于前人测量中采用的平均混合比 delta = -3.10(+0.36/-0.44) (测至 51/2+ 外推假定)",
        "理论文献中用于拟合 163Lu 摆动能量的核芯转动惯量参数属于微观模型输出，非直接实测量",
        "163Lu 发生在 R ~ 15–30 hbar 的强转动离心极限，满足简谐摆动势阱成立条件"
      ]
    },
    {
      "source_id": "odegard-2001-evidence-wobbling-163lu",
      "citation_key": "odegard-2001-evidence-wobbling-163lu",
      "canonical_source": "S. W. Ødegård et al., Phys. Rev. Lett. 86, 5866 (2001)",
      "raw_file": "knowledge/sources/odegard-2001-evidence-wobbling-163lu.md",
      "raw_sha256": "local-reference",
      "actual_read_pages": [1, 2, 3],
      "text_anchor": "First identification of wobbling excitation in 163Lu; angular distribution and linear polarization giving average delta ≈ -3.10.",
      "claims_supported": [
        "163Lu TSD2 首次作为一声子摆动带报道，测定带间连接跃迁混合比 delta ≈ -3.10"
      ]
    },
    {
      "source_id": "jensen-2002-second-phonon-wobbling-163lu",
      "citation_key": "jensen-2002-second-phonon-wobbling-163lu",
      "canonical_source": "K. A. Jensen et al., Nucl. Phys. A 703, 3 (2002)",
      "raw_file": "knowledge/sources/jensen-2002-second-phonon-wobbling-163lu.md",
      "raw_sha256": "local-reference",
      "actual_read_pages": [3, 4, 15],
      "text_anchor": "Detailed spectroscopy of 163Lu wobbling bands; confirmation of mixing ratio up to spin 51/2+.",
      "claims_supported": [
        "163Lu 摆动声子谱学测量，混合比 delta ≈ -3.10 测至 51/2+"
      ]
    },
    {
      "source_id": "matta-2015-transverse-wobbling-135pr",
      "citation_key": "matta-2015-transverse-wobbling-135pr",
      "canonical_source": "J. T. Matta et al., Phys. Rev. Lett. 114, 082501 (2015)",
      "raw_file": "raw/papers/2015_Matta et al_Transverse Wobbling in Pr 135.pdf",
      "raw_sha256": "8db644705dccfd58016753b759d19314a65284c48efc1758f95f1b3ce23551d6",
      "actual_read_pages": [1, 2, 3, 5],
      "text_anchor": "PDF pp. 1-3, 5: reported low-spin transverse wobbling in 135Pr on pi h11/2 (Band 3); extracted |delta| > 1 from angular distribution (e.g. delta = -2.0(4) for 747.0 keV); reported positive linear polarization and falling Ewob.",
      "claims_supported": [
        "Matta 等人报道 135Pr 基于 pi h11/2 的低自旋横向摆动带 (Band 3，自旋序列 13/2-, 17/2-, ...)",
        "基于角分布拟合选定大根 |delta| > 1 (如 747.0 keV 提取 delta = -2.0(4))，声称连接线由 E2 主导并伴随有效摆动能量下降"
      ]
    },
    {
      "source_id": "lv-2022-evidence-against-wobbling-135pr",
      "citation_key": "lv-2022-evidence-against-wobbling-135pr",
      "canonical_source": "B. F. Lv et al., Phys. Lett. B 824, 136840 (2022)",
      "raw_file": "raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf",
      "raw_sha256": "4b87c540bf9da5141fa88ef8f00859162cb08918d56a5da74726c7537df5e26b",
      "actual_read_pages": [1, 2, 3, 4, 5],
      "text_anchor": "PDF pp. 2-5, Table 1: 747.3 keV is 17/2- -> 15/2- with Rac = 0.98(7), small root delta = -0.47(+0.09/-0.22); 813.2 keV is 21/2- -> 19/2- with Rac = 1.01(8), small root delta = -0.46(+0.11/-0.19); from same 17/2- initial state, B(E2; 747.3)/B(E2; 526.2) = 0.7(+0.7/-0.5); core spin R ~ 1 hbar at bandhead.",
      "claims_supported": [
        "747.3 keV 跃迁能级身份严格为 17/2- -> 15/2- (连接 Band 3 与 Band 1)，小根拟合解为 delta = -0.47(+0.09/-0.22) (Table 1)",
        "813.2 keV 跃迁能级身份为 21/2- -> 19/2-，小根解为 delta = -0.46(+0.11/-0.19)",
        "同母态 17/2- 向两带退激的分支比 B(E2; 747.3 keV)/B(E2; 526.2 keV) = 0.7(+0.7/-0.5)，表明向签名伙伴带与基带具有相当的跃迁几率，否定了纯 1-phonon 摆动声子图像",
        "在小根解下 747.3 keV 跃迁由 M1 主导 (>80%)，带间 B(E2)_out 缺乏集体增强",
        "带头自旋 13/2- 处核芯集体转动动量仅 R ~ 1 hbar 破坏简谐强转动近似；QTR 计算表明该带源于单粒子对准向转动轴倾斜的平面转动或与 gamma 振动带混合"
      ]
    },
    {
      "source_id": "guo-2021-comment-transverse-wobbling-135pr",
      "citation_key": "guo-2021-comment-transverse-wobbling-135pr",
      "canonical_source": "S. Guo, C. M. Petrache, X. H. Zhou, and E. A. Lawrie, arXiv:2111.14150 (2021)",
      "raw_file": "knowledge/sources/guo-2021-comment-transverse-wobbling-135pr.md",
      "raw_sha256": "local-reference",
      "actual_read_pages": [1, 2],
      "text_anchor": "Demonstrated that angular distribution W(theta) has quadratic rational dependence on delta, giving two roots; positive linear polarization P(theta) > 0 does not uniquely exclude the small-magnitude root |delta| < 1.",
      "claims_supported": [
        "线偏振度正负符号不能作为排他性支持大根 |delta| > 1 的判据，小根在合适去取向张量下同样给出正偏振"
      ]
    },
    {
      "source_id": "nomura-2022-questioning-wobbling-ibfm",
      "citation_key": "nomura-2022-questioning-wobbling-ibfm",
      "canonical_source": "K. Nomura et al., Phys. Rev. C 106, 064313 (2022)",
      "raw_file": "knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md",
      "raw_sha256": "local-reference",
      "actual_read_pages": [3, 4, 6, 8, 10],
      "text_anchor": "PDF pp. 3-10: IBFM based on Gogny D1M EDF for 135Pr; reproduces Band 1 and Band 3 with M1-dominated interband transitions without wobbling phonons.",
      "claims_supported": [
        "微观泛函映射的 IBFM 计算自然重现 135Pr 能带结构与 M1 主导带间跃迁，无需假定横向摆动声子",
        "135Pr 核芯处于 gamma 软势能面，展现出复杂的玻色子-费米子耦合激发形态"
      ]
    },
    {
      "source_id": "lawrie-2020-tilted-precession",
      "citation_key": "lawrie-2020-tilted-precession",
      "canonical_source": "E. A. Lawrie et al., Phys. Rev. C 101, 034306 (2020)",
      "raw_file": "raw/papers/2020_Lawrie et al_Tilted precession and wobbling in triaxial nuclei.pdf",
      "raw_sha256": "777f935b0266fed8a9d9f2e1cc1f72995c84dd83e27ca1f5377ab2785b2ec405",
      "actual_read_pages": [1, 2, 3],
      "text_anchor": "PDF pp. 1-3, Eq. (1)-(4), Figs. 2-3: classical tilted precession (TiP) in triaxial nuclei as an alternative orientation mechanism.",
      "claims_supported": [
        "非主轴倾斜进动 (TiP) 提供了奇 A 三轴核在低自旋下的准经典取向动力学竞争模型"
      ]
    },
    {
      "source_id": "shimizu-2005-high-k-precession",
      "citation_key": "shimizu-2005-high-k-precession",
      "canonical_source": "Y. R. Shimizu, M. Matsuzaki, and K. Matsuyanagi, Phys. Rev. C 72, 014306 (2005)",
      "raw_file": "raw/papers/gpt/query/20261113-A130-precession-limits/shimizu-matsuzaki-matsuyanagi-2005-nucl-th-0412074v2.pdf",
      "raw_sha256": "6566edd91dc5765a21241ac553f599faf0037d1cadf4113edbe1d969645e97c7",
      "actual_read_pages": [2, 3, 5, 6],
      "text_anchor": "PDF pp. 2-3, 5-6, Eq. (1), (8)-(11), (32), (38)-(40): axially symmetric limit (gamma -> 0) of wobbling motion; J_z -> 0; frame frequency relation omega_wob = omega_prec - omega_rot; omega_prec = hbar K / J_perp^eff; initial level spacing hbar^2(K+1)/J_perp vs asymptotic hbar^2 K/J_perp.",
      "claims_supported": [
        "高 K 进动模式是三轴摆动在轴对称极限 (gamma -> 0) 下的连续退化极限",
        "参考系代数关系: omega_wob = omega_prec - omega_rot，其中 omega_prec = hbar K / J_perp^eff，K 为无量纲单粒子投影",
        "轴对称下绕对称轴集体转动惯量 J_3 -> 0，横向摆动能带收缩为单态",
        "绝热转子首能级间距严格为 hbar^2(K+1)/J_perp，与大 K 渐近频率 hbar^2 K/J_perp 存在 hbar^2/J_perp 的量子几何微商"
      ]
    },
    {
      "source_id": "sensharma-2020-longitudinal-wobbling-187au",
      "citation_key": "sensharma-2020-longitudinal-wobbling-187au",
      "canonical_source": "N. Sensharma et al., Phys. Rev. Lett. 124, 052501 (2020)",
      "raw_file": "raw/papers/2020_Sensharma et al_Longitudinal Wobbling Motion in Au 187.pdf",
      "raw_sha256": "f348dce9976ad076fd9b1d5281a728e0923053aced33b0270f643d770729366a",
      "actual_read_pages": [1, 2, 3],
      "text_anchor": "PDF pp. 1-3: reported longitudinal wobbling (LW) in 187Au on pi h9/2.",
      "claims_supported": [
        "Sensharma 等人报道在 187Au 中基于 pi h9/2 轨道的纵向摆动模型假定"
      ]
    },
    {
      "source_id": "guo-2022-low-spin-wobbling-187au",
      "citation_key": "guo-2022-low-spin-wobbling-187au",
      "canonical_source": "S. Guo et al., Phys. Lett. B 828, 137010 (2022)",
      "raw_file": "raw/papers/2022_Guo et al_Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei3.pdf",
      "raw_sha256": "de541977e4c8402c905ef8268ebc5707303f4b92f244eb4f59405a70c3473206",
      "actual_read_pages": [1, 2, 3, 4],
      "text_anchor": "PDF pp. 2-4: 376 keV (11/2- -> 9/2-) and 462 keV (15/2- -> 13/2-) linking transitions yield small roots delta ≈ -0.26 and -0.28; adopting B(E2)_in ~ 100-200 W.u. from 186Pt core / Band 1 estimates B(E2)_out to be only a few W.u. (B(E2)_out/B(E2)_in < 0.1); odd proton Fermi level near bottom of h9/2 favors short-axis alignment, conflicting with LW intermediate-axis alignment; core spin R ~ 1 at bandhead violates wobbling condition.",
      "claims_supported": [
        "连接 Band 2 与 Band 1 的 376 keV (11/2- -> 9/2-) 与 462 keV (15/2- -> 13/2-) 跃迁支持小混合比解 delta ≈ -0.26 与 -0.28",
        "由于缺乏 Band 2 能级直接寿命测量，通过采用邻近 186Pt 核芯或带内已知的 B(E2)_in ~ 100-200 W.u. 进行模型估算，导出带间 B(E2)_out 仅几个 W.u. (B(E2)_out/B(E2)_in < 0.1)",
        "奇质子处于 h9/2 底壳倾向对准短轴 s=2，与 LW 要求的中轴 m=1 对准在几何上产生根本性分歧；带头 R ~ 1 缺乏恢复力；支持长椭--扁椭三轴形状共存与多构型混合解释"
      ]
    },
    {
      "source_id": "frauendorf-2014-transverse-wobbling",
      "citation_key": "frauendorf-2014-transverse-wobbling",
      "canonical_source": "S. Frauendorf and F. Dönau, Phys. Rev. C 89, 014322 (2014)",
      "raw_file": "raw/papers/2014_Frauendorf_Dönau_Transverse wobbling.pdf",
      "raw_sha256": "36794ee1308adc1b34206ccdbf62353d6e79b3b485979e78709fd31efe5f57e3",
      "actual_read_pages": [1, 2, 3, 4],
      "text_anchor": "PDF pp. 1-4: PRM formulation of TW and LW; defined relative to maximum moment of inertia axis; frozen alignment assumption.",
      "claims_supported": [
        "TW 与 LW 严格定义为奇核子角动量 j 相对模型所指定的最大转动惯量轴的几何对准关系",
        "明确 TW 与 LW 依赖于准粒子冻结对准与特定核芯惯量排序假设"
      ]
    },
    {
      "source_id": "matsuzaki-2004-nuclear-inertia-and-wobbling",
      "citation_key": "matsuzaki-2004-nuclear-inertia-and-wobbling",
      "canonical_source": "M. Matsuzaki, Y. R. Shimizu, and K. Matsuyanagi, Phys. Rev. C 69, 034306 (2004)",
      "raw_file": "raw/papers/gpt/query/20261108-r2-g42-inertia-observables/matsuzaki-2004-nuclear-moments-of-inertia-prc69-034306.pdf",
      "raw_sha256": "9ea9fb2c8b9e73b0352a219ace7efc6182d6b5471b38d32cb96bc539e4aa6bf7",
      "actual_read_pages": [1, 2, 3, 7],
      "text_anchor": "PDF pp. 1-3, 7: Microscopic QRPA frequency-dependent moments of inertia J_k(omega) for 163Lu wobbling motion; pairing and Coriolis dynamical effects on inertia ordering.",
      "claims_supported": [
        "微观配对相互作用与科里奥利响应导致微观横向转动惯量呈现显著的旋转频率依赖性 J_k(omega)",
        "真实的核芯转动惯量排序受微观动力学演化调控，并非恒定固定于宏观流体比例"
      ]
    },
    {
      "source_id": "book-bohr-mottelson-nuclear-structure-vol2",
      "citation_key": "book-bohr-mottelson-nuclear-structure-vol2",
      "canonical_source": "A. Bohr and B. R. Mottelson, Nuclear Structure, Volume II: Nuclear Deformations, W. A. Benjamin, Inc. (1975)",
      "raw_file": "knowledge/sources/book-bohr-mottelson-nuclear-structure-vol2.md",
      "raw_sha256": "local-reference",
      "actual_read_pages": [176, 190],
      "text_anchor": "Chapter 4, Section 4-5, Eq. (4-188): classical asymmetric top wobbling Hamiltonian; R >> 1 condition for harmonic wobbling precession.",
      "claims_supported": [
        "非对称刚体转子三维定常转动与微扰简谐摆动角动量几何",
        "摆动简谐近似成立的必要条件为核芯具有大集体转动角动量 (R >> 1)"
      ]
    }
  ],
  "notations_and_conventions": {
    "radii_ordering": "R_k = R_0 [1 + sqrt(5/(4pi)) beta_2 cos(gamma - 2pi k / 3)], k=1,2,3; 0 < gamma < 60 deg 导出 R_2 < R_1 < R_3，即短轴 s=2, 中轴 m=1, 长轴 l=3",
    "rigid_moments_ordering": "J_k^rig propto R_i^2 + R_j^2 导出 J_2^rig > J_1^rig > J_3^rig (J_s > J_m > J_l)",
    "irrotational_moments_ordering": "J_k^irr = 4 B beta^2 sin^2(gamma - 2pi k / 3) 导出 gamma=30 deg 处 J_1^irr > J_2^irr, J_3^irr (J_m > J_s, J_l)",
    "wobbling_modes": "TW 严格定义为 j 垂直于最大惯量轴 (如类无旋流下 j on s=2 垂直于 J_max on m=1)；LW 严格定义为 j 平行于最大惯量轴",
    "fa_frequency_evolution": "hbar omega_wob = 2 sqrt((a_2 I + A_1 j)(a_3 I + A_1 j))，在 TW 条件 a_2 < 0, a_3 >= 0 下低自旋可呈现先升后降，非单调下降",
    "stability_condition": "要求两个横向二次系数严格为正 C_2 > 0 且 C_3 > 0，乘积正但两系数均为负代表局部能量极大，动力学失稳",
    "shimizu_frame_relations": "omega_wob = omega_prec - omega_rot; omega_prec = hbar K / J_perp^eff; K 无量纲单粒子投影; 首间距 hbar^2(K+1)/J_perp 与大 K 渐近 hbar^2 K/J_perp 区分",
    "electromagnetic_units": "B(E2) 以 e^2 b^2 或 W.u. 表示 (A=163, R0=1.2 fm 下 1 W.u. ≈ 0.00530 e^2 b^2)；B(M1) 以 mu_N^2 表示；电荷型与磁矩型算符数值在各自命名单位下一致，不人为除以 c^2"
  },
  "claims_and_derivations": [
    {
      "id": "CLAIM-4-4-1",
      "topic": "空间电荷几何主轴严格排序与惯量机制对立",
      "tex_symbol_or_expr": "R_2 < R_1 < R_3; \\mathcal{J}_s^{\\text{rig}} > \\mathcal{J}_m^{\\text{rig}} > \\mathcal{J}_l^{\\text{rig}}; \\mathcal{J}_m^{\\text{irr}} > \\mathcal{J}_s^{\\text{irr}}, \\mathcal{J}_l^{\\text{irr}}",
      "source_id": "book-bohr-mottelson-nuclear-structure-vol2",
      "derivation_steps": [
        "在小 beta_2 展开下，根据三角自变量区间严格证明 0 < gamma < 60 deg 时 cos(gamma - 4pi/3) < cos(gamma - 2pi/3) < cos(gamma)",
        "由此直接导出 R_2 < R_1 < R_3，即短轴 s=2, 中轴 m=1, 长轴 l=3，澄清旧稿中把 k=1 误作短轴的代数符号错误",
        "基于物质二阶矩证明刚体转子绕最短几何轴 s=2 惯量最大 (J_s^rig > J_m^rig > J_l^rig)",
        "基于玻尔表面无旋流公式证明无旋流体绕中间几何轴 m=1 惯量最大 (J_m^irr > J_s^irr, J_l^irr)",
        "强调微观核芯惯量受配对与单粒子能级控制，具有显著转动频率依赖性 J_k(omega)"
      ]
    },
    {
      "id": "CLAIM-4-4-2",
      "topic": "准粒子费米面对准几何与横向/纵向摆动模型边界",
      "tex_symbol_or_expr": "\\mathbf{j}_{\\text{particle}} \\parallel s; \\mathbf{j}_{\\text{hole}} \\parallel l; \\mathbf{j}_{\\text{mid}} \\parallel m; \\hbar\\omega_{\\text{wob}} = 2\\sqrt{(a_2 I + A_1 j)(a_3 I + A_1 j)}",
      "source_id": "frauendorf-2014-transverse-wobbling",
      "derivation_steps": [
        "依据单粒子四极密度重叠分析：底壳粒子型对准短轴 s=2，顶壳空穴型对准长轴 l=3，半满壳对准中轴 m=1",
        "在核芯最大惯量沿中轴的设定下，粒子对准短轴构成横向摆动 (TW)；粒子对准中轴构成纵向摆动 (LW)",
        "指出冻结顺排 (FA) 摆动能量在 TW 下低自旋可呈现先升后降，单一能量下降不能作为 TW 判定定理",
        "明确摆动微扰稳定条件为 C_2 > 0 且 C_3 > 0，不能仅凭实根判定能量极小",
        "澄清倾斜转动若局限在主平面内保持时间反演复合对称，不自动导致手征对称性自发破缺"
      ]
    },
    {
      "id": "CLAIM-4-4-3",
      "topic": "163Lu 的实测原表数据分析与集体增强判定",
      "tex_symbol_or_expr": "Q_t \\approx 6.7\\text{--}9.9\\ \\mathrm{b}; B(E2)_{\\mathrm{out}} \\approx 0.54\\text{--}0.70\\ e^2\\mathrm{b}^2 \\approx 100\\text{--}132\\ \\mathrm{W.u.}; R \\sim 15\\text{--}30\\hbar",
      "source_id": "campaign-g07-gorgen-2004-163lu-quadrupole-moments",
      "derivation_steps": [
        "核查 Görgen 2004 Table I 数据，指出 TSD1 与 TSD2 的 Qt 分布在 6.7–9.9 b 区间，体现了两带基于相近超形变核芯的特征",
        "核查 Table II 带间连接跃迁数据，实测带间 B(E2)_out 达到 0.54–0.70 e^2b^2，利用标准 Weisskopf 公式 B_W(E2) ≈ 0.05940 A^(4/3) e^2fm^4 ≈ 0.00530 e^2b^2 (A=163, R0=1.2 fm) 换算对应约 100–132 W.u.",
        "指明 Table II 中 B(E2) 与 B(M1) 的提取依赖于采用的历史平均混合比 delta = -3.10(+0.36/-0.44) (测至 51/2+ 外推假定)",
        "明确理论模型中使用的 Lu 核芯惯量为模型拟合参数，非直接实测量",
        "明确 163Lu 发生在 R ~ 15-30 hbar 的强转动极限与高 j (13/2) 孤立轨道的特殊边界，破除『所有 TSD 必摆动』的教条泛化"
      ]
    },
    {
      "id": "CLAIM-4-4-4",
      "topic": "135Pr 极化双根多义性、能级分支比证伪与多元微观竞争",
      "tex_symbol_or_expr": "\\delta = -0.47_{-0.22}^{+0.09}; \\frac{B(E2; 747.3)}{B(E2; 526.2)} = 0.7_{-0.5}^{+0.7}; R \\sim 1\\hbar",
      "source_id": "lv-2022-evidence-against-wobbling-135pr",
      "derivation_steps": [
        "指出在束角分布与方向角关联比值关于 delta 具有二次有理式代数结构，必然存在大根与小根双解",
        "证明正线偏振度不能排他性排除小根解",
        "核实 Lv 等人 2022 Table 1 实测数据：747.3 keV (17/2- -> 15/2-) 与 813.2 keV (21/2- -> 19/2-) 均支持磁偶极主导的小根解 (delta ≈ -0.47 与 -0.46)",
        "核实同母态分支比 B(E2; 747.3)/B(E2; 526.2) = 0.7(+0.7/-0.5)，直接推翻建立在基带上的纯摆动声子图像",
        "带头核芯自旋 R ~ 1 hbar 破坏强转动谐振展开；阐明微观 IBFM (Nomura 2022)、QTR 平面转动与 TiP 竞争解释"
      ]
    },
    {
      "id": "CLAIM-4-4-5",
      "topic": "轴对称高 K 进动极限与重区形状共存演化",
      "tex_symbol_or_expr": "\\omega_{\\mathrm{wob}} = \\omega_{\\mathrm{prec}} - \\omega_{\\mathrm{rot}}; \\omega_{\\mathrm{prec}} = \\frac{\\hbar K}{\\mathcal{J}_\\perp^{\\text{eff}}}; \\Delta E_{\\text{first}} = \\frac{\\hbar^2(K+1)}{\\mathcal{J}_\\perp}; \\hbar\\omega_{\\mathrm{prec}} \\simeq \\frac{\\hbar^2 K}{\\mathcal{J}_\\perp}",
      "source_id": "shimizu-2005-high-k-precession",
      "derivation_steps": [
        "推导三轴摆动在 gamma -> 0 轴对称极限下的连续退化：J_3 -> 0 使得横向摆动带收缩，垂直声子序列演化为高 K 进动态",
        "给出 Shimizu 轴对称 RPA 参考系代数关系 omega_wob = omega_prec - omega_rot，明确 K 为无量纲单粒子投影",
        "严格区分带头首能级间距 hbar^2(K+1)/J_perp 与大 K 渐近频率能量 hbar^2 K/J_perp，指出其相差 hbar^2/J_perp 量度项",
        "剖析 187Au 纵向摆动宣称中存在的质子底壳对准短轴与中轴假设冲突，核查 Guo 2022 小根解与采用量依赖性",
        "阐明重核区 Os/Pt/Hg 的 gamma 软势能面与多重形状共存，明确扁椭或形状共存决非证实轴对称假设"
      ]
    },
    {
      "id": "CLAIM-4-4-6",
      "topic": "跨核区取向运动迁移充要条件与物理不变量映射边界",
      "tex_symbol_or_expr": "\\text{Rigidity} + \\text{Strong Core Spin} (R \\gg 1) + \\text{Alignment Stability} + \\text{Phonon Decoupling Gap}",
      "source_id": "book-bohr-mottelson-nuclear-structure-vol2",
      "derivation_steps": [
        "系统提炼取向运动稳定呈现的四大物理充要条件：势能面刚度、强核芯转动 (R >> 1)、准粒子对准稳定性、声子本征解耦间隙",
        "以 135Pr 与 187Au 为反例，剖析低自旋下核芯转动极弱 (R ~ 1)、准粒子重对准与能带混合诱发摆动失效的物理机制",
        "严格界定 Qt 与 Qs、微观形状不变量比值 R 与 cos(3 gamma)、纵向转动惯量与横向恢复力惯量的映射边界",
        "明确磁偶极跃迁中 mu_N^2 与 (mu_N/c)^2 的单位规范"
      ]
    }
  ],
  "competing_explanations_and_boundaries": [
    {
      "case": "135Pr 低自旋横向摆动 vs 平面转动 / IBFM / 单粒子重对准",
      "primary_claim": "Matta 2015 宣称 Band 3 为基于 pi h11/2 的一声子横向摆动带",
      "counter_evidence": "Lv 2022 JUROGAM II 实测证实连接线支持小根解 (delta ≈ -0.47, M1 主导 >80%)，同母态分支比约为 0.7 否定纯声子态，核芯转动仅 R ~ 1 hbar",
      "competing_models": "微观 IBFM (Nomura 2022) 天然给出 M1 主导带间退激；QTR 放开冻结给出向转轴倾斜的平面转动；TiP (Lawrie 2020) 给出倾斜进动替代解释",
      "status": "摆动声子假说被排他性否定，平面转动/IBFM/多构型混合成为主导解释"
    },
    {
      "case": "187Au 纵向摆动 vs 形状共存与多构型混合",
      "primary_claim": "Sensharma 2020 宣称 Band 2 为基于 pi h9/2 的纵向摆动带",
      "counter_evidence": "奇质子处于 h9/2 底壳在微观能面上强烈倾向对准短轴 s=2，与 LW 中轴对准模型假设根本对立；带头 R ~ 1 hbar 缺乏恢复力；Guo 2022 实测支持小根解，采用 186Pt 估计带间 E2 仅数个 W.u.",
      "competing_models": "长椭--扁椭形状共存、单粒子态激发与多构型混合",
      "status": "纵向摆动假说缺乏坚实证据，形状共存提供更自洽的物理描述"
    },
    {
      "case": "三轴摆动 vs 高 K 进动",
      "primary_claim": "高 K 进动是三轴摆动在 gamma -> 0 轴对称极限下的连续退化",
      "counter_evidence": "随体旋转系与实验室固定 K 参考系存在不同物理含义；轴对称下对称轴集体惯量 J_3 -> 0，横向带退化为孤立单态",
      "competing_models": "Shimizu 2005 RPA 理论与绝热强耦合转子模型",
      "status": "确立了二者在微观取向几何上的连续统一与能标微商差异"
    }
  ],
  "reader_checks": [
    {"check": "半径余弦展开排序检查", "result": "逐项算出 cos(gamma-4pi/3) < cos(gamma-2pi/3) < cos(gamma) 导出 R_2 < R_1 < R_3，严格确立 s=2, m=1, l=3，修复旧稿 k=1 误作短轴错误"},
    {"check": "刚体与无旋流惯量主轴对应检查", "result": "严格证明刚体 J_s^rig 最大 (J_2 > J_1 > J_3)，无旋流在 gamma=30 deg 处 J_m^irr 最大 (J_1 > J_2, J_3)"},
    {"check": "TW 能量趋势与稳定性判据检查", "result": "指出 FA 模型下低自旋 TW 能可先升后降，阐明实根不等于能量极小 (必须 C_2, C_3 > 0)"},
    {"check": "163Lu 原件原表与采用量依赖检查", "result": "Table I 与 Table II 实测数据逐项核对，B_W(E2) ≈ 0.00530 e^2 b^2 导出 100–132 W.u.，注明 Table II 提取采用历史 delta=-3.10，注明核芯惯量为模型输出"},
    {"check": "135Pr 能级跃迁与小根数值检查", "result": "747.3 keV 为 17/2- -> 15/2-，小根 delta = -0.47(+0.09/-0.22)；分支比 0.7(+0.7/-0.5)；核芯转动 R ~ 1 hbar；纳入 IBFM、QTR 与 TiP 竞争解释"},
    {"check": "Shimizu 高 K 进动参考系与能标检查", "result": "参考系代数式 omega_wob = omega_prec - omega_rot，K 无量纲，首间距 hbar^2(K+1)/J_perp 与大 K 渐近 hbar^2 K/J_perp 严格区分"},
    {"check": "187Au 对准几何与采用依赖检查", "result": "指出底壳粒子倾向短轴 s=2 与 LW 中轴假设矛盾，带头 R ~ 1 hbar，采用 186Pt 导出带间 E2 仅数个 W.u.，澄清重区扁椭/共存非证实轴对称假设"},
    {"check": "单位与算符规范检查", "result": "mu_N^2 与 (mu_N/c)^2 数值一致，无多余除以 c^2 错误"}
  ],
  "prohibitions_strictly_obeyed": [
    "绝对禁止口号化用语（已全面剔除『金标准』、『铁证』、『彻底』、『毋庸置疑』等夸大词汇）",
    "严格区分独立实验与同源数据（明确 Sensharma 2019/2026 继承 Gammasphere 谱学与分组，Lv 2022 为独立 JUROGAM 实验）",
    "严格区分实验直接报告与模型计算（明确 163Lu 核芯惯量为推转/QRPA 计算，Table II 为采用 delta 外推提取；明确 187Au 带间强度为采用 186Pt 估算）",
    "不将单一能量下降作为判定 TW 的充要条件",
    "不将正线偏振作为排他性排除小根的根据"
  ],
  "open_issues": [
    "135Pr 与 187Au 特征激发带仍缺乏高精度直接能级寿命测量（如 DSAM 或 RDM），无模型依赖的绝对 B(E2)_out 与 B(M1)_out 尚未完全闭合",
    "在极低转动角动量 (R ~ 1 hbar) 区域，需要超越粒子--转子模型与简谐 RPA 的全微观含时三维角动量投影理论"
  ]
}

ledger_json_str = json.dumps(ledger, indent=2, ensure_ascii=False)

staging_ledger = 'outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/section-4-4.json'
with open(staging_ledger, 'w', encoding='utf-8') as f:
    f.write(ledger_json_str)

canonical_ledger = 'raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json'
with open(canonical_ledger, 'w', encoding='utf-8') as f:
    f.write(ledger_json_str)

print('Ledger section-4-4.json written successfully to staging and canonical!')
