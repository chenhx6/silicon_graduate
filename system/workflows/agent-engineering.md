---
type: system-workflow
graph-excluded: true
---

# Agent 开发、审查与验收

适用于通用开发、工具配置、界面核查和可复现的小实验。先写清用户可观察的结果与必要的验证，再查现有入口、调用方和测试。依次评估配置、现有实现、标准库和少量新代码。维护明确的兼容性、输入、错误和数据契约。借用已有用法时核查副作用及适用范围。

## 隔离与提交前核对

并行任务先用 `git worktree list --porcelain` 核对工作目录与分支。交接记录任务、工作树、基线提交、改动范围和最后一次验证。修改共享文件时检查实际暂存内容。已有 App 工作树和 `team` 按各自入口办理隔离及交接。发布继续走 `check.md` 的 Git 规则。

针对 Python 审查，可以用语法树寻找调用点、检查改动涉及的定义，并保留普通 Git diff 用于审阅：

```bash
python3 system/scripts/agent_checks.py calls subprocess.run system/scripts/literature_learning.py
python3 system/scripts/agent_checks.py compare tmp/before.py tmp/after.py
```

`calls` 匹配写在源代码里的调用表达式。单个名称可命中同名方法，完整路径可收窄结果。动态绑定与导入别名仍按调用关系人工或用现有工具检查。`compare` 报告 Python AST 是否一致和顶层定义增删改。模块级语句变更也会使整体 AST 不同。Git diff 仍用于检查注释、文档和其它语言。

## 保存原日志，只读取任务上下文所需的片段

```bash
python3 system/scripts/agent_checks.py capture literature-tests -- \
  python3 -m unittest system.tests.test_literature_learning
python3 system/scripts/agent_checks.py find tmp/agent-checks/RUN/receipt.json 'Ran tests'
```

`capture` 执行显式给出的命令，保留合并的 stdout 和 stderr、退出状态、原始输出哈希及短预览。原件保存在 `tmp/agent-checks/`。命令参数如需用于复现，由任务记录按权限保存。`find` 用本机 SQLite FTS5 临时索引已校验的日志，按词检索并返回行号。缺少 FTS5 时可直接用 `rg -n` 查同目录的 `output.log`。发布前按需要回查完整错误块。

## 用固定输入验收并比较迭代

```bash
python3 system/scripts/agent_checks.py evaluate \
  tmp/agent-checks/RUN/receipt.json tmp/expectations.json
```

期望清单是 JSON，例如 `{"exit_code": 0, "contains": ["OK"], "excludes": ["Traceback"]}`。`stdout_json` 可给出必须匹配的顶层字段。验收可对已保存结果重复运行，回执同时记录原结果和期望清单的哈希。完成结论以本轮针对当前改动得到的退出状态和断言为依据。

需要优化表现时先固定输入版本、成功指标、不可退化的条件和时间或调用预算，保存基线，再逐次比较候选。正式比较使用改动过程没见过的样本。一个候选即便通过训练样例，也要在相同预算的留出样本上核查，已有的 `arbor` 可管理多假设试验。原结果、失败记录与采用理由保存在适当的任务回执中。

## 回看原页与用户旅程

