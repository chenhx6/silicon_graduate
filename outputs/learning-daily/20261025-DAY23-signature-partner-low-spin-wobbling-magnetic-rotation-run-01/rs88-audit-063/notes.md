# Ragnarsson–Semmes 1988：有界形式体系核验

直接来源：I. Ragnarsson and P. B. Semmes, *Description of Nuclear Moments and Nuclear Spectra in the Particle-Rotor Model*, **Hyperfine Interactions 43 (1988), 425–440**。本PDF有2页front matter；PDF3–18对应文章425–440。哈希见 `source_manifest.json`，与父任务给定SHA匹配。

本批全文读/视觉核的是PDF5–10（427–432）；为核物理/拉伸坐标补读PDF4（426），为父代理新增正反模型例子定向读PDF17–18（439–440）。PDF3仅取身份文本。**不声称本worker读完16页文章**，全文主线由父代理负责。未扩新来源、未获取作者代码、未改canonical/raw/outputs/PLAN/Git。

## 源上直接结论

**核芯自旋与总自旋分开。** 427 Eq11清楚写Hcore=ΣAi Ri²=ΣAi(Ii−ji)²，Ai=ℏ²/(2Ji)。这是标准角动量以ℏ计的写法；具体代码单位仍须另核。Eq12采用体固连3轴量子化；作者明说体固连I+、I−分别降低、升高K，不能照搬实验室系升降算符的直觉。Eq13是D2对称化的强耦合BCS基。这里的时间反演态相位由Eq9指定，不可换相位而不改矩阵元。

**R依赖惯量靠重耦合。** 427末承认直接使用Eq13形式不便给不同核芯自旋R设不同惯量，随即引入R²为好量子数的基Eq14；428 Eq15通过两基重叠，把核芯本征能ERα重新装入强耦合表象。作者称这允许任意core-energy参数化，并称单奇粒子实现刚完成（Ref10当时to be published）。这不是用Ai(I)取代Ai(R)的同一操作，也不是整个odd-odd版本已完成相同实现的证据。

**pairing与ξ不是同一个因子。** 427 Eq13下正文写single-particle matrix elements乘UU′+VV′，并说有时用ad hoc ξ乘off-diagonal single-particle matrix elements。428 odd-odd末段对质子、中子分别采用其配对因子，并再次引入off-diagonal ξ。不能把ξ当成对整段H、对全部磁/电算符的普遍缩放；本段没有给作者程序逐条缩放实现，尤其j²项/一次单粒子矩阵元的代码选择不得补猜。

**stretched basis不等于physical operator。** 426 Sec2.1末三段说lt按拉伸坐标定义；拉伸基壳间耦合小，但物理算符在physical(spherical)系统表达，转到拉伸基求矩阵元繁琐，细节回Ref1。球形坐标用δ、γδ、δ4，与ε、γ、ε4不同。四极项可对应，十六极势形状不完全一样；令δ4和ε4取同一个数一般不是最佳形状匹配。作者把用球形l代替lt的差别称多数情况下可能很小，未说严格恒等。

**odd-odd有独立Vpn。** 428 Eq16–21把p/n各自时间反演伙伴纳入，轴对称时对应K=Ωp±Ωn；三轴时仍区分来自相应product的奇/偶K扇区。429 Eq22是有限程高斯、中心/自旋/空间交换/张量结构，Eq23的张量定义为[(σp·r)(σn·r)/r²]−(σp·σn)/3，保留其1/3约定，不强行用常见3倍定义替换。Eq24/25的Vpn配对A/B由四个U/V乘积组成，**不等于**单奇粒子UU′+VV′一个因子。对全部已占据轨道的额外求和被作者归为核芯贡献并丢弃。u0通常不影响Newby shift和同一partner对的GM splitting，但不同p-n组态的对角元可不同，因而仍可移动不同组态带头。

**电磁链尚未给全代码级归一。** 429 Eq26用约化矩阵元定义B；Eq27给M1的core+odd-particle形式，Eq28给E2积分。430 Eq29给√0.7 Eγ乘E2/M1约化矩阵元比；Eq30/31给静态μ/Qs的约化矩阵元与3j投影因子。M1/E2显式矩阵元仍回Ref1；本批没取得Ref1原文或作者producer。不能仅凭本PDF把球张量相位、μN、有效电荷、单位换算和多体矩阵元归一全部宣称闭合。只从B值得|δ|，得不到相位符号。

