---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/448-decade-of-mitraclip-in-real-world-practice-a-com.md]]"
tags: [SLDA, M-TEER, negation-aware NLP, 医疗器械不良事件报告（MDR）]
contentHash: 637-d1ad0266
generation_complete: true
---

# 真实世界 MitraClip 十年实践：2013-2025 年 22,221 份 MAUDE 不良事件报告分析 - 摘要

## 来源
- 原始文件：[[sources/448-decade-of-mitraclip-in-real-world-practice-a-com.md]]
- 收录日期：2026-06-29

## 核心内容
本研究对 FDA MAUDE 数据库中 2013-2025 年共 22,221 份 MitraClip 不良事件报告进行系统分析，是迄今规模最大的 MitraClip 纵向 MAUDE 研究。结构/器械信号（SLDA、不完全对合、残余 MR）占报告负担主体；死亡型报告中最常见高危信号为穿孔/填塞、卒中/CVA 和心脏骤停/休克。研究采用 negation-aware NLP 方法提高信号验证准确性，但强调 MAUDE 无法估计真实发生率或推断因果关系。

## 关键实体
- [[实体/mitraclip|MitraClip]]：MitraClip 是 Abbott 公司研发的经导管二尖瓣缘对缘修复（TEER）器械，2013 年获 FDA 批准，全球植入量已超 200,000 例。产品经历从 Gen 1 到 Gen 5 的多代演进，现有 NTW、XTW、XT 等多种型号，均通过 24 Fr 输送鞘经皮经房间隔路径完成夹合。EVEREST、COAPT、MITRA-FR、RESHAPE-HF2 等多项关键随机试验均以 MitraClip 为研究器械，证实其对原发性及继发性二尖瓣反流患者的有效性。目前它是 M-TEER 领域植入最广泛的代表性系统，亦是 PASCAL 等同类竞品的主要对照参照。
- [[实体/shreyas-nandyal|Shreyas Nandyal]]：Shreyas Nandyal，心血管介入领域研究者，以第一作者身份参与多项研究。其工作涵盖先天性心脏病介入治疗（包括巨大动脉导管未闭合并重度肺动脉高压的经导管封堵病例报告）及结构性心脏病器械安全评价（基于 MAUDE 数据库的 MitraClip 十年不良事件分析），声明无利益冲突。
- [[实体/maude|MAUDE]]：FDA 的 Manufacturer and User Facility Device Experience 数据库，是美国上市后医疗器械不良事件报告的主要来源，本研究从中提取十年 MitraClip 相关报告进行分析。

## 关键概念
- [[概念/slda|SLDA]]
- [[概念/m-teer|M-TEER]]
- [[概念/negation-aware-nlp|negation-aware NLP]]
- [[概念/医疗器械不良事件报告mdr|医疗器械不良事件报告（MDR）]]

## 要点
- 查询 MAUDE 数据库 MitraClip 相关产品代码（NKM、DRA、DQY），分析 22,221 份报告（2013 年 10 月-2025 年 12 月）
- 报告构成：Injury 58.0%（12,886 份）、Malfunction 36.5%（8,118 份）、Death-type 5.5%（1,217 份）
- 最常见信号：SLDA 28.8%、不完全对合 24.2%、残余 MR 22.7%
- 死亡型报告中高危信号：穿孔/填塞 13.4%、卒中/CVA 13.2%、心脏骤停/休克 13.0%
- SLDA 提及中 negation-aware NLP 确认率 93%；卒中提及确认率约 69%
- G4 代积累最多报告（38.6%，8,568 份）；G5 仅在 2025 年出现（341 份），SLDA 占比最低（10.9%）
- MAUDE 无分母、无因果，所有数字为报告比例而非患者发生率
