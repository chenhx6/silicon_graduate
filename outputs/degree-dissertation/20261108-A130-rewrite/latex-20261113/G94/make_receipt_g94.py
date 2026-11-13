import json, hashlib

def get_sha256(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

files_to_hash = [
    "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Appendices/AppendixA.tex",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G94/AppendixA.tex",
    "raw/writing/gpt/A130/latex-evidence-ledger/appendix-A.json",
    "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G94/appendix-A.json",
    "knowledge/research-notes/a130-rewrite-angular-momentum-appendix-audit-20261113.md"
]

file_hashes = {p: get_sha256(p) for p in files_to_hash}

receipt = {
  "task": "G94 (Appendix A narrow repair based on T20 audit report)",
  "worker": "G90",
  "status": "COMPLETED",
  "recorded_at": "2026-11-14T00:35:00Z",
  "file_hashes": file_hashes,
  "canonical_tex_sha256": file_hashes["raw/writing/gpt/A130/these_2023_template/these_template/Tex/Appendices/AppendixA.tex"],
  "canonical_ledger_sha256": file_hashes["raw/writing/gpt/A130/latex-evidence-ledger/appendix-A.json"],
  "eight_reconciled_items": {
    "T20-01 (SI vs Gaussian magneton and physical BS)": {
      "status": "RECONCILED",
      "action": "在 AppendixA.tex 式 (eq:appA-mun-def)-(eq:appA-bs-bmu-trans) 中全面纠偏：SI 核磁子写作 mu_N^SI = e hbar / (2 m_p)，引入质子康普顿特征长度 ell_N = hbar / (2 m_p c) ≈ 0.105155 fm，导出 mu_N^SI / c = e ell_N；物理电荷型跃迁几率严格补齐 e^2，写作 B_S(M1) = b_M1 (e ell_N)^2 = b_M1 e^2 (0.105155 fm)^2，彻底消除丢失 e^2 的量纲错误；高斯单位制独立分段说明。"
    },
    "T20-02 (5.9 C_M1 units consistency)": {
      "status": "BOUNDED",
      "action": "本任务恪守不碰 5.9 的边界指令，在附录 A 式 (eq:appA-b-m1-dimensionless) 处确立无量纲 b_M1 标度，保证与 5.9 主公式完全自洽对齐。"
    },
    "T20-03 (Krane-Steffen vs Rose-Brink and Hamilton +2 delta F)": {
      "status": "RECONCILED",
      "action": "在附录 A 第 245-256 行明确说明：本书在发射过程选用 Krane-Steffen (KS) 混合比约定，式 (eq:4-5-delta-def-app) 算符相位与角分布几何系数按同一约定配套；Hamilton 对应正干涉项 +2 delta F_k(LL')；明确 Lange 1982 给出的发射约定转换式 delta_KS = -delta_RB，已发表数据保留原约定，转换时同步转换干涉系数并区分发射与吸收。"
    },
    "T20-04 (Bohr-Mottelson Vol I square root normalization)": {
      "status": "RECONCILED",
      "action": "实际核读 Bohr & Mottelson 卷 I PDF 100-101 页式 (1A-60)，证实原书明确包含 (2I_2+1)^(-1/2) 因子，与 Suhonen 式 (2.27) 形式严格一致。附录 A 式 (eq:appA-we-bm) 及表 A.1 已彻底删除旧稿中关于 BM 缺少该因子的错误断言；ledger 中 source id 规范为 book-bohr-mottelson-nuclear-structure (无 -vol1)。"
    },
    "T20-05 (Hermitian tensor RME conjugation without (-1)^k)": {
      "status": "RECONCILED",
      "action": "附录 A 第 34-38 行与式 (eq:appA-rme-exchange) 已重写：球张量自伴条件定义为 [T_q^(k)]^dagger = (-1)^q T_{-q}^(k)，明确这是一项附加厄米性条件而非群旋转性质本身推论；RME 初末态对调共轭关系严格推导为 <j_f || T^(k) || j_i> = (-1)^(j_f - j_i) <j_i || T^(k) || j_f>^*，彻底剔除多余的 (-1)^k 指数。"
    },
    "T20-06 (3j - CG intermediate conversion phase)": {
      "status": "RECONCILED",
      "action": "附录 A 式 (eq:appA-3j-cg-relation) 替换为严格对称式：3j 符号首列为 j_f, -m_f 时对应相因子为 (-1)^(j_f - m_f) / sqrt(2j_f+1) C_{j_i m_i k q}^{j_f m_f} = (-1)^(j_i + k - m_f) / sqrt(2j_f+1) C_{k q j_i m_i}^{j_f m_f}，在整数阶 k 下两者完全一致并与式 (eq:appA-we-3j) 及 (eq:appA-we-cg) 严格自洽。"
    },
    "T20-07 (9j to 6j reduction phase depending on j_1')": {
      "status": "RECONCILED",
      "action": "附录 A 式 (eq:appA-9j-to-6j) 纠正为 (-1)^(j_1' + j_2 + J + k) / sqrt((2j_2+1)(2k+1)) delta_{j_2 j_2'} {j_1', J', j_2; J, j_1, k}，相位严格使用末态自旋 j_1'，与其下单体算符约化矩阵元公式 (eq:appA-single-op-1) 完全自洽。"
    },
    "T20-08 (6j triangle indicator chi vs Racah Delta_R)": {
      "status": "RECONCILED",
      "action": "附录 A 式 (eq:appA-6j-ortho-theorem) 将正交完备性定理右端三角指示函数改记为 chi(a,b,c) 并明确定义角动量和为整数的条件；式 (eq:appA-racah-formula) 改记为 Racah 三角系数 Delta_R 并补齐中间参量 (v1,v2,v3,v4) 与 (w1,w2,w3) 定义；1/5 解析求和算例明确声明为特定代数自洽性控制，不充当全附录无条件证明。"
    }
  },
  "erratum_audit_boundary": {
    "target": "Lange, Kumar, Hamilton 1982 APS Erratum, Rev. Mod. Phys. 54, 673 (1982), DOI: 10.1103/RevModPhys.54.673",
    "local_archive_precheck": "未在本地 raw/ 或 knowledge/ 中找到该勘误原件",
    "online_retrieval_status": "APS 付费墙限制 (HTTP 403 Forbidden)，未取得开放全文",
    "scientific_decision": "主要修正已基于本地原版 Lange 1982 完整综述 (PDF pp. 3-4) 与 Hamilton 1975 专著原件闭合；绝不依据勘误标题猜测或修改既有正确公式，忠实记录未取得边界"
  },
  "prohibitions_strictly_obeyed": [
    "未触碰正文第 5.9 节、公共 Bib 文件、Git 状态、编译管线或生成新提交",
    "未将特定有限自旋组态的 1/5 有理数求和闭合冒充为全附录全局证明",
    "严格以本地物理原件为基准，不凭空脑补未获勘误的内容"
  ]
}

receipt_path = "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G94/receipt.json"
with open(receipt_path, 'w', encoding='utf-8') as f:
    json.dump(receipt, f, indent=2, ensure_ascii=False)

print(f"Receipt written successfully to {receipt_path}!")
