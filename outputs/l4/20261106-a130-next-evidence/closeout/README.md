# 2026-11-06 中文阶段汇报

打开 [a130-stage-report-20261106.pdf](a130-stage-report-20261106.pdf)。
12页主体、2页附录，中文16:9，适合10–15分钟。阶段结论见
[brief.md](brief.md)，口头汇报可用[speaker-notes.md](speaker-notes.md)。

可编辑源码为[同名TeX](a130-stage-report-20261106.tex)。图件由
[make_figures.py](make_figures.py)从冻结JSON/CSV重绘；原件与长期知识
路径见[evidence-ledger.md](evidence-ledger.md)。图件输入哈希在
`figure-inputs.json`，逐页布局与编译结果在`layout-check.json`。

编译环境使用本地Tectonic/XeTeX、ctexbeamer、DejaVu Sans与
WenQuanYi Zen Hei字体。其它机器应安装这些字体，或在TeX中显式替换后
重新检查排版。在本目录可执行：

```bash
python3 -B make_figures.py
mkdir -p build
/workspace/wiki/tmp/tectonic --outdir build --keep-logs --keep-intermediates a130-stage-report-20261106.tex
```

也可用支持相同宏包与字体的XeLaTeX两遍编译。`build/`和`rendered/`仅是
本地检查目录；交付PDF与生成图件均位于本目录和`figures/`。

该报告关闭本次阶段，未宣称全库阅读或投稿准备完成。英文10页稿仍是
新控制／新限制整合前的候选版本，状态见其
[收束说明](/workspace/wiki/raw/writing/gpt/odd-ba-quadrupole-closure/analysis/closeout-20261106.md)。
