# RESILIA 与旧代球囊扩张瓣中 percentage resizing 和 TAVR 后梯度

## 核心要点

* 研究为 2 中心回顾性观察研究，筛查 1,236 例 TAVR，排除 valve-in-valve 和 Medtronic 瓣后纳入 1,114 例；S3/S3 Ultra n = 600，S3 Ultra RESILIA n = 514。
* percentage resizing 定义为 [(THV nominal area / CT-derived annular area) - 1] × 100，分为 0-10% upsizing、10-20% upsizing、>20% upsizing、0-10% undersizing、>10% undersizing。
* 主要血流动力学终点为 90 天 TTE、VARC-3 标准下的高梯度（平均主动脉瓣压差 ≥ 20 mmHg）和中重度瓣周反流（PVR）。
* Firth bias-reduced logistic regression 显示 RESILIA 中 percentage resizing 每增加 1 SD，高梯度 odds 下降 54%，OR 0.46（95% CI 0.30-0.72）；非 RESILIA 中 OR 0.96（95% CI 0.74-1.25），不显著。
* 器械代际与 resizing 效应存在显著交互：interaction OR 0.48（95% CI 0.29-0.80），交互 p = 0.005；模型 AUC 0.704，Brier score 0.06。
* RESILIA 队列的最佳区间为 10-20% upsizing，梯度最低且平均 AE 负担最低；过度 upsizing（>20%）和任何 downsizing 均趋向更高梯度及更高 AE 负担。

### 题目与作者

标题页写作“Impact of Percentage Resizing on Hemodynamic and Safety Outcomes after Balloon-Expandable TAVR: SAPIEN S3/S3 Ultra versus S3 Ultra RESILIA”，中文可译为“球囊扩张式 TAVR 后 percentage resizing 对血流动力学和安全结局的影响：SAPIEN S3/S3 Ultra 对比 S3 Ultra RESILIA”。作者为 Vivek Joseph Varughese MD、Vince Vismara MD、Michael Cryer MD、Joseph Bates MStat。作者单位包括 Internal Medicine, Prisma Health Midlands 和 Department of Cardiology, Prisma Health Midlands。

### 利益关系披露

作者声明没有需要披露的财务关系，原文为“Authors DO NOT have any financial relationships to disclose.”

### 研究引言

瓣膜尺寸策略是球囊扩张式 TAVR 的核心，因为 undersizing 和过度 oversizing 都可能不利于血流动力学结局。PARTNER 3 子研究中，Ihdayhid 等显示，SAPIEN 3 的瓣环 oversizing 程度对血流动力学结局没有显著影响；主要决定因素是 prosthesis size，而不是 oversizing 程度。然而 RESILIA 平台具有不同的组织性质和瓣叶结构，因此该发现不一定能外推到更新一代瓣膜。现有文献对于瓣环 resizing 程度是否会在不同瓣膜代际中差异性影响血流动力学结局仍然有限。页脚参考文献为 Ihdayhid AR 等关于 PARTNER 3 中 annular oversizing、PVR 和瓣膜血流动力学的研究，发表于 *JACC Cardiovascular Interventions* 2021。

### 研究设计

研究为多中心回顾性观察研究，覆盖 2 个中心：Prisma Health Richland 和 Greenville；时间为 2021 年 1 月至 2025 年 9 月。共筛查 1,236 例 TAVR 手术，排除 valve-in-valve 和 Medtronic 瓣手术后，纳入 1,114 例。两组分别为 S3/S3 Ultra（n = 600）和 S3 Ultra RESILIA（n = 514）。

Percentage resizing 定义为：[(THV nominal area / CT-derived annular area) - 1] × 100。研究预设 5 个 resizing 类别：0-10% upsizing、10-20% upsizing、>20% upsizing、0-10% undersizing、>10% undersizing。IRB 信息为 2409494-1，项目题名为“Outcomes of TAVR using Balloon Expandable Valves across Resizing Strategies”，Prisma Health IRB，Exemption Category #4。

### 终点定义

主要血流动力学终点来自 90 天 TTE，并采用 VARC-3 标准。第一，高梯度定义为平均主动脉瓣压差 ≥ 20 mmHg。第二，PVR 定义为中重度瓣周反流（moderate-to-severe paravalvular regurgitation）。安全终点在住院期间或 ≤90 天内评估，包括新发左束支传导阻滞（LBBB）、永久起搏器植入（PPI）、装置栓塞和瓣环破裂。

