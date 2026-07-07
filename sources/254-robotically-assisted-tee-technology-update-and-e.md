# 机器人辅助 TEE：技术更新与早期临床经验

## 核心要点

* 结构性心脏病影像需求与人力供给之间存在缺口：美国估计有 5M 非瓣膜性房颤患者、5.6M 中重度二尖瓣/三尖瓣反流患者，而相应年手术量分别约 100K 和 22K。
* ROB’E 远程控制机器人 TEE 系统将 TEE Guide、TEE Base 和 RCR Controller 分开，目标是让超声系统与控制器远离射线源，并可重复调用理想探头位置。
* ROB’E 首次人体测试纳入 5 例，5 个目标切面均获得，平均用时 12:10 ± 5:28 min；存储视图再现性 75%，用时 16:28 ± 5:18 sec。
* Laza AI 软件利用超过 1000 个 CT 和超过 100 个 TEE 建模，一次 3D 容积扫描后可在少于 1 秒内检测预定义超声切面。
* 首次人体 AI 软件研究为前瞻性、单中心、单臂，n=8；AI 处理图像 99% 被评为 adequate 或以上，68% 被评为 excellent。
* 讲者强调 AI 与机器人 TEE 不是替代影像专家，而是扩展影像能力、标准化图像获取，并扩大复杂结构性心脏病介入的可及性。

### 标题与讲者

本报告题为“Robotically Assisted TEE: Technology Update and Early Clinical Experience”，中文可译为“机器人辅助 TEE：技术更新与早期临床经验”。讲者为 Scott M. Chadderdon, MD，来自 Oregon Health & Science University。

### 利益关系披露

讲者说明，在过去 24 个月内与生产、营销、销售、转售或分销患者医疗产品的公司存在财务关系。研究资助来自 Phillips、GE Healthcare 和 Siemens。顾问费或讲课费来自 Edwards Lifesciences 和 Medtronic Inc.。个人股票或股票期权为 Laza Medical, Inc.。专利或版税受益为 None，管理职务或所有权权益为 None，其他财务利益为 None。所有相关财务关系均已缓解，教师披露信息可在会议 app 中查看。

### 患者需求与心脏科人力之间的缺口

结构性心脏病和相关介入需求增长，而结构超声心动图专家人力受培训、支付和射线暴露等因素限制。

非瓣膜性房颤方面，美国估计患者数为 5M，美国每年相关手术约 100K。中重度二尖瓣和三尖瓣反流方面，美国估计患者数为 5.6M，美国每年 TTMr/R 手术约 22K。页面中央用跷跷板示意说明，单纯依靠增量生产率提升并不足够。

右侧为美国心脏科劳动力问题：预计到 2037 年短缺 8,650 名心脏科医师；美国 46% 的县没有心脏科服务可及性。结构超声心动图医师短缺预计会更严重，原因包括需要大量额外培训、支付结构和报销问题、累积射线暴露。

### 用新技术弥合缺口：ROB’E 机器人辅助 TEE

ROB’E Remote-Control Robotic TEE 系统由 TEE Guide、TEE Base 和 RCR Controller 组成，图中同时展示 GE Vivid E95 与 6VT-D TEE 探头。

该页提出通过开发并实施新技术来弥合缺口，重点是机器人辅助 TEE 的开发。系统名为 ROB’E Remote-Control Robotic (RCR) TEE system。

A 为 TEE Guide，用于固定柔性胃镜，可推进、回撤和稳定探头，并带有力限制器。B 为 TEE Base，用于固定 TEE 手柄，支持轴向旋转、前屈/后屈，以及右/左屈曲旋钮操作。C 为 RCR Controller，是探头操控界面，可存储和保存探头位置。右侧照片标注为 GE Vivid E95 with 6VT-D TEE probe and ROB’E System。引用：Schewel J. et al. Concept, Design, and Preclinical Testing of a Remote-Control Robotic System for Transesophageal Echocardiography. Structural Heart. 2024;8(6)。

### 机器人辅助 TEE 工作流和体外测试

