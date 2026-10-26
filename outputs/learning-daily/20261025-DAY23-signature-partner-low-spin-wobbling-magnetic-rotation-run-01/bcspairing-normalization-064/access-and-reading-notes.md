# Larsson–Leander–Ragnarsson 1978：访问审计与RS88替代解析

目标：S. E. Larsson, G. Leander, I. Ragnarsson, “Nuclear core-quasiparticle coupling”, Nuclear Physics A 307(2) (1978)189–223，DOI10.1016/0375-9474(78)90613-9。

**状态：书目身份已核，1978正文未取得，1978正文实际阅读0页。** 下面没有假称全文精读或把摘要升级为原论文矩阵元。合法入口本轮未给可下载正文，不等于全世界不存在合法可访问版本。

## 访问与证据层

Crossref MCP返回题名、三作者、1978、NPA307(2)、189–223及DOI，与Ce Ref40/RS88 Ref1目标一致。Lund机构两个公开记录重复确认身份及35页，提供摘要但无全文附件。摘要只作为研究scope发现，未用作1978具体EM/BCS公式证据。

|入口|实际结果|处理|
|---|---|---|
|Crossref get_paper_by_id|元数据成功|保存metadata-mcp.json|
|MCP discover_paper_access|linkinghub landing状态200，但candidateCount=0|不把200当PDF，未取得正文|
|Google Scholar MCP exact-title|一次timeout|保留错误，不重复该endpoint|
|ScienceDirect本文landing|HTTP403，HTML，非PDF|保存响应与状态，不重试|
|ScienceDirect本文pdfft|HTTP403，HTML，非PDF|保存响应与状态，不改UA/绕过挑战|
|Elsevier匿名API PDF请求|HTTP406 XML：PDF Accept restricted|不当PDF；不推断已有机构许可或实际全文可用|
|OpenAlex exact DOI|HTTP200，closed、无pdf_url/全文仓储|索引状态本身不排除其它真实公开端点，但该记录未给正文|
|Lund Research Portal|HTTP200，题名/作者/DOI/abstract，无附件|检查真实链接，只有DOI/Scopus等|
|Lund LUP record|HTTP200，同一身份，只有DOI等记录链接|没有fulltext附件，不猜存储URL|
|现有配置Semantic Scholar exact-title|一次HTTP429|不重复撞限流入口|

本地downloader配置只显示已配OpenAlex/Semantic Scholar，未配Elsevier key；没有新配置或修改凭据，没有导出cookie/登录状态，也没有构造额外机构授权。任务仅指定本篇正文，未扩SI或不定论文批次。下载内容只写本独占tmp目录；未保存任何“HTML伪PDF”，也没有1978 PDF hash。没有借RS88的Springer成功记录来推断Elsevier1978必可访问。

## 实际转读RS88原页

既有公开publisher staging文件为tmp/day23-theses/ragnarsson-semmes-1988.pdf；SHA256 af5b8588ac78f40ecb7ac5eb8f2dd8070c3457296e8fdcd63e9ea0d828a2fa6d，本轮重新计算一致，18页。

本轮定向读取并fresh visual核：

- PDF5 / 印427：Eq9的conjugate相位、Eq10的Bogoliubov operator；Eq11–13及body-fixed I+降K/I−升K；其后UU′+VV′和off-diagonal ξ段。
- PDF7 / 印429：Eq26 B定义、Eq27 core+particle M1、Eq28 E2积分/分项。
- PDF8 / 印430：Eq29 √.7 Eγ的mixing relation，Eq30/31静态矩；“explicit M1/E2 matrix elements in Ref1”，及§2.7 λF/Δ为其pairing方法derived quantities的文字。

只是这三页的有界原读，未重复声称本worker读完整16页，也没有获得Ref1显式矩阵元。源图与文字均在本目录rs88-pdf05/07/08.png/txt，定位见fallback-source.json。

## 来源到条件推导的桥梁

RS88 Eq10的符号结构为：αi†=ui ci†−vi cbar_i，αbar_i†=ui cbar_i†+vi ci；Eq9负责把barred state相位定好。下面用相同类型的Kramers相位构造一个独立16维Fock控制，核何时出现plus、何时是minus。它不是2022代码或1978公式的替代版本。

RS88 Eq26的B定义需要清楚区分full laboratory matrix element与reduced element。下面用独立3j精确平方和控制检验2Ji+1到底在何处，防止把某一个Mi/Mf矩阵元直接平方当B，或把初态平均重复除两次。

## 练习A：精确Fock空间核BCS散射因子

四个费米模式按1、bar1、2、bar2排序，creation符号由occupied lower-mode数给出。BCS真空取

$$|\Phi\rangle=(u_1+v_1c_1^\dagger c_{\bar1}^\dagger)
(u_2+v_2c_2^\dagger c_{\bar2}^\dagger)|0\rangle,$$

$$u_1=3/5,\quad v_1=4/5,\quad u_2=5/13,\quad v_2=12/13.$$

