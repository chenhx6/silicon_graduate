# 2015阻塞规则：量化前预测

2026-10-15T18:20:50.127375+08:00，已受Zhao2015 arXiv1506.08340v2全文13页、Figs1–5及PDF5 normalized U/V、O1/O2段落priming。当前Day14/partial15，原formal21/24不改。PDF SHA ce3c7672420b07e9bbe7d7a869049771c5cef9aa64f4dffce5dfd18bcb0b3c21。

源规则按字面分别最大化O1=〈ψu,ψu′〉+〈ψv,ψv′〉与O2=〈ψu,ψv′〉+〈ψv,ψu′〉；O1大则继承k1′ blocking，O2大则反转k2′ blocking。文中未把相位处理、严格相等、并列最大值或零norm的分支写成代码。这不说明实际实现欠缺，只说明公开表达式不足以逐位重放。

下一构造一个实的canonical BCS双态：U=uI、V=v[[0,−1],[1,0]]，声明u²=.7/v²=.3，验证canonical条件再用源归一/规则。预测same-state control继承、particle-hole swap反转并保持相应blocked density；整体qp符号−1保持ρ/κ和blocked density，但字面signed scores可能出现与原相位不同的tie/decision。绝不默补abs或认为作者代码直接用了本脚本。

再以同一positive-qp子空间实正交旋转测试：小角可following，45度并列需tie policy；零V分量令源归一未定义，不能输出随意轨道。这些不代表实际Pr136或135Nd发生了该失败。若展示abs-score/phase alignment，只作为声明的替代控制，仍要保留与源字面不同且不能唯一解near-degenerate identity的边界。目标是列出最小replay contract，而不是把算法不明确升级为代码错误。

## 扩展前检查：旋转的eigenbasis合法性

2026-10-15T18:29:02.949157+08:00：首42-check通过后，为避免把任意canonical旋转直接称为eigenstate following，下一补一个声明E=1的BdG矩阵，验证正能双态严格简并、U/V为其eigenvectors，子空间旋转仍是合法eigenbasis。此为所选实简并极限，不是源TAC实际谱；同时使用ρ与κ共同校核particle-hole reference变换，不能只看meanN或ρ。
