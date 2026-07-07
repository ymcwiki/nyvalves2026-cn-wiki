# 基于 AI 的心电图筛查工具

## 核心要点

* 讲者提出结构性心脏病（SHD）的筛查缺口：65 岁以上成人 1/8有临床显著 SHD，但约一半患者未被诊断。
* EchoNext 被定位为 ECG AI 生物标志物，目标是从常规心电图识别所有形式 SHD 的高风险人群，已筛查50 万+美国人。
* SAGE/CACTUS 试点在纽约都会区8 个城市急诊开展，AI 组为1,135例，usual care 组为1,699例。
* AI 组接受 TTE 的比例为443/1,135（39.0%），usual care 为284/1,699（16.7%）；SHD 阳性 TTE 为184/1,135（16.2%）对151/1,699（8.9%）。
* 90 天内 Class 1/2A 管理改变为 AI 组70/1,135（6.2%），usual care 组66/1,699（3.9%）。
* 操作模式强调“远程筛查”：CACTUS 团队根据 EHR 和 EchoNext 标记决定是否安排门诊超声，讲者强调下单前从未见过这些患者。

### 重新设计结构性心脏病筛查工作

标题页写作“Reimagining the Work”。讲者为 Pierre Elias, MD，职务包括 Columbia University 心脏病学与生物医学信息学助理教授，以及 NewYork-Presbyterian Hospital 人工智能医学主任。

### 利益披露

讲者披露，在此前24 个月内曾与生产、营销、销售、转售或分销患者使用医疗产品的公司存在财务关系。Grant/Research Support：Amyloidosis Foundation、Eidos Therapeutics、Pfizer、Janssen Pharmaceuticals、Edwards Lifesciences、GE Healthcare。Equity：Pathway Labs, Inc.。幻灯片注明所有财务关系均已缓解，讲师披露信息可在会议 app 中查看。

### 结构性心脏病的筛查缺口

Pathway Labs 对 SHD 筛查缺口的三点概括：患病率、诊断不足和结局。

页面题为“The Gap - Structural Heart Disease”，核心句为：目前尚没有针对全球最常见死因的筛查测试。幻灯片把缺口分成三类：第一，患病率，65 岁以上成人 1/8有临床显著结构性心脏病，多数人在症状进展前并不知道；第二，诊断，约一半患者未被诊断，只有一部分高风险患者能做超声心动图，路径受可及性、费用和转诊阻力影响；第三，结局，疾病在失代偿前常保持沉默，未治疗 SHD 会推动心衰、卒中和过早死亡，早期发现可改变病程轨迹。

### EchoNext 的部署和影响

EchoNext 被呈现为覆盖所有 SHD 形式的 ECG AI 生物标志物，并列出筛查量、诊断增幅和论文影响。

页面题为“Impact - Evidence and Deployment”。讲者称 EchoNext 是“世界首个用于所有形式结构性心脏病的 ECG AI 生物标志物”。四个结果卡片依次为：已筛查50 万+美国人；在8 个急诊科中新发 SHD 诊断近2 倍增加，具体数值写为91%；Nature 2025 发表后成为最被阅读的心脏 AI 论文，标注“#1”；由 AI 促成的三个“world firsts”包括二尖瓣修复、主动脉瓣置换和心脏移植。

### SAGE 研究题名

页面介绍“The SAGE Study”，全名为“Structural Heart Disease Diagnosis Using Artificial IntelliGence in Urban Emergency Departments”，即在城市急诊使用人工智能诊断结构性心脏病。

### SAGE 方法与终点

研究设计为病例对照研究，覆盖纽约市都会区8 个城市急诊科（ED）。AI treatment arm 在 ED 患者中实施整合式 AI-ECG 系统，用于识别尚未诊断的 SHD；usual care arm 使用前一年同一人群，并追踪结局。

纳入/排除标准包括：年龄≥40 岁且 EchoNext 评分高风险的成人；既往没有 SHD 诊断，过去2 年内没有 TTE。排除或不适用情形包括预期寿命<2 年，例如转移性癌症或严重合并症；住在护理机构、晚期痴呆或显著活动受限。