概念验证工作流和硅胶心脏模型体外测试，右侧显示机器人装置、控制器、心脏模型和超声图像。

概念验证工作流包括：医生进行食管插管，并将探头设置在 guide/base 中；超声系统和控制器远离射线源；实现 TEE 探头全远程控制；可调用已存储设置；能够从高度、旋转、屈曲和 omniplane angle 快速且可靠地返回理想图像。右侧为 in vitro testing，使用 silicon heart model。引用同为 Schewel J. et al. Structural Heart. 2024;8(6)。

### ROB’E 首次人体测试

ROB’E 首次人体测试比较“今天”的人工 TEE 工作流与“明天”的机器人 TEE 工作流，强调射线安全和图像采集标准化。

ROB’E 首次人体测试包括 5 例患者，均接受标准 TEE 加 RCR 引导 TEE。所有患者在全身麻醉下进行。影像目标包括 4C、3C、AV SAX、bicaval 和 LAA。安全性方面，在操作前后均进行 EGD。

首次人体结果：5 例中，3 例用于瓣膜性心脏病，2 例用于 PFO。RCR 测试中，全部 5 个目标切面均获得，耗时 12:10 ± 5:28 min。存储视图测试显示 75% 再现性，耗时 16:28 ± 5:18 sec。引用：Schewel J. et al. Robotic Transesophageal Echocardiography. First-in-Human Experience. JACC: Cardiovasc Imag. 2025;18(8):934-36。

### 第二部分：Laza Medical Intelligent TEE System

Laza Medical Intelligent TEE System 是用于心血管介入的 AI 驱动、机器人辅助影像系统，包含可调机器人臂、现成 TEE 探头和 AI 集成影像软硬件。

该页将技术方向扩展到 Laza Medical Intelligent TEE System。系统定位为用于心血管介入的 AI-powered、robotically-assisted imaging system。图中标注组件包括 adjustable robotic arm、off-the-shelf TEE probe，以及 AI integrated software and hardware imaging system。

页面免责声明：Laza Medical System 仍在开发中，尚未获准在美国或世界任何地区使用。版权标注为 @2026 Laza Medical。

### AI 引导软件如何完成全心 3D 重建与导航

一次 3D 容积扫描后，AI 软件识别心腔并生成患者特异性全心 3D 模型，再自动定位预定义超声切面。

AI 软件通过分析超过 1000 个 CT 和超过 100 个 TEE，并标注心脏结构而建立。通过一次心脏 3D volume scan，AI 软件可以识别心腔，并创建患者特异性的全心 3D 模型。系统可在少于 1 秒内自动检测预定义超声切面。影像医师和/或介入心脏病医师可以使用控制面板选择感兴趣图像。

页面免责声明：Laza Medical System 仍在开发中，尚未获准在美国或世界任何地区使用。版权标注为 @2026 Laza Medical。

### AI 软件可行性测试：首次人体研究设计

首次人体 AI 软件研究使用单个中食管 3D 数据集，评估 AI 从实时 3D 数据计算 7 个标准 TEE 切面的能力。

| 项目 | 内容 |
| --- | --- |
| 研究 | 前瞻性、单中心、单臂研究，n=8 |
| PI | Scott Chadderdon 与 Firas Zahr，OHSU |
| 目的 | 评估 AI 从 3D 实时数据计算 7 个预定义标准 TEE 切面的能力 |
| 方法 | 8 例患者接受 SOC TEE，入组时间为 2025 年 7 月至 8 月；每例患者采集单个 mid-esophageal 3D 数据集 |
| 主要终点 | AI 计算切面平面准确性，由 3 名独立结构超声专家评分 |

页面还标注“The 7 Views”。页面免责声明：Laza Medical System 仍在开发中，尚未获准在美国或世界任何地区使用。版权标注为 @2026 Laza Medical。

### AI 计算切面示例

AI 从 3D 容积中提取 2D 切面，视图平面计算处理时间为 100 ms，评分标准为解剖完整性与方向。

该页显示 AI-calculated view planes 示例。视图平面计算处理时间为 100 ms。这些 2D view planes 来自 3D volume，评估标准为 anatomical completeness 与 orientation。

