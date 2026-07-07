# EuroSMR 评分预测不同二尖瓣反流病因患者 M-TEER 后 1 年死亡：REPAIR 研究

## 核心要点

* EuroSMR 原本是用于 SMR 患者 M-TEER 后 1 年死亡预测的 AI 风险模型，包含 18 个变量，既往阈值为 52.5 分。
* REPAIR 注册研究纳入 2,580 例 2019-2024 年接受 PASCAL M-TEER 的患者，中位年龄 80 岁，女性 44.2%。
* 按病因分层：SMR 1,307 例，50.7%；PMR 847 例，32.8%；MMR 426 例，16.5%。
* EuroSMR 在 SMR 中区分度最好但仍属中等，AUC 0.67；PMR 的 AUC 为 0.58；MMR 的 AUC 为 0.57，且高低风险 1 年事件率相同。
* 讲者认为， contemporary 队列、心衰治疗进步和患者选择变化，可能解释该评分在现代队列中表现不如开发队列。

### 题目与讲者

本研究题为“The EuroSMR Score for Predicting 1-Year Mortality After Transcatheter Edge-to-Edge Repair Across Mitral Regurgitation Etiologies: The REPAIR Study”，中文可译为“EuroSMR 评分预测不同二尖瓣反流病因患者经导管缘对缘修复后 1 年死亡：REPAIR 研究”。讲者为 Felix Rudolph, MD。

### 利益关系披露

Felix Rudolph 声明没有需要披露的财务关系。幻灯片提示，教师披露信息可在会议 app 中查看。

### 研究背景

EuroSMR Score 是一个风险模型，包含 18 个变量，用于预测继发性二尖瓣反流 SMR 患者接受 M-TEER 后的 1 年死亡风险。既往研究确定 52.5 分 可区分“低风险”和“高风险”患者。

该模型来自一个大型 M-TEER 注册队列，纳入 2008-2019 年接受治疗的患者。它在当代 SMR 患者中的表现，以及在 PMR 原发性二尖瓣反流和 MMR 混合性二尖瓣反流患者中的表现，仍不清楚。

脚注文献为 Hausleiter 等，题名“Artificial intelligence-derived risk score for mortality in secondary mitral regurgitation treated by transcatheter edge-to-edge repair: the EuroSMR risk score”，发表于 European Heart Journal，2024，DOI 为 https://doi.org/10.1093/eurheartj/ehad871。

### EuroSMR 在线计算器与 18 个预测变量

EuroSMR 在线计算器截图及 AI-based risk predictors 的 SHAP 变量重要性图。

本页展示 EuroSMR Risk Score Online Calculator。页面地址为 https://www.eurosmr.com/eurosmr-risk-score/8c1d641ead0ce48b。计算器说明该分数为 AI 派生风险评分，用于预测接受二尖瓣 M-TEER 患者的 1 年结局；开发和验证使用了超过 4,600 例 M-TEER 患者，包含 18 个临床、超声、实验室和用药参数。

左侧 score widget 可输入或选择变量，截图中可见 Age、NYHA、BMI、COPD、Diabetes mellitus 等字段，并有“Determine EuroSMR Score now”按钮。右侧 SHAP 图横轴为 SHAP value，左侧代表 survival likely，右侧代表 death likely；颜色条表示 feature value 从低到高。

| 变量 | 图中重要性数值 |
| --- | --- |
| NT-proBNP | 0.298 |
| NYHA | 0.134 |
| Haemoglobin | 0.090 |
| TAPSE | 0.066 |
| Age | 0.066 |
| eGFR | 0.059 |
| RA area | 0.059 |
| sPAP | 0.054 |
| LVEDV | 0.034 |
| TR grade | 0.030 |
| Diabetes mellitus | 0.029 |
| RVmid diameter | 0.023 |
| EROA mitral | 0.023 |
| BMI | 0.020 |
| LA volume | 0.014 |
| LVEF | 0.013 |
| Triple GDMT | 0.010 |
| COPD | 0.001 |

### 研究方法

