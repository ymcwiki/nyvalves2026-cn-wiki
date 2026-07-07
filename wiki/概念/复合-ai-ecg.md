---
type: concept
created: 2026-06-29
updated: 2026-06-29
sources: ["[[来源/671-ai-enabled-ecg-analysis-for-detection-and-predic]]"]
tags: [method]
aliases:
  - "composite AI-ECG"
  - "AI-ECG composite"
generation_complete: true
---

# 复合 AI-ECG

## 基本信息
- Type: method
- Source: [[来源/671-ai-enabled-ecg-analysis-for-detection-and-predic|671-ai-enabled-ecg-analysis-for-detection-and-predic]]

## 定义
将 LVSD 和 LVDD 两个已部署 AI-ECG 二分类模型以 OR 规则组合，任一阳性即判为 composite 阳性，无需重新训练，用于覆盖完整 SHD 谱系的筛查。

## 相关概念
- [[概念/结构性心脏病shd|结构性心脏病（SHD）]]
- [[概念/ai-ecg-筛查|AI-ECG 筛查]]
- [[概念/lvsd-模型|LVSD 模型]]
- [[概念/lvdd-模型|LVDD 模型]]
- [[概念/youden-阈值|Youden 阈值]]

## 相关实体
- [[实体/columbia-university-irving-medical-center|Columbia University Irving Medical Center]]
- [[实体/hak-seung-lee|Hak Seung Lee]]
- [[实体/medical-ai-inc|Medical AI, Inc.]]
- [[实体/ish|ISH]]
- [[实体/uk-biobank|UK Biobank]]

## 来源提及
- "Composite AI-ECG 的定义是：左室收缩功能障碍模型 LVSD 或左室舒张功能障碍模型 LVDD 任一阳性，即为复合阳性" — [[来源/671-ai-enabled-ecg-analysis-for-detection-and-predic|671-ai-enabled-ecg-analysis-for-detection-and-predic]]
- "该组合没有重新训练，也没有重新校准" — [[来源/671-ai-enabled-ecg-analysis-for-detection-and-predic|671-ai-enabled-ecg-analysis-for-detection-and-predic]]
