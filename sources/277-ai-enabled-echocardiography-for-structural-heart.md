# 结构性心脏病介入中的 AI 超声心动图：最新进展与未来展望

## 核心要点

* 瓣膜病误诊仍常见，AI 的近期定位不是替代医生，而是可扩展的“第二读片”，用于发现临床报告可能漏判或低估的病例。
* MR 六级分类中，多切面模型优于单 A4C 模型：weighted kappa 0.87 vs. 0.80，±1 级准确率 96% vs. 91%，严重 MR AU-ROC 0.96 vs. 0.93。
* 部署方式会改变认知偏倚：并行 AI 辅助可能增加 automation bias；“人工先读、AI 后读、临床最终审核”更有机会保留独立判断。
* Delineate 前瞻性阶段目标是识别误诊 MR 和 TR；AI-临床不一致病例的专家复核不一致率更高：MR 49.3% vs. 16.0%，TR 40.0% vs. 13.5%。
* 示例病例中，临床报告为中度 MR，但 AI 提示显著 MR，专家组判定重度 MR：RV 63 mL、RF 50%；进一步 3D 定量显示 RV 80 cc、RF 65%、EROA 0.44 cm²。

### 题目与讲者

幻灯片题目为 “AI-Echo for VHD: Better Diagnosis, Fewer Mistakes?”，讲者 Timothy Poterucha, MD，Mayo Clinic 医学助理教授。讲座聚焦 AI 在瓣膜病超声诊断中的应用：能否改善诊断并减少错误。

### 利益披露

过去 24 个月内，讲者与生产、营销、销售、再销售或分销患者使用医疗产品的公司存在财务关系。研究/资助支持：Pfizer、BridgeBio、Janssen。个人股票/股票期权：Baxter、Abbott。版税/专利受益：Columbia University / Pathway Labs。讲者同时是 AI-ECG 算法 EchoNext 的发明人，未来可能获得版税。其他研究支持包括 Tianqiao & Chrissy Chen Institute、CV Prospective Award、NIH R01HL177055、American Heart Association 奖项 933452 和 23SCISA1077494。所有相关财务关系已完成缓解。

### 病例起点：约 60 岁女性气短

病例以一名约 60 岁女性因气短就诊开始。此页没有影像或数据，主要引出后续 MR 严重程度判断问题。

### MR 到底多重？临床报告为中度

多切面彩色多普勒图像显示二尖瓣反流喷射，右下角问题为“MR 有多严重？”临床报告写作 Moderate。

页面展示多幅二维和彩色多普勒超声图像，包括胸骨旁/心尖视图中的反流喷射。右侧文字提出问题 “How severe is the MR?”，临床报告结论为 Moderate，即中度 MR。该页用于提示：传统读片可能低估 MR 严重度。

### 人为错误与变异性

本页展示 Institute of Medicine 报告封面 “To Err is Human: Building a Safer Health System”。讲者借此强调：临床误差存在，诊断变异性是常态，不是例外。

### AI 读片管线：从片段识别到研究级诊断

AI 工作流：识别相关 clips、clip 级分类、study 级诊断。

工作流由左至右：先从超声检查中识别相关 clips，再进行 clip-level classification，最后汇总为 study-level diagnosis。页面中心提问：Could AI help? 下方文字为 “To err is human (even if AI is not divine)” 和 “Variability is the rule, not the exception”。引用 Coisene et al, Arch Card Dis 2020 与 Biner et al, JACC Cardiovascular Imaging 2010。

### MR 模型内部测试：多切面模型优于 A4C 单切面

MR 六级分类混淆矩阵与 A4C-only / multiple-view 模型性能比较。

左侧混淆矩阵的纵轴为心脏科医生临床解读，横轴为 AI model prediction；四个等级为 none/trace、mild、mild-moderate or moderate、moderate-severe or severe。

| 临床解读 \ AI 预测 | none/trace | mild | mild-moderate or moderate | moderate-severe or severe |
| --- | --- | --- | --- | --- |
| none/trace | 5,499 | 382 | 12 | 0 |
| mild | 608 | 1,097 | 169 | 1 |
| mild-moderate or moderate | 14 | 276 | 675 | 68 |
| moderate-severe or severe | 2 | 1 | 43 | 140 |

| 内部测试指标 | A4C-only model | Multiple-view model |
| --- | --- | --- |
| MR 6 step classification：weighted kappa | 0.80 [0.775, 0.827] | 0.87 [0.849, 0.885] |
| MR 6 step classification：accuracy | 48% [0.447, 0.509] | 55% [0.524, 0.585] |
| MR 6 step classification：±1 accuracy | 91% [0.891, 0.927] | 96% [0.948, 0.972] |
| Moderate or greater：AU-ROC | 0.92 [0.902, 0.941] | 0.95 [0.932, 0.960] |
| Severe：AU-ROC | 0.93 [0.900, 0.957] | 0.96 [0.951, 0.976] |

来源：Long A et al, Circulation 2024。

### TR 与 AR 模型：三尖瓣和主动脉瓣反流混淆矩阵

TR 与 AR 的 AI 解读矩阵，纵轴为心脏科医生解读，横轴为 AI interpretation。

三尖瓣反流矩阵如下：

| TR 医生解读 \ AI 解读 | none | mild | mild-moderate or moderate | moderate-severe or severe |
| --- | --- | --- | --- | --- |
| none | 4,711 | 397 | 18 | 0 |
| mild | 647 | 1,093 | 217 | 0 |
| mild-moderate or moderate | 22 | 174 | 716 | 59 |
| moderate-severe or severe | 0 | 2 | 42 | 101 |

