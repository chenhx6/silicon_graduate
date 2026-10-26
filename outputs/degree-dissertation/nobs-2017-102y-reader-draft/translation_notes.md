# Nobs双语阅读草稿：翻译与提取边界

此稿是Day23补充阅读的增量交付，不是已完成的全文翻译。原文138页的可提取文字已读；读完文字、索引建成、局部译文完成、图像逐一核验是不同状态。

## 当前覆盖

- 原PDF138页；PDF19=印刷p1，正文p1–113，参考p114–120，前置页另列。
- 全138页3612个native layout blocks，均有稳定ID、page、bbox和原文或embedded-image类型。原文直接来自PyMuPDF，不作OCR；有40个编号公式区域回退。曾误把图中(1379.6)/(804.7)能量当式号，已排除并移除两个误提取临时裁图。
- 262个page-local段落fragment中63个完成中文初稿，199个明确待译。除此之外，标题、图中标签、数学碎片、部分表格及前/后置原文仍有待译/不适用块；不能用63/262当全文字符翻译覆盖率。
- 69图与15表全部建立caption目录；18幅关键图表已裁图、译图注并经三张crop contact sheets复查。初裁9处漏轴标/自旋/表头边界已修正。其余66幅图表仍未裁图；部分caption native text可能因数学符号被拆分，全文block清单保留后续碎片，不伪称图注完整重建。
- 实际视觉核的源页为PDF54、57、59、60、64、83、107、109、111、113、114、117、119、123、125、129；其它122页尚未逐页视觉核验。图8.8另作放大读取logft及Iβ。
- 40个编号公式均用原页区域回退，未转写LaTeX。式号居中的自动裁图边界未逐式复核，可能含邻文或需要扩大；阅读完整式时回原PDF。公式语法验证通过不认证这些裁图都完整。

## 原文与译文

paper.md按page及S编号给Original/中文双语对。段落是页内fragment，跨页continuation、内嵌公式和source句子断行会使同一语义段分成多块；不是编辑校订过的完整段落集合。所有未进入S段落的native blocks也完整保留在该页details中，中文写明待译或未独立解释。每个native ID均有可跳转anchor。

原文层source_map.json保留原始字符和bbox。paper.md把PDF不可打印控制字符改成�以便渲染，精确原始字符串仍在JSON；带符号的图像以PDF或资产为准。公式没有猜测转写，科学符号不以模型记忆补齐。

原文中的不一致在译文保留，在notes.md单列：S0217保留0+→0−与内转换的原陈述，但不采纳为一般选择规则；S0227保留764/1090倒数问题；S0257保留结论段的路径归属反向问题。模型辅助结论的较强原语气被保留在原文译段，使用时必须阅读notes.md条件审计。

## 术语与误差

isomeric state固定译异能态；Ramsey cleaning固定译Ramsey清洗；blocked BCS译包含阻塞的BCS；prolate保留英文并译长轴形变；relative intensity必须带各自152keV或244keV归一。0−、5−、1+、Nilsson标签、keV/ns/ms等不跨核替换。

论文中的括号误差按原数保留，不把作者模型误差改写成实验CI。没有新AD/P/DCO/δ、state-separated寿命、绝对βfeeding/logft拟合；Fig8.8 logft来自重印Hill1986。独立来源、同源旧数据与模型input见notes.md。

## 可复制提取与检查命令

下面命令只写本独占tmp目录；不是Day22的producer，不运行任何既有Day22分析脚本。

```bash
python3 tmp/day23-theses/nobs-worker/build_reader.py
python3 tmp/day23-theses/nobs-worker/make_paragraphs.py
python3 tmp/day23-theses/nobs-worker/finish_reader.py
python3 tmp/day23-theses/nobs-worker/enhance_reader.py
python3 tmp/day23-theses/nobs-worker/correct_crops.py
python3 tmp/day23-theses/nobs-worker/verify_reader.py
python3 /root/.codex/skills/nature-reader/scripts/validate_reader_math.py tmp/day23-theses/nobs-worker/paper.md --source-map tmp/day23-theses/nobs-worker/source_map.json --strict
```

读取原文另外用PyMuPDF逐页get_text()，按PDF1–18、19–40、41–71、53–60（补足工具截断）、72–86、87–97、98–111、112–123、124–138等区间实际输出审读；原图以get_pixmap()写到assets后用view_image查看四张source contact sheets、PDF125放大图以及修正前后三张crop contact sheets。读取过程中无外网调用、无外部API、无原始event重分析。

首次结构检查因尚未写translation_notes.md出现一条missing link；补齐本文件后重跑。数学检查先发现非标准E2_1等式号ID；改为E001–E040并排除两条能量后，strict通过。检查日志只证明结构与语法，不代表全译/全图/科学结论通过。

所有本worker变更仅位于tmp/day23-theses/nobs-worker/；未改raw、PLAN、凭据、knowledge、review或任何Day22 producer。未执行Git add/commit/push。父代理负责后续knowledge写回、课程状态和发布。

## 已译段落ID

S0001, S0002, S0003, S0080, S0081, S0082, S0085, S0087, S0088, S0089, S0090, S0093, S0101, S0102, S0103, S0105, S0112, S0113, S0114, S0127, S0128, S0130, S0131, S0133, S0135, S0136, S0137, S0140, S0141, S0150, S0152, S0153, S0167, S0182, S0193, S0195, S0196, S0197, S0199, S0200, S0205, S0206, S0207, S0215, S0217, S0223, S0224, S0227, S0228, S0230, S0231, S0235, S0236, S0237, S0238, S0239, S0243, S0245, S0249, S0250, S0257, S0259, S0262

## 待译段落ID（此外另有非S的native块）

S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0083, S0084, S0086, S0091, S0092, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0104, S0106, S0107, S0108, S0109, S0110, S0111, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0129, S0132, S0134, S0138, S0139, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0151, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0194, S0198, S0201, S0202, S0203, S0204, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0216, S0218, S0219, S0220, S0221, S0222, S0225, S0226, S0229, S0232, S0233, S0234, S0240, S0241, S0242, S0244, S0246, S0247, S0248, S0251, S0252, S0253, S0254, S0255, S0256, S0258, S0260, S0261
