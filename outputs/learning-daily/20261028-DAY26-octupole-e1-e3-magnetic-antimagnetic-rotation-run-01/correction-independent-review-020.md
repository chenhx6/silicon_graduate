# Day26 定量纠错独立复核 020

2026-10-28；只审阅 [更正笔记](../../../knowledge/research-notes/day26-quantitative-claim-corrections.md) 与原件，不修改该笔记。`octupole-microscopic-sccm-droplet-015.py/json` 和 `amr-cadmium-palladium-systematics-013.json` 属于本地自设计算，不计作独立实验。本次另修复 018 独立笔记的 research-note 必需标题；未代替全库 lint。

## 原件与算术逐项结果

| 项目 | 复核判断 | 直接定位或边界 |
| --- | --- | --- |
| 144Ba/146Ba 的 E3 误差交换 | 更正正确。144Ba `0.65(+0.17/−0.23)`、`B(E3;3−→0+)=48(+25/−34)` W.u.；146Ba `0.65(+0.14/−0.20)`、`48(+21/−29)` W.u. | Bucher 2016 PRL 116 112503 PDF p.4 Table I/正文；Bucher 2017 PRL 118 152504 arXiv-copy PDF p.3 Table I/正文。两者打印中心相同不证明真值严格相等。 |
| 146Ba Table I 的 E1 单位与 SCCM 偏差 | 更正正确。表头统一为 `e·b^(λ/2)`，`0+→1−` E1 行 Exp `0.000223`、SCCM `0.00474`，因此幅度比 21.2556、同方向强度比约 451.8。`0.000223` 不是 `e fm`：换算为 `0.00223 e fm`。表中标记 `a` 表示先前数据约束，不能归给此次独立 E1 测量。 | Bucher 2017 PDF p.3 Table I、其下 `earlier work [7–9]` 与本次 E1 γ 线说明；表头/注脚直接目视与文本核对。完整联合协方差未取得。 |
| 97.1% 与逐核素带符号分项 | 撤回科学认证正确。BU17 提供的是 SCCM 占据机制与模型中的正→近零→负趋势，未提供 015 的逐核素质子/中子分项；实测强度取绝对平方也不能确定 D0 符号。 | Bucher 2017 PDF pp.3–5、Fig.4/5；015 Python `compute_droplet_vs_shell_cancellation` 的权重与系数为本地设定。 |
| 015 的生产 HWG/绝对强度与 85.9% | 更正正确。015 JSON 两核 `ME1`、`ME3` 和对应 `B` 均打印为 0.0；`85.93%` 来自设定高斯范数核，BU17 只写 `very large overlap`，没有此数值。015 将截去小范数本征模后的矩阵嵌回原维数，再对整个矩阵取最低本征向量；这会引入零空间候选，因此输出还需在保留的 natural basis 中重算。这个数值病因是**代码风险判断**，尚无完整本征谱诊断，不写成唯一已证根因。 | 015 Python `solve_hwg` 和 JSON `parity_projected_hwg`；Bucher 2017 PDF p.4 Fig.4 与相关正文；Bernard 2016 arXiv:1604.06706v1 PDF p.2 Eqs.(3)–(5)。 |
| E1 核局部零值推出非对角核全零 | 更正正确。$O(q_0,q_0)=0$ 不约束 $O(q,q')$，而 SCCM 跃迁是两个坐标上的相干求和；所需生产算符核未提供。 | Bernard 2016 PDF p.2 Eq.(4)，Bucher 2017 PDF p.4。 |
| “所有振动模型仅 8 W.u.” | 更正正确。8 是 015 自设对照；Bernard 2016 的 2D-GCM Table I 为 `0.460 e b^(3/2)`，正文对应向下约 25 W.u.，并非所有动态模型被一个强度排除。 | Bernard 2016 PDF p.4 Table I 与相邻正文；Bucher 2016 PDF p.4 的模型比较。 |
| 区间 Jaccard 84.8% | 算术上 $^{144}$Ba 的 $[14,73]$ 与 $^{146}$Ba 的 $[19,69]$ 交长 50、并长 59，`50/59=84.75%`。更正把它降为区间几何量是对的；但它不能替代两次拟合的联合似然、后验或静态/动态形状判决。 | 两篇论文报告的各自 $B(E3)$ 区间；未取得联合 covariance 或 likelihood。 |
| 3qp–5qp 的单体 E2 零定理 | BCS 反例成立：$|\Phi\rangle=u|0\rangle+v|12\rangle$、$|2qp\rangle=-v|0\rangle+u|12\rangle$，$\langle2qp|q(n_1+n_2)|\Phi\rangle=2quv=0.96q$（$u=0.8,v=0.6$）。加三旁观 qp 后仍非零。若将 $q(n_1+n_2)$ 解释成 E2 的一个轴向单体分量，应明确选 $j\ge3/2$ 且该时间反演对的 $Q_{20}$ 对角元非零；此代数例**没有**给定 $^{135}$Pr 的 good-$I$ 约化 E2。 | 标准 Bogoliubov 代数；Garg 2015 PRC 92 054325 PDF p.7 的 3qp/5qp 是 TAC 组态指认，非零定理的原文依据。 |
| MR 比值与交叉 | 更正边界准确：2015 原文明确无本带寿命和绝对 $B(M1)$，Fig.7 比值仅至约 $35/2^-$；后段缺 crossover，因此不能以比值判 crossing 之后的趋势。交叉约 $33/2^-$、0.37 MeV 是作者/TAC 解释。2019 erratum 正文仍未核。 | Garg 2015 PDF pp.7–8，Figs.7–8、正文及结论。 |
| 宇称位移公式 | 代数正确：若 $E(I)=aI(I+1)$，简单邻点平均给 $-a$；加权式 $[(I+1)E(I-1)+I E(I+1)]/(2I+1)$ 恰好还原 $E(I)$。应对奇自旋负宇称态与相邻偶自旋正宇称态明确使用同一约定；不同惯量、位移定义或混带时“零”不再是普适刚度判据。 | 本任务解析代数；010 逐核能量未经原表核验，仍为未认证输入。 |
| AMR 横向与纵向磁矩 | 理想镜像双刃的**横向**磁矩相消，纵向 $2g_hj_h\cos\theta+g_pj_p$ 一般非零；公式中的 $g_h$ 必须说明为穴的有效磁旋比/符号约定。纵向静磁矩不等于准许带内辐射 M1。若讨论时间反演，应限定定向有电流的内禀转动图像；一般 good-$I$ 实验态是否为时间反演本征态另需量子态分析。 | 对称矢量代数；Roy 2011 的经典两粒子加转子模型，PLB 694 pp.323–325 Eqs.(1)–(6)。 |
| 同壳双穴上限及 110Cd 强度 | 同种 $j=9/2$ 费米子占不同 $m$，最大 $M=j+(j-1)=8$，所以纯 $(g_{9/2})^{-2}$ 的 $J_{max}=8\hbar$，经典 `2j=9` 不是严格量子上限。Roy 原 Table 1 的 110Cd 五个 $B(E2)$ 值确为 `0.14(1),0.12(2),0.11(2),0.09(3),0.06(2) (e b)^2`；p.326 明说最高 $28^+$ 似乎非 AMR。013 JSON 模型列首尾 `0.116→0.011`，故“完满再现”不成立。 | Roy 2011 PDF p.324 Table 1、p.326 Fig.4 讨论；013 JSON `BE2_model`。中间模型点也应逐点核对，不能只凭端点宣布拟合优劣。 |

## 额外核查：018 对 Gaffney 数值的身份

直接目视 Gaffney *et al.*, *Nature* **497**, 199–204 (2013) 本地原 PDF 第3页（期刊 p.201）Table 1：$^{224}$Ra 的 `$\langle0^+\Vert E3\Vert3^-\rangle$` 行，在 `|m.e.| (e fm^3)` 栏为 `940 ± 30`，同一行的向下 $B(E3)$ 为 `42 ± 3` W.u.。原 PDF 第4页（期刊 p.202）Table 2 才给内禀 `Q3=2520 ± 90 e fm^3`。因此 018 将 940 用作约化矩阵元的身份正确；其 `Q3=\sqrt{16\pi/7}\,940=2518.9` 只在声明的轴对称转子约定内成立，也与 Table 2 的舍入中心相符。此数值身份已由原图核对，不依赖 source 页转述。

018 的先前文字把“E3 单独固定 $R$，再令共同权重变化”的不相容误写成单通道方程普遍无解。已在 018 脚本/JSON/笔记中显式求解 $D=w e|c_1|R$ 与 $Q_3=2we|c_3|R^3$：对 BU17 的打印中心，$R=219.84$ fm、$w=4.46\times10^{-5}$，数学上有解；该距离约为示意核接触距离 $8.17$ fm 的 $26.9$ 倍。018 现仅在核尺度局域距离和同一跃迁权重前提下指出点团簇模型失败，并将 $w$ 与通道概率 $S_\alpha$ 分开。

## Egido–Robledo 1990 正文获取账本

Crossref 识别目标为 Egido & Robledo, “A self-consistent approach to the ground state and lowest-lying negative-parity state in the barium isotopes,” *Nuclear Physics A* **518**, 475–495 (1990), DOI `10.1016/0375-9474(90)90141-8`，PII `0375947490901418`。Crossref 同卷给一个 `Erratum` DOI `10.1016/0375-9474(90)90192-O`（p.801）；**两篇正文均未取得或阅读**，不得拿原文或勘误为当前壳贡献数值背书。

- `nature-downloader` 此次以 `--no-si`、DOI 和指定目录尝试正文，返回状态为 `credentials_missing`；其 OA fallback 为 `oa_not_found`，见本目录外的 [获取清单](../../literature-acquisition/day26-egido-review-020/manifest.json)。此次调用没有核验 SI/必要附件清单，附件可用性未知；正文亦未取得。该调用状态不能推断整个容器的凭据配置。
- Crossref 入口 `https://doi.org/10.1016/0375-9474(90)90141-8`；其 Elsevier API text-mining 链为 `https://api.elsevier.com/content/article/PII:0375947490901418?httpAccept=text/xml`。本轮直接 API 请求返回 HTTP 200、`text/xml`、1852 字节的**元数据 XML**，含 DOI、PII、题名和 `openaccess=0`，没有正文；不能因 HTTP 200 把它当全文。
- OpenAlex 对 DOI 回 `is_oa=false`、`any_repository_has_fulltext=false`，无 PDF location；Semantic Scholar 标 `CLOSED`、`openAccessPdf.url` 为空。ScienceDirect `https://www.sciencedirect.com/science/article/pii/0375947490901418` 返回 HTTP 403，未进行权限绕过。
- INSPIRE 以 DOI 查到同题元数据，但记录中没有 `documents` 正文链接。Google 搜索入口本轮 TLS 握手失败，未取得可核验候选链接；这些检索失败不构成论文不存在开放副本的证明。
- 正文文件：**未取得**；正文格式签名：无（无 `%PDF` 或可读 full-text XML）；正文页数：未验证（Crossref 的 475–495 是编目页码，非实际读页）；正文 SHA-256：无；实际正文阅读覆盖：0 页。获取目录中只保存 downloader manifest，不保存受限网页或把元数据伪装为正文。

## 审计结论

更正笔记的撤回方向和主要原件数字得到支持。需保持的细节边界为：BCS 反例要说明 E2 分量的轨道条件；AMR 的纵向磁矩不等于辐射 M1，也不自动决定实验态的时间反演性质；015 的伪零模是待本征谱诊断的代码风险。Egido–Robledo 正文缺口仍在，不能从其书目信息恢复有符号偶极分解或绝对壳修正数字。
