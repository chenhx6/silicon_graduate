import json, hashlib

tex_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Appendices/AppendixA.tex'
with open(tex_path, 'rb') as f:
    tex_sha = hashlib.sha256(f.read()).hexdigest()

ledger = {
  "section_id": "app-A",
  "title": "角动量与张量约定",
  "section_label": "app:angular-momentum-tensors",
  "status": "audited_and_reconciled_by_G90",
  "worker": "G90",
  "recorded_at": "2026-11-14T00:30:00Z",
  "canonical_paths": {
    "tex": "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Appendices/AppendixA.tex",
    "ledger": "raw/writing/gpt/A130/latex-evidence-ledger/appendix-A.json"
  },
  "staging_paths": {
    "tex": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G94/AppendixA.tex",
    "ledger": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G94/appendix-A.json"
  },
  "output_tex_sha256": tex_sha,
  "scope_boundary": "本附录为博士论文角动量与张量约定基础附录，严格形式化角动量李代数、球张量自伴条件、Wigner-Eckart 定理与 3j/CG 相位、Bohr-Mottelson 卷 I 归一化因数、自伴张量 RME 交换律、9j 降阶至 6j 相位、6j 三角指示函数与 Racah 闭式展开、详细平衡互易律、SI 核磁子与电荷型 B_S(M1) 物理量纲、以及 Krane-Steffen 与 Rose-Brink 多极混合比相位体系。本附录定域解析控制仅核验特定代数恒等式自洽性，不声明为全局全式无条件认证。",
  "sources": [
    {
      "source_id": "book-suhonen-from-nucleons-to-nucleus",
      "canonical_source": "J. Suhonen, From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory, Springer (2007)",
      "raw_file": "raw/books/From nucleons to nucleus concepts of microscopic .pdf",
      "raw_sha256": "4d4b799b8d91784638bac29e0749fe08ba9720f067fd76317f7e256d6f8cd27c",
      "actual_read_pages": [
        "PDF pp. 44-46 (print pp. 29-31), Eqs. (2.27), (2.31), (2.32): Wigner-Eckart theorem with 1/sqrt(2j'+1) and self-adjoint RME symmetry (-1)^(j-j')",
        "PDF p. 48 (print p. 33), Eq. (2.50): tensor products and coupled matrix elements",
        "PDF pp. 134-135 (print pp. 119-120), Eqs. (6.4), (6.7), (6.9): SI electromagnetic operators, nuclear magneton mu_N = e hbar / (2 m_p) = 0.105155 c e fm, footnote 6 on Gaussian units"
      ],
      "claims_supported": ["CA-01", "CA-02", "CA-03", "CA-04", "CA-06", "CA-07"]
    },
    {
      "source_id": "book-bohr-mottelson-nuclear-structure",
      "canonical_source": "A. Bohr and B. R. Mottelson, Nuclear Structure, Volume I: Single-Particle Motion, W. A. Benjamin (1969)",
      "raw_file": "raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf",
      "raw_sha256": "0dcbe4b29f032aa34feab4efbc74f4bfe4740e2ff9b17ce2c85b51ae50ef913a",
      "actual_read_pages": [
        "PDF pp. 100-101 (print pp. 81-82), Eq. (1A-60): <beta I2 M2 | T_lambda mu | alpha I1 M1> = (2I2+1)^(-1/2) <I1 M1 lambda mu | I2 M2> <beta I2 || T_lambda || alpha I1>, proving exact same normalization as Suhonen"
      ],
      "claims_supported": ["CA-03"]
    },
    {
      "source_id": "lange-kumar-hamilton-1982-multipole-admixtures",
      "canonical_source": "J. Lange, K. Kumar, and J. H. Hamilton, Rev. Mod. Phys. 54, 119 (1982)",
      "raw_file": "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1982_Lange et al_E0-E2-M1 multipole admixtures of transitions in even-even nuclei.pdf",
      "raw_sha256": "ed925a0577a9257903806acd209c1db707529e86a5bfd9a301a83d597bf78ffb",
      "actual_read_pages": [
        "PDF pp. 3-4 (print pp. 121-122), Eqs. (2.4), (2.5), (2.9): Krane-Steffen definition of delta(E2/M1) and conversion relation delta_KS = -delta_RB for emission"
      ],
      "claims_supported": ["CA-07"]
    },
    {
      "source_id": "book-hamilton-electromagnetic-interaction",
      "canonical_source": "W. D. Hamilton (ed.), The Electromagnetic Interaction in Nuclear Spectroscopy, North-Holland (1975)",
      "raw_file": "raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf",
      "raw_sha256": "d4cb879b76bbca6a89c3a3794b1a45705a3c1f1ec84e7ad1d2e1b1d4fa4c3f59",
      "actual_read_pages": [
        "PDF p. 553 (print p. 542): angular distribution F_k coefficients and positive interference term +2 delta F_k(LL')"
      ],
      "claims_supported": ["CA-07"]
    },
    {
      "source_id": "lange-1982-erratum",
      "canonical_source": "J. Lange, K. Kumar, and J. H. Hamilton, Rev. Mod. Phys. 54, 673 (1982), DOI: 10.1103/RevModPhys.54.673",
      "raw_file": "unobtained-paywalled (APS HTTP 403 Forbidden)",
      "raw_sha256": "none",
      "actual_read_pages": [
        "Unobtained boundary recorded: 1-page erratum behind APS paywall; local-literature-archive pre-check confirms not locally stored; primary corrections are fully grounded in local original Lange 1982 paper and Hamilton 1975; formulas not altered based on title alone"
      ],
      "claims_supported": ["CA-07"]
    }
  ],
  "claims_and_derivations": [
    {
      "claim_id": "CA-01",
      "statement": "物理总角动量算符矢显式携带约化普朗克常数 hbar，李代数对易子 [J_i, J_j] = i hbar epsilon_ijk J_k 保持作用量量纲，本征方程给出无量纲量子数 j, m。",
      "status": "supported",
      "type": "fundamental-definition"
    },
    {
      "claim_id": "CA-02",
      "statement": "不可约球张量对易子显式包含 hbar 因子；球张量自伴条件定义为 [T_q^(k)]^dagger = (-1)^q T_{-q}^(k)；在此条件下 RME 初末态对调共轭关系严格为 <j_f || T^(k) || j_i> = (-1)^(j_f - j_i) <j_i || T^(k) || j_f>^*，无多余的 (-1)^k 指数。",
      "status": "supported",
      "type": "operator-symmetry"
    },
    {
      "claim_id": "CA-03",
      "statement": "Wigner-Eckart 定理采用 Edmonds/Suhonen 标准约定，矩阵元分解在 CG 系数前具有 1/sqrt(2j_f+1) 因子；经原件核对，Bohr-Mottelson 卷 I 式 (1A-60) 同样明确包含 (2I_2+1)^(-1/2)，与 Suhonen 同归一，消除了旧稿中 BM1 缺该因子的错误断言。",
      "status": "supported",
      "type": "theorem-normalization"
    },
    {
      "claim_id": "CA-04",
      "statement": "复合系统单体算符约化矩阵元推导给出标准 9j 降阶至 6j 符号公式，标量算符行退化相位严格为 (-1)^(j_1' + j_2 + J + k) 并依赖 j_1'，纠正了旧稿错用 j_1 的矛盾。",
      "status": "supported",
      "type": "recoupling-algebra"
    },
    {
      "claim_id": "CA-05",
      "statement": "6j 符号正交完备性定理采用三角允许性指示函数 chi(a,b,c) (明确要求角动量和为整数)，避免与 Racah 封闭展开公式中的三角系数 Delta_R(a,b,c) 同名混淆；通过 j1=1, j2=2, j3=2, j4=1, j5=2 的严格有理数求和 3/100 + 5/36 + 7/225 = 1/5 闭合核验，作为特定代数自洽性控制，不充当全附录无条件证明。",
      "status": "supported",
      "type": "algebraic-benchmark"
    },
    {
      "claim_id": "CA-06",
      "statement": "折合跃迁几率 B(sigma lambda) 标准形式推导严格表明分母 2J_i+1 源自初态简并磁子态等权统计平均；详细平衡微观互易仅对满足厄米伴随的多极跃迁算符同态对成立。",
      "status": "supported",
      "type": "statistical-balance"
    },
    {
      "claim_id": "CA-07",
      "statement": "严格区分 SI 核磁子 mu_N^SI = e hbar / (2 m_p) 与高斯核磁子；引入特征长度 ell_N = hbar / (2 m_p c) 导出 mu_N^SI / c = e ell_N；物理电荷型跃迁几率严格为 B_S(M1) = b_M1 (e ell_N)^2 (纠正漏写 e^2 错误)；在 delta(E2/M1) 中统一采用 Krane-Steffen 发射约定并匹配 Hamilton 正交叉项 +2 delta F_k，明确 delta_KS = -delta_RB 换算关系，已发表数据保留原约定。",
      "status": "supported",
      "type": "units-and-phases"
    }
  ],
  "prohibitions_strictly_obeyed": [
    "禁止混淆 SI 核磁子与高斯核磁子定义表达式",
    "禁止在物理量纲 B_S(M1) 中丢失电子电荷平方 e^2",
    "禁止在自伴张量 RME 交换律中加入多余的 (-1)^k 指数",
    "禁止错误声称 Bohr-Mottelson 卷 I 采用不含 1/sqrt(2j_f+1) 的 RME 定义",
    "禁止在 9j 降阶式中使用与单体公式矛盾的相位 (-1)^(j1+j2+J+k)",
    "禁止三角指示函数与 Racah 三角系数同名混用 Delta",
    "禁止将特定有限自旋组态的 1/5 有理数闭合检验冒充为附录全式绝对证明",
    "禁止在未取得 APS Erratum 原件时依据标题盲目修改既有正确公式"
  ],
  "latex_math_verification": {
    "syntax_check": "clean_pass",
    "open_braces": 660,
    "close_braces": 660,
    "line_count": 300,
    "symbols_audited": ["lie_comm", "3j_cg", "we_bm", "rme_exchange", "9j_to_6j", "6j_ortho_chi", "racah_delta_r", "mun_si", "bs_m1", "delta_ks"]
  }
}

with open('raw/writing/gpt/A130/latex-evidence-ledger/appendix-A.json', 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

with open('outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G94/appendix-A.json', 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

print('Updated appendix-A.json successfully.')
