# MitralValveAi：从标准心脏 CT 到患者特异性二尖瓣数字孪生

## 核心要点

* 报告的实际主题是 TEER 规划数字孪生：从 CT 到解剖，再到血流动力学预测，目标是在夹子释放前评估不同 TEER 策略。
* 当前规划主要依赖 CT、TEE 和术者经验，能看见解剖，但不能在治疗前测试不同夹子策略。
* 作者的假设是：患者特异数字孪生可重建瓣膜、模拟修复，并预测不同夹子策略对跨二尖瓣血流动力学的影响。
* 系统路径为 CT → segmentation → valve reconstruction → simulation；进一步从 anatomy → mechanics → flow → gradient。
* 示例中，虚拟 TEER 可给出预测跨二尖瓣压差，如 P7 的 predicted transmitral gradient 4.2 mmHg。
* P15 的虚拟夹策略比较显示，越积极的夹合方案 MR 降幅越大，但压差越高：中央双夹 aggressive 方案峰值/均值压差达 13.8/6.1 mmHg，超过平均压差 >5 mmHg 的二尖瓣狭窄警戒线。

### 题目：TEER 规划的数字孪生

幻灯片题目为“A Digital Twin for TEER Planning: From CT to Anatomy to Hemodynamic Prediction”，即用于 TEER 规划的数字孪生，从 CT 进入解剖建模，再进入血流动力学预测。讲者为 Kaoutare Chbini, MD。

### 利益关系披露

Kaoutare Chbini 声明没有需要披露的相关财务关系。

### 科学问题：夹子释放前能否预测结果

本页提出核心问题：在部署夹子之前，能否预测结果？这不是单纯判断夹子是否能夹住，而是希望在 TEER 前预判修复后的血流动力学后果，包括残余 MR 与跨二尖瓣压差之间的平衡。

### 夹子应放在哪里

解剖示意图显示 TEER 常见目标区域：A1-P1、A2-P2、A3-P3。

本页问题为“Where Should We Place the Clip?”图中以二尖瓣瓣叶对应关系标出三个可能夹合区：外侧/前外侧区域 A1-P1，中央区域 A2-P2，内侧/后内侧区域 A3-P3。这些位置的选择会同时影响 MR 消除程度和术后二尖瓣口面积/跨瓣压差。

### TEER 的核心取舍：修复反流，避免狭窄

TEER 需要减少残余 MR，但也要避免造成术后二尖瓣狭窄；示意图中给出平均跨二尖瓣压差 5 mmHg 的例子。

本页标题为“The TEER Trade-Off”。左侧显示 residual MR，中间为 TEER 夹合，右侧为 transmitral gradient。示例超声频谱标出 mean gradient 5 mmHg；右侧速度坐标以 m/s 标注，关键刻度为 0、0.5、1.0、1.5 m/s。页面底部总结治疗目标：fix the regurgitation，avoid creating stenosis，即修复反流，同时避免新造成狭窄。

### 当前规划依赖解剖：能看见，不能试策略

当前 TEER 规划主要依靠 CT、TEE 和术者经验，能够识别解剖，但不能在介入前测试不同方案。

现有规划依赖三类信息：CT、TEE 和 experience。CT 图像用于看二尖瓣与心腔结构；TEE 提供二维、多平面、3D 和彩色多普勒信息；术中屏幕和操作者经验用于把影像转化为操作决策。页面底部给出限制：we can see anatomy；we cannot test strategy。也就是说，目前能看到结构，却不能在真实治疗前量化比较策略。

### 研究假设：治疗前测试策略

数字孪生工作流：重建患者瓣膜、模拟修复、预测血流动力学后果；示例预测跨二尖瓣压差为 4.2 mmHg。

本页提出“What If We Could Test Before We Treat?”流程分三步。第一，reconstruct the patient’s valve，重建患者瓣膜。第二，simulate the repair，模拟 TEER 修复。第三，predict the hemodynamic consequence，预测血流动力学后果。右侧示例显示 predicted transmitral gradient 4.2 mmHg。