REPAIR 的全称为 Registry of Pascal for mItral Regurgitation，是一项研究者发起、多中心的 M-TEER 患者注册研究，纳入 2019-2024 年接受治疗的患者。所有数据，包括二尖瓣反流病因，均由研究中心报告。

患者根据 EuroSMR 阈值 52.5 分 分为“低风险”或“高风险”。主要终点为 1 年全因死亡。

### 总体结果与病因分布

研究总样本量为 N=2,580。患者年龄为 80 岁，中位数，四分位距 74-84 岁；女性比例为 44.2%。按二尖瓣反流病因分组，SMR 为 n=1,307，占 50.7%；PMR 为 n=847，占 32.8%；MMR 为 n=426，占 16.5%。

### SMR 结果：评分可区分高低风险

SMR 亚组中高风险组 1 年死亡率更高，ROC AUC 为 0.67。

SMR 亚组 EuroSMR 分数为 50.1 分，四分位距 41.8-57.4 分。按 52.5 分阈值，SMR 高风险患者占 41.5%，SMR 低风险患者占 58.5%。

左侧 Kaplan-Meier 生存曲线纵轴为 survival，横轴为 time since intervention，范围 0-12 个月。低风险组蓝线在整个随访期高于高风险组红线，log-rank P<0.001。观察到的事件率为：SMR 高风险 19.6%，95% CI 15.6-23.5%；SMR 低风险 8.6%，95% CI 6.1-11.0%。换算为 1 年生存率约为高风险 80.4%，低风险 91.4%。

右侧 ROC 图题为“EuroSMR Score and 1-Year Mortality [SMR]”，纵轴 sensitivity，横轴 1-specificity。AUC 为 0.67，95% CI 0.61-0.72，显示区分度中等。

### PMR 结果：有统计区分，但区分度有限

PMR 亚组高风险组 1 年死亡率较高，log-rank P=0.016，但 ROC AUC 仅 0.58。

PMR 亚组 EuroSMR 分数为 43.6 分，四分位距 35.2-52.5 分。按阈值分层，PMR 高风险占 24.1%，PMR 低风险占 75.9%。图例中使用 DMR low-risk 与 DMR high-risk，和本页 PMR 结果对应。

Kaplan-Meier 曲线显示低风险组蓝线高于高风险组红线，log-rank P=0.016。观察事件率为：PMR 高风险 14.3%，95% CI 8.3-19.9%；PMR 低风险 7.8%，95% CI 5.2-10.3%。对应 1 年生存率约为高风险 85.7%，低风险 92.2%。

右侧 ROC 图题为“EuroSMR Score and 1-Year Mortality [PMR]”。AUC 为 0.58，95% CI 0.50-0.67，说明虽然高低风险生存曲线有差异，但总体区分能力有限。

### MMR 结果：高低风险无区分

MMR 亚组高低风险 1 年事件率相同，log-rank P=0.72，AUC 为 0.57。

MMR 亚组 EuroSMR 分数为 47.4 分，四分位距 38.6-54.2 分。按阈值分层，MMR 高风险占 32.9%，MMR 低风险占 67.1%。

Kaplan-Meier 曲线中蓝色低风险组和红色高风险组几乎重叠，log-rank P=0.72。观察事件率完全相同：MMR 高风险 10.7%，95% CI 5.9-15.4%；MMR 低风险 10.7%，95% CI 4.1-16.8%。对应 1 年生存率两组均约 89.3%。

右侧 ROC 图题为“EuroSMR Score and 1-Year Mortality [MMR]”。AUC 为 0.57，95% CI 0.47-0.68，置信区间跨越 0.5 附近，说明在 MMR 中预测区分能力很弱。

### 总结与解释

讲者总结，EuroSMR score 能够在 SMR 和 PMR 中区分生存与死亡患者，但在 MMR 中不能区分。总体区分性能在 SMR 中为 modest，即中等或有限；在 PMR 和 MMR 中更有限。

可能解释包括：REPAIR 是更当代的患者队列，可能反映了心力衰竭治疗进步和患者选择改善。因此，来自 2008-2019 年开发队列的评分，在 2019-2024 年当代 M-TEER 实践中的泛化表现下降。
