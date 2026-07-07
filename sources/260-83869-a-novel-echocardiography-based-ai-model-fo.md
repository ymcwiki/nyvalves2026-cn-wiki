# 基于超声心动图的 AI 模型预测主动脉瓣狭窄进展

## 核心要点

* 主动脉瓣狭窄进展存在明显个体差异：相同的 mild AS 起点，3 年后可表现为稳定 mild AS，也可进展为 severe AS + HF。
* 既往中度 AS 纵向队列显示快进展与临床结局恶化相关：全因死亡 adjusted HR 1.77，HF admission/CV death HR 1.76，AVR HR 3.44。
* 本项目目标是用结构化超声报告参数建立 AS 进展预测模型，数据来自本地超声注册库，基础规模超过 500K+ patients，且只使用 echo-report parameters。
* 外部验证使用 Rabin 与 Sheba 多中心协作。内部队列 2,870 例，外部队列 1,666 例，年龄、性别、LVEF 和心腔尺寸总体接近。
* 模型在 1 年、3 年、5 年预测的 AUC 均约 0.88-0.91；外部验证最大 AUC 下降不超过 0.03。
* 局限包括没有临床结局、缺失数据和泛化性仍有限；下一步是临床终点预测、基于图像分析、规模化部署和个体化风险管理。

### 题目与讲者

报告题为“A Novel Echocardiography-Based AI Model for Predicting Aortic Stenosis Progression”，中文可译为“基于超声心动图的 AI 模型预测主动脉瓣狭窄进展”。讲者为 Leor Perl, MD，来自 Rabin Medical Center，以色列。

### 利益关系披露

讲者披露过去 24 个月与患者使用医疗产品相关企业存在财务关系。Grant/Research Support 来自 Edwards Lifesciences；Consultant Fees/Honoraria 来自 Abbott Laboratories；Individual Stock(s)/Stock Options 分别涉及 PreClusion、Powerful Medical 和 Holosis Health。所有相关财务关系均已处理，教师披露信息可在会议 app 中查看。

### AS 起点相同，路径不同

同样从 mild AS 出发，3 年后患者 A 稳定，患者 B 进展为 severe AS + HF。

基线示例为 mild AS：AVA 1.4 cm²，mean gradient 18 mmHg，EF 60%，NYHA I。经过 3 年随访后，患者 A 仍为 mild AS 且稳定，AVA 1.3 cm²，mean gradient 21 mmHg，EF 60%，NYHA I，无症状。患者 B 则进展为 severe AS + HF，AVA 0.8 cm²，mean gradient 52 mmHg，EF 40%，NYHA III，有症状并出现心力衰竭。

### 无症状重度 AS 预后因素：钙化程度

N Engl J Med 2000 数据：中重度钙化者事件-free survival 明显更差。

该页引用 N Engl J Med 2000;343:611-7，标题为“Predictors of Outcome in Severe, Asymptomatic Aortic Stenosis”。Kaplan-Meier 曲线纵轴为 event-free survival，横轴为 years。No or mild calcification 组随访曲线较平缓，moderate or severe calcification 组快速下降，组间差异 P<0.001。风险人数显示 no or mild calcification 组在 0、1、2、3、4 年分别为 25、23、20、17、9；moderate or severe calcification 组分别为 101、48、38、21、7。

### 快速流速增加后的事件-free survival

1 年内流速增加 >0.3 m/s 的 AS 患者，之后 event-free survival 快速下降。

本页同样引用 N Engl J Med 2000;343:611-7。对象为 AS 患者且 1 年内峰速增加 >0.3 m/s。横轴为 observation of rapid velocity increase 后的年份，纵轴为 event-free survival。曲线在第 1 年前后迅速降至约 30%，到 3 年约 15%。风险人数为 34、12、7、5。

### 既往中度 AS 纵向队列：个体进展率概念

JACC Advances 2024：540 例中度 AS 中，快速进展与死亡、AVR、HF admission 增加相关。

该页介绍“Prediction of the Individual Aortic Stenosis Progression Rate and its Association With Clinical Outcomes”，JACC Advances 2024;3:100879。这是一项 retrospective longitudinal cohort study，纳入 540 例 moderate AS 患者。快速进展示例患者为 80 岁，有 AF、CKD 和 LV hypertrophy，瓣膜从 mild 到 moderate 再到 severe，并伴随 mortality、AVR 和 HF admissions 增加。慢进展示例患者为 60 岁，有 COPD，从 mild 到 moderate，横向时间轴为 0-4 年。

### 既往研究流程：慢进展与快进展分组

2011-2022 年 686 例中度 AS，最终分为慢进展 270 例和快进展 270 例。

流程图显示，2011-2022 年 moderate aortic stenosis 患者 n=686。排除 n=144，原因包括 AVR/P n=58，少于 2 次 TTE n=54，TTE 间隔少于 6 个月 n=16，subvalvular AS n=16。剩余有 2 次或以上 TTE 的患者 n=542，其中 2 例因 AVA 测量不足无法计算 slope 被排除。

最终 slow progressors n=270，AVA 斜率 -0.04，范围 -0.06 至 0.00 cm²/year；rapid progressors n=270，AVA 斜率 -0.15，范围 -0.22 至 -0.11 cm²/year。

### 快进展与临床结局

快速进展者全因死亡、HF admission/CV death 和 AVR 风险更高。

图 A 为 all-cause mortality，slow 与 rapid 两条 event-free survival 曲线逐渐分离，adjusted HR 1.77，95% CI 1.26-2.48。图 B 为 CV mortality，adjusted HR 1.89，95% CI 0.81-4.38。图 D 为 HF admissions/CV death，adjusted HR 1.76，95% CI 1.22-2.53。图 E 为 AVR，快速进展者更早接受 AVR，adjusted HR 3.44，95% CI 2.55-4.64。

