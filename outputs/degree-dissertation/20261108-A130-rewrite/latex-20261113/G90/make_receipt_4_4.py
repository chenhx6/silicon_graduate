import json, hashlib, os

def get_sha256(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

files_to_hash = [
    "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/sec-4-4.tex",
    "raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/section-4-4.json",
    "knowledge/research-notes/a130-rewrite-orientation-cross-region-conditions-20261113.md",
    "system/scripts/a130_orientation_comparison_figure.py",
    "raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.svg",
    "raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.pdf",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/new-references.bib"
]

file_hashes = {p: get_sha256(p) for p in files_to_hash}

receipt = {
  "worker": "G90",
  "section": "4.4",
  "title": "$A\\approx 130$、稀土与重区的取向对照",
  "status": "COMPLETED",
  "timestamp": "2026-11-13T19:45:00Z",
  "file_hashes": file_hashes,
  "canonical_tex_sha256": file_hashes["raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex"],
  "canonical_ledger_sha256": file_hashes["raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json"],
  "scientific_checks": {
    "axis_ordering_proof": "严格证明在 Lund 约定 0 < gamma < 60 deg 下，cos(gamma - 4pi/3) < cos(gamma - 2pi/3) < cos(gamma) 导出 R_2 < R_1 < R_3，即短轴 s=2, 中轴 m=1, 长轴 l=3；彻底消除旧稿把 k=1 误作短轴的代数符号错误；证明刚体 J_s^rig 最大 (J_2 > J_1 > J_3)，无旋流在 gamma=30 deg 处 J_m^irr 最大 (J_1 > J_2, J_3)",
    "chapter_3_boundaries_integrated": [
      "冻结顺排 (FA) 模型下 TW 摆动频率 hbar omega_wob = 2 sqrt((a_2 I + A_1 j)(a_3 I + A_1 j))，在 a_2 < 0, a_3 >= 0 下低自旋可呈现先升后降，指出单一能量下降非 TW 充分条件，能量上升亦不能单方否定摆动",
      "稳定性严格要求两横向曲率同时为正 C_2 > 0 且 C_3 > 0，不能仅凭实根判定能量极小 (C_2, C_3 < 0 为局部能量极大)",
      "临界自旋 I_c = j / (1 - J_1/J_2) 严格受限于冻结 j 近似与特定惯量排序假设",
      "倾斜转动若在主平面内保持时间反演复合对称，不自动导致手征对称性自发破缺"
    ],
    "primary_table_163lu": {
      "table_source": "Görgen 2004 Table I 与 Table II 逐项核对",
      "in_band_Qt": "TSD1 与 TSD2 测量值均分布在 6.7–9.9 b 区间，加权平均约 8.5 b 与 8.2 b",
      "interband_collectivity": "B(E2)_out ≈ 0.54–0.70 e^2 b^2，采用标准 Weisskopf 公式 B_W(E2) ≈ 0.05940 A^(4/3) e^2 fm^4 ≈ 0.00530 e^2 b^2 (A=163, R0=1.2 fm) 导出 100–132 W.u. 的宏观集体增强",
      "adopted_delta_caveat": "明确 Table II 中 B(E2) 与 B(M1) 提取依赖前人采用的历史平均混合比 delta = -3.10(+0.36/-0.44) (测至 51/2+ 外推)",
      "model_inertia_caveat": "明确理论文献中使用的 Lu 核芯惯量为推转/QRPA 模型计算值，非直接实测物理量",
      "core_spin_boundary": "163Lu 发生在 R ~ 15–30 hbar 的强转动极限"
    },
    "competing_models_135pr": {
      "experimental_chains_separated": "严格区分 Matta 2015 (ATLAS/INGA, 大根选定)、Guo 2021 comment (方法学双根指出)、Lv 2022 (JUROGAM II 独立实验, 小根确认与分支比证伪)、Sensharma 2019/2026 (同源 Gammasphere 数据流, 继承分组与条件性倾向)",
      "falsification_branching": "747.3 keV (17/2- -> 15/2-) 与 813.2 keV (21/2- -> 19/2-) 支持小根 delta ≈ -0.47 与 -0.46 (M1 主导 >80%)；同母态分支比 B(E2; 747.3)/B(E2; 526.2) = 0.7(+0.7/-0.5) 否定纯摆动声子",
      "competing_models_included": "微观 IBFM (Nomura 2022 基于 Gogny D1M 映射天然产生 M1 主导带间退激)、QTR 放开冻结后的平面转动 (Planar Rotation / 单粒子重对准)、TiP 倾斜进动 (Lawrie 2020) 与 gamma 振动混合",
      "quantum_distribution": "带头 R ~ 1 hbar 处角动量波函数角度弥散大，不能套用局域简谐高斯波包"
    },
    "shimizu_high_k_precession": {
      "frame_relations": "omega_wob = omega_prec - omega_rot; omega_prec = hbar K / J_perp^eff; K 为无量纲投影量子数",
      "energy_gap_vs_asymptote": "绝热强耦合转子带头首能级间距 Delta E_first = hbar^2(K+1)/J_perp；大 K 渐近频率能量 hbar omega_prec ≈ hbar^2 K/J_perp；二者相差严格的 hbar^2/J_perp 量度微商"
    },
    "pt_au_heavy_region": {
      "au187_alignment_conflict": "质子处于 h9/2 底壳倾向对准短轴 s=2，与 LW 要求的中轴 m=1 对准发生根本几何冲突；带头 R ~ 1 hbar 缺乏恢复力；Guo 2022 实测小根解，采用 186Pt 估算带间 E2 仅数个 W.u.",
      "shape_coexistence_boundary": "明确重核区 Os/Pt/Hg 的 gamma 软势能面与多重形状共存，绝对不能将扁椭或形状共存作为证实轴对称假设的证据"
    },
    "transfer_and_failure_conditions": {
      "four_conditions": "势能面刚度、强核芯转动 (R >> 1)、准粒子对准稳定性、声子本征解耦能隙",
      "failure_mechanisms": "低自旋下弱转动 (R ~ 1)、准粒子动态重对准、能带混合与电磁跃迁退化"
    }
  },
  "parent_review_questions": [
    "163Lu Table II 中的高自旋 (I > 51/2) 跃迁目前文献均采用 delta=-3.10 外推，未来若有直接高自旋偏振/寿命数据，是否需在第5章进一步单设反演不确定度专题？",
    "135Pr 与 187Au 目前关键带间连接线缺乏直接能级寿命测量（DSAM/RDM），建议在全论文后续总结中列为重点实验鉴别课题。"
  ],
  "new_bib_candidates": [
    "guo-2021-comment-transverse-wobbling-135pr",
    "sensharma-2020-longitudinal-wobbling-187au",
    "guo-2022-low-spin-wobbling-187au"
  ],
  "modified_files": [
    "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex",
    "raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json",
    "knowledge/research-notes/a130-rewrite-orientation-cross-region-conditions-20261113.md",
    "system/scripts/a130_orientation_comparison_figure.py",
    "raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.svg",
    "raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.pdf",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/new-references.bib",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/sec-4-4.tex",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/section-4-4.json",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/receipt-sec-4-4.json"
  ]
}

receipt_path = "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/receipt-sec-4-4.json"
with open(receipt_path, 'w', encoding='utf-8') as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False)

print(f"Receipt written successfully to {receipt_path}!")
