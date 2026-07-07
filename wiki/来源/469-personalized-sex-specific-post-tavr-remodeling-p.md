---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/469-personalized-sex-specific-post-tavr-remodeling-p.md]]"
tags: [3D数字孪生, LV reverse remodeling (LVMR), 统计形态分析（SSA/PLS）, TotalSegmentator, support vector regression (SVR), 左室质量指数（LVMI）, 性别特异形态预测]
contentHash: 63f-70e6a376
generation_complete: true
---

# Personalized Sex-Specific Post-TAVR Remodeling Prediction by AI-Driven Left Ventricular Geometry in Aortic Stenosis - 摘要

## 来源
- 原始文件：[[sources/469-personalized-sex-specific-post-tavr-remodeling-p.md]]
- 收录日期：2026-06-29

## 核心内容
本研究利用 pre-TAVR CT 中提取的 3D 左室几何信息，通过 AI 分割和统计形态分析，建立性别特异模型预测 TAVR 后左室质量回缩（LVMR）。339 例 BWH+MGH 患者（2015-2023）中，女性特异形态模型交叉验证 R² 达 0.89，远优于传统临床基线指标的 0.16。研究表明 3D 左室形态优于 LVMI/LVEF 等 2D 标量，且男女形态模式存在显著差异，具有不同预测价值。

## 关键实体
- [[实体/brigham-and-womens-hospital|Brigham and Women's Hospital]]：Brigham and Women's Hospital（BWH）是位于波士顿的哈佛医学院附属医院，隶属于 Mass General Brigham Heart and Vascular Institute。作为心脏外科重要临床中心，该院具有三尖瓣手术专业背景，与麻省总医院（MGH）共同承担多项心脏外科研究，包括提供 2015-2023 年间 339 例患者队列数据。讲者 Edoardo Zancanaro 任职于此，并在此完成多项手术操作及研究汇报。
- [[实体/shahab-masoumi|Shahab Masoumi]]：Shahab Masoumi 是哈佛医学院（Harvard Medical School）附属 Brigham and Women's Hospital 的心血管 fellowship 研究者，隶属于 Mass General Brigham 医疗系统。他主导了两项 AI 驱动的心脏病学研究：一项专注于通过人工智能预测左室几何形态，另一项提出了名为 Intelligent TAVR 的系统，旨在优化经导管主动脉瓣置换术的临床决策流程。

## 关键概念
- [[概念/3d数字孪生|3D数字孪生]]
- [[概念/lv-reverse-remodeling-lvmr|LV reverse remodeling (LVMR)]]
- [[概念/统计形态分析ssapls|统计形态分析（SSA/PLS）]]
- [[概念/totalsegmentator|TotalSegmentator]]
- [[概念/support-vector-regression-svr|support vector regression (SVR)]]
- [[概念/左室质量指数lvmi|左室质量指数（LVMI）]]
- [[概念/性别特异形态预测|性别特异形态预测]]

## 要点
- 3D 左室几何形态预测 TAVR 后 LVMR，女性特异模型 R² 达 0.89，比传统指标提升约 4 倍
- AI 分割（TotalSegmentator）平均 Dice 0.93，300k 网格降采样至 5k 对应点，保留绝对左室大小
- 339 例患者中 65% 在 1 年出现 positive LVMR，男女差异 P=0.99，但形态预测模式存在显著性别差异
- 女性偏向心性重构/小腔室，男性偏离心性重构/扩张；形态模式涉及全局大小、球形-卵圆形比和壁厚
- 研究为回顾性双中心设计，需前瞻性外部验证；形态来自 CT 但结局来自 echo，存在操作者依赖偏差
