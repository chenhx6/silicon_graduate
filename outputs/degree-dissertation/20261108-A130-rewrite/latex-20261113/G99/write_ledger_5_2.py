import json, hashlib

tex_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-2.tex'
with open(tex_path, 'rb') as f:
    tex_sha = hashlib.sha256(f.read()).hexdigest()

ledger = {
  "section_id": "5.2",
  "title": "探测器与光子响应",
  "section_label": "sec:5-2",
  "worker": "G99",
  "status": "audited_and_reconciled",
  "recorded_at": "2026-11-14T02:00:00Z",
  "canonical_paths": {
    "tex": "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-2.tex",
    "ledger": "raw/writing/gpt/A130/latex-evidence-ledger/section-5-2.json"
  },
  "staging_paths": {
    "tex": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G99/sec-5-2.tex",
    "ledger": "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G99/section-5-2.json"
  },
  "output_latex": {
    "file": "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-2.tex",
    "sha256": tex_sha,
    "lines_count": 152,
    "figures_count": 1,
    "labels": [
      "sec:5-2",
      "subsec:5-2-1",
      "eq:5-2-compton-electron",
      "eq:5-2-compton-edge",
      "subsec:5-2-2",
      "eq:5-2-norm-cond",
      "eq:5-2-peak-to-total",
      "eq:5-2-eff-decomp",
      "eq:5-2-eff-geom",
      "fig:5-2-detector-response",
      "subsec:5-2-3",
      "eq:5-2-fwhm-stat",
      "eq:5-2-fwhm-quad",
      "subsec:5-2-4",
      "eq:5-2-summing-out",
      "subsec:5-2-5",
      "eq:5-2-klein-nishina-pol",
      "eq:5-2-asymmetry"
    ],
    "citations": [
      "book-wu-nuclear-experiment-methods",
      "book-hamilton-electromagnetic-interaction",
      "akkoyun-2012-agata-instrument-response"
    ]
  },
  "sources": [
    {
      "source_id": "book-wu-nuclear-experiment-methods",
      "citation_key": "book-wu-nuclear-experiment-methods",
      "canonical_source": "吴治华, 《原子核物理实验方法》（第三版）, 原子能出版社 (2005)",
      "raw_file": "raw/books/原子核物理实验方法--第三版 (吴治华) (Z-Library).pdf",
      "raw_sha256": "e23f010ff8d3b4737405235c4aba920533f44e89409ebb7e2cb076b7ab4ee591",
      "locators": [
        "第2章第4节印刷第54–65页/PDF第62–73页：γ射线与物质相互作用（光电效应、康普顿散射、电子对生成截面与逃逸峰）",
        "第5章第3节印刷第146–151页/PDF第154–159页：HPGe探测器工作原理、载流子产生与Fano统计展宽、能量分辨率微观贡献",
        "第10章第1节印刷第257–260页/PDF第265–268页：γ谱仪峰总比P/T与峰康比定义、全能峰净面积拟合提取",
        "第10章第3节印刷第278–281页/PDF第286–289页：反符合γ谱仪与BGO主动屏蔽结构、假否决机制"
      ]
    },
    {
      "source_id": "book-hamilton-electromagnetic-interaction",
      "citation_key": "book-hamilton-electromagnetic-interaction",
      "canonical_source": "W. D. Hamilton (ed.), The Electromagnetic Interaction in Nuclear Spectroscopy, North-Holland (1975)",
      "raw_file": "raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf",
      "raw_sha256": "93b32a8debb66ad036229d860ad56f0434dc49b56edd32f1628af1d71a21ae00",
      "locators": [
        "Chapter 15 §5 by P. J. Twin印刷第716–717页/PDF第727–728页：康普顿散射偏振计原理、Klein-Nishina截面方位角非对称性与散射不对称度线偏振测量",
        "Chapter 12印刷第505–558页/PDF第516–569页：核自旋取向张量与方向关联角分布理论"
      ]
    },
    {
      "source_id": "akkoyun-2012-agata-instrument-response",
      "citation_key": "akkoyun-2012-agata-instrument-response",
      "canonical_source": "S. Akkoyun et al., AGATA—Advanced GAmma Tracking Array, Nucl. Instrum. Methods Phys. Res. A 668, 26 (2012) [41-page manuscript arXiv:1111.5731v1]",
      "raw_file": "raw/papers/gpt/learning-daily/20261013-DAY13-doppler-correction-recoil-velocity/akkoyun-2012-agata-overview.pdf",
      "raw_sha256": "13882c8bb1dbebb02db5df3300f9cf5981a1ffb519b3731dab099647be168d8b",
      "locators": [
        "41页手稿PDF第1–10页：高度电分段HPGe探测器规范、脉冲形状分析（PSA）反演三维空间击中点坐标与正向径迹重构架构（设计4pi构型由180块六角晶体组成，实际在束实验按Demonstrator等子阵列运行）"
      ]
    }
  ],
  "claims": [
    {
      "claim_id": "CLAIM-5-2-1",
      "statement": "光电效应在能量高于锗K吸收边11.1 keV的给定能区下主要由K壳层贡献，空穴退激特征X射线在晶体表面或电极附近存在逃逸概率导致锗逃逸峰；远离吸收边光电截面近似遵循经验标度 sigma_pe propto Z^n / E^3.5 (Ge中n≈4-5)。",
      "status": "supported",
      "source_id": "book-wu-nuclear-experiment-methods"
    },
    {
      "claim_id": "CLAIM-5-2-2",
      "statement": "仪器响应函数在条件概率测度下严格归一化为1；总谱正交分解为净全能吸收峰分量R_FEP与其余不完全能量沉积分量R_other，峰总比定义为P/T = int_0^infty R_FEP dE，全能峰面积须通过局部本底扣除提取净面积A_peak，不能将有限窗未经本底扣除的原始总计数等同于真全能吸收概率；绝对峰效率满足 epsilon_p = epsilon_tot * (P/T)。",
      "status": "supported",
      "source_id": "book-wu-nuclear-experiment-methods"
    },
    {
      "claim_id": "CLAIM-5-2-3",
      "statement": "在77 K锗半导体典型评价与教学参考参数中，产生一个电子-空穴对的平均有效能量常取参考标称值 epsilon ≈ 2.96 eV，Fano因子取经验参考值 F ~ 0.1；电子-空穴对数目方差为无量纲数 sigma_N^2 = F N = F E_gamma / epsilon，转换到观测能量尺度的等效能量方差为 sigma_{E,stat}^2 = epsilon^2 sigma_N^2 = F epsilon E_gamma (MeV^2)，统计展宽严格为 FWHM_stat = 2.355 sqrt(F epsilon E_gamma)。",
      "status": "supported",
      "source_id": "book-wu-nuclear-experiment-methods"
    },
    {
      "claim_id": "CLAIM-5-2-4",
      "statement": "Clover探测器Add-back多通道能量相加重构总能量方差不仅包含两晶叶固有噪声，还受晶体间能量分配起伏与接触层电容串扰协方差调控：sigma_add^2 = sigma_A^2 + sigma_B^2 + 2 Cov(E_A, E_B)；纯前放电子学噪声独立时方差线性相加。",
      "status": "supported",
      "source_id": "book-wu-nuclear-experiment-methods"
    },
    {
      "claim_id": "CLAIM-5-2-5",
      "statement": "真符合相加（TCS）发生在同核级联退激中，在理想线性响应、固定立体角几何与无死时间阻塞下，单事件发生概率与放射源活度或宏观计数率无关，仅取决于分支比、级联角关联W与绝对立体角Omega；但在实际高计数率下，脉冲堆积与死时间门控会非线性改变观测相加损失。",
      "status": "supported",
      "source_id": "book-wu-nuclear-experiment-methods"
    },
    {
      "claim_id": "CLAIM-5-2-6",
      "statement": "Clover微型康普顿偏振计利用Klein-Nishina截面方位角非对称性测定散射不对称度A = (N_perp - a N_parallel) / (N_perp + a N_parallel) = Q P，参数a = N_perp^0 / N_parallel^0约定与第5.7节式(eq:5-7-asym-exp)完全一致；偏振度符号与电磁性质对应关系依赖自旋序列与放置角。",
      "status": "supported",
      "source_id": "book-hamilton-electromagnetic-interaction"
    },
    {
      "claim_id": "CLAIM-5-2-7",
      "statement": "AGATA与GRETINA跟踪阵列利用36分段HPGe晶体脉冲形状分析（PSA）反演三维击中点坐标，结合正向康普顿径迹重构（Forward Tracking）去除厚重BGO屏蔽实现高立体角探测；设计设想的完整4pi阵列由180块六角晶体组成，实际在束实验均按分阶段安装的子阵列构型运行。",
      "status": "supported",
      "source_id": "akkoyun-2012-agata-instrument-response"
    }
  ],
  "parent_review_reconciliations_52": {
    "52-1": "Hamilton专著偏振计引用定位符已严格修正为真实原页：Chapter 15 §5 by P. J. Twin，印刷第716–717页 / PDF第727–728页，彻底消除了引用PDF 355/印344的错误。",
    "52-2": "吴治华专著章节定位符已校正至真实原页 (第2章§4 PDF 62–73, 第5章§3 PDF 154–159, 第10章§1 PDF 265–268, 第10章§3 PDF 286–289)；77 K锗晶体平均电离能 epsilon ≈ 2.96 eV与Fano因子 F ~ 0.1已明确标注为文献教学与评价参考参数，删除了未经验证的F=0.08–0.12绝对范围宣称。",
    "52-3": "响应函数已按R = R_FEP + R_other严格分解，明确峰总比P/T为全能峰净积分份额，指出在有限窗未扣本底直接积分不仅截断高斯尾还会混入康普顿本底，全能峰面积须通过局部拟合扣除本底提取净计数A_peak，消除了窗计数与真吸收率等同的歧义。",
    "52-4": "光电效应明确说明在高于锗K吸收边11.1 keV时主要由K壳层贡献，澄清了特征X射线在晶体表面/死层逃逸形成锗逃逸峰的条件；载流子统计展宽清晰区分了电子-空穴对数目的无量纲方差sigma_N^2与等效能量方差sigma_E^2 (MeV^2) 的量纲转换。",
    "52-5": "Clover散射不对称度参数a = N_perp^0 / N_parallel^0与第5.7节约定完全一致；Add-back明确补充了晶叶间电荷分配起伏与接触层电容串扰协方差项2 Cov(E_A, E_B)；TCS明确阐述单事件率无关性是针对固定几何与理想线性响应区间，指出在高计数率下堆积与死时间门控会引起计数率依赖偏离。",
    "52-6": "AGATA引用严格规范为41页预印本手稿 (arXiv:1111.5731v1) PDF第1–10页，未捏造正式期刊排版页码，明确区分设计4pi 180晶体构型与实际在束运行的分阶段子阵列；图5.1注明确说明Add-back增益因子为选取的教学合成参数，声明纵轴为任意单位对数计数。"
  }
}

with open('raw/writing/gpt/A130/latex-evidence-ledger/section-5-2.json', 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

with open('outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G99/section-5-2.json', 'w', encoding='utf-8') as f:
    json.dump(ledger, f, indent=2, ensure_ascii=False)

print('Updated section-5-2.json successfully.')
