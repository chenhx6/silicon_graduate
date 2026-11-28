---
name: documents-qa
description: 当用户要求编写、修改、校订、修复、预览或交付科学文档、Markdown、LaTeX、公式、表格、README、科研报告、教材或 PDF 时使用。也用于乱码、公式不渲染、表格错列、GitHub 预览和 Pandoc/XeLaTeX 编译问题。其他写作技能参与时照样使用。
---

# documents_QA

1. 读取 [Markdown 与 LaTeX 约定](references/markdown-latex-style.md)。保留科学内容、原有措辞、章节与编号，检查工作树并限定本轮修改路径。
2. 从仓库根目录运行 `python3 system/scripts/documents_qa.py PATH ...` 检查实际编辑的文档。使用 `--changed` 检查 Git 变更、`--all` 盘点维护范围、`--format json` 导出结构化诊断。Wiki 页面继续用 `wiki_lint.py` 检查知识 schema、链接和证据结构。
3. 按文件和行号修复可确定的字符、公式定界符与表格结构，核对 diff 和渲染结果。涉及符号含义、数值、单位、物理解读或无法确认的列归属时，回到原件或列入人工核查。用 [QA 规则及验收方式](references/qa-rules.md) 判断工具分工和兼容边界。
4. 每轮修复后重跑同一 QA，最多两轮。若仍有问题，给出含原始位置和原因的核查清单。项目 Stop Hook 可触发同一个增量检查。
5. 涉及数学命令或渲染时对目标 Markdown 追加 `--render`。PDF 交付复用现有 Pandoc/XeLaTeX，按参考文档核验字体、公式、表格、章节、分页。GitHub 兼容性、实际 GitHub 页面和 PDF 分别记录。
