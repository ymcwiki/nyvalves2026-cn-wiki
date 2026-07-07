# CRF New York Valves 2026 中文知识库

本仓库是 **CRF New York Valves 2026（The Structural Heart Summit）** 会议公开报告的中文整理与知识图谱，覆盖经导管主动脉瓣（TAVR）、二尖瓣（TEER/TMVR）、三尖瓣（TTVR/T-TEER）、左心耳封堵、瓣周漏封堵等结构性心脏病领域的最新试验、器械与病例。

内容全部为**文字**：逐场报告的中文转述稿，加上从中抽取的实体 / 概念 / 来源知识图谱。**不含任何原始幻灯片、PDF 或图片**。

## 🕸️ 交互式关系图谱

**[▶ 打开在线知识图谱](https://ymcwiki.github.io/nyvalves2026-cn-wiki/)** —— 4,598 个页面、35,032 条链接的力导向图，可拖动、缩放、悬停看名字、点击聚焦邻居、搜索定位。橙=实体、蓝=概念、绿=来源，节点大小随连接数变化。

图谱数据由 `scripts/build_graph.py` 从 `wiki/` 的 `[[链接]]` 生成，页面在 `docs/`（GitHub Pages）。

## 内容构成

| 目录 | 数量 | 说明 |
| --- | --- | --- |
| `sources/` | 862 篇 | 每一场报告的详细中文整理，保留讲者、数据、表格与关键结论 |
| `wiki/实体/` | 1486 页 | 器械、试验、机构、人物等实体页，含定义、别名与来源反链 |
| `wiki/概念/` | 2250 页 | 术语、方法、影像/评估流程等概念页，附相关概念互链 |
| `wiki/来源/` | 862 页 | 每篇来源的摘要页，链接回对应实体与概念 |
| `wiki/index.md` | — | 全库索引，按被引次数排序 |

知识图谱采用 [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 模式：页面间以 `[[wiki 链接]]` 互连，可直接用 [Obsidian](https://obsidian.md/) 打开 `wiki/` 或整个仓库浏览与检索。

## 怎么用

- **浏览**：从 `wiki/index.md` 进入，按最常被引用的器械 / 试验往下钻。
- **读全文整理**：`sources/` 下每个 `NNN-*.md` 是一场报告的完整中文稿。
- **Obsidian**：把仓库作为一个 vault 打开，即可用图谱视图和双向链接导航。
- **检索**：全部是纯文本 Markdown，`grep` / ripgrep 直接搜。

## 来源与版权

- 整理内容基于 **CRF New York Valves 2026** 的公开会议报告，讲者幻灯片与原始数据版权归各讲者及 Cardiovascular Research Foundation (CRF) 所有。
- 本仓库为对公开报告的**中文演绎与结构化整理**，供学习与学术交流；**不含原始幻灯片 / PDF / 图片**。
- 讲者联系邮箱等个人信息已从文本中隐去。
- 医学内容仅供专业参考，不构成任何诊疗建议。

如任何讲者或权利方希望调整或移除相关内容，请提 issue。

## 许可

本仓库整理性文本以 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 授权（署名 — 非商业 — 相同方式共享）。原始会议报告的版权不受此许可影响，仍归原权利方所有。