这些是人为精确有理数，占据归一但没有来自任何核素λ/Δ的假定。时间反演定义Tc_i†T^−1=cbar_i†、Tcbar_i†T^−1=−ci†；T²在奇费米子空间为−1，在真空/偶空间为+1。脚本逐项核creation/annihilation反对易、真空归一及TR保持、α湮灭BCS真空和四个one-qp态的正交归一。

分别构造T-even和T-odd的实Hermitian一体prototype：

$$O_\pm=c_1^\dagger c_2+c_2^\dagger c_1
\ \pm(c_{\bar1}^\dagger c_{\bar2}+c_{\bar2}^\dagger c_{\bar1}).$$

此处O+为时间偶，O−为时间奇。直接在完整16维Fock空间作矩阵元，得到

$$\langle1_{\rm qp}|O_-|2_{\rm qp}\rangle=u_1u_2+v_1v_2=63/65,$$

$$\langle1_{\rm qp}|O_+|2_{\rm qp}\rangle=u_1u_2-v_1v_2=-33/65.$$

这独立支持RS88 core角动量散射段plus因子相位结构，并显示不能把其plus因子原样搬给一切时间偶的粒子电算符。prototype没有指定完整球张量rank，实际q分量/相位仍要按真实tensor规则恢复；**不声称“所有E2输出只乘minus因子”，更不把整个core+particle E2一起缩放。**

对角时间偶算符还要分开BCS真空/core贡献。选N1=c1†c1+cbar1†cbar1：

$$\langle\Phi|N_1|\Phi\rangle=32/25,\qquad
\langle1_{\rm qp}|N_1|1_{\rm qp}\rangle=1,$$

$$\langle N_1\rangle_{\rm qp}-\langle N_1\rangle_{\rm vac}
=u_1^2-v_1^2=-7/25.$$

若直接拿完整qp期望1当“配对后的单粒子电矩阵元−7/25”，就混入了真空/core背景。相比之下，时间奇n1−nbar1的qp期望为u1²+v1²=1。

此控制仅涉及指定一体算符的one-qp散射块；Bogoliubov变换还会产生pair creation/annihilation项，其它态间跃迁不能忽略。也不能用本plus/minus因子决定复合j²项的代码处方、odd-odd Vpn四u/v因子或整个particle-core矩阵元。这些仍需要Ref1/actual producer。

## 练习B：reduced-B的归一检查

选标准Wigner–Eckart convention

$$\langle J_fM_f|T_{kq}|J_iM_i\rangle
=(-1)^{J_f-M_f}
\begin{pmatrix}J_f&k&J_i\\-M_f&q&M_i\end{pmatrix}
\langle J_f\Vert T_k\Vert J_i\rangle.$$

令reduced matrix element的平方为人为R²=9/4。对固定Mi，把全部Mf、q求和，应得到

$$\sum_{M_f,q}|\langle J_fM_f|T_{kq}|J_iM_i\rangle|^2
=\frac{|R|^2}{2J_i+1}=B.$$

全部Mi再求和得到|R|²；只有在对全部Mi求和时才再除2Ji+1作初态平均。对已经固定Mi的完整Mf/q和再除一次，会重复归一。

脚本通过Racah阶乘和计算3j²，保留Fraction精确值，不使用外部角动量库。另以Ji=1/2→Jf=3/2、rank1、Mi=+1/2的独立已知CG极限核q=−1/0/+1对应系数平方1/12、1/6、1/4，总和1/2。

|Ji→Jf|rank|R²|固定Mi完整和/初态平均B|
|---|---:|---:|---:|
|1/2→3/2|1|9/4|9/8|
|3/2→1/2|1|9/4|9/16|
|3/2→3/2|2|9/4|9/16|
|5/2→3/2|2|9/4|3/8|
|3/2→3/2|0（数学标量控制）|9/4|9/16|

rank0这一行仅测试数学归一，不是实际单光子γ跃迁。Hermitian tensor的正反reduced模相同，故(2Ji+1)Bforward=(2Jf+1)Breverse控制亦通过；不把不同初态的B直接当相等。

单个M或q的矩阵元不是B，只有满足该完整求和/已知tensor约定后才能对照RS88 Eq26。这里也未恢复RS88/Ce使用的有效电荷、μN/eb归一或physical-stretched坐标变换，不能拿toy R=3/2当实际133Ce矩阵元。

## 尚未关闭的输入边界

1978 Ref1的显式single-particle M1/E2矩阵元仍未读；source本文把它们指回Ref1，不能由本控制补造。body-fixed D2波函数、完整轨道/时间反演相位、physical operator与stretched basis的变换、BCS实际λ/Δ共同单位/零点、阻塞与真空core项、约化矩阵元的完整张量规范都仍需原件/actual producer。RS88参数derived λ/Δ不自动恢复Ce表中ε≈5–6MeV与λ≈50MeV的接口。

86项精确检查全部通过，只认证选定Fock及3j归一恒等式，不认证完整作者程序、物理模式、实验CI或新g/τ。脚本仅依赖Python标准库Fraction/math；运行命令：python3 tmp/day23-theses/larsson1978-worker/fallback_controls.py。

本轮未改raw/PLAN、canonical、既有review、课程学分、凭据或Git；不发布任何未取得再分发许可的正文PDF。
