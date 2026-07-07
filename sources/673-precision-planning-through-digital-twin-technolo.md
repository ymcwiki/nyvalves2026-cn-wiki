# 数字孪生技术用于结构性心脏介入的精准规划

## 核心要点

* 传统 TAVR 规划依赖手工或自动测量，存在 15–20% 人为变异，且难以预测器械与器官相互作用。
* DASI 的数字孪生以生物力学模型和人类数据训练为基础，针对 BE 和 SE 瓣分别建模，可动态预测 THV、主动脉根部、钙化和组织变形。
* 冠脉阻塞预测使用 DLC/d 指标，示例页面显示 DLC 11.4 mm、d 4.1 mm、DLC/d 2.8；验证页给出阈值 0.7，并展示 n=1500 患者数据。
* 在 158 例 ViV/redo TAVR 队列中，DASI 将 28 例 CT 高危患者中的 25 例重新分类为低危，占 89.3%；其中 80%，即 20/25，无需 leaflet modification 即成功处理。
* 高钙解剖中的 root stretch 阈值为 1.7；术后压差预测示例给出平均压差 13 mmHg、峰值压差 23 mmHg；HALT 相关阈值约 20–23。

### 题目与讲者

本报告题为“Precision Planning Through Digital Twin Technology in Structural Heart Interventions (DASI Simulations)”，中文可译为：通过数字孪生技术实现结构性心脏介入的精准规划。

讲者为 Lakshmi Prasad Dasi, PhD, FACC。

### 利益相关披露

讲者说明，过去 24 个月内与生产、营销、销售、转售或分销用于患者或作用于患者的医疗产品的公司存在财务关系。所有财务关系均已 mitigation。教师披露信息可在会议 app 中查看。

| 财务关系性质 | 不合格公司或机构 |
| --- | --- |
| Grant/Research Support | NIH/NHLBI, DOD, NSF, AHA |
| Consultant Fees/Honoraria | 未列出 |
| Individual Stock(s)/Stock Options | DASI SIMULATIONS LLC |
| Royalties/Patent Beneficiary | Ohio State University, Georgia Tech, Emory University |
| Executive Role/Ownership Interest | DASI SIMULATIONS LLC |
| Other Financial Benefit | 未列出 |

### 动机：当前建模是否不够理想

传统 TAVR 手工规划、治疗决策局限，以及并发症给医疗系统带来的成本。

传统 TAVR 规划需要对每一种治疗选择进行手工测量，存在人为误差，变异约 15–20%；同时存在 sponsor analyses and bias。

治疗决策方面的不足包括：不能预测 device/organ interaction；无法区分不同治疗选项；算法基于平均人群而非患者个体；没有 lifelong planning tools。

Desai ND, ACC 2020 表格总结 N=52,561 例患者的端点分类：

| 端点类别 | 人数 | 百分比 |
| --- | --- | --- |
| 住院内或 30 天死亡 | 1671 | 3.2% |
| 住院内或 30 天卒中 | 1077 | 2.0% |
| 住院内或 30 天 VARC major/life-threatening/disabling bleeding | 3024 | 5.8% |
| AKI：住院内或 30 天显著肌酐升高或新发透析 | 336 | 0.6% |
| 住院内或 30 天中重度 PVL | 1304 | 2.5% |
| 以上均无 | 45149 | 85.9% |

按 95% 区间进行统计分类的医院数为：worse than expected 34/301，即 11%；as expected 242/301，即 80%；better than expected 25/301，即 8%。页面还标注并发症给医疗系统造成约 20 亿美元额外费用，每位 TAVR 患者归因成本 >8000 美元，并增加 2 天住院。

### 下一代建模范式

从 Tier 1 测量工具，到 Tier 2 传统计算建模，再到 Tier 3 数字孪生。

Tier 1 是每个治疗选项的手工或自动测量，仍有 15–20% 人为变异。页面列出 3mensio、Circle、Siemens Healthineers、Philips、HiD imaging 等规划或影像工具。