主动脉瓣反流矩阵如下：

| AR 医生解读 \ AI 解读 | none | mild | mild-moderate or moderate | moderate-severe or severe |
| --- | --- | --- | --- | --- |
| none | 6,585 | 232 | 4 | 1 |
| mild | 169 | 721 | 90 | 0 |
| mild-moderate or moderate | 2 | 66 | 214 | 35 |
| moderate-severe or severe | 0 | 0 | 20 | 45 |

来源：Long et al, EHJ 2025。

### 问题转换：AI 如何部署到超声解读流程？

本页提出问题：“How do we deploy AI for echocardiography interpretation?”，即 AI 应如何进入超声心动图解读流程。它是从模型性能过渡到临床部署策略的章节页。

### 标准流程：医生开单、技师采图、人工解读、生成报告

传统超声流程：开单、采图、技师与心脏科医生解读、生成报告。

标准路径为：provider orders echocardiogram；sonographer acquires images；sonographer & cardiologist interprets images；echo report is generated。上方回环箭头提示报告可能反馈给后续临床决策与再次检查。

### 两种 AI 部署方式：并行辅助读片与人工先读后 AI 复核

并行 AI 辅助读片与 human-first sequential AI review 的流程差异。

并行 AI-assisted read：sonographer acquires images 后，AI 与人工解读并行参与，最后生成 echo report。另一种 human-first sequential AI review：sonographer acquires images 后先进行 independent human-first read，形成 echo report drafted，随后 AI second read，最后 clinical final review。讲者倾向于后一种方式，因为它可先保留人工独立判断，再利用 AI 做第二读片。

### 临床使用 AI 的偏倚：信太多与听太少

AI 使用中的 automation bias、own-information bias 与 optimal strategy。

页面标题为 “How should I use AI in my echo practice?” 图中左侧为 automation bias，右侧为 own-information bias，中间交叉区域为 optimal strategy。Automation bias 指我们对 AI 结果的信任超过应有程度；own-information bias 指即使应当听取 AI，也因为已有判断而忽视 AI 结果。额外风险为 de-skilling，即临床技能退化。

### DELINEATE 前瞻性阶段目标

DELINEATE prospective phase 的目标是识别误诊的 MR 和 TR：Goal: identify misdiagnosed MR and TR。

### DELINEATE 研究流程：不一致组与一致组均进入专家复核

DELINEATE 前瞻性阶段流程图，包括纳入、排除、深度学习分析、专家组复核和主要/次要终点。

纳入为 comprehensive TTEs，要求 >60 clips，并评估 MR 和 TR。排除标准包括：limited or follow-up studies；severely limited quality；intraprocedural studies；prior echo within 2 days to 3 months；complex congenital heart disease；left ventricular assist device；prior valve intervention。若临床医生和 AI 均评估瓣膜反流 <moderate，则也排除。

流程为：comprehensive TTEs 进入 deep learning model analysis；若 DL 与 clinician 对 MR/TR 的评估存在 ≥1 级差异，进入 MD-AI discrepancy group；若 DL 与 clinician 对 MR/TR 的评估无差异，进入 MD-AI concordance group。两个组均进入 expert panel review，结局分类为反流严重度改变或不改变。

主要终点：临床医生与专家组对 MR 和 TR 严重度评估之间的不一致率。次要终点：具有临床意义的不一致率，定义为 ≥2 级差异或升级到 severe。

### 结果：AI 找出被误分类病例

MR 与 TR 中，MD-AI 不一致组较一致组有更高的 adjudication-clinical discordance。

纵轴为 adjudication-clinical discordance (%)。MR 图中，MD-AI concordance 组为 16.0%，MD-AI discrepancy 组为 49.3%。TR 图中，MD-AI concordance 组为 13.5%，MD-AI discrepancy 组为 40.0%。图中误差线未给出具体数值，但明显显示不一致组的专家判定修正率更高。

### 病例回看：AI 提示显著 MR，专家复核为重度 MR

同一病例的多切面彩色多普勒图像，AI 预测 significant MR，专家组评估 severe MR。

右侧文字给出判定链：AI predicted significant MR，随后 panel review 判定 severe MR。定量结果为 RV 63 mL，RF 50%。这与 P4 的临床报告 Moderate 形成对照，说明 AI 第二读片可能发现被低估的严重 MR。

### 专家复核定量：风湿性二尖瓣病与重度 MR

3D TEE 与彩色多普勒显示风湿性二尖瓣病、A2/P2 与 A3/P3 内侧 coaptation gap，以及重度 MR。

专家描述为：图像符合 rheumatic mitral valve disease；瓣膜内侧在 A2/P2 与 A3/P3 之间存在 coaptation gap，并伴 severe mitral regurgitation。

3D QD 定量：regurgitation volume 80 cc，regurgitant fraction 65%，EROA 0.44 cm²。3D planimetry 测得 VCA 0.48 cm²，计算 regurgitant volume 116 cc。这些数字均支持临床报告“中度”对该病例的低估。

### 结论：AI 是可扩展第二读片，不是替代者

结论 1：VHD 误诊仍是顽固问题，AI 可能提高处理这类问题的能力。

结论 2：部署策略很重要。Concurrent AI assistance 可能增加 automation bias；human-first AI review 可能保留独立解读。

结论 3：近期 AI 的角色不是替代医生，而是可扩展的第二读片，用于避免错误。讲者联系方式：[邮箱已隐去]。
