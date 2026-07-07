---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/673-precision-planning-through-digital-twin-technolo.md]]"
tags: [ViV-TAVR, HALT, BASILICA, digital twin, DLC/d, Reduced Order Model, Root Stretch]
contentHash: 521-7389a9ac
generation_complete: true
---

# 数字孪生技术用于结构性心脏介入的精准规划 - 摘要

## 来源
- 原始文件：[[sources/673-precision-planning-through-digital-twin-technolo.md]]
- 收录日期：2026-06-29

## 核心内容
本报告介绍 DASI Simulations 开发的数字孪生技术，用于 TAVR 精准规划。系统以生物力学模型和人类数据训练为基础，可对球扩瓣（BE）和自膨瓣（SE）分别建模，动态预测支架/组织变形、冠脉阻塞风险（DLC/d 指标）、根部 stretch 和 HALT 风险。在 158 例 ViV/redo TAVR 队列中，DASI 将 89.3% 的 CT 高危患者重新分类为低危，显著减少 leaflet modification 使用率。

## 关键实体
- [[实体/dasi-simulations|DASI Simulations]]：DASI Simulations 是一家专注于心血管人工智能计算建模的公司，其平台基于患者 CT 数据构建个体化解剖模型，用于模拟候选瓣膜的血流动力学参数（如 DLC/d）及 neo-LVOT 预测，辅助 TAVR/TMVR 术前冠脉风险分层与解剖筛选。该公司亦参与工程化瓣叶血栓（HALT）定义的建模研究，部分心血管领域讲者持有其股权并担任科学顾问委员会成员。
- [[实体/lakshmi-prasad-dasi|Lakshmi Prasad Dasi]]：本报告讲者，PhD、FACC，持有 DASI Simulations LLC 股权，来自 Ohio State University 及 Georgia Tech/Emory University。

## 关键概念
- [[概念/viv-tavr|ViV-TAVR]]
- [[概念/halt|HALT]]
- [[概念/basilica|BASILICA]]
- [[概念/digital-twin|digital twin]]
- [[概念/dlcd|DLC/d]]
- [[概念/reduced-order-model|Reduced Order Model]]
- [[概念/root-stretch|Root Stretch]]

## 要点
- 传统 TAVR 规划存在约 15-20% 人为变异，无法预测器械与器官相互作用
- DASI 数字孪生使用简化阶模型动态演化三角网格，覆盖 THV、钙化结节和主动脉根部
- 冠脉阻塞预测关键指标为 DLC/d，阈值 0.7，基于 n=1500 例患者数据验证
- Root stretch 阈值：<1.5 低风险，1.5-1.7 灰区，>1.7 根部损伤风险增加
- 158 例 ViV/redo TAVR 中，DASI 将 25/28 例 CT 高危患者重新分类为低危（89.3%），其中 80% 无需 leaflet modification 成功处理
- 术后压差预测示例：平均压差 13 mmHg，峰值压差 23 mmHg
- 未来扩展方向包括 TMVR、LAAO 和 TEER