Tier 2 是传统计算建模，需要求解 governing equations，并依赖准确的材料属性，包括患者组织和专有器械材料属性。页面示意包括 without split 与 with split 的模型、raphe、leaflet calcium，以及 FEOPS 等工具。

Tier 3 是 digital twin，即基于生物力学、由人类数据训练的模型。它强调 interactive、scalable、accurate，并通过力学分辨来预测结局。该页右下角展示 DASI Simulations。

### DASI 预测建模如何工作

DASI 使用简化阶模型动态演化 THV 与解剖的三角网格，并输出支架/组织变形评估。

DASI 为每种瓣膜类型分别建模，包括 balloon-expandable, BE 和 self-expanding, SE。其 proprietary reduced order model 会演化一个 triangulated mesh model，覆盖经导管心脏瓣膜 THV 和解剖结构的各部分。

被建模的组成部分包括：stent，支架；native leaflets，自体瓣叶；individual calcific nodules，单个钙化结节；aortic root，主动脉根部。

模型训练数据集由术前 CT 与术后 CT 组成，融合物理表达与 data science。右侧动态输出显示 model output dynamic、stent/tissue deformation assessment，并在局部显示 contact region。页面结论为：相比传统 physics based models，更准确且更快。

### 生物标志物层：从部署参数到风险评估

预测建模用于优化部署参数和操作修改，并基于部署后解剖预测进行风险评估。

预测建模可优化 deployment parameters 和 procedural modifications。它预测 THV、主动脉解剖和钙化的变形，并基于 post-deployment anatomy 的预测进行风险评估。

页面脚注强调：该工具不是为了替代标准规划或 cardiac imager 分析，而是提供额外信息，并且 valve agnostic，即不依赖单一瓣膜品牌或类型。

### 互动数字孪生体验：冠脉

DASI 互动界面展示冠脉相关参数、瓣型选择、部署深度、扩张和旋转控制。

页面展示 Interactive Report 界面。顶部病例标识为 HS133325, 1 M，解剖为 Tricuspid；可选 SE 29 mm 与 BE 26 mm，截图中 BE 26 mm 高亮。

左上参数框显示 DLC 11.4 mm，d 4.1 mm，DLC/d 2.8。右侧角度显示 RAO 6、CAU 41。控制面板中选择 Coronary 标签，子标签包括 Pre-Deploy、Expansion、Coronary、Apposition、Stretch；冠脉选项有 Left Coronary 与 Right Coronary。

右侧显示 deployment depth 90.0%，界面刻度还标出 90% 和 80%；expansion level 为 +1 cc；sizing 显示 18.9% oversized；下方还有 rotation 滑条。

### 预测冠脉阻塞

冠脉阻塞预测以 DLC/d 为关键指标，并展示敏感性/特异性曲线与下游处理策略分布。

左侧 CT 图标注 RCA HEIGHT，读数为 R 11.1 mm。中间 3D 图示例标注 DLC/d =0.2。右侧定义图显示 DLC 和 d 的测量关系。

敏感性与特异性图横轴为 DLC/d，从 0 到 1；纵轴为 Percentage，从 0 到 120。图中红线阈值为 DLC/d 0.7。灰线为 sensitivity，蓝线为 specificity；阈值附近敏感性维持约 100%，特异性在高 DLC/d 区间下降。

页面标注“Out of n=1500 pts”，下方标题为 prospective computational modeling for CO。黑色流程框的小字在原图中不可可靠辨认，因此此处只记录可清楚识别的信息。

右下 Venn 图显示处理策略分布：prosthesis selection N=29，BASILICA N=10，coronary access N=11，coronary stenting N=8，BASILICA + stent N=3。

页面引用：Heitkemper M et al., J Thorac Cardiovasc Surg. 2020；Holtz K et al., Ann Thorac Surg. 2024。

### 冠脉通路与终身管理

数字孪生可视化 TAVR 后冠脉通路，按非冠窦、左冠窦和右冠窦分色。

