# 博士论文前置章节研究稿（LaTeX）

当前正文入口为
[Thesis.tex](these_2023_template/these_template/Thesis.tex)，
编译预览为[Thesis.pdf](these_2023_template/these_template/Thesis.pdf)。
分节正文位于工程的`Tex/Sections/`，证据台账位于本目录`latex-evidence-ledger/`。
当前研究稿已整合五章39节与附录A–F，共374个物理页。19组正文图件均由Python生成，
保留SVG/PDF双格式；3项CSV和6组有限数学控制分别说明模型与算法的适用条件。
全稿完成逐节科学核验、整稿编译与代表页视觉检查；编译结果不替代原件证据。

工作架构仍为五章39节及必要附录，见
[章节合同](../../../../knowledge/research-notes/doctoral-thesis-architecture-and-section-map-20261108.md)。
Gemini承担主体阅读、写作、Python绘图和工程修复；当前GPT会话负责蓝图、
详细任务书、关键证据核查与接受/定点返修；复杂独立推导按需交Terra。
覆盖与验收状态见`manuscript-status.json`。

新图全部由Python生成，SVG与PDF成对保存于工程`Img/`，正文引用PDF。

SVG路径属性、冻结返回稿与本任务审计载荷按精确Git属性保留原始空格和文件指纹；
Python、知识页及活动LaTeX源码仍接受普通空白检查。仅格式变化的Python代码同时核对AST不变，
生产脚本指纹随之刷新，既有数值结果的原始运行记录保持原来的身份。
图源清单为`Img/figure-manifest.json`；各图件采用的通用或专用生成脚本逐项记入附录F及清单。
构建入口为`python3 system/scripts/a130_latex_build.py`。
本次在隔离工程中完成整稿编译，再核对全部输入与当前canonical工程字节一致。
最终报告为`outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/final39/final-build.json`，
输入、45份分节/附录证据台账与PDF指纹的核对记录见同批`final39/`。
致命错误、缺失引用、越界排版、缺字及BibTeX错误/警告均为0；保留91项underfull排版提示。
实际使用的39节和19组图均直接载入，没有未完成章节或缺图回退框。
授权发布的稳定指针为`main / thesis: complete A130 nonpersonal foundations in LaTeX`，
实际commit/push结果以`final39/publication-final-receipt.local.json`为准。

`research-draft/`、`evidence-ledger/`、`frontmatter-draft.md`与HTML预览
保留为先前阶段的研究输入及历史工件，此后正文直接用LaTeX续写。
`references.csl.json`是已核书目输入；当前LaTeX书目在工程`Biblio/ref.bib`，
引用键继续采用canonical source basename，不修改用户Zotero inbox。
`review-inputs/`保存冻结返回稿，不作为当前正文或独立核物理事实源。

模板的49项原始文件已逐文件校验备份，演示内容可恢复移出活动工程。
原始模板及移出内容以字节保真的
[归档包](../_archive/20261113-A130-template-original.tar.gz)
保存，包描述见`../_archive/20261113-A130-template-original.bundle.json`；
冻结写作返回稿另有`review-inputs-20261113.tar.gz`与同名bundle描述。
逐个成员均已与未改动的本地原件核对SHA-256；这些包只供恢复和来源核对，
不参与当前LaTeX编译，也不作为独立科学证据。
另一个11月8日的旧稿归档在后续外部操作中被移除；11月13日只读核实，
17项原正文、源文件和旧PDF可按原SHA从Git历史恢复，17项编译中间产物不称已恢复。
保持用户删除现状，没有恢复旧归档或改写Git历史。

本稿只写前置非个人成果内容；未知的作者、导师、用户装置、实验数据与成果不填造。

本次有限范围是前置非个人成果研究稿，并非整部含个人成果的学位论文。尚未进行真实初学者阅读试验，未声明学校送审就绪。
