#!/usr/bin/env python3
from pathlib import Path

content = """
## Checkpoint139：排版印刷异常与物理证伪边界审计

这是本任务L3方法学边界审计，系统澄清在原子核结构能谱分析中如何区分排版印刷异常与真实物理反证：

### 印刷排版异常的三大判据

1. **选择律与多证据冲突（334.4 keV案例）**：若孤立表格单元违反电磁宇称选择律（如 M1/E2 连接相反宇称），而正文、能级图及线偏振测量一致给出相反而自洽的结论，该单元必定为孤立印刷字符脱漏（如正宇称 '+' 误印为 '-'），绝不能当作相反宇称的反证；
2. **多门谱质心微小漂移与闭合自洽（998.1 vs 997 keV案例）**：998.1 keV 与其打印母态（5412.6 keV）闭合残差严格为零，与另一门谱质心（5411.6 keV）的 1.0 keV 差属于多维符合谱拟合残差，属于统计/系统误差范畴，而非谱线物理身份冲突；
3. **分栏续表排版归属（934.9/966.3 keV案例）**：多栏排版跨页导致的列延续重叠属于编排假象，必须对照能级纲图（Fig. 1）确定真实母态归属（属于 Band D5 而非 Band D6 新态）。

### 实验结论边界法则

- **规则一（保留出版物原字面）**：严禁在知识库或数据库中静默改写文献打印数据，必须保留原文原貌并加以标注；
- **规则二（排版问题不可等同于物理证伪）**：严禁将出版物孤立的印刷脱漏、四舍五入残差或排版归属错误，拔高为推翻核结构动力学对称性的实验反证；
- **规则三（物理反证的排他性要求）**：推翻某一集体模式（如手征振动）必须依赖明确的物理可观测量与排他性判据（如 Checkpoint 134 建立的 225.8 keV 康普顿线偏振度正值 P > 0 判决）。

代码见 `system/scripts/day21_checkpoint139_typographical_anomaly_audit.py`，基准输出 `typographical-anomaly-scope-139.json`。
"""

p = Path("knowledge/research-notes/day21-135nd-same-input-falsification-design.md")
orig = p.read_text(encoding="utf-8")
p.write_text(orig.rstrip("\n") + "\n" + content.strip() + "\n", encoding="utf-8")
print("Appended Checkpoint 139 to design note")
