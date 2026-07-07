---
type: source
created: 2026-06-29
updated: 2026-06-29
source_file: "[[sources/100-ai-based-planning-and-prediction-models-in-bicus.md]]"
tags: [永久起搏器植入, digital twin, bicuspid aortic valve TAVR, contact pressure index, finite element analysis, automated TAVR planning]
contentHash: 83c-97f532fd
generation_complete: true
---

# AI规划与预测模型在二叶瓣TAVR中的应用 - 摘要

## 来源
- 原始文件：[[sources/100-ai-based-planning-and-prediction-models-in-bicus.md]]
- 收录日期：2026-06-29

## 核心内容
本报告系统介绍AI和计算建模在二叶瓣TAVR规划中的应用框架，涵盖从自动测量（Tier 1）到AI预测（Tier 2）、计算建模（Tier 3）和未来混合数字孪生（Tier 4）四个层级。PRECISE-TAVI研究显示接触压力指数可预测新PPI（AUC 0.83），Mimics for TAVR自动规划与3-MENSIO sizing一致率87-90%并将规划时间从9分钟压缩至1分钟。讲者强调AI置信度随解剖复杂性和训练数据相似性变化，越罕见的二叶瓣解剖越需要人类专家判断。

## 关键实体
- [[实体/nicolas-van-mieghem|Nicolas Van Mieghem]]：比利时Ziekenhuis Oost-Limburg心脏介入专家，本报告讲者，PRECISE-TAVI和Mimics for TAVR研究共同作者。
- [[实体/precise-tavi|PRECISE-TAVI]]：PRECISE-TAVI 是一项前瞻性、多中心欧洲观察性研究，评估CT衍生仿真（FEops预测规划）在复杂主动脉瓣解剖（含17例二叶瓣）TAVI术前规划中的临床价值。研究结果显示，35%的术前决策在仿真辅助后发生改变，且与临床结局改善相关联。相关成果发表于Catheterization and Cardiovascular Interventions 2023年。
- [[实体/mimics-for-tavr|Mimics for TAVR]]：Mimics for TAVR 是 Materialise 公司开发的全自动 TAVR 术前规划软件，基于 3D U-Net 深度学习架构，直接从 DICOM 数据生成患者特异性主动脉根部三维模型并自动完成关键解剖测量。软件支持多种瓣膜 sizing 方案，与 3-MENSIO 等参照软件具有高度一致性，并通过网页界面提供实时访问能力。
- [[实体/feops|FEops]]：FEops HEARTguide 是一款基于 CT 的 AI 计算建模平台，支持 LAAC 和 TAVR 等结构性心脏手术的术前患者特异性计算机仿真。在 LAAC 场景中，可生成个体化 LAA-器械交互模拟，预测植入后器械形态、色彩图及推荐 C 臂角度，辅助复杂解剖的器械选型。在 TAVR 场景中，可预测瓣架形态、瓣周漏路径、冠脉阻塞风险及传导异常风险，为术者提供决策支持。
- [[实体/dasi|DASI]]：DASI（由 DASI Simulations 开发）是一个面向 TAVR 手术的 AI 辅助术前决策平台，整合机器学习、患者 CT 解剖数据与患者特异性 3D 模拟，生成风险预测、器械推荐及瓣膜尺寸建议。其核心功能之一是冠脉阻塞风险建模，通过冠脉距离、冠脉直径、相对瓣叶高度和 radial flow gap 等参数评估风险，能将大多数 CT 判定的高风险病例重新分类为低风险。在 redo TAVR 等复杂场景中，DASI 还可对不同器械落点策略进行数字化分析，为临床团队提供是否存在可行经皮方案的具体结论。
- [[实体/ziekenhuis-oost-limburg|Ziekenhuis Oost-Limburg]]：比利时医疗机构，本报告讲者Nicolas Van Mieghem所在单位。

## 关键概念
- [[概念/永久起搏器植入|永久起搏器植入]]
- [[概念/digital-twin|digital twin]]
- [[概念/bicuspid-aortic-valve-tavr|bicuspid aortic valve TAVR]]
- [[概念/contact-pressure-index|contact pressure index]]
- [[概念/finite-element-analysis|finite element analysis]]
- [[概念/automated-tavr-planning|automated TAVR planning]]

## 要点
- AI工作流分为预测、专家解释、heart team决策三步，AI提供精准性，专家提供视角
- MSCT一次采集可支持诊断、二叶瓣表型、冠脉、TAVR sizing、并发症预测和终身管理等多项决策
- PRECISE-TAVI研究：接触压力指数预测新PPI的AUC 0.83，预测>trace PVL的AUC 0.69
- Mimics for TAVR自动规划与3-MENSIO一致率SAPIEN 90%、Navitor 87%、Evolut 88%，时间从9分钟降至1分钟
- TAVR规划分为4个层级，越罕见的解剖越依赖人类专家，AI提供地图，专家决定路径