| 切面 | 3 名评分者评分 | Excellent 比例 |
| --- | --- | --- |
| LAX | 5、5、5 | 95% |
| Aortic SAX | 5、5、5 | 81% |
| Mitral Comm. | 4、5、4 | 71% |
| RV inflow/Outflow | 3、4、4 | 57% |

页面免责声明：Laza Medical System 仍在开发中，尚未获准在美国或世界任何地区使用。版权标注为 @2026 Laza Medical。

### Render Study 结果

Render Study 结果显示，多数 AI 处理图像达到良好或优秀，评分量表为 1 非诊断、2 次优、3 可接受、4 良好、5 优秀。

| View Planes | N | Mean (SD)，1-5 分 |
| --- | --- | --- |
| Overall | 147 | 4.49 ± 0.75 |
| 5-Chamber | 21 | 4.05 ± 0.97 |
| 4-Chamber | 21 | 4.71 ± 0.46 |
| Mitral Commissural | 21 | 4.52 ± 0.68 |
| 2-Chamber | 21 | 4.38 ± 0.80 |
| LAX | 21 | 4.81 ± 0.51 |
| SAX | 21 | 4.48 ± 0.75 |
| RV Inflow/Outflow | 21 | 4.48 ± 0.81 |

总体上，99% 的 AI 处理图像被评为 adequate 或以上，68% 被评为 excellent。评分定义为：1 非诊断，2 次优，3 adequate，4 good，5 excellent。

| 切面 | Suboptimal | Adequate | Good | Excellent |
| --- | --- | --- | --- | --- |
| Overall | 约 1% | 12% | 19% | 68% |
| 5Ch | 5% | 24% | 24% | 47% |
| 4Ch | 0 | 0 | 24% | 76% |
| MC | 0 | 10% | 19% | 71% |
| 2Ch | 0 | 19% | 24% | 57% |
| LAX | 0 | 0 | 10% | 90% |
| SAX | 0 | 5% | 14% | 81% |
| RV In/Out | 0 | 24% | 19% | 57% |

图例还列出 Non-diagnostic，但本页堆叠条没有显示明确的非诊断比例。页面免责声明：Laza Medical System 仍在开发中，尚未获准在美国或世界任何地区使用。版权标注为 @2026 Laza Medical。

### 这项技术将走向何处

该页用学习驾驶或辅助驾驶的图片作比喻，表达机器人和 AI 影像技术从辅助到更高自主度的演进方向。

页面标题为“Where is this Technology Headed?”，画面中是一名学习驾驶者与指导者在车内的图片。该视觉隐喻用于说明技术正向更成熟的辅助控制和导航能力发展。

页面免责声明：Laza Medical System 仍在开发中，尚未获准在美国或世界任何地区使用。版权标注为 @2026 Laza Medical。

### 下一代可能性

下一代可能性包括：TEE 探头管理反馈，涵盖高度、平面、倾斜视图和反馈传感器；自动确定最佳超声角度和 omniplane，以实现影像和操作目标；针对器械植入的主动阴影管理策略；针对 LAA 或二尖瓣的经房间隔路径，用于 m-TEER 和 TMVR；TEER 治疗中的位置、轨迹、方向或瓣叶抓取支持；TTVR/TMVR 治疗中的位置、轨迹和瓣环释放支持。

### 为什么影像医师和介入心脏病医师应支持 AI 与机器人 TEE

结尾页强调 AI 与机器人 TEE 的目标是增强影像专家能力、扩大实践范围，并改善结构性心脏病介入可及性。

在创新层面，讲者强调这项技术不会替代影像专家，而是增强专业能力并扩展实践范围。它可以使复杂影像能力更可普及，并扩大结构性心脏病手术的可及性。

在进步层面，目标是改善患者可及性、患者照护和患者结局。右侧图像再次展示 Laza 系统渲染图、机器人辅助操作场景、当前临床 TEE 场景，以及未来机器人 TEE 场景，其中未来图像标注 radiation safety 和 standardized image acquisition。