### 统计方法

第一部分：连续变量的器械间差异使用 Wilcoxon rank sum test 评估 stochastic superiority/differences；分类变量的器械间比例差异使用 Pearson Chi-square test。主模型使用 Firth's bias-reduced logistic regression，因为事件较少，事件率为 6.73%。模型加入 percentage resizing 与 device 的交互项，以评估效应异质性，并校正年龄、术前梯度和左室瓣环钙化。由于事件率低、需保持模型稳定性，未纳入更多协变量。连续变量，包括 percent resizing、pre-gradient 和 age，按每 1 SD 增加进行标准化。另行分析 TAVR device diameter 在交互存在情况下的关联。

第二部分：为比较 5 个 resizing 类别之间的 TAVR 后平均梯度差异，研究使用 10% trim 的 Yuen trimmed ANOVA，并辅以 Kruskal-Wallis test。Kruskal-Wallis test 用于检验 resizing 类别之间的差异。两两比较使用 Benjamini-Hochberg procedure 进行修正，以比较 trimmed means 的差异。按 sizing 类别分析不良事件时，使用 adverse events 的平均值。

### 基线人口学与数据分布

年龄、性别、钙化和 LVEF 在 Non-RESILIA 与 RESILIA 队列中的分布。

| 图表 | Non-RESILIA | RESILIA | 统计检验/补充 |
| --- | --- | --- | --- |
| 年龄 | N 600，均值 78.7，中位数 80.0，标准差 9.4，最小 27.0，最大 99.0 | N 514，均值 74.1，中位数 75.0，标准差 9.0，最小 38.0，最大 95.0 | Wilcoxon rank sum test p < 0.0001；虚线为中位数，金色菱形为均值 |
| 性别 | 男性 26.6%，女性 23.0% | 男性 30.1%，女性 20.3% | p = 0.058，χ² test；Non-RESILIA N 505，RESILIA N 514，Female N 441，Male N 578 |
| 钙化 | Minimal/None 24.7%，Moderate/Severe 29.2% | Minimal/None 23.7%，Moderate/Severe 22.4% | p = 0.0657，χ² test；Non-RESILIA N 600，RESILIA N 514，Minimal/None N 539，Moderate/Severe N 575 |
| LVEF | N 599，均值 56.2，中位数 60.0，标准差 11.0，最小 20.0，最大 77.0 | N 514，均值 54.5，中位数 60.0，标准差 10.8，最小 19.0，最大 71.0 | Wilcoxon rank sum test p = 0.0002；虚线为中位数，金色菱形为均值 |

### 瓣膜直径分布与梯度-resizing 散点

上图为 TAVR 瓣膜直径分布，下图为平均梯度与 percent resizing 的散点图。

上方柱状图显示 device type 与 TAVR device diameter 的关系。图内列出 Non-RESILIA N = 600、RESILIA N = 514；直径分布为 20 mm：N 74，23 mm：N 441，26 mm：N 419，29 mm：N 180。各直径下柱状百分比分别为：20 mm，Non-RESILIA 3.6%、RESILIA 3.1%；23 mm，Non-RESILIA 21.0%、RESILIA 18.6%；26 mm，Non-RESILIA 21.1%、RESILIA 16.5%；29 mm，Non-RESILIA 8.2%、RESILIA 8.0%。图内注明未使用比例相等性检验。

下方散点图题为“Average Mean Gradient vs Percent Resizing, Grouped by Device Type”。横轴为 Percent Resizing，范围约 -50 至 145；纵轴为 Average Mean Gradient，范围约 0-70。绿色虚线位于平均梯度 20 mmHg，用于标记高梯度阈值。多数点聚集在 resizing 约 -25% 至 +25%、梯度 0-20 mmHg 区间；少数 outlier 梯度可达约 60-70 mmHg，也可见 resizing 高至约 145% 的点。图例中 Non-RESILIA 为黄色方点，RESILIA 为蓝色圆点。

### Firth 校正 logistic 回归：器械特异效应

