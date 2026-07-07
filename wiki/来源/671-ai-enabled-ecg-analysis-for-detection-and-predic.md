---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/671-ai-enabled-ecg-analysis-for-detection-and-predic.md]]"
tags: [复合 AI-ECG, 结构性心脏病（SHD）, AI-ECG 筛查, LVSD 模型, LVDD 模型, Youden 阈值]
contentHash: 6e8-956e513f
generation_complete: true
---

# AI 辅助 ECG 分析用于结构性心脏病的检测与预测 - 摘要

## 来源
- 原始文件：[[sources/671-ai-enabled-ecg-analysis-for-detection-and-predic.md]]
- 收录日期：2026-06-29

## 核心内容
本文报告一项跨国研究，将已部署的 LVSD 和 LVDD 两个 AI-ECG 二分类模型以 OR 规则合成为复合模型，用于结构性心脏病（SHD）的横断面检测和纵向预测。在韩国（ISH）、美国（CUIMC）、英国（UKB）三个队列验证中，复合模型对既存 SHD 的敏感性 71.8-76.1%，NPV 95.6%，新发 SHD 预测 HR 为 2.75-3.75，C-statistics 0.69-0.78，支持将其作为超声前分诊工具。

## 关键实体
- [[实体/columbia-university-irving-medical-center|Columbia University Irving Medical Center]]：Columbia University Irving Medical Center（CUIMC）是位于纽约的学术医疗中心，与NewYork-Presbyterian Hospital合作运营，设有专业的结构性心脏病与瓣膜中心（Structural and Valve Center）。该中心在经导管主动脉瓣和二尖瓣介入领域积累了丰富经验，包括TAV-in-TAV手术及Cephea EFS经导管二尖瓣置换研究。Rebecca Hahn、Torsten Vahl、Michael I. Brener、Tamim Nazif等结构性心脏病领域的知名医师均任职于此，并参与多项临床试验（如Protect H2H）。
- [[实体/hak-seung-lee|Hak Seung Lee]]：本文讲者，来自 Digital Healthcare Institute、Sejong Medical Research Institute 和 Medical AI Co., Ltd.，持有 Medical AI, Inc. 股票及专利权益。
- [[实体/medical-ai-inc|Medical AI, Inc.]]：讲者持有股票和专利权益的公司，开发了文中使用的 LVSD 和 LVDD AI-ECG 模型，两个模型已在韩国获得监管批准并临床部署。
- [[实体/ish|ISH]]：韩国队列（n=46,082 经筛选），用于横断面 SHD 检测和纵向新发 SHD 预测，SHD 患病率 12.7%。
- [[实体/uk-biobank|UK Biobank]]：英国大规模人群生物样本库（UKB），本研究使用其中 n=41,226 例无既往 SHD 者进行新发 SHD 纵向预测，composite 阳性 HR 2.75。

## 关键概念
- [[概念/复合-ai-ecg|复合 AI-ECG]]
- [[概念/结构性心脏病shd|结构性心脏病（SHD）]]
- [[概念/ai-ecg-筛查|AI-ECG 筛查]]
- [[概念/lvsd-模型|LVSD 模型]]
- [[概念/lvdd-模型|LVDD 模型]]
- [[概念/youden-阈值|Youden 阈值]]

## 要点
- 复合 AI-ECG = LVSD 阳性 OR LVDD 阳性，不重新训练、不重新校准，直接组合两个已部署模型
- ISH 队列（n=46,082）：敏感性 71.8%，特异性 88.3%，NPV 95.6%；CUIMC（n=36,286）：敏感性 76.1%，PPV 66.3%
- 每发现一例 SHD 所需超声数量从 7.9 降至 2.1（ISH 队列）
- 新发 SHD 预测：composite 阳性 vs 阴性 HR: ISH 3.75，UKB 2.75；C-statistics 0.69-0.78
- LVSD 主要检出 reduced LVEF，LVDD 驱动 VHD、LVH 和 PH 的检出，两者互补覆盖完整 SHD 谱系
- 相同 Youden 阈值跨韩国、美国、英国三个队列直接应用，未做站点特异性调参
