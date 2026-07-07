---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/290-personalized-mitral-intervention-from-advanced-i.md]]"
tags: [M-TEER, digital twin, ECHO-PREP, MONAI Auto3DSeg, AutoNavigate, 4D Fusion]
contentHash: 65b-5277f381
generation_complete: true
---

# 个体化二尖瓣介入：从高级影像到 AI 预测工具 - 摘要

## 来源
- 原始文件：[[sources/290-personalized-mitral-intervention-from-advanced-i.md]]
- 收录日期：2026-06-29

## 核心内容
本文系统梳理 AI 和深度学习在结构性心脏影像中的应用演进，聚焦二尖瓣介入的术前规划、术中导航和器械决策。AI 瓣膜分割效率已从人工 46 小时压缩至深度学习 17 分钟/用户时间 3.5 分钟，LARALAB/Abbott 平台实现自动 CT 分割、测量和瓣叶重建。ECHO-PREP 全自动工作流通过三个算法模块支持 M-TEER 适合性筛查和决策，并采用 MVSEG2023 数据集结合 MONAI Auto3DSeg 分割瓣叶和瓣环。未来方向包括 digital twin、AI 器械检测、AutoNavigate 和增强现实/机器人手术。

## 关键实体
- [[实体/laza-medical|Laza Medical]]：Laza Medical 是一家医疗科技公司，专注于开发 AI 驱动的机器人辅助经食道超声心动图（TEE）影像与探头导航系统。该系统目前仍处于开发阶段，尚未在美国或其他任何地区获得监管批准，被视为未来超声导航技术的代表方向之一。
- [[实体/laralab|LARALAB]]：LARALAB GmbH 是德国一家专注于心脏影像 AI 分析的公司，已被 Abbott 结构性心脏部门收购。其软件平台提供自动 CT 分割、测量、病例规划和瓣叶重建工具，主要用于二尖瓣分析，同时也支持 CT 重建及右室容积功能分析。
- [[实体/ralph-stephan-von-bardeleben|Ralph Stephan von Bardeleben]]：本报告讲者，来自 Montreal Heart Institute Canada 和 University Medicine Mainz Germany，专注于二尖瓣结构性影像与 AI 应用研究。
- [[实体/mvseg2023-challenge|MVSEG2023 Challenge]]：MICCAI 2023 卫星挑战赛，提供 135 个 3D 超声体积作为二尖瓣分割训练数据集，被 ECHO-PREP Algorithm 3 采用。

## 关键概念
- [[概念/m-teer|M-TEER]]
- [[概念/digital-twin|digital twin]]
- [[概念/echo-prep|ECHO-PREP]]
- [[概念/monai-auto3dseg|MONAI Auto3DSeg]]
- [[概念/autonavigate|AutoNavigate]]
- [[概念/4d-fusion|4D Fusion]]

## 要点
- AI 深度学习将瓣膜分割总时间从 46 小时压缩至 17 分钟，用户时间从 46 小时降至 3.5 分钟
- LARALAB（现被 Abbott SH 收购）提供自动 CT 分割、测量、病例规划和二尖瓣叶 AI 重建
- ECHO-PREP 全自动工作流：算法 1 处理 TTE 视图/质量，算法 2 处理 TEE 视图/M-TEER 适合性，算法 3 处理图像测量支持决策
- Algorithm 3 使用 MVSEG2023 Challenge 数据集（135 个 3D 体积，70/15/15 划分），采用 MONAI Auto3DSeg 分割瓣叶和瓣环
- Digital twin 从 CT 或 3D 超声生成患者特异性二尖瓣生物力学模型，用于治疗规划、器械选择和结局优化
- AI 驱动 AutoNavigate 整合解剖、器械和目标点实现实时路径引导
- 监管框架需适应 AI 创新速度，评估安全性、有效性和伦理影响