预测 TAVR 后平均梯度 >20 mmHg 的概率曲线，RESILIA 中 percent resizing 增加与高梯度 odds 下降显著相关。

左侧图题为“Predicted Probabilities for Post TAVR Gradient > 20mmHg”。Device-specific adjusted odds ratios 显示：RESILIA 中 percent resizing 每增加 1 SD，高梯度 odds 的 OR 为 0.46（95% CI 0.30, 0.72）；Non-RESILIA 中 OR 为 0.96（95% CI 0.74, 1.25）。交互项为 RESILIA vs Non-RESILIA OR 0.48（95% CI 0.29, 0.80）。图下注明 odds ratio 和 profile likelihood 95% CI 来自 Firth bias-reduced logistic regression；预测概率根据术前梯度、年龄、钙化等协变量调整到均值和参考值。

右侧三条结论为：在 RESILIA 队列中，percent resizing 每增加 1 个标准差，高梯度 odds 降低 54%，置信区间具有统计学显著性，OR 0.46（0.30-0.72）。在非 RESILIA 队列中，percent resizing 每增加 1 个标准差，高梯度 odds 降低 4%，但置信区间不显著，OR 0.96（0.74-1.25）。模型 AUC 为 0.704，提示中等判别能力；Brier score 为 0.06。

### Firth 模型详细输出

Firth bias-reduced logistic regression 的惩罚最大似然估计、判别指标和部分 OR 估计。

| 参数 | DF | Estimate | Standard Error | Wald Chi-Square | Pr > ChiSq | Exp(Est) |
| --- | --- | --- | --- | --- | --- | --- |
| Intercept | 1 | -2.4334 | 0.1894 | 165.0907 | <.0001 | 0.088 |
| pct\_resizing | 1 | -0.0405 | 0.1358 | 0.0887 | 0.7659 | 0.960 |
| resilia = Resilia | 1 | -0.7385 | 0.2725 | 7.3458 | 0.0067 | 0.478 |
| pct\_resizing \* resilia = Resilia | 1 | -0.7274 | 0.2538 | 7.8963 | 0.0050 | 0.483 |
| age | 1 | -0.4948 | 0.1117 | 19.6192 | <.0001 | 0.610 |
| pre\_grad | 1 | 0.1542 | 0.1157 | 1.7768 | 0.1826 | 1.167 |
| cal\_mod\_sev = 0 | 1 | -0.0117 | 0.2482 | 0.0022 | 0.9622 | 0.988 |

| 模型判别指标 | 值 | 相关指标 | 值 |
| --- | --- | --- | --- |
| Percent Concordant | 70.4 | Somers' D | 0.408 |
| Percent Discordant | 29.6 | Gamma | 0.408 |
| Percent Tied | 0.0 | Tau-a | 0.052 |
| Pairs | 78,650 | c | 0.704 |

| OR 估计 | Unit | Estimate | 95% Confidence Limits |
| --- | --- | --- | --- |
| age | 1.0000 | 0.610 | 0.489-0.760 |
| pre\_grad | 1.0000 | 1.167 | 0.924-1.460 |
| cal\_mod\_sev 0 vs 1 | 1.0000 | 0.988 | 0.607-1.607 |

右侧文字强调：percent resizing 的效应随 device generation 不同而不同。percent resizing 每增加 1 SD 时，RESILIA 相比非 RESILIA 队列观察到梯度相关 odds 约 51% 更低。

### RESILIA 队列：五类 resizing 与梯度/AE 负担

RESILIA 队列中，10-20% upsizing 组显示最低平均不良事件负担，并处于较低梯度区间。

该页要点为：中度 upsizing（10-20% resizing）似乎产生最低的平均梯度和最低的 adverse event 负担；极端 downsizing（resizing < -10.0）与最高平均 AE 负担相关；Yuen trimmed ANOVA 和 Kruskal-Wallis 两个统计检验均确认 resizing 类别之间存在显著差异，Yuen trimmed ANOVA 的 F = 5.14、p = 0.00081，Kruskal-Wallis χ² = 21.92、p = 0.0002。

