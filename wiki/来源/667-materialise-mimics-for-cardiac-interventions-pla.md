---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/667-materialise-mimics-for-cardiac-interventions-pla.md]]"
tags: [TAV-in-TAV, DLC/d, 瓣周漏（PVL）, lifetime management, 患者特异性计算机仿真, peak areal stretch]
contentHash: 8c4-627122a0
generation_complete: true
---

# Materialise Mimics 用于心脏介入：FEops 预测洞察赋能的规划 - 摘要

## 来源
- 原始文件：[[sources/667-materialise-mimics-for-cardiac-interventions-pla.md]]
- 收录日期：2026-06-29

## 核心内容
本文介绍 Materialise Mimics 与 FEops HEARTguide 平台在 TAVR 术前规划中的应用，通过 AI 三维分割、虚拟植入与患者特异性有限元仿真，预测瓣架变形、PVL 路径、冠脉阻塞风险和传导异常风险。两个临床病例展示了仿真指导器械选型的实际价值，PRECISE-TAVI 真实世界研究证实该技术使 35% 的术前决策发生改变，并与更低起搏器率和更低 PVL 率相关。

## 关键实体
- [[实体/evolut-fx+|Evolut FX+]]：Evolut FX+ 是 Medtronic 研发的新一代自膨式经导管主动脉瓣系统，采用瓣上设计，提供 23、26、29、34 mm 多种型号，适用于原生瓣膜狭窄、纯反流及外科瓣衰败后的瓣中瓣手术。其可重新定位特性与较大的瓣架单元有助于改善植入精度和术后瓣周漏处理时导管的同轴性。该系统已在多种入路（经股动脉、经颈动脉）及复杂解剖场景（二叶瓣、钙化改良后、多次 ViV）中得到临床应用，但也有因超指征后扩张导致瓣叶损伤、短期内需取出的并发症报告。
- [[实体/precise-tavi|PRECISE-TAVI]]：PRECISE-TAVI 是一项前瞻性、多中心欧洲观察性研究，评估CT衍生仿真（FEops预测规划）在复杂主动脉瓣解剖（含17例二叶瓣）TAVI术前规划中的临床价值。研究结果显示，35%的术前决策在仿真辅助后发生改变，且与临床结局改善相关联。相关成果发表于Catheterization and Cardiovascular Interventions 2023年。
- [[实体/feops|FEops]]：FEops HEARTguide 是一款基于 CT 的 AI 计算建模平台，支持 LAAC 和 TAVR 等结构性心脏手术的术前患者特异性计算机仿真。在 LAAC 场景中，可生成个体化 LAA-器械交互模拟，预测植入后器械形态、色彩图及推荐 C 臂角度，辅助复杂解剖的器械选型。在 TAVR 场景中，可预测瓣架形态、瓣周漏路径、冠脉阻塞风险及传导异常风险，为术者提供决策支持。
- [[实体/anene-ukaigwe|Anene Ukaigwe]]：本文讲者，介入心脏病学专家，来自 University Hospitals Harrington Heart and Vascular Institute 瓣膜与结构性心脏团队。
- [[实体/sapien-ultra|Sapien Ultra]]：Sapien Ultra 是 Edwards Lifesciences 生产的球囊扩张式经导管主动脉瓣系统，适用于经导管主动脉瓣置换术。多项研究将其与 Evolut FX+ 等自膨胀瓣进行对比，其中 BE 26 规格在仿真测试中显示出 undersizing 及较大环形拉伸值。临床上，该瓣膜（如 23 mm 规格）也用于瓣中瓣手术，例如在 UNICORN 瓣叶改良后植入原有 Evolut 29 瓣内，实现 TAV-in-TAV 配置。
- [[实体/university-hospitals-harrington-heart-and-vascular-institute|University Hospitals Harrington Heart and Vascular Institute]]：本文讲者 Anene Ukaigwe 所在机构，专注瓣膜与结构性心脏介入。

## 关键概念
- [[概念/tav-in-tav|TAV-in-TAV]]
- [[概念/dlcd|DLC/d]]
- [[概念/瓣周漏pvl|瓣周漏（PVL）]]
- [[概念/lifetime-management|lifetime management]]
- [[概念/患者特异性计算机仿真|患者特异性计算机仿真]]
- [[概念/peak-areal-stretch|peak areal stretch]]

## 要点
- FEops HEARTguide 通过 frame deformation、skirt apposition 和 contact area 三类参数分别预测环部损伤/冠脉风险、PVL 风险和传导异常风险
- DLC/d ≤ 0.7 是文献提示的 TAVR 相关冠脉阻塞风险阈值，TAV-in-TAV 场景下需预先建模评估
- PRECISE-TAVI 前瞻性多中心研究：术前决策改变 35%（12% 尺寸改变，23% 位置改变），关联更低起搏器率和更低 PVL
- 87 岁膜部室间隔瘤病例：仿真指导选择高位 29 mm Evolut PRO，实际仅轻度 PVL，未发生室间隔瘤破裂
- 73 岁二叶瓣病例：SE 29（Evolut FX+）与 BE 26（Sapien Ultra）对比，最终选 SE 29，术后无起搏器
- TAVR simulations not yet available for clinical use in the USA