### 挑战：建立新的 AS 随访范式

本页提出挑战：build a new paradigm for AS surveillance。新范式需要具备四个特征：personalized、predictive、pragmatic、fair。也就是从固定间隔随访转向个体化、可预测、实际可部署并且公平的 AS 监测策略。

### 本地超声注册库模型构建

模型构建流程：本地超声注册库、500K+ 患者、仅使用超声报告参数；测试集混淆矩阵显示 375 TN、64 FP、102 FN、433 TP。

项目流程包括 3 步：1，local echo registry；2，500K+ patients；3，echo-report parameters only。右侧展示 JACC Advances 2025 年文章“Prediction of Aortic Stenosis Progression Using Artificial Intelligence: A Machine Learning Model”，作者包括 Edward Itelman、Yaron Shapira、Alon Shechter、Nadav Loebl、Yuval Altman、Leor Perl 和 Ran Kornowski。

测试集 ROC 曲线显示整体 AUC 约 0.90。混淆矩阵以真实标签 No ASG 与 ASG、预测标签 No ASG 与 ASG 交叉：真实 No ASG 被判为 No ASG 375，被判为 ASG 64；真实 ASG 被判为 No ASG 102，被判为 ASG 433。性别分层 ROC 显示 female AUC 0.93，male AUC 0.89。

### 问题与解决方案：AI 模型泛化

左侧说明 AI models don't travel well；右侧用 Rabin 和 Sheba 多中心协作作为解决方案。

本页左侧指出问题：AI models don't travel well。图中横轴为 external performance difference，显示多项外部验证中 AUC、accuracy、sensitivity、specificity 或其他性能指标在外部数据上下降。右侧提出解决方案：multi-site collaboration。图中列出 Rabin Medical Center Beilinson-Hasharon 与 Sheba Tel HaShomer City of Health，通过多中心协作来验证模型泛化能力。

### 内部与外部队列基线特征

内部队列 2,870 例，外部队列 1,666 例；多数基础超声和体型指标接近。

| 变量 | Internal cohort | External cohort |
| --- | --- | --- |
| Number of unique patients | 2,870 | 1,666 |
| Age, years | 74.8 ± 11.4 | 73.6 ± 13.5 |
| Female | 46.8% | 48.7% |
| Aortic valve mean gradient, mmHg | 27.6 ± 8.7 | 24.4 ± 7.6 |
| Left ventricular ejection fraction, % | 59.9 ± 7.0 | 59.7 ± 6.4 |
| Interventricular septum thickness, cm | 1.2 ± 0.2 | 1.2 ± 0.2 |
| Left ventricular end-diastolic diameter, cm | 4.6 ± 0.6 | 4.7 ± 0.6 |
| Left ventricular end-systolic diameter, cm | 2.9 ± 0.7 | 2.9 ± 0.6 |
| Weight, kg | 75.3 ± 15.6 | 76.6 ± 15.6 |
| Height, cm | 163.9 ± 9.6 | 165.1 ± 9.7 |
| Body surface area, m² | 1.8 ± 0.2 | 1.8 ± 0.2 |

### 1、3、5 年 ROC：外部验证性能保持

1 年、3 年、5 年模型在测试集与外部队列的 AUC 均接近。

1 年 ROC curve 中，test AUC 0.89，external AUC 0.91。3 年 ROC curve 中，test AUC 0.88，external AUC 0.88。5 年 ROC curve 中，test AUC 0.90，external AUC 0.87。外部数据最大性能差为 0.03 AUC。

### CatBoost 模型特征重要性

CatBoost 特征重要性：主动脉瓣平均压差和瓣口面积权重最高。

特征重要性图的横轴为 importance score，单位为 relative influence %。最重要变量为 aortic valve mean gradient，约 27%；其次为 aortic valve area，约 18%；age 约 9%；Doppler velocity index 约 9%；aortic valve maximum gradient 约 8%；stroke volume 约 5%；interventricular septum thickness 约 4%。其后依次包括 aortic root diameter、left ventricular ejection fraction、pulse、left ventricular end-diastolic diameter、left atrial diameter、body surface area、ascending aorta diameter、left ventricular outflow tract diameter、weight、height、left atrial area、left ventricular end-systolic diameter、biological sex 和 left ventricular posterior wall thickness，单项影响多在 0-3% 范围。

### 局限性

局限性包括三点：没有临床结局，no clinical outcomes；存在 missing data；泛化性仍有限，limited generalizability。也就是说，目前模型更偏向结构化超声进展预测，尚未直接证明对死亡、住院、AVR 或管理策略改善的临床获益。

### 下一步路线图

下一步包括临床终点预测、基于图像分析、规模化部署和个体化风险管理。

The road ahead 包括 4 项：1，clinical endpoints prediction；2，image based analysis；3，deploy at scale，ongoing；4，personalized risk-based management。右侧展示多张超声图像，提示未来将从结构化报告进一步扩展到图像级特征。

### 结论

讲者总结三点。第一，机器学习模型可从结构化超声心动图数据准确预测主动脉瓣狭窄进展，AUC 0.90-0.91。第二，模型跨机构泛化时性能损失很小，ΔAUC ≤0.03，回应了 AI 泛化能力不足的问题。第三，这一方法有助于从固定随访间隔转向个体化 precision medicine。

### 致谢

最后一页为 Special Thanks，展示团队合影和机构照片，没有新增研究数据。
