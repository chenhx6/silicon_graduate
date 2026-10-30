# 046：Bengtsson–Ragnarsson1985 身份、完整正文获取与下一读区

状态：**身份与69页PDF完整性已核；仅入口/参数表定向阅读，尚未全文阅读或认证。** 同一Day24/133Ce参数谱系问题，不授新课程学分，不推进course/session；没有写canonical/raw/BibTeX或Git。

## 身份与已有重叠

Crossref精确DOI endpoint返回200，题名/作者/刊物卷期页一致：Tord Bengtsson and Ingemar Ragnarsson, “Rotational bands and particle-hole excitations at very high spin”, *Nuclear Physics A* **436**(1),14–82 (March1985), DOI `10.1016/0375-9474(85)90541-X`（Crossref DOI大小写归一为末尾x），PII `037594748590541X`。PDF首页视觉核的刊物卷页、作者与题名一致，received1984不改写为出版年。

`knowledge/sources/`及133Ce blueprint的定向重叠搜索未发现本1985 source。已有 `ragnarsson-nilsson-sheline-1978-shell-structure.md` 是三作者1978 *Physics Reports*45,1–87的另一篇review；领域/方法有重叠，身份不相同，不能以已读1978替代本69页。已有WK22-38与blueprint分别记录κ/μ来自Ref11、程序/惯量来自其它引用路由；本次取回的是该参数候选原件，不是2022 actual参数卡或producer。

## 获取与完整性

- 使用已配置Elsevier publisher API，复用skill的`providerCredentials`读取私有配置，仅通过HTTP headers传送；没有输出/改写凭据、改外部skill或使用非授权镜像。
- 用户既有daily资源授权涵盖正文/SI，按`--si`执行本任务定向helper，不再询问。helper：`tmp/day24-bengtsson1985-046/fetch-entry.mjs`。
- 第一次：Article API `doi/...?...httpAccept=text/xml&view=FULL`，HTTP200，361,294B；XML SHA256 `b49f97724af84df03ab5ea0f46e7c7a8c3d2f3bd37fd02562417b6de8a895742`。
- FULL XML实际列出`1-s2.0-037594748590541X-main.pdf` attachment，第二次通过Object API取得PDF，HTTP200。没有再撞已知可能仅返回首页的普通DOI-PDF端点。
- 正文：`tmp/day24-bengtsson1985-046/attachment-object-response.pdf`，**4,596,459B，69页**，SHA256 **`605e785734279f1a7a6dfd234f1d3ff6b136f983b134ccf9d6b766f3b027d6b8`**；`%PDF` signature、pdfinfo有效，非加密。首physicalPDF1为printed14、末physicalPDF69为printed82均视觉核，与14–82含首尾共69页匹配；不再是仅首页对象。
- SI：FULL XML attachment inventory只见main.pdf及main_1.png，未识别mmc/supp/_si_候选；记`not_identified_in_full_xml_attachment_inventory`。main_1.png不冒作SI，未宣称所有出版商入口绝无SI。
- 无API失败、无OA fallback或browser route需求，`oa_status=not_checked_api_first`，不推断文章的全局OA属性。

实际响应与去凭据审计保存在tmp的`crossref-response.json`、`crossref-identity.json`、`fullview-response.xml`、`access-manifest.json`。全部本轮下载只落tmp；未摄入raw。

## 已读范围与参数表 locator

直接阅读PDF1的身份/abstract/首段、PDF5–6的§2.1.1与Table1上下文、PDF69末页reference；视觉核PDF1、6、69。对其余全文只作文本抽取/关键词和section-heading定位，**这不算阅读这些页**。PDF2/3等文本文件即使已提取也未记为已读；其余方法/应用/结果不能据机器命中先作认证。