**参数不是普适自由输入。** 430 Sec2.7：standard Nilsson κ/μ来自Ref7，局部精细拟合有小调整；pairing parameters来自Ref14，在其方法里Fermi level与BCS gap是derived quantities；此处应用的惯量取Grodzin关系；只有明确说明时才用ξ<1。gs取free-nucleon的70%，gR=Z/A，coreQ微观计算。单奇粒子保留10–15个形变轨道并称收敛，odd-odd通常各4个p/n态并判断截断影响可忽略。这是作者对具体计算的收敛声明，不是对新133Ce模型无条件保证。gs=.7与Ce学位论文另处采用.6必须分别保留；本worker没有在此batch重新读取thesis的.6所在页，不以父消息替代该页的独立核验。

## 同一模型必须保留正面与反面

431的Ho应用已经展示配置/形变/ξ变化可改变排序：157Ho需ξ=.8使7/2最低；155Ho的5/2不能由强烈attenuation到.4的h11/2带解释，转向[402]5/2配置，并讨论Nilsson参数修订对费米面和Qs的影响。162Ho的负宇称带采用ξ=.7才再现更高自旋。它们是作者模型比较，不是新取得的独立实验。432 Fig2显示158Ho有/无Vpn时带排序和混合变化，作者在431归纳其主要作用为约50–100keV的配置相关位移，通常附加混合不大；不能推广到任意核素。

439 Table2与正文的185Au例子尤其值得保留：原表来源明确observed /28/，这里不是新采集实验。

| 185Au跃迁 | 源报B(M1)实验(n.m.)² | 计算(n.m.)² | 源报B(E2)实验(e²b²) | 计算(e²b²) |
|---|---|---|---|---|
| (9/2−)1→5/2−(g.s.) | 空白 | 空白 | 1.25±.12 | 1.50 |
| (7/2−)1→5/2−(g.s.) | (1.5±.7)×10⁻³ | 3.5×10⁻² | (.29±.14)，原表带括号 | .13 |
| (7/2−)1→(9/2−)1 | (1.1±.5)×10⁻² | 3×10⁻⁵ | 空白 | .10 |

作者称到5/2基态的跃迁大致再现，9/2→5/2的大E2提供形变信息；但7/2→9/2实验被判为M1而模型近乎纯E2，作者据此指出这些态可能不能如此简单描述。因此不能只保留模型对谱/部分E2的符合度而忽略磁算符反例。未补空白数据、寿命或CI。

439 Table3给另一组**模型特定的可检验分歧**：strong-coupled prolate h11/2，ε=.24，内部ΔI1序列13/2→11/2、15/2→13/2、17/2→15/2、19/2→17/2，其δ分别+.256/+.259/+.260/+.262；oblate h9/2，ε=−.16，序列11/2→9/2、13/2→11/2、15/2→13/2、17/2→15/2，δ分别−.72/−.71/−.69/−.70。它们是各候选带内部的模型连接，不能因为上文讲feeding而把Table3默认成两带间连接。作者称强Coriolis attenuation及偏离轴对称至20°时相关结果基本不变；没有参数扫描网格或误差域，不把文字“stable”改写成统计鲁棒界。

Table3后语境讨论oblate h9/2 feeding oblate h11/2与cross-talk，但原文确写“calculate the intraband transitions”，随后说B(E2)≲.001e²b²和B(M1)≲.001n.m.²及大ΔK。该指称存在语境张力，本笔记保literal，不静默改interband，也不把此数字分配给未逐条指定的实际观测。所有这些都是185Au；不得迁成187Au连接线的观测、δ或模式判定。

440 Ref28= C. Bourgeois et al., Nucl. Phys. A386 (1982)308；Ref33=V. Berg et al., Nucl. Phys. A410 (1983)445。它们在此仅是源列依赖，未读直接原件，不把同实验后续模型重复引用计独立票。Ho实验背景来自Refs18/19且有prepublication/private communication成分；缺这些直接producer时保留来源边界。

## 仍缺的作者producer／实现合同

没有取得此版作者可运行源代码、版本commit或原始包、GAMPN/ASYMO/PROBMO输入输出、矩阵元表、实际基截断列表、相位/排序约定、完整Nilsson/pairing参数表、g与Q/EM单位约定、R重耦合实现及Vpn径向积分程序。本文430给了部分参数方案但不是完整运行manifest；本文440还感谢Hans Frisk提供Vpn代码，不代表代码随文章公开。Ref1（1978）、Ref10（当时待刊）、Ref11（1976残余力）均未在本batch取原文。本次可完成source/claim self-audit和条件代数蓝本，不能称“作者QTR producer重现完毕”。这些是当前研究证据边界，不自动转为用户待办。

实际视觉证据：assets/pdf05–10.png、补充pdf04/pdf17/pdf18；`crop_manifest.json`列关键公式/参数/表格裁图。原OCR保存在pdfXX.txt供检索，但所有以上关键数学/数值均回视觉检查，不以乱码确定符号。
