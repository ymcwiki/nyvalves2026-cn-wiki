# 超越多普勒：瓣膜运动学实现主动脉瓣狭窄严重度的快速单切面评估

## 核心要点

* 研究问题是：仅分析主动脉瓣叶受限和运动学特征，能否准确区分 AS 严重度，而不依赖 Doppler、AVA、压差和流速。
* 内部回顾性队列包含223份超声心动图：无 AS 65例、中度 AS 69例、重度 AS 89例。
* 外部验证队列包含270例：无 AS 96例、中度 AS 73例、重度 AS 101例。
* 算法只使用单一胸骨旁长轴（PLAX）切面，提取瓣叶角位移、速度和加速度，再由机器学习模型分类严重度。
* 内部队列准确率84.4%、总体 AUC 0.96；外部队列准确率85.2%、总体 AUC 0.94。

### 题目与单位

本研究题为“Beyond Doppler: Valve Kinematics Enables Rapid, Single-View Assessment of Aortic Stenosis Severity”，中文可译为“超越多普勒：瓣膜运动学实现主动脉瓣狭窄严重度的快速单切面评估”。讲者为 Farhan Mohammed, PhD，来自澳大利亚悉尼 Victor Chang Cardiac Research Institute 的 Heart Valve Disease and AI Lab。

### 利益关系声明

Farhan Mohammed 声明没有任何需要披露的财务关系。幻灯片提示 faculty disclosure 信息可在会议 app 中查看。

### 致谢

共同作者包括 Thomas Meredith、Amy Pomeroy、Heath Adams、Thomas Moran、Sebastiano Barbieri、Erik Meijering、David Roy、Jason Kovacic、Christopher Hayward、David Muller、Michael Feneley 和 Mayooran Namasivayam。

### 背景与研究目的

主动脉瓣叶受限是主动脉瓣狭窄（AS）严重度的关键决定因素。传统评估使用 Doppler、主动脉瓣面积（AVA）、跨瓣压差和流速。瓣膜运动学（Valve Kinematics）关注瓣叶位移、速度和加速度。

研究目的为评估：是否仅通过研究瓣膜受限本身，就能准确分类 AS 严重度。

### 方法

研究使用覆盖完整 AS 谱系的回顾性队列，共223份超声心动图，其中无 AS 65例、中度 AS 69例、重度 AS 89例。输入影像只取单一胸骨旁长轴（PLAX）切面。研究团队开发计算机视觉算法，用于捕捉瓣叶角位移、速度和加速度。随后使用机器学习模型对 AS 严重度进行分类。

外部验证使用独立队列，共270例患者，其中无 AS 96例、中度 AS 73例、重度 AS 101例。

### 总体结果：内部与外部队列

内部队列和外部队列的 ROC 曲线，均使用 LogisticRegression 分类器。

内部队列 n=223，总体准确率为84.4%，总体 AUC 为0.96。ROC 图横轴为 false positive rate，纵轴为 true positive rate，坐标均从 0.0 到 1.0。图例显示：NoAS 类 AUC=1.00，ModerateAS 类 AUC=0.94，SevereAS 类 AUC=0.95。

外部队列 n=270，总体准确率为85.2%，总体 AUC 为0.94。外部队列图例显示：NoAS 类 AUC=0.99，ModerateAS 类 AUC=0.90，SevereAS 类 AUC=0.93。

### 内部队列 ROC 结果

内部队列 n=223 的多分类 ROC 曲线，准确率 84.4%，总体 AUC 0.96。

内部队列 ROC 曲线标题为“ROC Curves for LogisticRegression”。横轴 false positive rate，纵轴 true positive rate，坐标均从 0.0 到 1.0，黑色虚线为随机分类参考线。三条曲线分别为：NoAS，AUC=1.00；ModerateAS，AUC=0.94；SevereAS，AUC=0.95。页面底部强调内部队列准确率84.4%，总体 AUC 0.96。

### 外部验证 ROC 结果

外部队列 n=270 的多分类 ROC 曲线，准确率 85.2%，总体 AUC 0.94。

外部队列 ROC 曲线同样使用 LogisticRegression。横轴 false positive rate，纵轴 true positive rate，坐标均从 0.0 到 1.0。三条曲线分别为：NoAS，AUC=0.99；ModerateAS，AUC=0.90；SevereAS，AUC=0.93。页面底部强调外部队列准确率85.2%，总体 AUC 0.94。

### 临床影响

该方法支持单一 PLAX 切面评估，不需要 Doppler 测量。分析时间可从约40 分钟降至数秒。潜在价值在于改善工作流程效率和可扩展性。

### 结论

瓣膜运动学可以在不使用 Doppler 的情况下，对 AS 严重度进行清晰分型。模型在不同队列中表现一致。该方法是一个快速、单切面的工具，有潜力简化临床 AS 评估工作流程。