**κ/μ表位置：physicalPDF6 / printed19，Table1；上文从physicalPDF5 / printed18 Eq7及§2.1.1开始。** caption字面为“which have been used in this work”，不是作者声称对所有后来计算无条件有效的常数。表头第一列印`N_rot`；上文说κ与μ依赖main oscillator quantum number N。确切rotating-basis实现、N_rot与各分类/追踪的关系须接读§2.1.2等，不把这个标签直接等同WK22某ν轨道ID。

仅为已视觉核Table1的字面索引，表值如下；不是Ce实际输入的认定：

| N_rot | proton κ | proton μ | neutron κ | neutron μ |
|---|---:|---:|---:|---:|
|0|.120|.00|.120|.00|
|1|.120|.00|.120|.00|
|2|.105|.00|.105|.00|
|3|.090|.30|.090|.25|
|4|.065|.57|.070|.39|
|5|.060|.65|.062|.43|
|6|.054|.69|.062|.34|
|7|.054|.69|.062|.26|
|8|.054|.69|.062|.26|

邻文直接说：这些参数旨在essentially reproduce所引Ref25对**rare-earth/actinide valence orbitals**的fit；较轻区特别注意Z或N=8、20、28的single-particle gaps；另要求κ/μ随N平滑变化；作者说ground-state shapes/masses的测试精度与其它Nilsson参数集相近（引Ref26）。这段只提供本文选参目标/作者测试声明，本轮未读Ref25/26或执行验证，不能自动延伸为已核A≈130实际fit或WK22 adopted values。

PDF1与PDF5还直接声明本篇**忽略pairing**，详细very-low-spin theory/experiment比较无意义，适用性留给实验比较判断。这是定向已读的明显方法边界；不是WK22含BCS参数可自动删去的理由。

## 下一轮有信息的读区 proposal

以下以机器section定位作路线，题内物理结论尚未认证；physical页+13=printed页。

1. **首先完整读PDF1–16 / printed14–29。** §2“Calculational technique”从PDF2起；§2.1 single-particle PDF5起（含Table1、rotating basis、Nilsson实现及Figs2/3）；§2.2“Removal of virtual interactions”PDF11起；§2.3“Choosing occupied orbitals”PDF14起；§2.4“Calculation of total energies”PDF15起。这能真正核κμ表如何进Hamiltonian、形变/轴/space、fixed configuration与crossing追踪、能量计算。不能仅有Table1就选参数。
2. **完整读applications/continuum段PDF17–46 / printed30–59。** heading索引指向§3 continuum-type quantities；§4 187Au的collective/aligned两coupling schemes；§5 terminating bands；§6 continuum spectra与effective moment of inertia；§7 coincidence/J^(2)相关量。目的是识别direct experiment、作者解释与计算对象，避免把高spin方法名当低能QTR输出。
3. **完整读discrete-state/general段PDF47–66 / printed60–79，再核PDF67–69 references。** 特别值得优先定向看**§8.4 `130Ce`，physicalPDF60 / printed73起**，邻PDF61进入§9。当前仅通过heading与首页abstract定位，有直接Ce质量区比较价值，但本轮未读此段，不能先称其支持或反驳WK22。其它Yb/Hf/Ta段与no-pairing/general限制也应读完再定全source边界。

若父任务按完整原件分工，以上三区可作为不遗漏全文的reading units；必要共享页保留显式重叠。本单元不自行派发，不因取得全文或读完Table1即授分。

## 不得由本入口回执推出的内容

- 不能由historical Table1反推WK22实际选用哪一行、是否修改某shell参数、νID、完整basis/截断、ε/λ的共同能量零点或negative λ。
- 不能把CNS no-pairing high-spin Hamiltonian、configuration追踪、gamma-axis convention或total-energy式自动等同WK22 GAMPN→ASYMO→PROBMO。
- 未读正文的application、bandcrossing方法、Ce结论或全部限制仍未认证；本单元只关闭身份/完整获取与Table1精确入口。

停止在父任务要求的entry gate：完整资源已可供下一阶段阅读，尚无全文source总结或课程状态变更。下一动作由父任务确定完整读分工，而非再向用户索要正文/SI。
