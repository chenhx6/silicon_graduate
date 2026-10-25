# Day23 checkpoint021：goodI协变约束后做band-mixing/完整EM块readiness

原run2026-10-25-day-23-01/session01a172fd-cbfb-7a13-b715-cfa0c479e08e，deadline2026-10-26T15:00:00+08、run_date仍25，goalactive/Farmer2698；completed=[] partial=[23,24] next23，Day24仅一张无学分preview、Day25不开，正式credit仅Day23。仍11h+持续，原15:00后才收束。raw/PLAN/Bib/旧review/credit/114隔离producer不动。

021先modelcontract，新day24_preview_covariant_partner_tensors.py：goodI1/2,3/2,5/2,7/2每个×2multiplicity共40维，H在各I/alpha为标量identity，rotational/T/C invariant；alpha能量不同、M/Kramers简并仍在每irrep内。完整rank1/2 tensor由WE/real2x2RME和reverseR=(-1)^(Ii-If)R^T构，核[Jz/J±,T]、sphericaladjoint、timeparity（rank1magtimeodd/rank2electric timeeven）、Ccovariance、CGsumB/detailedbalance、rank1非generator等47controls过，max3.4e-15。C=-K此basis，C²1不强制谱学两alpha相等。

注意这全是abstractrepresentations/tensors，没核素/handedgeometry，不能认证实际onebody核EM可任意RME。两case改变了tensor而非固定operator只改configuration：同/反三步曲率符号只是数学例，非universalstaggering或newphysicalg。specialrealL/R kernel M=aI+bσx有B±∝(a±b)²，若a≠0、|b/a|<=eps<=1则差商abs<=2eps/(1+eps²)。eps是未知EMcrosskernel界，不从小energygap或旧QtproxyCI推定，不赋核参数。sourceF01-D24P-003、LKH82-D24P-002/3和concept新增needs_reviewtrue，旧humanreviewflags保留。实际Mu07pattern+TAC/RPA支持不因抽象例抹掉。

freshboundary/lint/diff/tensor0、true报告/30changed知识writebackvalid，lint0error220warning/182citation债务；currentpub指针main · Day23: distinguish rotation symmetry from partner-strength dynamics；actualH3/hash看task-publication-receipt021。

下一sameDay24preview具体问题：bandmixing还是basisrelabel？对于同I/If+同parity、固定完整2stateprojectors和固定operator，R->Uf†RUi不改Frobenius/ΣB(共同2Ii+1)或singularvalues；但若只有4个B模，仍缺loop相位/符号，不必确定det/singularvalues。可先合同/2x2明确unitary controls，不呼physicalmodel，新案例不赋等可信。**sumB不是sumΓ**，Eγ不同/初态不同的rates不可借此闭合；若真实configmix漏到pair外/多于2states，closedblock不成立。基底变换同时变H和T不改任何物理，真实statemixing固定T改变H（可isospectral但不是只标签）；角色要分开。

已实际定向读Bark2024rawPDF7/8（32pages非新全读），SH A46e19f9654d4e966638757c7e71fdb6fd0ff8800a039e356eb0f6ee60b552f3d；文字强调realisticmodel六最低带不能简单按E配对，需尽可能多band/qp几何/decaypatterns。只secondarymodel证据，不转新实验。tmp/day23-originals/bk24-p7/8-022.png已渲染但本轮尚未看图像（文本读完）。若用它支持closed2state边界，source需明确targetscope/non-fullread，不复用其数字作实际135Nd数据。

实际IAEA135NdCSV018又只读查询missing四cell：candidateA31/2idx55->B29/2idx56 ΔE中心−130.7keV（upward，逆向+130.7），A33/2idx60->B31/2idx59 +1.4keV，A35/2idx63->B33/2idx61 +125.6，A37/2idx68->B35/2idx66 +254.0。forward/inverse四组均无行出现在此cutoff2008snapshot，**不是experimentalupperlimit/zeroB**；idx56B29/2 half_life空、Mu07TableB从31/2开始，逆向B/lifetime/IC也缺。若构completeM1 block，firstclosedgamma不能设B0，只能绑定inverseRME/其它信息；detailedbalance带spinweight，1.4中心不能无Cov认证确有放光/IC可达。CSV在tmp/day23-originals/iaea-nd135-*-018.csv，实际读levels/gammas不依赖旧output绿标。

020normalizationcompoundhypothesis、019authorPS精度、018WU/clock/lineidentity、017antiunitary以及Day23Pr/Au校准/SH26支持全保；旧QtCI/225.8P/机时撤回不恢复。不机械重跑producer、不Day25、不日终早停。