| RESILIA resizing 类别 | Max | Min | Nobs | Std | Median | Mean | AE 负担读图 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cat 1：0-10% upsizing | 19 | 3 | 171 | 4.5429 | 8 | 9.0474 | 约 0.11 |
| Cat 2：10-20% upsizing | 21 | 2 | 114 | 4.2577 | 8 | 9.5203 | 约 0.06，最低 |
| Cat 3：>20% upsizing | 21 | 5 | 28 | 5.8499 | 11.5 | 12.308 | 约 0.11-0.12 |
| Cat 4：0-10% downsizing | 22 | 3 | 148 | 4.911 | 10 | 11.008 | 约 0.16 |
| Cat 5：>10% downsizing | 20 | 4 | 55 | 7.6879 | 11 | 13.704 | 约 0.18，最高 |

图例说明蓝色箱线图为 mean gradient mmHg，绿色虚线为 average AE；中位数为红线，均值为橙色菱形。AE 负担由中重度 PVR、新发 LBBB 和永久起搏器植入（PPI）的发生率估计；未报告瓣环破裂或装置栓塞事件。

### RESILIA 队列：Benjamini-Hochberg 校正两两比较

五个 resizing 类别之间的 trimmed mean 差异，P 值经 Benjamini-Hochberg 程序调整。

本页图题为“Pairwise Comparisons Using Benjamini-Hochberg Correction By Resizing Category for Resilia”。横轴为 trimmed means 的差异，纵轴为 resizing category pair。图中标注的差异和 P 值包括：Cat 1 vs Cat 5：-2.32，p = 0.07；Cat 3 vs Cat 5：-0.89，p = 0.58；Cat 3 vs Cat 4：1.08，p = 0.42；Cat 2 vs Cat 4：-3.44，p = 0.0096；Cat 2 vs Cat 1：-1.46，p = 0.02；Cat 2 vs Cat 3：-2.5，p = 0.06；Cat 2 vs Cat 5：-3.22，p = 0.0096；Cat 1 vs Cat 4：-1.25，p = 0.03；Cat 1 vs Cat 3：0.22，p = 0.66。页脚说明估计值是 10% trimmed means 的差异，P 值用 Benjamini-Hochberg procedure 进行多重比较调整。

### RESILIA 队列：显著和不显著差异汇总

统计学显著差异（p < 0.05）包括四项。Cat 2（10-20% upsizing）vs Cat 4（0-10% downsizing）：trimmed mean difference -3.44，p = 0.0096。Cat 2 vs Cat 5（>10% downsizing）：trimmed mean difference -3.22，p = 0.0096。Cat 2 vs Cat 1（0-10% upsizing）：trimmed mean difference -1.46，p = 0.02。Cat 1 vs Cat 4：trimmed mean difference -1.25，p = 0.03。

未达统计学显著差异（p ≥ 0.05）包括五项。Cat 1 vs Cat 5：trimmed mean difference -2.32，p = 0.07。Cat 2 vs Cat 3（>20% upsizing）：trimmed mean difference -2.5，p = 0.06。Cat 3 vs Cat 5：trimmed mean difference -0.89，p = 0.58。Cat 3 vs Cat 4：trimmed mean difference 1.08，p = 0.42。Cat 1 vs Cat 3：trimmed mean difference 0.22，p = 0.66。

### 讨论：代际交互与 RESILIA 的 sizing 响应

percentage resizing 对 TAVR 后梯度 >20 mmHg 的影响取决于 device generation，交互作用显著，p = 0.005。在 RESILIA 中，percentage resizing 每增加 1 SD 与高梯度 odds 降低 54% 相关，OR 0.46，95% CI 0.30-0.72。在非 RESILIA 中，同样增加仅带来不显著的 4% odds 降低，OR 0.96，95% CI 0.74-1.25。

interaction OR 0.48（95% CI 0.29-0.80）确认 resizing 对 RESILIA 的效应相比非 RESILIA 具有约 51% 更低的高梯度 >20 mmHg 机会，提示 RESILIA 瓣膜对 sizing optimization 的响应具有代际特异性。研究新颖性在于证明了 device-generation-specific interaction，即更新的 RESILIA 瓣膜相较前代瓣膜，从 upsizing 获得的血流动力学获益被放大。

### RESILIA 最佳 resizing 区间：sweet spot

RESILIA 队列中，5 个 resizing 类别的梯度差异显著：Yuen trimmed ANOVA F = 5.14，p = 0.00081；Kruskal-Wallis χ² = 21.92，p = 0.0002。Category 2（10-20% upsizing）被认为是最佳范围，具有最低中位梯度，约 9.5 mmHg，并且平均 AE 负担最低。

