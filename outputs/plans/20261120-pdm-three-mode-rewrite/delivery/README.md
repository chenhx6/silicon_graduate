# multipolePDM 0.1.0 交付回执

已发布：https://pypi.org/project/multipolePDM/0.1.0/

```sh
python -m pip install multipolePDM
pdm-gui
```

- 秘书手册：`raw/writing/pado/20261029_review_v1/PDM/main.pdf`（26页）；同目录保留可维护TeX及Python数据图。
- 程序与Notebook：`raw/code/PDM/GUI/`、`raw/code/PDM/analysis/`。
- 完整开源源码包：本目录 `multipolePDM-0.1.0-source.zip`，MIT许可，含analysis和示例，不包含私人工作簿或出版社原件。
- 153项测试、4项Xvfb测试、真实PyPI安装后的三模式GUI自测通过；从源码包解压后的三个Notebook亦执行通过。
- 文献比较覆盖偶偶、奇A、奇奇各两个核；PDCO仅一个实测核。点几何／理想环假设、不吻合结果、读图与校准局限完整保留，不计为完整阵列重放。
- Windows/macOS原生未测；本次使用已批准的Linux Docker虚拟GUI验收。PyPI方式需要已有Python，不是原生解压免安装程序。
- 未指定独立软件Git远端，因此未推送软件仓库；完整源码包是已约定的交付替代。不把整个Wiki作为软件仓库发布。

`acceptance.json`、`pypi-readback.json`、`software-results.json`、`source-manifest.json`及 `validation-logs/` 保存实际证据；0.1.0的逐项验收保存在本目录 `0.1.0-task-ledger.json`；上一级 `tasks.json` 维护当前新一轮优化计划，不能用本发行完成状态替它验收。静态绘图脚本启发式不能识别导入样式和外部验收包装，逐项解释见 `figure-static-resolution.json`；实际PDF字体、碰撞和面板对齐检查通过，没有将静态检查写成全绿。