右侧速度图的色标为 velocity，单位 m/s，范围从 0 到 1.5。右侧压差曲线图以 mmHg 为单位，纵轴关键刻度为 0、4、8、12 mmHg。页面底部的假设为：患者特异性数字孪生可以在介入前预测不同夹子策略的影响。

### 为什么选择 CT

从全相位原始 CT 转换到跳动的 4D 心腔模型，理由包括全心覆盖、全相位、可重复和可扩展。

本页回答“Why CT?”左侧为 raw CT（all phases），右侧为 4D chambers（beating）。选择 CT 的理由包括：whole heart、all phases、reproducible、scalable。也就是 CT 覆盖全心、包含心动周期各相位，数据可重复，并适合扩展到标准化工作流。

### 构建数字孪生的四步流程

数字孪生构建流程：CT、分割、瓣膜重建、模拟。

本页标题为“Building the Digital Twin”。流程由左到右依次为 CT、Segmentation、Valve Reconstruction、Simulation。也就是说，先从 CT 获取原始数据，再完成结构分割，随后重建二尖瓣模型，最后进行模拟。

### 科学挑战：预测夹合前的血流动力学结果

本页将科学挑战明确为：能否在部署夹子前预测血流动力学结果？这个挑战把问题从“图像上的夹合位置”推进到“夹合后的跨瓣血流、压差和残余反流”预测。

### 二尖瓣动态重建：训练模型读取瓣膜

动态 CT 重建被用作瓣膜运动参考，模型通过叶瓣跟踪、逐相位重建和钙化映射来恢复患者特异机械属性。

本页标题为“Dynamic Reconstruction of the Mitral Valve”，副标题为“Training Our Model to Read The Valve”。训练内容包括 leaflet tracking、phase-by-phase reconstruction、calcification mapping，以及 keep separate annotation。右侧多张 CT 小图显示不同相位下的彩色标注，用于捕捉 valve dynamics。

页面底部说明：dynamic CT reconstruction serves as the reference motion of the valve。通过匹配这一运动，physics model 可以恢复 CT 不能直接测量的患者特异性机械属性。

### 从解剖到生理

从 Anatomy 到 Mechanics，再到 Flow 和 Gradient，表示数字孪生从结构建模进入血流动力学预测。

本页流程为 From Anatomy to Physiology。箭头依次连接 Anatomy、Mechanics、Flow、Gradient。含义是：先建立解剖模型，再赋予机械属性，随后求解流动，最终得到跨二尖瓣压差。

### 从 CT 解剖到患者特异生理：体积、流量和压差

由 CT 推导左室体积和 dV/dt 流量条件，再通过连续性方程和 Bernoulli 关系预测跨二尖瓣速度与压差。

本页标题为“From CT Anatomy to Patient-Specific Physiology”。左图为 LV Volume (CT)，横轴 t(s) 从 0.0 到 0.8 秒，纵轴单位 mL，关键刻度约为 80、100、120、140、160 mL。曲线从约 155 mL 下降到约 90 mL，随后回升到约 155 mL。

中图为 Flow = dV/dt of LV，横轴 t(s) 同为约 0.0 到 0.8 秒，纵轴单位 mL/s，关键刻度从约 -400 到 200 mL/s。蓝色代表 transmitral inflow（diastole），黄色代表 aortic ejection（systole）。黄色收缩期射血曲线最低约到 -350 mL/s；蓝色舒张期跨二尖瓣流入出现多峰，峰值大约在 80-100 mL/s 区间。

右图为 0D preview（continuity + Bernoulli）。红线为 transmitral velocity，公式为 V = Q/A，单位 m/s；蓝色虚线为 gradient，公式为 ΔP = 4V2，单位 mmHg。横轴 t(s) 约从 0.4 到 0.8 秒；左纵轴速度约为 0.5 到 2.5 m/s，右纵轴压差约为 0 到 25 mmHg。三次舒张峰中，速度峰大致约 1.7、1.8、1.9 m/s，对应压差峰约 12-18 mmHg。页面底部总结：从 CT 得到的患者特异流量条件可用于预测跨二尖瓣血流动力学和多普勒压差。

### 虚拟 TEER：从 CT 到血流动力学评估

