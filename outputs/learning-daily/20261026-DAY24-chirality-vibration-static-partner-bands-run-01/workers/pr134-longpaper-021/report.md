# 134Pr Tonev2007 长文：三条新路线后正文仍未取得

**结论：正文 0 页。** 已核准目标身份，但未获得可读正文、PDF 或作者稿。不建立 τ/B/BR/ICC 表，不确认它与2006短文是否同一采集，也不判断其对 mixing / dynamic chirality / shape 解释到底作了怎样的修订。

## 已核准身份

**D. Tonev et al., “Question of dynamic chirality in nuclei: The case of 134Pr,” Physical Review C76,044313(2007)**，DOI **10.1103/PhysRevC.76.044313**，Crossref publication date **2007-10-17**。作者表包括 G. de Angelis、S. Brant、S. Frauendorf、P. Petkov、A. Dewald、F. Dönau 等。

Fresh exact-DOI Crossref 返回 HTTP200 JSON，12714 bytes，SHA256 **78b71f6573aacd6ec0909e1a79840360d0bfbdd59abe5bcd975081ea77a0bb63**；OpenAlex exact-DOI record 返回 HTTP200 JSON，47100 bytes，SHA256 **b8c095fddac0c6e0dd64fc588c5a4939bcd19b653c1331b945b81c0781550ee2**。两者一致支持题名/DOI身份，**不作为正文科学证据**。

本次 scoped Wiki 查询未找到该题名/DOI的既有 source 页面；raw 文件名查询未返回 Tonev/044313/dynamic-chirality 对应文件。这不是对全仓库未命名文件的穷尽证明。

## 严格限额内三次新正文入口

| 次数 | 有依据的新路线 | 实际结果 |
|---|---|---|
|1|Crossref 登记的 APS fulltext 入口：`https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevC.76.044313/fulltext`|HTTP **401**, application/json,66 bytes；正文为目标 DOI not authorized。SHA256 **f692b64a0397ed55a6b9fd7f07c9175e06cb809c8c381387bf4a5a85490fdf52**；非PDF|
|2|OpenAlex 指出的 HAL 记录，以 exact DOI 的结构化 API 查询 fileMain/files/外链：`in2p3-00180827v1`|HTTP **200** JSON,422 bytes；只有指向 `http://prc.aps.org/abstract/PRC/v76/i4/e044313` 的外链，未返回 fileMain_s/files_s。SHA256 **243eeb396d0c27a33b38d3a2a68b840520fce8db867af13164258ab1b802566f**；非正文|
|3|OpenAlex 指出的 Camerino 机构记录：`https://pubblicazioni.unicam.it/handle/11581/457046`|HTTP **403**, text/html,5438 bytes；“Just a moment… Enable JavaScript and cookies to continue”验证页。SHA256 **8e2ce9dfd07647586440cb0ad1e9788f7ef9ac400a4f08a4ea77aeedb751d22e**；无PDF/正文链接|

每条只请求一次。没有循环重撞这些入口，也没有重复 Tonev2006 的旧失败页面或尝试绕过访问控制。未进一步猜测 PDF URL；三次正文路线后停止。所有响应均无 `%PDF` 签名，文件用 `.response` 保存，不伪装为 PDF。

OpenAlex 的 OA 字段列 green / any_repository_has_fulltext，但其显示 URL 是 APS 旧摘要地址，实际请求未取得正文。**OA 标签不等于本次完整下载成功**，也不能据当前失败宣称世界上没有合法可访问副本。

## 仍 unknown 的科学对象

| 对象 | 本轮状态 |
|---|---|
|实际正文页/图/表/公式|**0 /0 /0 /0**|
|τ、BR、ICC、初末态绑定、normalizer、side feeding 与误差关系|unknown，不构造数表|
|2007 与2006 的 campaign、events、寿命数据复用或新增测量关系|unknown；共同作者/引用不足以确定|
|两带混合与 chiral vs shape 解释的真实变化|unknown，不能用题名“dynamic chirality”补写作者结论|
|作者稿/accepted version/VoR 的正文版本身份|未核|
|新的独立实验次数|**未增加**；不按2006/2007两篇发表计两套独立数据|

Crossref 参考文献字段中有 Tonev2006 PRL96,052501（Ref20）与 Petrache2006 PRL96,112502（Ref21）。这只确定了可检的**书目连接**，没有建立正文中的数据共享说明或具体反驳/修订内容。

## 可交回 root 的下一项既有源可解析问题

本路线已经停在 body0，不再给另一个泛搜/下载循环。现有可解析节点是 **Petrache2006 的两带混合定义与比较对象**：

- printed112502-2/3 的 Eqs1–5、Table I，先区分 yrast/nonyrast 标签与未混合原配置身份，再区分它给的 allowed Q ratio1.6–2.4 与 Tonev 的直接寿命 B 值。已有 PE06-D21-R45 已完成这项关键纠错，root 可在 Day25 三核矩阵直接复用其边界，不把它当新 δ。
- printed112502-3/4 明确其寿命结果来自 Ref9、分支来自另一个当时待出版 Ref11。未来若有**新且明确的本长文副本或最终 Ref11 身份**，再检正文是否真正闭合这些输入；目前不把 PRC76,044313 自动认作 Ref11 或新的独立采集。
- Day25 比较可以如实保留：134Pr 的理想伙伴解释受到现有 primary 混合/EM分析的挑战，但动态手征残余/shape竞争的最终裁决仍需所缺原件与输入；Nd 的既有正支持不因 Pr 的正文缺口而降为不存在。

## 回执与执行边界

`receipt.json` 汇总 exact URLs、HTTP、content、bytes、SHA、0页状态及三次限额；各 JSON 保存独立响应记录。只写 `tmp/day24-pr134-longpaper-021/` 与本 worker prefix；canonical/raw/PLAN/Bib/Git、session、课程学分不变。仍 same Day24 run 的 Day25 无学分 preview，未读 Day26、未运行114或未知代码。此报告只有身份/访问/缺口信息，没有新增正文科学 claims。