- 文档定位完成后，用 [PDF 版面定位](literature-learning.md#按问题定位原页)保留原件页和坐标。对双栏、表格与图注，按原件的实际版面核对阅读顺序、列头、单位和注释。
- 界面改动按实际用户旅程验收。终端中用已可用的无头 Playwright 查看本地页面，通过角色和可访问名称定位元素，检查动作前后的状态，必要时保存截图和控制台错误。DOM 更新后重新定位元素。保留可复现的输入。示例是点击 `page.get_by_role("button", name="保存")` 后用 `expect(page.get_by_role("status")).to_have_text("已保存")` 断言真实结果。

## 固定来源与本地适配

下表各行均核读了链接所指文件。SHA-256 对应该文件。本地工具采用对应的设计，自行实现。

| 固定来源 | 采用的办法 | 源文件 SHA-256 |
| --- | --- | --- |
| [Ponytail · MIT](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail/SKILL.md) | 先找足以解决问题的现有入口，再选最小完整改动 | `9badd22a32e19cb884e46dfa8d3aae82bb81dfa5484105b8b4f0262df823a509` |
| [RTK · Apache-2.0](https://github.com/rtk-ai/rtk/blob/3b97a8715c222bcdab2d57d6f7c61db6efcbb088/src/cmds/git/git_cmd.rs) | 先读短输出，保留完整日志和退出状态 | `3edf9463a438704ff2c12083895f6965a5db5b8c4bb3c592aaa7f2ec5c021634` |
| [Context Mode · Elastic License 2.0](https://github.com/mksglu/context-mode/blob/a0e429558100c41fba1bb91be852da23c3423a90/src/core/store/fts.ts) | 借鉴 FTS5 按需找命中行，在本机对回执日志建临时索引 | `acee87ca5d38e2a1206be7e12f3f22b084e7c5f7f17c2446c8ef16c63c39d4f3` |
| [Promptfoo · MIT](https://github.com/promptfoo/promptfoo/blob/fbd8e7e69680fa7361856c8177aa968bff7157a3/examples/eval-standalone-assertions/asserts.yaml) | 用版本固定的断言检查已保存结果 | `989acef031d93a35ac0492aeeadba7a8d9c7c6c3cebfd215f7870c791b483c3b` |
| [ast-grep · MIT](https://github.com/ast-grep/ast-grep/blob/8a92260ad4b65cf4b716518a76b919e6f0d051b8/crates/cli/tests/scan_test.rs) | 先查语法结构中的真实调用，再检查实际语义 | `e727fdfb04df546d0ca01b5ce9902988448abce8d8bbcb07a9d510a043d45e7f` |
| [Worktrunk · MIT 或 Apache-2.0](https://github.com/max-sixty/worktrunk/blob/862ea96f9a55a75068987790104eddfb04fae5e0/skills/wt-switch-create/SKILL.md) | 交接明确绑定任务、分支和工作树 | `5f360f44cd20bd7b3f6610c74c0c9b7c0c045b1012887d0a1f73651336b11bdf` |
| [Superpowers · MIT](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) | 按本轮实测退出状态和断言报告完成 | `2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3` |
| [gstack · MIT](https://github.com/garrytan/gstack/blob/a26529ac8eb2c55a458058cbca428374318b370b/qa/SKILL.md) | 按用户旅程复现并验证状态变化 | `ddd4da85169ecfec0638e2b726de6a84cc11460b737e6818979c4173cd500b57` |
| [autoresearch · 固定树中未找到许可证](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) | 仅借鉴以固定预算和相同指标比较候选的实验思路 | `86cf987a5c381e46eefe0d0a82765223fd766d8d7acdc2afacfbbce15ecacece` |
| [Docling · MIT](https://github.com/docling-project/docling/blob/f93ee6bc72717da7384389434d90fbb1977047df/docling/pipeline/standard_pdf_pipeline.py) | 区分文本内容与原页几何，用现有 Poppler 取文本块位置 | `a374a5fb14f5d0754fbaa4de9db4dd3f03f026b92c10788ca08c4b31ee250578` |
| [agent-browser · Apache-2.0](https://github.com/vercel-labs/agent-browser/blob/4605d82cfc20dbd051f57a631b5b7130e32141a5/skills/agent-browser/SKILL.md) | 按页面语义定位、操作并验证更新后的状态 | `7d46deeb0101e84f8d70fd2e5cd18e3b6017edfb973607ff23e95e22c92ce73e` |
| [Difftastic · MIT](https://github.com/Wilfred/difftastic/blob/4b834ef576fa17920468372165f9938e2dc46596/manual/src/diffing.md) | 对比 Python 语法树与定义改动 | `7057531bc7fbe6845b7540a4314adc4e87cde3d19a5bbd64ce1f7a194206ba6b` |
