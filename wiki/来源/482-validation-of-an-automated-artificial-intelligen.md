---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/482-validation-of-an-automated-artificial-intelligen.md]]"
tags: [组内相关系数, Bland-Altman 分析, 多层螺旋 CT (MSCT), 3D U-Net, 主动脉根部 sizing]
contentHash: 752-d31ef573
generation_complete: true
---

# 自动化 AI TAVR 规划器的验证 - 摘要

## 来源
- 原始文件：[[sources/482-validation-of-an-automated-artificial-intelligen.md]]
- 收录日期：2026-06-29

## 核心内容
本研究在鹿特丹 Erasmus MC 纳入 126 例连续患者（含 50% 复杂解剖），前瞻性验证全自动 AI 软件 Mimics for TAVR 相对半自动 3Mensio 的测量准确性。结果显示主动脉根部各参数 ICC 均超过 0.90，AI 对面积有轻度低估（约 -1.9% 至 -5.0%），但经导管瓣膜尺寸选择一致率约 90%。Mimics 平均分析时间仅 1.03 分钟，约为 3Mensio 的九分之一，显著提升工作流效率。

## 关键实体
- [[实体/erasmus-mc|Erasmus MC]]：Erasmus MC 是位于荷兰鹿特丹的伊拉斯姆斯大学医学中心，其下设 Thoraxcenter 为高容量三级介入中心。该机构开展了多项心脏介入研究，包括在 conductance catheter 血流动力学监测下实施的专用 TAVR 手术。
- [[实体/navitor|Navitor]]：Navitor 是 Abbott Structural Heart 推出的自膨式经导管主动脉瓣（TAVR）系统，采用高框架设计，具备大冠脉窗口和主动密封裙（Active NaviSeal cuff），可用于原生瓣膜狭窄及 TAV-in-TAV 等复杂场景。临床数据显示其血流动力学表现良好，术后平均跨瓣压差通常在3–8 mmHg 区间，重度患者-假体不匹配（PPM）发生率约7%。与 SAPIEN 3、Evolut FX 同为当前主流 TAVR 平台之一，常用规格涵盖25、26、27、29 mm，偶有支架不完全展开或瓣膜迁移等并发症报道。
- [[实体/mimics-for-tavr|Mimics for TAVR]]：Mimics for TAVR 是 Materialise 公司开发的全自动 TAVR 术前规划软件，基于 3D U-Net 深度学习架构，直接从 DICOM 数据生成患者特异性主动脉根部三维模型并自动完成关键解剖测量。软件支持多种瓣膜 sizing 方案，与 3-MENSIO 等参照软件具有高度一致性，并通过网页界面提供实时访问能力。
- [[实体/3mensio|3mensio]]：3mensio 是荷兰 Pie Medical Imaging 开发的心血管 CT 后处理专用软件，支持三维重建及多种结构性心脏病手术（TAVR、LAAC 等）的术前 CTA 规划，可自动或半自动分析主动脉瓣环平面、钙化分布、房间隔穿刺位置及透视投照角度。多项研究将其作为人工测量的参照标准，单次分析耗时约 9.55 分钟。
- [[实体/l-uchoa-de-assis|L. Uchoa de Assis]]：Erasmus MC Thoraxcenter 心脏病学研究者，本研究主要讲者，专注于 AI 辅助 TAVR 规划验证。

## 关键概念
- [[概念/组内相关系数|组内相关系数]]
- [[概念/bland-altman-分析|Bland-Altman 分析]]
- [[概念/多层螺旋-ct-msct|多层螺旋 CT (MSCT)]]
- [[概念/3d-u-net|3D U-Net]]
- [[概念/主动脉根部-sizing|主动脉根部 sizing]]

## 要点
- Mimics for TAVR 基于 3D U-Net，用 449 份 CT 训练、200 份验证，网页界面可实时访问
- 126 例连续患者，50% 为复杂解剖（重度钙化 30 例、小瓣环 14 例、二叶瓣 12 例、失败生物瓣 7 例）
- Annulus area ICC 0.976，LVOT area ICC 0.970，STJ area ICC 0.953，几乎所有参数 ICC >0.90
- AI 对面积普遍轻度低估：annulus -1.9%，LVOT -2.7%，STJ -2.6%，冠脉高度 -3.5% 至 -3.9%
- 分析时间：Mimics 1.03 分钟 vs 3Mensio 9.55 分钟，约 9 倍更快（P=0.001）
- 三类瓣膜（SAPIEN 3、Evolut FX、Navitor）尺寸选择一致率约 90% 或更高
