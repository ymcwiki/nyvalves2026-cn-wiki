---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/559-tavi-pilot-robotic-valve-placement-system-carvol.md]]"
tags: [AI augmented teleoperation, VLL Location, supervised control, NCC检测]
contentHash: 811-1f527ffe
generation_complete: true
---

# TAVI Pilot 机器人瓣膜定位系统（Carvolix） - 摘要

## 来源
- 原始文件：[[sources/559-tavi-pilot-robotic-valve-placement-system-carvol.md]]
- 收录日期：2026-06-29

## 核心内容
本文介绍 TAVIPILOT，一套结合 AI、增强现实与机器人技术的 TAVI 实时定位系统，由澳大利亚 Macquarie University Hospital 的 Stephen Worthley 团队开发。系统无需额外标记物，可在透视中实时追踪 non-coronary cusp 与人工瓣位置，并在 supervised control 模式下实现自动瓣膜定位闭环。ROTAO 1 澳大利亚阶段已完成 9 例，手术成功率 100%，零并发症，平均手术时间 31.7 分钟。

## 关键实体
- [[实体/sapien-3-ultra-resilia|SAPIEN 3 Ultra Resilia]]：SAPIEN 3 Ultra Resilia 是 Edwards Lifesciences 推出的新一代球囊扩张式经导管心脏瓣膜，采用 RESILIA 牛心包处理技术，通过改进化学工艺减少瓣叶钙化并更新瓣叶悬吊机制，旨在提升长期耐久性。可用规格涵盖 20、23、26、29 mm，适用于主动脉瓣、二尖瓣及三尖瓣位置的经导管置换，支持原生瓣环植入、瓣中瓣（ViV/TAV-in-TAV）及退变手术瓣膜内植入等多种场景。与前代 SAPIEN 3/Ultra 相比，该瓣膜在 redo TAVR 中表现出更低的跨瓣压差和更大的有效瓣口面积；现有随访数据显示 2 年死亡率约 7.1%，2 年再干预率约 0.8%，长期数据尚待积累。
- [[实体/carvolix|Carvolix]]：开发 TAVIPILOT 机器人瓣膜定位系统的公司，官网为 carvolix.eu，在澳大利亚 Macquarie University Hospital 完成了首次临床应用。
- [[实体/stephen-worthley|Stephen Worthley]]：Stephen Worthley 是澳大利亚悉尼 Macquarie University Hospital 的心脏病学家，曾作为主要讲者参与 TAVIPILOT Robot 首次临床使用的报告，同时主导 SAITO 1B 澳大利亚研究。
- [[实体/macquarie-university-hospital|Macquarie University Hospital]]：Macquarie University Hospital 是位于澳大利亚悉尼的一所医学研究型医院，在多项心脏介入机器人技术的临床首创中扮演核心角色：完成了 TAVIPILOT Robot 的全球首次临床使用并主导 ROTAO 1 研究，同时也是 SAITO 1B 澳大利亚队列的首次人体应用地点。
- [[实体/rotao-1|ROTAO 1]]：TAVIPILOT 机器人 TAVI 系统的澳大利亚首期临床研究，采用遥操作机器人，适用 Edwards S3 和 S3 ultra 瓣膜，已完成 9 例，手术成功率 100%。
- [[实体/tavipilot|TAVIPILOT]]：结合 AI、增强现实与机器人技术的 TAVI 实时瓣膜定位系统，可作为独立软件或整合到机器人平台，在 supervised control 下实现自动瓣膜定位。

## 关键概念
- [[概念/ai-augmented-teleoperation|AI augmented teleoperation]]
- [[概念/vll-location|VLL Location]]
- [[概念/supervised-control|supervised control]]
- [[概念/ncc检测|NCC检测]]

## 要点
- TAVIPILOT 是全球首个 AI 驱动的 TAVI 实时 GPS，无需 markers 或 landmarks，可实时检测和追踪 non-coronary cusp 与人工瓣
- AI augmented teleoperation 定位误差分布最窄，约 -0.3 至 0.5 mm，优于手动操作和遥操作
- ROTAO 1 澳大利亚阶段：9/10 例，100% 手术成功，0 并发症，平均手术时间 31.7 min [SD 7.7]
- 2024 年完成全球首个动物机器人 TAV 递送；first-in-human 从 2025 年 Q4 开始
- 系统可作为 standalone software 或整合至机器人系统，在 supervised control 下实现从实时引导到自动定位的闭环
- 未满足的临床需求：植入深度不理想可导致永久起搏器植入、瓣周漏、冠脉阻塞和早期结构退化
