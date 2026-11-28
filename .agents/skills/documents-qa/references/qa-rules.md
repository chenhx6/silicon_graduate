# 检查与验收

## 增量入口

`documents_qa.py` 是只读检查器。增量检查处理 staged、unstaged 和未忽略的新文档。全库检查读取 Git 维护的根目录文档、`.agents/skills/`、`knowledge/`、`system/` 和 `outputs/` 中的 Markdown 与 LaTeX，跳过 `raw/`、缓存、临时目录与标记为生成物的文件。

| 规则 | 检查范围 |
| --- | --- |
| `ENCODING`、`BEL`、`CONTROL_CHAR` | UTF-8 严格解码及位置。U+FFFD 需对照原件。 |
| `TEX_FRAGMENT_A` | 字面 `\a` 碎片，保留 `\alpha` 和 `\approx`。 |
| `MATH_UNCLOSED`、`MATH_UNOPENED`、`MATH_NESTED_DOLLAR`、`MATH_BRACE` | 常见数学定界符与分组。围栏、行内代码和 HTML 注释作为 Markdown 上下文处理。 |
| `TEX_TAB_ESCAPE`、`TEX_DOUBLE_SUBSCRIPT` | 查找有 TeX 上下文的制表符残片和明显的连续下标。 |
| `TABLE_HEADER`、`TABLE_ROW` | 直接核对源码列数，可发现解析器已丢弃的内容。核对单元格内容归属。 |
| `MATH_RENDER` | `--render` 调用 Pandoc，用 GFM 的源位置定位无法转成 MathML 的公式。用户宏和实现差异需按目标渲染器核对。 |

`UserPromptSubmit` 保存本轮 Git HEAD 和原有脏文档的内容指纹。`Stop` 检查本轮实际变动的文档，也覆盖本轮已经提交的文档。遇到诊断会给 Codex 返回行号并要求修复，最多继续两轮；超限时在 `tmp/documents-qa/hooks/` 给出完整清单。Hook 只做快速结构检查。新会话需按 Codex 的项目信任流程确认项目 hook。手动运行同一检查器不依赖 hook 信任。测试入口为 `python3 -m unittest system.tests.test_documents_qa -v`。

## 社区工具与适用边界

- `markdownlint-cli2` 通过 glob 或精确路径调用 `markdownlint`，支持依配置增删规则、自定义规则和输出 formatter。`MD056`/`MD058` 以 micromark 已识别的表格为输入。头行错列时可能没有表格节点。用已安装的 CLI 和[精简配置](.markdownlint-cli2.jsonc)做旁路检查。初始化或 hook 不需要 Node。

  ```bash
  markdownlint-cli2 --config .agents/skills/documents-qa/references/.markdownlint-cli2.jsonc --no-globs README.md
  ```

- `unified`、`remark`、`remark-gfm` 和 `remark-math` 可保留 AST 节点的源码位置，把 `code`、`inlineCode` 与数学节点区分开。对缺少闭合符的流式数学，解析器有时仍生成数学节点，有时仅生成正文。边界诊断仍要回到源码。GitHub 的 `cmark-gfm` 表格夹具适合对照转义、超列及整表退化为段落的情况。
- KaTeX 的 `renderToString` 支持 `throwOnError` 和严格选项，MathJax TeX 输入支持格式化错误的回调，两者的宏、扩展和支持命令不同。`rehype-katex`、`rehype-mathjax` 适合已有 rehype 流程。本库已有 Pandoc/XeLaTeX，按目标使用 GFM/MathML 和最终 PDF，避免让日常检查额外加载 JavaScript 渲染栈。
- ChkTeX 可辅助找原生 LaTeX 常见排版错误。`pre-commit` 的变更路径过滤值得复用，项目已由 Codex 的本轮钩子处理增量。`mdformat` 等重排工具适合独立的格式迁移。本库历史文档修复以最小 diff 为准。

## 最终渲染

Markdown 选代表文档按 GFM 实际渲染，检查数学节点和表格的行列及关键文本。可访问已发布 GitHub 页面时，再核对其 MathJax 显示。Obsidian 扩展需要用本地阅读视图另外确认。仅有离线渲染时应标明。

交付 PDF 或修改重点公式文档时沿用原模板、编译命令、中文字体和数学字体。已有 Pandoc 环境可用以下命令检查适用的 Markdown。

```bash
pandoc --from=markdown+wikilinks_title_after_pipe --columns=72 --standalone --to=latex \
  -V fontfamily=fontspec -V mainfont='DejaVu Serif' -V monofont='DejaVu Sans Mono' \
  -V CJKmainfont='Noto Serif CJK SC' -V mathfont='Latin Modern Math' \
  INPUT.md -o tmp/documents-qa/preview.tex
xelatex -no-shell-escape -halt-on-error -interaction=nonstopmode \
  -output-directory=tmp/documents-qa tmp/documents-qa/preview.tex
```

按编译日志再运行 XeLaTeX，直至表格列宽、目录与引用稳定。用编译日志核对缺字、未知命令和溢出。用 `pdffonts`、`pdfinfo` 和 `pdftotext -layout` 核对字体嵌入、页数和关键文字。抽看公式、表格和分页页面，发现字形缺失或内容被裁切时修复后重编。保留原生 LaTeX 项目的已有编译和验收流程。