试点终点有两项。第一，新发 SHD 诊断率，定义包括 LVEF ≤45%、中度或重度 RV 功能障碍、中度或重度瓣膜性心脏病（VHD）、估测肺动脉收缩压≥45 mmHg的肺高压、左室肥厚（室间隔/后壁≥1.5 cm）或中大量心包积液。第二，TTE 后90 天内 Class 1 或 Class 2A 临床管理改变。

### CACTUS 试点流程

CACTUS 试点设计：ED 心电图经 EchoNext 标记高风险后，由团队查阅病历并决定是否协调门诊超声。

流程从 ED visit with ECG 开始，EchoNext AI model 计算 SHD 风险；若 ECG 被 EchoNext 标记为高风险，患者仍接受 ED work-up，同时 CACTUS Team 评估电子病历图表。团队若同意安排检查，RN care manager 协调门诊超声心动图，患者在门诊接受 echo；若不同意，则不进入该超声路径。该流程发生在急诊处置决策时点。

缩写说明：ED 为 emergency department，RN 为 registered nurse，EHR 为 electronic health record。此处 SHD 包括任一以下情况：左室射血分数（LV ejection fraction）≤45%，左室壁厚≥1.3 cm，中重度瓣膜性心脏病，RV 收缩功能障碍，中大量心包积液，肺动脉收缩压≥45 mmHg，或三尖瓣反流速度≥3.2 m/s。

### 主要执行结果：TTE 与 SHD 阳性 TTE

AI 组较 usual care 组有更高 TTE 完成比例和更高 SHD 阳性 TTE 比例。

| 指标 | AI Intervention | Usual Care |
| --- | --- | --- |
| 研究组样本量 | N=1,135 | N=1,699 |
| 接受 TTE | 443（39.0%） | 284（16.7%） |
| SHD 阳性 TTE | 184（16.2%） | 151（8.9%） |

左侧柱状图纵轴为患者百分比，范围从0%到50%，显示“Underwent TTE”。右侧柱状图纵轴为患者百分比，范围从0%到20%，显示“SHD-positive TTE”。两张图的横轴均为 Study Group。

### 90 天内 Class 1/2A 管理改变

AI 介入组中达到 Class 1/2A 管理改变的比例高于 usual care。

| 指标 | AI Intervention | Usual Care |
| --- | --- | --- |
| 研究组样本量 | N=1,135 | N=1,699 |
| Class 1/2A Management Changes | 70（6.2%） | 66（3.9%） |

图表纵轴为患者百分比，刻度显示0%、2%、4%、6%、8%。横轴为 Study Group。AI 组柱高约6.2%，usual care 组柱高约3.9%。

### EchoNext 下单超声数量

页面为单句结论：在 NewYork-Presbyterian（NYP）过去12 个月内，EchoNext 下单的超声心动图数量超过任何单个临床医生。

### EchoNext 的阳性率

页面为单句结论：EchoNext 在 NYP 的阳性率高于任何单个临床医生。

### 远程筛查模式

页面强调流程特征：团队在为患者下单超声前从未见过任何患者。这对应 P7 的 CACTUS 模式，即依赖 ECG AI 风险信号和病历审核触发门诊 TTE。

### 公众传播案例

纽约时报页面截图：以 ECG AI 发现被误认为哮喘的严重心脏问题为公众传播案例。

最后一页展示纽约时报报道截图。截图的要点是，医生最初认为患者为哮喘，但 AI 从心电图中提示严重心脏问题；报道说明 AI 程序可识别人类容易漏掉的 ECG 模式，并有项目计划免费提供给医生使用。截图中还可见“Listen: 5:48 min”和分享、收藏、评论等网页控件，主图为胸前贴 ECG 电极的照片，图注提到一项临床试验中 AI 程序从45 岁患者心电图中发现可能严重心脏损害的证据。
