---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/513-lost-in-translation-why-engineers-need-a-seat-at.md]]"
tags: [医疗器械开发五阶段模型, Translational Imaging（转化影像）, PIV（粒子图像测速）, 非劣效贝叶斯分析, THV 欠扩张]
contentHash: 694-bdceeaa2
generation_complete: true
---

# 断译：为什么工程师需要坐到临床桌前 - 摘要

## 来源
- 原始文件：[[sources/513-lost-in-translation-why-engineers-need-a-seat-at.md]]
- 收录日期：2026-06-29

## 核心内容
Boston Scientific 研发副总裁 Aaron Chalekian 从工程视角阐述医疗器械从概念到临床转化的五阶段路径，指出 Phase III 至 IV 之间工程与临床连接断裂是 ACURATE IDE 失败的深层原因。根因分析发现 ACURATE neo2 瓣膜欠扩张是核心问题，改进方向包括常规预扩、围术期双视角影像评估和后扩，并主张将工程测试工具纳入 ISO 标准推动跨界协作。

## 关键实体
- [[实体/boston-scientific|Boston Scientific]]：Boston Scientific 是全球医疗器械公司，旗下产品涵盖左心耳封堵器（WATCHMAN / WATCHMAN FLX 系列）和经导管主动脉瓣膜（ACURATE neo2）等结构性心脏领域核心器械。该公司是 CHAMPION-AF 等关键临床试验的主要资助方之一，多位讲者与其存在研究资助及顾问费财务关系。其员工 Aaron Chalekian 曾以 ACURATE IDE 试验失败为案例，探讨工程与临床协作中的断层问题。
- [[实体/acurate-neo2|ACURATE Neo2]]：ACURATE Neo2 是 Boston Scientific 研发的自膨式经导管主动脉瓣膜（TAVR），采用自上而下释放设计。在 SCOPE I/II 及 ACURATE IDE 三项 RCT 中均未能达到非劣效终点，事后分析确认核心问题为钙化瓣环中中段框架展开不足（发生率约 20-21.6%），导致瓣周漏显著增高并与一年不良事件相关。
- [[实体/acurate-ide|ACURATE IDE]]：Boston Scientific 开展的 ACURATE neo2 随机对照研究（N=1500），与 Evolut 和 SAPIEN 3 对照，一年主要终点非劣效未达成，成为本讲核心案例。
- [[实体/aaron-chalekian|Aaron Chalekian]]：Boston Scientific 研发新兴疗法副总裁，本讲讲者，从工程师视角阐述临床-工程协作断层与 ACURATE IDE 失败教训。
- [[实体/university-of-minnesota|University of Minnesota]]：讲者引用的心血管医学历史圣地，列出多项世界首例心脏外科成就，用于说明工程与临床协作对医疗产品成功的重要性。

## 关键概念
- [[概念/医疗器械开发五阶段模型|医疗器械开发五阶段模型]]
- [[概念/translational-imaging转化影像|Translational Imaging（转化影像）]]
- [[概念/piv粒子图像测速|PIV（粒子图像测速）]]
- [[概念/非劣效贝叶斯分析|非劣效贝叶斯分析]]
- [[概念/thv-欠扩张|THV 欠扩张]]

## 要点
- Phase III-IV 之间是工程与临床连接最易断裂的阶段，早期境外经验未有效转化到美国 ACURATE IDE 试验
- ACURATE IDE RCT 中 ACURATE neo2 一年主要终点（全因死亡/卒中/再住院）非劣效未达成，后验中位差 6.63%，95% BCI 上限 10.20% 超过 8.0% 界值
- 根因调查确认瓣膜欠扩张是核心问题，优化方向：常规预扩、围术期双视角影像、可行时后扩
- 台架测试影像需与临床透视影像建立可翻译对应关系（Translational Imaging）
- 主张将 PIV、FEA、blood loop、3D light scanning、material shedding 等工程工具转化为可监管标准
