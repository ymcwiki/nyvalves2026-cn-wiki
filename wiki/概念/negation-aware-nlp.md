---
type: concept
created: 2026-06-29
updated: 2026-06-29
sources: ["[[来源/448-decade-of-mitraclip-in-real-world-practice-a-com]]"]
tags: [method]
aliases:
  - "medspaCy"
  - "NegEx-ConText"
generation_complete: true
---

# negation-aware NLP

## 基本信息
- Type: method
- Source: [[来源/448-decade-of-mitraclip-in-real-world-practice-a-com|448-decade-of-mitraclip-in-real-world-practice-a-com]]

## 定义
采用 medspaCy/NegEx-ConText 框架对 MAUDE 报告自由文本叙述进行语义分析，仅在并发症被肯定描述时计数，以避免单纯关键词搜索的过度计数（如卒中提及中仅 ~69% 为真实事件）。

## 相关概念
- [[概念/slda|SLDA]]
- [[概念/m-teer|M-TEER]]
- [[概念/医疗器械不良事件报告mdr|医疗器械不良事件报告（MDR）]]

## 相关实体
- [[实体/mitraclip|MitraClip]]
- [[实体/shreyas-nandyal|Shreyas Nandyal]]
- [[实体/maude|MAUDE]]

## 来源提及
- "Pass 2（Validate）采用 negation-aware NLP，即 medspaCy / NegEx-ConText 重新读取叙述，仅在并发症被肯定描述时计数" — [[来源/448-decade-of-mitraclip-in-real-world-practice-a-com|448-decade-of-mitraclip-in-real-world-practice-a-com]]