两两比较确认：Cat 2 vs Cat 4（0-10% downsizing）差异 -3.44 mmHg，p = 0.0096；Cat 2 vs Cat 5（>10% downsizing）差异 -3.22 mmHg，p = 0.0096；Cat 2 vs Cat 1（0-10% upsizing）差异 -1.46 mmHg，p = 0.02；Cat 1 vs Cat 4 差异 -1.25 mmHg，p = 0.03。两端极值，即 >20% upsizing 和任何 downsizing，均趋向更高梯度和更高 AE 负担。该发现与 Ogami 等研究一致，后者发现 10-20% oversizing 与最低全因死亡率相关，HR 0.63，p = 0.02。

### 机制解释

SAPIEN 3 Ultra RESILIA 29 mm 瓣膜示意及机制解释：更薄瓣叶和不同连合设计可能使适度 upsizing 更容易转化为低梯度。

S3 Ultra RESILIA 采用更薄的心包瓣叶，厚度 0.28 mm 对比 0.36 mm，同时具有更高 tensile strength，并在 20 mm 和 23 mm 尺寸中重新设计连合附着，以减少 adhesive surface area 并促进更大的开口面积。这意味着当瓣膜被适当 oversize 时，更薄、更柔顺的瓣叶可以在扩张后的框架内充分打开，从而最大化有效瓣口面积并最小化梯度。

相反，较旧的 SAPIEN 3/Ultra 瓣膜瓣叶更厚，可能无法从 upsizing 中获得同等血流动力学收益，因为即使框架更大，较厚组织仍限制充分打开。RESILIA 的组织处理还可能改变所有瓣膜尺寸的流体动力学表现；即便在没有连合重新设计的 26 mm 和 29 mm 尺寸中，也观察到更低梯度。页脚参考 Delarive 等关于第五代球囊扩张式经导管心脏瓣膜组织处理和瓣叶设计影响的研究，发表于 *JACC Cardiovascular Interventions* 2026。

### 临床意义

临床含义包括三点。第一，RESILIA 的 sizing strategy 相比旧代瓣膜更重要。当术者在两个尺寸之间犹豫时，数据支持为 RESILIA 选择较大的瓣膜，也就是 10-20% oversizing。这与 PARTNER 3 数据一致：在边界瓣环中，较大 THV 可减少 PVR 并改善血流动力学。第二，过度 oversizing（>20%）会失去这项获益，可能原因包括瓣膜扩张不足、几何畸变或传导障碍风险增加。第三，模型 AUC 0.704、Brier score 0.06，提示判别力中等且校准良好；尽管研究具有探索性且存在未测量混杂、因罕见事件无法完全调整等局限，结果仍具有一定临床实用性。

### 研究局限：模型和数据限制

本探索性分析可能存在未测量混杂，且无法完成充分调整。即使 device 与 percent resizing 的交互稳定，引入完整调整模型仍可能改变估计值。研究没有 post-TAVR balloon dilatation、commissural alignment strategy 和 implantation depth 的数据，因此存在潜在混杂。主模型中由于事件罕见，加入更多协变量会带来过拟合风险；仅有 75 个事件和 1,026 个非事件，因此没有纳入额外协变量。由于随访有限，无法推断 percentage resizing 对长期血流动力学表现和结构性瓣膜退化的影响。研究还易受时间偏倚影响。复合 AE 负担将 LBBB、起搏器和瓣周反流合并为平均 adverse event burden，但这些事件实际上具有非常不同的临床权重和长期意义。

### 研究局限：探索性分析和外推性

该分析没有预设假设，属于 exploratory analysis。五个 resizing 类别之间的两两比较使用 Benjamini-Hochberg procedure 控制 false discovery rate，但仍属于探索性框架，因此结果应被视为 hypothesis-generating，而非 confirmatory。研究对更广泛实践环境、不同术者经验水平以及不同 CT sizing protocols 的外推性尚不确定。模型判别方面，AUC 0.704 表明判别力中等，可接受但并不优秀；这代表模型区分梯度 >20 mmHg 与 <20 mmHg 患者的能力。
