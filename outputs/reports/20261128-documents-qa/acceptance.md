# documents_QA 验收记录

2026-11-28。入口为 [documents_QA](../../../.agents/skills/documents-qa/SKILL.md)。[逐文件修复清单与诊断](audit.json) 包含初始和结束统计、全部修复路径、待核对的原文位置、GitHub GFM 和 PDF 样例结果。

## 本地结果

| 检查 | 修复前 | 修复后 |
| --- | ---: | ---: |
| 字面反斜杠 a 碎片 | 318 | 126 |
| 表头或数据行列数 | 219 | 31 |
| 数学定界符及大括号 | 94 | 0 |
| 双下标 | 61 | 17 |
| 疑似 Python 制表符转义残片 | 48 | 36 |
| BEL | 7 | 0 |
| 其它字符诊断 | 24 | 24 |
| 合计 | 771 | 234 |

同一版检查器比较 3,753 份原有文档。新规范文档另行检查。修复 210 份既有文档，其中技能资料 89 份、知识库 100 份、输出 20 份、系统文档 1 份。修复了卢希庭第 1 章和入口的近似号、对称能下标、β 稳定线和块公式布局，以及 γ–γ 符合表格的错列。保留物理数值、各原文采用的参数和历史科学判断。未修改原始材料。部分先前损坏源自 Python 解释 `\a`、`\t`、`\n` 等转义，修复依据是现有文字、可判断的命令残片及相邻公式。

待核查项包括交接及追加式历史日志中的旧残片、OCR 原文字形、证据表列归属或缺值，以及需用目标渲染器或原件确认的宏和公式。对修改过的文档追加了 Pandoc MathML 检查，余下 84 条渲染诊断见 JSON。该列表同时包含可能兼容于其它渲染器的式子。此次仅调整可确认的排版和结构。

## 工具核验

- 试跑 `markdownlint-cli2` 0.24.2 / `markdownlint` 0.42.2。六个样例中，MD056 定位多列，MD058 定位表格前缺空行。JSON formatter 证实本样例中 MD056 没提供修复，MD058 提供了插入空行的修复。错表头、未知 TeX 命令及缺闭合符需要其它检查。该 CLI 配置可选，日常 hook 只用 Python 和 Git。
- `unified` 11、`remark` 15、`remark-gfm` 4、`remark-math` 6 和 micromark 4 试验返回带位置的代码、表格和数学节点。对未闭合的流式块，`remark-math` 仍生成数学节点。KaTeX 0.19.1 的 `throwOnError` 和 MathJax TeX 3.2.1 的 `formatError` 都检出未知命令，并都能渲染上述未闭合块的内部数学。核对了 `rehype-katex`、`rehype-mathjax` 的适配代码，并对照 GitHub cmark-gfm、GitHub 的 markdownlint 配置、ChkTeX、pre-commit 和 mdformat 的适用范围。
- Codex CLI 0.172.0 的 `hooks/list` 识别了 `UserPromptSubmit` 与 `Stop` 两个项目 hook，配置无错误。实际 Git 测试覆盖无文档改动时跳过、原有脏文件不纳入本轮、检测本轮提交、修复后放行和两次失败后输出清单。当前客户端把新 hook 标为 `untrusted`，首次自动执行仍遵循客户端项目 hook 信任流程。
- GitHub Markdown API 返回 HTTP 200。修复后的公开样例返回一个列表内独立数学节点、一个行内数学节点和四个表格数据单元格，代码里的字面竖线完整保留。反例缺少数学节点且代码单元格内容被截断。只向该 API 送了合成样例。GitHub 页面上最终由客户端绘出的数学，本轮以本地 MathJax 对照，未逐一核验每份仓库文档的挂页。
- 实际用 Pandoc 3.1.3 和 XeLaTeX 编译卢希庭第 1 章（1 页）、技能入口（3 页）和 γ–γ 符合笔记（4 页）。检查字体嵌入、标题、上下标、列表内公式、四栏表头和重点页面。宽表用 Pandoc 的列宽布局，XeLaTeX 重跑稳定表头。三份终版日志均无未知命令、缺字或盒子溢出。预览在 `tmp/documents-qa/pdf/`。

## 可追溯来源

- [markdownlint-cli2 0.24.2](https://github.com/DavidAnson/markdownlint-cli2/tree/d4df4cec471ce155946474590d7b95920f623ccb) 与 [markdownlint 0.42.2](https://github.com/DavidAnson/markdownlint/tree/92992da11c2da77f8c4261378563098f3dc77f80) 均为 MIT。CLI 入口、MD056 与 MD058 的 SHA-256 分别为 `df2b3d35cb9d1719886bbb261d8af2dfe0dcc3382f33b20fc5ed6d45889004fd`、`58f10d6332c7c178b122cb6cc9d07143a92bf3528d6e714aa7a1264dec163180` 和 `68d3f394cb852706fba787f6a455a3ea3dbf0768020fbc04b161ca19bcbd0e58`。
- [Codex 0.172.0 hooks 线协议](https://github.com/openai/codex/tree/3d86e43b075adeba2193ec5c22ac92f55afd82e6/codex-rs/hooks/schema/generated)。[GFM 规范](https://github.github.com/gfm/) 和 [GitHub 数学表达式](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)。[Pandoc 手册](https://pandoc.org/MANUAL.html)。
- [remark-gfm](https://github.com/remarkjs/remark-gfm)、[remark-math 和 rehype 适配器](https://github.com/remarkjs/remark-math)、[KaTeX API](https://katex.org/docs/api) 和 [MathJax](https://docs.mathjax.org/)。相关源码样本、npm 锁定文件、测试输出和报告草稿集中在 `tmp/documents-qa/`。
