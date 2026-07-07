---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/260-83869-a-novel-echocardiography-based-ai-model-fo.md]]"
tags: [AS进展预测AI模型, 主动脉瓣狭窄进展率, 超声心动图注册库, 个体化AS随访范式, 外部验证泛化性]
contentHash: 49e-4a40d358
generation_complete: true
---

# 基于超声心动图的AI模型预测主动脉瓣狭窄进展 - 摘要

## 来源
- 原始文件：[[sources/260-83869-a-novel-echocardiography-based-ai-model-fo.md]]
- 收录日期：2026-06-29

## 核心内容
本报告介绍了一种仅利用结构化超声心动图报告参数、基于机器学习（CatBoost）预测主动脉瓣狭窄（AS）进展的AI模型，内部测试AUC约0.90，外部验证性能损失不超过0.03 AUC。研究来自以色列Rabin和Sheba医学中心的多中心协作，内部队列2,870例，外部队列1,666例，1年、3年、5年预测AUC均在0.88至0.91之间。讲者认为该模型有助于从固定随访间隔转向个体化精准医学监测。

## 关键实体
- [[实体/leor-perl|Leor Perl]]：本报告讲者，来自以色列Rabin Medical Center，JACC Advances 2025年AS进展AI预测文章的通信作者之一。
- [[实体/rabin-medical-center|Rabin Medical Center]]：Rabin Medical Center是位于以色列Petah Tikva的医疗机构，承担内部训练队列的数据采集工作，同时作为多中心外部验证协作机构之一参与研究。心脏病学领域学者Kornowski所在单位，也是首例人体研究（FIH）的主要参与机构之一。
- [[实体/sheba-medical-center|Sheba Medical Center]]：以色列Sheba Tel HaShomer医疗机构，作为外部验证协作中心参与本研究的多中心泛化性评估。

## 关键概念
- [[概念/as进展预测ai模型|AS进展预测AI模型]]
- [[概念/主动脉瓣狭窄进展率|主动脉瓣狭窄进展率]]
- [[概念/超声心动图注册库|超声心动图注册库]]
- [[概念/个体化as随访范式|个体化AS随访范式]]
- [[概念/外部验证泛化性|外部验证泛化性]]

## 要点
- AS进展存在明显个体差异，同样mild AS起点3年后可保持稳定或进展为severe AS合并心衰
- 既往中度AS队列（540例）显示快速进展者全因死亡HR 1.77、HF入院/CV死亡HR 1.76、AVR HR 3.44
- 模型仅用结构化超声报告参数，来自500K+患者的本地超声注册库
- 1年、3年、5年AUC分别为0.89/0.91、0.88/0.88、0.90/0.87（测试集/外部队列）
- 最重要特征为主动脉瓣平均压差（约27%）和瓣口面积（约18%）
- 局限：无临床结局、存在缺失数据、泛化性仍有限
- 下一步路线图包括临床终点预测、图像级分析、规模化部署和个体化风险管理