该页展示冠脉通路和 lifetime management 的 3D 视图。图例中紫色为 Non-Coronary Cusp，绿色为 Left-Coronary Cusp，蓝色为 Right-Coronary Cusp。

页面通过多个视角展示瓣架、瓣叶、窦部和冠脉口的空间关系，用于判断未来冠脉进入是否受阻，以及不同瓣架取向对终身管理的影响。

### 对 leaflet modification rate 的影响

在 ViV/redo TAVR 患者中，DASI 风险重分类减少 CT 高危患者的 leaflet modification 使用。

研究纳入 158 例连续 ViV/redo TAVR 患者，时间为 2022 年 1 月至 2025 年 12 月。其中 ViV，即 TAVR-in-SAVR，为 n=122，占 77.2%；redo TAVR，即 TAVR-in-TAVR，为 n=35，占 22.2%。

按 CT risk classification 分组：CT high-risk n=86，占 54.4%；CT not evaluated n=13，原因是不完整记录；CT low-risk n=59，占 37.3%。

primary analysis 中，CT high-risk 患者再按术前规划方式分层：traditional CT 中 CT high-risk 为 n=60；AI-augmented 中 CT high-risk 为 n=28，并进行了 DASI simulation。

统计分析包括：traditional CT vs AI-augmented LM comparison，限 CT high-risk subgroup，使用 Boschloo’s exact test，one-sided，并给出 95% Wilson confidence intervals；DASI risk reclassification，即 CT high-risk 到 low-risk，使用 McNemar’s test；DASI downgraded subgroup 中 observed vs expected LM rates 使用 one-sided binomial test。所有检验的显著性阈值为 p<0.05。

DASI 风险重分类图显示，在 28 例 CT high-risk 患者中，89.3% 被 DASI 重新分类为 low-risk，即 n=25；仍为 high-risk 为 n=3。

重分类患者结局图显示，在 25 例 DASI low-risk 患者中，80% 成功无需 leaflet modification 处理，即 n=20；进行了 LM 的为 n=5。该结果与 expected 48.3% 比较，binomial p=0.003。

| 比较 | Leaflet modification rate | 样本量 | p 值 |
| --- | --- | --- | --- |
| No-DASI CT High-Risk | 48.3%，即 29/60 | n=60 | p=0.003 |
| DASI Downgraded to Low-Risk | 20.0%，即 5/25 | n=25 |

### 互动数字孪生体验：gap analysis

Apposition/gap 分析界面显示瓣架与解剖之间的局部间隙。

该界面同样显示 HS133325, 1 M，Tricuspid，SE 29 mm 与 BE 26 mm，其中 BE 26 mm 高亮。左侧 gap 指标为 GAP 2 0.6 mm，GAP 1 1.7 mm。

右侧视角显示 LAO 89 posterior、CAU 5。控制面板选中 Apposition 标签，并选择 From Aorta；另一选项为 From LVOT。部署深度显示 90.0%，刻度含 90% 与 80%。Expansion Level 为 Nominal，oversizing 为 13.9% oversized，下方为 offset 滑条。

### 互动数字孪生体验：stretch 与测量

Stretch 分析解释组织面积增加比例，并把 root injury 风险分为低风险、灰区和高风险。

左侧显示 MAX STRETCH 1.4，色标从 1.0 到 1.5。右侧控制面板选中 Stretch 标签，deployment depth 90.0%，expansion level 为 Nominal，oversizing 13.9% oversized。各窦 stretch 值为 LCC 1.2、NCC 1.4、RCC 1.4。

弹窗题为“Stretch Analysis Clinical Significance”。Stretch 被定义为 THV 部署后主动脉根部空间变形指标，用于测量 TAVR 部署前后根部解剖组织面积的百分比增加。Stretch 1.0 表示没有变形，ratio 1.3 表示组织面积增加 30%。Stretch Analysis 可视化由瓣叶钙化移位造成的 SOV 局部面积 stretch。