虚拟 TEER 界面展示数字孪生和虚拟夹操作；右侧示意夹子压力、瓣叶几何/运动和血流动力学之间的平衡求解。

本页标题为“Virtual TEER”。左侧界面显示 MitraClip 虚拟操作，夹子位置下拉框为 A2-P2 (central)，同时显示 cut-plane/long axis、transmitral gradient、blood speed 等窗口；示例状态包含 35% R-R systole 和 regurg 32 ml/s 等界面读数。底部流程为 CT → Digital Twin → Virtual Clip → Hemodynamic Assessment。

右侧框图写明：“An equilibrium: push the clip, the balance re-settles”。clip pressure 作用于 LEAFLETS，叶瓣模块包含 geometry 和 motion；LEAFLETS 与 HEMODYNAMICS 双向耦合，血流动力学模块包含 flow 和 gradient，输出 Δgradient。图中还标注 move one, the other follows；系统由 Newton’s laws 保持平衡，并迭代到 | free - recorded | < ε。

### 血流动力学影响：不同虚拟夹策略的压差比较

不同虚拟夹位置下的跨二尖瓣压差曲线：从术前到单夹、双夹，MR 降幅增加，同时峰值和平均压差上升。

本页标题为“Hemodynamic Impact”，左侧为 virtual clip placement 的三维模型，右侧曲线标题为“Transmitral gradient vs. virtual clip placement, v2\_case04 (OD preview)”。横轴为 t(s)，范围约 0.40 到 0.80 秒，标注为 diastolic filling。纵轴为 Δp，单位 mmHg，范围 0 到 16 mmHg。虚线水平参考线标注为 mitral stenosis caution，平均压差 >5 mmHg。

| 策略 | 曲线 | 峰值压差 | 平均压差 | MR 变化 |
| --- | --- | --- | --- | --- |
| baseline (pre-clip) | 蓝色实线 | 5.6 mmHg | 2.5 mmHg | 术前基线 |
| lateral single clip (conservative) | 绿色虚线 | 7.8 mmHg | 3.5 mmHg | MR ↓55% |
| central single clip (standard) | 黄色虚线 | 10.3 mmHg | 4.6 mmHg | MR ↓80% |
| central double clip (aggressive) | 红色虚线 | 13.8 mmHg | 6.1 mmHg | MR ↓92% |

图上三组舒张期峰值大致位于 0.44、0.59 和 0.76 秒附近。所有策略均较基线升高压差；中央双夹 aggressive 方案虽然 MR 下降比例最高，为 92%，但平均压差 6.1 mmHg 已越过平均压差 >5 mmHg 的警戒线。页面提出的问题是：which clip position minimizes post-TEER gradient?

### 超越解剖：介入前测试策略

本页描述端到端规划（End-to-End Planning）：上传 CT、重建 twin、模拟 repair、评估不同 strategies。作者强调该工具不是取代临床判断，而是增强决策制定。

### 当前阶段：概念验证与下一步

目前阶段为 proof of concept。已经展示的能力包括 CT-based reconstruction、dynamic digital twin、virtual TEER simulation 和 end-to-end workflow。

下一步包括提升 hemodynamic prediction accuracy，其中包含 full 3D CFD flow simulation 和 leaflet angular shape mechanics integration；还包括 chordae extraction，以及 clinical validation and decision impact。这些也是当前工作的主要局限：现阶段仍需验证预测精度、完善三维 CFD 和瓣叶/腱索力学，并证明其对临床决策的实际影响。

### 意义：从解剖指导到模拟指导

今天的流程是 Image → Procedure；设想中的明天是 Image → Simulation → Best Strategy → Procedure。

本页解释“Why This Matters?”今天的流程是 Image → Procedure，即影像后直接进入操作。明天的目标流程是 Image → Simulation → Best Strategy → Procedure，即先模拟，再选择最佳策略，然后实施操作。页面底部总结为：from anatomy-guided planning to simulation-guided planning。

### 总结与发布信息

总结语为“Test before we treat”。作者认为，患者特异性数字孪生可能允许在介入前对 TEER 策略进行虚拟评估。页面下方给出通知链接：pulsiondev.com/nyv2026，并附有二维码。
