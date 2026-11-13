import json, hashlib

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
  "round": "Round-2 (father feedback reconciliation)",
  "title": "$A\\approx 130$、稀土与重区的取向对照",
  "status": "COMPLETED_ROUND2",
  "timestamp": "2026-11-13T20:35:00Z",
  "file_hashes": file_hashes,
  "canonical_tex_sha256": file_hashes["raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex"],
  "canonical_ledger_sha256": file_hashes["raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json"],
  "father_feedback_11_items_reconciliation": {
    "44-1": "已区分定域能量极小与线性动力学稳定性：明确 C_m, C_l > 0 为正能声子基态；C_m, C_l < 0 为旋转坐标系定域能量极大，陀螺力可保线性稳定，但不能作为声子激发稳定基态，不把极大简单归为指数增长失稳。",
    "44-2": "已彻底删除 J_3 -> 0 导致全横向带坍塌为单能级的断言；明确 R_3=0 为形状冗余规范约束，保留固定内禀 K 下的有限转动能带 E_K(I) 与首间距 Delta E_first = hbar^2(K+1)/J_perp。",
    "44-3": "已依据 Lv 2022 原件 Table 1 完全更正所有数据：747.3 keV 实测 P=0.04(+0.08/-0.13), Rac=0.37(4), delta=-0.47(+0.09/-0.22); 813.2 keV 实测 P=-0.03(+0.05/-0.12), Rac=0.48(6), delta=-0.37(+0.10/-0.14); 450.2 keV 实测 Rac=0.49(4), delta=-0.31(+0.10/-0.13)。明确 M1 百分比为 delta 的条件变换。",
    "44-4": "已将分支比 0.7(+0.7/-0.5) 准确限定为作者在采用 526.2 keV 多极性与相对强度下的解释，删除了无根据的通用 10-100 阈值与『毫无争议』口号，指出同核导出参量非独立重复实验。",
    "44-5": "已更正 Nomura 2022 核心泛函：134Ce 偶偶核芯映射自相对论 DD-PC1 泛函与可分离配对力 (Gogny D1M 用于 132Ba/128Xe)；明确 QTR 模型在固定形变 (gamma=26 deg) 下给出准粒子向转轴倾斜，区分 IBFM 软性与 QTR 平面转动机制。",
    "44-6": "已明确 R=|I-j| 为矢量/算符关系，R ~ 1 hbar 为带头特定模型顺排估计而非经验测量值，小 R 属于简谐近似局限，保留全量子/QRPA 争议与模型空间。",
    "44-7": "已严格将 LW 定义为准粒子沿最大惯量轴顺排，指出半满壳属单粒子趋势而非定义充要条件，删除了『跨区充要条件』与任意 R>>1 门槛的武断断言。",
    "44-8": "已澄清二次有理式方程实根可有 0、1 或 2 个及退化情形，将特定双根仅联系于实测响应与误差，删除了人造的『合理 sigma/I 0.25-0.35』准则。",
    "44-9": "已注明 TSD nw 标签为作者指派，相近 Qt 不唯一固定波函数或三轴刚度；注明采用 delta 外推非完全独立测量；注明核芯惯量为模型参数；注明 187Au 估计采用 186Pt 输入，且重区 PES 非普适极度平坦。",
    "44-10": "已阐明微观惯量受单粒子能级与配对调控，不必然受刚体/无旋流包络限制；使用物理角度与无量纲角动量，剔除所有口号与夸大词汇。",
    "44-11": "已显式置换几何轴 (k1=m, k2=s, k3=l) 与第3.3节局部 FA 展开坐标 (1=qp 沿短轴 s, 2=最大惯量沿中轴 m, 3=长轴 l)，重写公式为 A_s, A_m, A_l 与 C_m, C_l 及 I_c=j/(1-J_s/J_m)，消除了下标冲突。"
  },
  "modified_files": [
    "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/sec-4-4.tex",
    "raw/writing/gpt/A130/latex-evidence-ledger/section-4-4.json",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/section-4-4.json",
    "knowledge/research-notes/a130-rewrite-orientation-cross-region-conditions-20261113.md",
    "system/scripts/a130_orientation_comparison_figure.py",
    "raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.svg",
    "raw/writing/gpt/A130/these_2023_template/these_template/Img/orientation-comparison-modes.pdf",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/receipt-sec-4-4.json"
  ]
}

receipt_path = "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/receipt-sec-4-4.json"
with open(receipt_path, 'w', encoding='utf-8') as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False)

print(f"Round 2 Receipt written successfully to {receipt_path}!")