| Stretch 范围 | 临床解释 |
| --- | --- |
| <1.5 | 低组织变形，root injury 风险低。 |
| 1.5–1.7 | 灰区。评估 root injury 风险时考虑年龄、性别和 stretch 位置；aorto-mitral curtain 处对 stretch 的耐受高于左冠窦下方。 |
| >1.7 | 显著组织变形，root injury 风险增加。 |

附加说明为：stretch 阈值来自盲法 root injury 或 rupture 队列，stretch pattern 的 footprint 可能进一步提示风险。免责声明为：数据基于由瓣叶钙化导致的 sinus-based rupture；stretch analysis 只依赖钙化诱导的 stretch，不包括瓣架本身造成的 stretch。

页面引用：Jilaihawi H, NY Valves. 2025；Siroset T et al., J Am Coll Cardiol Intv. 2023。

### 高钙解剖中的瓣架扩张优化

高钙解剖中 root tissue stretch 的局部热点和阈值；过度 stretch 可导致破裂。

左侧 3D 图显示高钙解剖中的 stretch risk，色标为 1.0 low 到 1.5 high。页面文字指出：root tissue stretches，过度 stretch 可以导致 rupture。

右上柱图题为“Sinus Location and Average Peak Stretch Values”。纵轴为 average peak areal stretch，范围约 0 到 2.5；横轴位置包括 RCS、LCS、NCS 和 Peak Stretch。蓝色代表 rupture max stretch average，橙色代表 negative max stretch average。

右下敏感性/特异性曲线以 Stretch 为横轴，图中橙色竖线标出阈值 1.7。该阈值用于区分 root injury 或 rupture 风险较高的 stretch 区间。

### 预测植入后压差

通过术前 Doppler 和瓣膜参数预测 TAVR 后波形、平均压差和峰值压差。

左侧曲线题为“Predicted gradient versus ejection phase in 100 days post-TAVR implanted with 26 mm THV”。纵轴为 pressure gradient, mmHg，范围约 0–80；横轴为 ejection percentage，范围 0–100%。图例包括 pre、predicted post 和 95% confidence interval。蓝色向下箭头表示预期压差降低。

| 指标 | Predicted Mean Gradient | Predicted Peak Gradient |
| --- | --- | --- |
| Value | 13 mmHg | 23 mmHg |
| 95% Confidence Interval | 7–14 | 15–31 |

输入变量包括 pre-TAVR Doppler waveform、pre-TAVR peak velocity、aortic valve area、deployed valve size 和 body surface area。输出为 post-TAVR predicted waveform，并给出 mean 与 peak gradient values。讲者强调波形形状本身是动态生物标志物，比单独的平均或峰值压差更有信息量。

### 预测 HALT

HALT 预测结合流体循环、neo-sinus 几何和血栓体积，图中阈值约为 20–23。

左侧示意分为 acceleration、peak systole 和 deceleration 三个时相。峰值收缩期标注 main jet (V)、induced vortices (Γ)、neo-sinus 与 TAV stent。

下方散点图纵轴为 normalized circulation，约 0–100；横轴为 thrombus volume，约 -0.05 到 0.30。红线标注阈值约 20–23。

右侧几何示意包括 stent direction crossing from tip of leaflet、V、HR、v、d、h=height of the NS、annulus，以及 A1。下方三维截面标注 separated area、neo-sinus area、STJ plane 和 TAV leaflet。

页面引用：Hatoum H et al., Cardiovasc Eng Tech. 2021；Venkatesh A et al., JTCVS. 2025。

### 未来：扩展到所有结构性心脏介入

DASI 数字孪生未来方向包括 TMVR、LAAO 和 TEER。

未来扩展方向包括 TMVR、LAAO 和 TEER。左侧示意 TMVR，中间示意 LAAO，右侧为 DASI Simulations 的 mTEER 可视化互动应用。

mTEER 可视化界面中有 Slice longitudinal 和 Slice transverse 按钮，可勾选 anterior leaflet 与 posterior leaflet。界面还显示 device location，lateral-medial 滑条，以及 simulation time 0%。底部说明为：view the change of patient geometry as the device is being placed，即在器械放置过程中查看患者几何结构变化。
