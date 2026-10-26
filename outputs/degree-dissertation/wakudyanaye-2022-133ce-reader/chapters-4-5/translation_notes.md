# 第4–5章reader翻译与提取说明

## 覆盖

范围明确为用户提供论文的PDF51–74（印刷40–63），包含Chapter4/5全部实际正文段落、标题、7幅图的完整图注、5张表的完整表注和6个编号公式。表格数值与公式按委派要求采用原件裁图回退，未把表格行总结成文字代替原表。跨页段落合并显示，并在source_map保留每段所有页与PDF文字block坐标。

只有本次指定两章完成，非全130页翻译完成。图表按首次实质讨论插入；PDF65–71等纯图表页提供回链页锚。引用[数字]保留原顺序，未拓展为已核新引用。

## Source map

每个S/C/F/T/E块有稳定ID、PDF页/印刷页、原文与译文、source_segments或bbox、图表关系；source_segments中的PDF_text_block_indices_zero_based明确为PyMuPDF文本block序号。图片bbox以PDF points为单位，2.5倍渲染；旋转仅为便于阅读，不修改原数字。Original经NFKC连字/空白规范化和英文行末断词拼接；数学排版必要时只恢复上标、上下标及行内数学定界，原始重排文本也保留在JSON。

## 不确定性与审计

本地未发现可用pdf skill文件，因此使用已验证的PyMuPDF文字层/坐标提取，不做OCR；nature-reader静态规则、figure extraction、equation handling与output spec均已读取。

公式回退没有LaTeX转写，原件图为权威；不因裁图代表高可信图像而认证公式物理正确。图内数字、表格单元格未另作中文重排；表头和全部caption已翻译。正文不改语法、数值或逻辑疑点，独立审计集中在paper.md末尾；包括式4.1文本提取位置的澄清、装置配置、iTL先后措辞、δ定义、M1+E2条数、870/871门标签和Table5.3原标签。

未读取用户独立事件数据、未改raw/canonical/PLAN/Git、不联网、不派生agent。

## 验证

构建命令：python3 tmp/day23-theses/proposal-worker/reader-ch4-5/build_reader.py。
数学检查采用nature-reader/scripts/validate_reader_math.py，范围为Markdown定界/源映射/图片路径，不替代科学审计。最终检查结果另存validation_math.json及coverage_receipt.json。
