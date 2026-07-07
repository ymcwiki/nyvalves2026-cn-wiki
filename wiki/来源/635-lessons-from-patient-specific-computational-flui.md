---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/635-lessons-from-patient-specific-computational-flui.md]]"
tags: [器械相关血栓（DRT）, 左心耳封堵, CFD（计算流体动力学）, TAWSS（时间平均壁面剪切力）, RRT（相对停留时间）, ECAP（内皮细胞激活潜能）]
contentHash: 611-bfa87168
generation_complete: true
---

# 左心耳封堵中患者特异性CFD的启示 - 摘要

## 来源
- 原始文件：[[sources/635-lessons-from-patient-specific-computational-flui.md]]
- 收录日期：2026-06-29

## 核心内容
本报告由 Hoda Hatoum 呈现，探讨患者特异性计算流体动力学（CFD）在左心耳封堵（LAAO）中对器械选择、植入策略和血栓风险评估的潜在价值。DRT 组患者的 TAWSS 显著低于对照组（p<0.01），ECAP 显著高于对照组（p<0.01），提示不利的近壁血流环境与器械相关血栓相关。深植入与更高 RRT（提示更差的血流冲洗）相关。Amulet 和 Watchman FLX 植入后的流体动力学变化模式不同，但这种差异尚未与 DRT 的发生与否直接相关联。

## 关键实体
- [[实体/watchman-flx|WATCHMAN FLX]]：WATCHMAN FLX 是 Boston Scientific 生产的第二代经皮左心耳封堵器，于 2020 年获 FDA 批准，提供 20/24/27/31/35 mm 多种规格，采用双排 J 形锚点和远端爪足封闭设计。相比早期 Watchman 2.5，其围手术期并发症显著减少，器械栓塞/迁移率极低，心包积液需干预率降至约 0.39%。该器械是 CHAMPION-AF、OPTION、SIMPLAAFY 等多项重要随机试验的研究对象，2025 年 7 月 FDA 进一步扩展标签，允许与房颤消融同期或分期使用。其后继产品为 WATCHMAN Elite。
- [[实体/amulet|Amulet]]：Amulet 是 Abbott 公司生产的经导管左心耳封堵装置，采用 lobe-disc 双层结构，lobe 部分配备单排 10 个锚点（每个 2.5 mm），无远端爪足，植入需约 12 mm 可用深度。在 Amulet IDE 随机对照试验中，其装置相关血栓发生率约 1.5%-3.9%，心包积液发生率 2.4%，45 天完全封堵率约 63%，低于 Watchman FLX。该装置已被多项大型研究采用，包括 CATALYST、STROKECLOSE 试验及纳入逾万例患者的 EMERGE LAA 注册研究，新一代 Amulet 360（Amulet 2）在原有设计基础上进一步改进。
- [[实体/hoda-hatoum|Hoda Hatoum]]：本报告讲者，专注于计算流体动力学在结构性心脏病中的应用研究，与 Dasi Sim 存在专利受益关系。

## 关键概念
- [[概念/器械相关血栓drt|器械相关血栓（DRT）]]
- [[概念/左心耳封堵|左心耳封堵]]
- [[概念/cfd计算流体动力学|CFD（计算流体动力学）]]
- [[概念/tawss时间平均壁面剪切力|TAWSS（时间平均壁面剪切力）]]
- [[概念/rrt相对停留时间|RRT（相对停留时间）]]
- [[概念/ecap内皮细胞激活潜能|ECAP（内皮细胞激活潜能）]]

## 要点
- LAAO 术后器械相关血栓（DRT）发生率最高可达7%，与不利的近壁血流环境相关
- DRT 组 TAWSS 显著低于对照（p<0.01），ECAP 显著高于对照（p<0.01），OSI 差异无统计学意义
- 深植入与较高 RRT 相关，提示 poor washout，增加 DRT 风险
- Amulet 植入后更常见血流动力学改善（TAWSS 升高），Watchman FLX 植入后 TAWSS 整体下降
- 患者特异性 CFD 流程：CT扫描→模型分割→有限元模拟→边界条件→CFD动态流动结果
