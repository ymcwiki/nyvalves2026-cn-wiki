---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/188-mitralvalveai-from-a-standard-cardiac-ct-patient.md]]"
tags: [TEER, 数字孪生（Digital Twin）, 跨二尖瓣压差预测, 4D心脏CT重建, TEER取舍（MR vs 压差）]
contentHash: 4c1-7608ca3b
generation_complete: true
---

# MitralValveAi: From a Standard Cardiac CT Patient-Specific Mitral Valve Digital Twin - 摘要

## 来源
- 原始文件：[[sources/188-mitralvalveai-from-a-standard-cardiac-ct-patient.md]]
- 收录日期：2026-06-29

## 核心内容
本文介绍基于标准心脏CT构建患者特异性二尖瓣数字孪生（digital twin）的概念验证研究，目标是在TEER手术前虚拟测试不同夹子策略，预测跨二尖瓣压差与残余反流之间的平衡。系统流程为CT分割、瓣膜重建、机械物理建模、血流动力学仿真，可输出各方案的预测压差。示例显示中央双夹积极方案在MR降幅最大（92%）的同时平均压差达6.1 mmHg，超过5 mmHg的二尖瓣狭窄警戒线，说明虚拟规划能量化取舍。

## 关键实体
- [[实体/mitraclip|MitraClip]]：MitraClip 是 Abbott 公司研发的经导管二尖瓣缘对缘修复（TEER）器械，2013 年获 FDA 批准，全球植入量已超 200,000 例。产品经历从 Gen 1 到 Gen 5 的多代演进，现有 NTW、XTW、XT 等多种型号，均通过 24 Fr 输送鞘经皮经房间隔路径完成夹合。EVEREST、COAPT、MITRA-FR、RESHAPE-HF2 等多项关键随机试验均以 MitraClip 为研究器械，证实其对原发性及继发性二尖瓣反流患者的有效性。目前它是 M-TEER 领域植入最广泛的代表性系统，亦是 PASCAL 等同类竞品的主要对照参照。
- [[实体/kaoutare-chbini|Kaoutare Chbini]]：本报告讲者，提出并展示从标准心脏CT构建二尖瓣数字孪生用于TEER术前规划的概念验证工作。

## 关键概念
- [[概念/teer|TEER]]
- [[概念/数字孪生digital-twin|数字孪生（Digital Twin）]]
- [[概念/跨二尖瓣压差预测|跨二尖瓣压差预测]]
- [[概念/4d心脏ct重建|4D心脏CT重建]]
- [[概念/teer取舍mr-vs-压差|TEER取舍（MR vs 压差）]]

## 要点
- 当前TEER规划能看到解剖但无法在介入前测试不同夹子方案的血流动力学后果
- 数字孪生构建流程：CT → 分割 → 瓣膜重建 → 模拟（力学+血流+压差）
- 从CT导出左室容积和dV/dt流量条件，通过连续性方程和Bernoulli关系预测跨二尖瓣压差
- 虚拟TEER可比较不同夹子位置和数量方案：MR降幅越大，压差越高
- 中央双夹积极方案MR降幅92%但平均压差6.1 mmHg超过警戒线
- 目前处于概念验证阶段，下一步需完整3D CFD仿真和临床验证
