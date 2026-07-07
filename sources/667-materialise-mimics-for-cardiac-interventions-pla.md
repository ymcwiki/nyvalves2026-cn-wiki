# Materialise Mimics 用于心脏介入：FEops 预测洞察赋能的规划

## 核心要点

* 讲题强调用 AI、三维分割、虚拟植入和患者特异性计算机仿真，提高 TAVR 术前规划的精度，覆盖器械选择、入路策略、解剖风险、PVL、冠脉阻塞、传导异常和 lifetime management。
* FeOps/HEARTguide 用于预测 frame deformation、skirt apposition 和 contact area；页面同时注明 TAVR simulations not yet available for clinical use in the USA。
* 膜部室间隔瘤病例显示，29 mm Evolut PRO 高位植入在仿真中 PVL 路径最小，实际植入后仅轻度 PVL，未发生室间隔瘤破裂或瓣膜移位。
* 73 岁女性二叶瓣病例比较 26 Sapien Ultra 与 29 Evolut FX+：BE 26 为 -0.6% undersized、最大间隙 1.4 mm、最大 stretch 1.6；SE 29 最大间隙 0.7 mm，植入后无起搏器。
* TAV-in-TAV 预测建模中，BE 23 in SE 29 node 4 的左冠 DLC/d 为 1.9，右冠 DLC/d 为 2.6；均高于文献提示的冠脉阻塞风险阈值 0.7。
* PRECISE-TAVI 真实世界证据显示，术前决策改变 35%，其中 12%为尺寸改变、23%为位置改变，并关联较低起搏器率和较低大于 trace 的 PVL。

### 标题页

页面题为“TAVR Case Planning Powered by Predictive Precision Insights”，即由预测性精准洞察驱动的 TAVR 病例规划。讲者为 Anene Ukaigwe, MD，专业为介入心脏病学，来自 University Hospitals Harrington Heart and Vascular Institute 的瓣膜与结构性心脏团队。

### 利益关系披露

讲者在过去 24 个月内与生产、营销、销售、转售或分销患者用医疗产品的公司存在财务关系，相关关系已被缓解。披露如下：

| 财务关系性质 | 公司 |
| --- | --- |
| Grant/Research Support | Medtronic Inc, Laplace |
| Consultant Fees/Honoraria | Medtronic Inc, Edwards LifeScience, Boston Scientific |
| Individual Stock(s)/Stock Options | 无 |
| Royalties/Patent Beneficiary | 无 |
| Executive Role/Ownership Interest | 无 |
| Other Financial Benefit | 无 |

完整 faculty disclosure 信息可在会议 app 中查看。

### AI 在结构性心脏介入术前规划与结局预测中的路径

流程图列出 AI 对术前规划的五个作用：提高工作流效率、器械和入路选择、解剖风险评估、虚拟手术仿真和结局预测。

该页引用 Allaham、Haytham 等的框架，题为“Artificial Intelligence in Pre-Procedural Planning and Outcome Prediction of Structural Heart Interventions”。五个模块按箭头连接：

| 模块 | 页面文字的中文转写 |
| --- | --- |
| 提高工作流效率 | 自动完成解剖分割，并标准化血管测量，以简化术前规划。 |
| 器械和入路选择 | 优化器械选择、定位和血管入路策略，以提高操作效率并改善总体手术结局。 |
| 解剖风险评估 | 识别与技术复杂性、手术成功和残余瓣膜病相关的患者特异性解剖与手术风险。 |
| 虚拟手术仿真 | 通过虚拟模拟器械植入策略，在术前测试多个场景，减少术中反复尝试，并提高操作精度。 |
| 结局预测 | 个体化结局预测使风险分层超越传统模型，支持更充分的患者咨询和共同决策。 |

### FeOps 预测规划：瓣架形态与钙化移位

Schultz 等 2016 年 EuroIntervention 工作展示患者特异性图像计算机仿真，用于预测 CoreValve 和 SAPIEN 术后瓣架形态及钙化移位。

左侧显示 Case 1-4，每例按三行比较：TAVI 前 MSCT、TAVI 后 MSCT，以及模型预测。右侧四个散点图比较 CT 与模型的 inflow 直径：左上为 model inflow Dmin 对 CT inflow Dmin，坐标范围约 14-26 mm与15-27.5 mm；右上为 CT minus model 的 Dmin 差值，纵轴约 -6 至 4 mm；左下为 model inflow Dmax 对 CT inflow Dmax，坐标范围约 18-32 mm与20-32.5 mm；右下为 Dmax 差值，纵轴约 -5 至 3 mm。页脚文献为 Schultz et al., Patient-specific image-based computer simulation for the prediction of valve morphology and calcium displacement after TAVI with the Medtronic CoreValve and the Edwards SAPIEN valve, EuroIntervention, 2016。

### FeOps 用于并发症风险预测

FeOps 把瓣架变形、裙边贴合和接触面积分别对应到环部损伤/冠脉风险、PVL 风险和传导异常风险。

页面列出三类风险评估。第一类为 **Frame deformation**：准确预测瓣架形态和钙化移位，用于评估 annular injury、coronary obstruction/reaccess。第二类为 **Skirt apposition**：评估 paravalvular regurgitation，即 PVL 风险。第三类为 **Contact area**：评估 conduction abnormalities，即传导异常风险。页脚注明：TAVR simulations not yet available for clinical use in the USA。

### FeOps 对 TAV-in-TAV 的预测建模

FeOps 用于 TAV-in-TAV 场景下 neoskirt 顶部器械与解剖距离、瓣叶 overhang 和冠脉通路的三维分析。

该页显示 TAV-in-TAV 仿真界面。页面文字包括：在 neoskirt 顶部对 device-anatomy distance 进行定性评估；对 leaflet overhang 进行定性评估；leaflet overhang 会受 commissural alignment 影响；冠脉通路进行三维分析，红色区域表示 gap < 2 mm。

### 在 index TAVR 前模拟 redo-TAVR 场景

redo-TAVR 场景在 index TAVR 前被预先模拟，示例比较 S3 位于 node 4、node 5 和 node 6。

FeOps 可在第一次 TAVR 器械选择前，预先评估未来 redo-TAVR 场景。页面分别展示 S3 at node 4、S3 at node 5、S3 at node 6的模拟。页脚再次注明：TAVR simulations not yet available for clinical use in the USA。

### 病例 1：87 岁女性，膜部室间隔瘤合并主动脉瓣狭窄

CT 图像用星号标出 interventricular membranous septal aneurysm，右侧列出 annular plane、瓣膜选择和 PVL 风险三个难点。

患者为 87 岁女性，有动脉高血压病史，因重度有症状主动脉瓣狭窄就诊，症状为 NYHA II。解剖难点为 interventricular membranous septal aneurysm，即膜部室间隔瘤。页面列出三个挑战：1，环平面和直径定义困难；2，瓣膜尺寸、瓣膜类型和最佳定位选择需要权衡破裂风险；3，存在瓣周反流风险。页脚为 FEops HEARTguide case study TAVI-20-COL005。

### 患者特异性仿真用于评估 PVL 路径与接触面积

膜部室间隔瘤病例中，患者特异性仿真用于比较不同 TAVR 位置和尺寸对 PVL 路径及 contact area 的影响。

页面说明：患者特异性计算机仿真可评估不同 TAVR 位置和尺寸对 PVL 路径与 contact area 的影响。深位植入可以被模拟，用于评估是否可能闭合室间隔瘤而不造成 PVL。页脚仍标注 FEops HEARTguide case study TAVI-20-COL005。

### HEARTguide 仿真：29 mm Evolut PRO 与 34 mm Evolut R

四种组合比较：29 mm Evolut PRO 高位、29 mm Evolut PRO 低位、34 mm Evolut R 高位、34 mm Evolut R 低位；红色代表贴合不良或 PVL 路径。

页面将仿真结果分为两行：上行为 skirt apposition 与 PVL 路径，下行为 contact area。29 mm Evolut PRO 高位显示 very tiny path for PVL；29 mm Evolut PRO 低位显示 small path for PVL；34 mm Evolut R 高位显示 small path for PVL；34 mm Evolut R 低位显示 largest path for PVL。色标从约 <1.0 mm到 >1.0 mm，用于表示局部间隙或贴合程度。页脚为 FEops HEARTguide case study TAVI-20-COL005，并带有 Uniklinik Köln 标识。

### 病例 1 结果：选择高位 29 mm Evolut PRO

高位植入结果页显示仿真预测区域与术后彩超结果，实际 PVL 为轻度，未发生室间隔瘤破裂或瓣膜移位。

FEops HEARTguide 仿真提示，高位植入时 PVL 最少，且与室间隔瘤的相互作用最小。因此实际植入 29 mm Evolut PRO并选择高位。TAVI 后 PVL 出现在预测区域，超声评估为轻度 PVL。未发生膜部室间隔瘤破裂，也未发生瓣膜脱位。页脚标注为 Feops HEARTguide case study LAAO-19-ASZ005。

### 病例 2：73 岁女性二叶瓣，26 Sapien Ultra 对比 29 Evolut FX+

病例 2 基本信息和 annulus 测量：73 岁女性、二叶瓣、annulus area 521.97 mm²，比较 26 Sapien Ultra 与 29 Evolut FX+。

|  |  |
| --- | --- |
| 年龄 | 73 |
| 性别 | 女性 |
| 瓣膜类型 | 二叶瓣 |
| Annulus area & phase | 521.97 mm²，30% systole |
| 分割相位 | 30% systole |
| CT 质量 | Meets requirements |
| Annulus 细节 | 面积 521.97 mm²；周长 83.37 mm；直径 30.69 mm × 21.52 mm；平均直径 26.10 mm。 |

图例中绿色为 left-right coronary cusp，蓝色为 non-coronary cusp。页面比较 26 Sapien Ultra与29 Evolut FX+。页脚 DASI 声明指出：这些仿真用于研究目的，或受美国 21st Century Cures Act监管；产品未获准用于诊断、治疗、治愈或预防疾病；DASI 为多种 THV 释放选项提供仿真，可能包含适当与次优选项；内容不构成标准治疗建议；仿真基于特定参数假设，不能完全覆盖个体解剖、材料与组织属性、术中预扩/后扩等变异；医生应结合 THV 说明书、病史、症状和其他 TAVR 术前评估独立判断。

### BE 26 stretch 分析

球扩 26 mm 方案的 stretch map 显示最大钙化诱导 cusp-wise stretch：LCC-RCC 1.1，NCC 1.6。

页面题为“Balloon-Expandable 26 Stretch Analysis”。图例中绿色为 left-right coronary cusp，蓝色为 non-coronary cusp。STJ view 旁的表格显示最大 calcium-induced cusp-wise stretch：LCC-RCC = 1.1，NCC = 1.6。引用文献为 Sirset, T. et al., J Am Coll Cardiol Intv. (2023)。页脚保留与 P12 相同的 DASI 研究用途和非临床诊疗用途声明。

### SE 29 扩张动画

自膨 29 mm THV 的扩张动画截图，显示二叶瓣钙化、瓣架释放和左/右冠瓣叶区域。

页面题为“Self-Expandable 29 Expansion Animation”。图例显示绿色为 left-coronary cusp，蓝色为 right-coronary cusp。画面展示自膨 29 mm THV 在患者二叶瓣解剖内的扩张过程，左侧和右侧分别为不同观察角度。页脚仍为 DASI 仿真研究用途声明。

### SE 29 THV 贴合和流线评估

SE 29 贴合评估：flow trajectories、annulus view 和 gap assessment，两个间隙厚度均为 0.7 mm。

页面题为“Self-Expandable 29 THV Apposition”。左侧显示 flow trajectories，中部为 annulus view。右侧 gap assessment 表格显示：Gap I 厚度 0.7 mm；Gap II 厚度 0.7 mm。页脚仍为 DASI 仿真研究用途声明。

### 病例 2 总结：BE 26 与 SE 29 对比

病例总结表：BE 26 的 undersizing、冠脉 DLC/d、最大贴合间隙和 stretch；SE 29 的 DLC/d 与间隙更小。

| Valve | % Oversizing | Coronary Analysis | Stent Apposition | Stretch Analysis |
| --- | --- | --- | --- | --- |
| BE 26 | -0.6% undersized | LCA DLC/d = 2.8 RCA DLC/d = 3.4 | Largest gap = 1.4 mm | Max Stretch 1.6 |
| SE 29 | N/A | LCA DLC/d = 2.8 RCA DLC/d = 3.4 | Largest gap = 0.7 mm | N/A |

页面注释写明：DLC/d ≤ 0.7被报道与 TAVR 相关冠脉阻塞发生有关；最大 stretch 1.6预测环部破裂。右下图为“Peak Areal Stretch，Outlier Omitted”，纵轴为 sensitivity/specificity，横轴 stretch 约 1-3；图中标注最大 stretch 1.6的敏感度为 100%，特异度为 57%。参考文献包括 Blanke 2017、Holst 2024、Heitkemper 2020、Sirset 2023。

### SE 29 左冠分析

自膨 29 mm 方案的左冠分析，给出 DLC、冠脉直径、DLC/d、相对瓣叶高度和 radial flow gap。

| 指标 | 数值 |
| --- | --- |
| Distance from Leaflet to Root (DLC) | 8.1 mm |
| Coronary Artery Diameter (d) | 2.9 mm |
| DLC/d | 2.8 |
| Relative Leaflet Height (Hrel) | -2.9 mm |
| Max Radial Flow Gap | 8.1 mm |
| Mean Radial Flow Gap | 4.4 mm |

DLC/d 的计算方法来自 Holst 等和 Heitkemper 等；DLC/d ≤ 0.7被报道与 TAVR 导致冠脉阻塞发生有关。页脚仍为 DASI 仿真研究用途声明。

### SE 29 右冠分析

自膨 29 mm 方案的右冠分析，DLC/d 为 3.4，最大 radial flow gap 6.3 mm。

| 指标 | 数值 |
| --- | --- |
| Distance from Leaflet to Root (DLC) | 5.6 mm |
| Coronary Artery Diameter (d) | 1.6 mm |
| DLC/d | 3.4 |
| Relative Leaflet Height (Hrel) | -1.6 mm |
| Max Radial Flow Gap | 6.3 mm |
| Mean Radial Flow Gap | 3.9 mm |

同样采用 Holst 等和 Heitkemper 等的 DLC/d 计算，阈值提示为 DLC/d ≤ 0.7与 TAVR 相关冠脉阻塞有关。页脚仍为 DASI 仿真研究用途声明。

### 膜部室间隔测量与传导风险

膜部室间隔测量显示 infra-annular MS length 5.3 mm，并标示 annulus、His bundle 及 right-non cusp overlap views。

页面题为“Membranous Septum Measurements”。测量结果为 infra-annular membranous septum length 5.3 mm。图中以红/蓝虚线标示 annulus 和 His bundle，右侧示意 BE 26 在 left-right coronary cusp 与 non-coronary cusp 关系中的位置，底部标题为 right-non cusp overlap views。参考文献为 Chen, YH et al., JTCVS, Vol. 164, 42-51.e2。页脚仍为 DASI 仿真研究用途声明。

### 实际结果：29 Evolut FX+，无起搏器

29 Evolut FX+ 植入后透视、超声和彩色/连续多普勒图，页面标题明确写明 No pacemaker。

实际治疗使用 29 Evolut FX+，页面标题为“No pacemaker”，即术后未植入起搏器。图像包括透视下瓣架位置、超声血流和彩色多普勒/频谱评估，用于展示最终瓣膜功能和传导结局。

### 基于既往 CT 的 TAV-in-TAV 左冠分析

BE 23 in SE 29 node 4 的左冠分析：左冠直径 2.9 mm，DLC 5.5 mm，DLC/d 1.9。

页面题为“Precitive Modeling”，原页拼写如此，内容为基于既往 TAV CT scan 的 TAV-in-TAV 预测建模：BE 23 in SE 29 Node 4 Left Coronary Analysis。左冠直径 d 为 2.9 mm；leaflet 到冠脉的距离 DLC 为 5.5 mm；DLC/d 为 1.9。DLC/d 计算来自 Holst 等和 Heitkemper 等；DLC/d ≤ 0.7被报道与 TAVR 冠脉阻塞发生有关。图例中紫色为 non-coronary cusp，绿色为 left-coronary cusp，蓝色为 right-coronary cusp。页脚仍为 DASI 仿真研究用途声明。

### 基于既往 CT 的 TAV-in-TAV 右冠分析

BE 23 in SE 29 node 4 的右冠分析：右冠直径 1.6 mm，DLC 4.1 mm，DLC/d 2.6。

页面题为“BE 23 in SE 29 Node 4 Right Coronary Analysis”。右冠直径 d 为 1.6 mm；leaflet 到冠脉的距离 DLC 为 4.1 mm；DLC/d 为 2.6。DLC/d 计算和风险阈值同 P21：DLC/d ≤ 0.7与 TAVR 冠脉阻塞发生有关。图例同样区分 non-coronary cusp、left-coronary cusp 和 right-coronary cusp。页脚仍为 DASI 仿真研究用途声明。

### 预测规划的真实世界证据：PRECISE-TAVI

PRECISE-TAVI 为前瞻性观察性欧洲多中心研究，术前决策改变 35%，其中 12% 为尺寸改变，23% 为位置改变。

PRECISE-TAVI 是 prospective, observational multi-center study。研究包括欧洲 6个中心，77例患者，中位年龄 79.9 岁。挑战性解剖包括二叶瓣、小瓣环，定义为平均瓣环直径 <20 mm，或主动脉瓣重度钙化，Agatston score 男性 >3000、女性 >1600。研究评估对 heart team 手术规划和总体器械成功的影响，同时评估传导异常和新发永久起搏器植入。右侧显示术前决策改变 35%，并与有利临床结局相关，其中 12%为尺寸改变，23%为位置改变。页面还写明，与聚焦 BAV 解剖和小瓣环的科学出版物相比，起搏器率更低，PVL 大于 trace 的比例更低。

### 完整解决方案：高级 TAVR 规划

完整方案包括自动测量、交互式审阅、主动脉根和股动脉入路评估、预测仿真与 HEART team 云协作。

页面标题为“Complete solution: Advanced TAVR planning”。五个组成部分为：AI-driven case preparation with automated measurements，即 AI 驱动病例准备与自动测量；Interactive review，即交互式审阅；Intuitive assessments: Aortic root, femoral delivery path, intra-op views，即主动脉根、股动脉输送路径和术中视角直观评估；Predictive simulations with lifetime management insights, index and Valve-in-Valve device planning，即结合 lifetime management、index TAVR 与 Valve-in-Valve 器械规划的预测仿真；Cloud-based collaboration with the HEART team and straight into the Cathlab，即基于云端的心脏团队协作并直接进入导管室流程。

### 总结

人工智能算法正在发展，用于提高 TAVR 规划的精度；其有助于根据特定解剖进行 TAVR 假体个体化定制和 lifetime management；可让不同经验水平的植入者都获得精准规划工具；精准规划算法应整合进入 heart team。

### 致谢与提问

页面写明“THANK YOU”和“QUESTIONS”，背景为会议模板城市图像，无额外医学数据。

### 空白页

该页为空白模板页，仅保留会议页脚，无实质医学内容。

### 备份病例：82 岁男性二叶瓣与瓣环 sizing

备份病例信息：82 岁男性二叶瓣，annulus area 708 mm²；图中另示 area 683 mm²、perimeter 94 mm，并列出 BE 与 SE sizing 表。

|  |  |
| --- | --- |
| 年龄 | 82 |
| 性别 | 男性 |
| 瓣膜类型 | 二叶瓣 |
| Annulus area & phase | 708 mm²，30% systole |
| 分割相位 | 30% systole |
| Annulus 测量框 | 面积 707.63 mm²；周长 95.85 mm；直径 33.92 mm × 26.96 mm；平均直径 30.44 mm。 |
| 橙色标注 | Area 683 mm²；Perimeter 94 mm。 |

左下球扩瓣 sizing 表显示：20 mm对应面积 273-346 mm²、area-derived diameter 18.6-21 mm、TEE 16-19 mm；23 mm对应 338-430 mm²、20.7-23.4 mm、18-22 mm；26 mm对应 430-546 mm²、23.4-26.4 mm、21-25 mm；29 mm对应 540-683 mm²、26.2-29.5 mm、24-28 mm。

右下自膨瓣 sizing 表显示：size 23 mm、26 mm、29 mm、34 mm；annulus diameter 分别约为 17\*/18-20 mm、20-23 mm、23-26 mm、26-30 mm；annulus perimeter 分别为 53.4\*/56.5-62.8 mm、62.8-72.3 mm、72.3-81.7 mm、81.7-94.2 mm；sinus of Valsalva mean diameter 分别需 ≥25 mm、≥27 mm、≥29 mm、≥31 mm；sinus of Valsalva mean height 分别需 ≥15 mm、≥15 mm、≥15 mm、≥16 mm。引用为 Blanke P et al., J Am Coll Cardiol Img. 2019 Jan;12(1):1-24。

### DASI 冠脉阻塞风险与环部损伤预测

DASI 冠脉阻塞风险 marker：DLC/d；右侧展示 peak areal stretch 预测主动脉根破裂风险，示例 peak 1.8。

页面左侧标题为“DASI Coronary obstruction risk Marker for Coronary Obstruction”。定义为：DLC 是 leaflet 到主动脉根的距离；d 是冠脉直径。DLC/d 按 Holst 等和 Heitkemper 等描述计算；DLC/d ≤ 0.7被报道与 TAVR 冠脉阻塞发生有关。左下图横轴为 DLC/d，曲线包括 sensitivity、specificity 和 ROC；图中标注 AUC = 1.0。右侧标题为“DASI Annular Injury Prediction”，stretch map 示例标注 peak 1.8。右上 ROC 图显示 1.8 threshold和1.7 threshold female only，图注写明计算模型得出的 stretch 在图 A 中展示，图 B 的 ROC AUC 分别为 0.84和0.92。右侧要点为：术前 TAVR CT 派生的 peak areal stretch 通过计算模型可预测主动脉根破裂，从而帮助定量确定患者特异性风险。页脚致谢 Courtesy Lakshmi Dasi。

### 备份柱状图页

示例柱状图，三组 Item 中 Item 1 的 p=0.001，Item 2 的 p=NS，Item 3 的 p=0.125。

页面题为“Chart Slide”，副标题为“Subtitle text 18 pt Bold Ital”。纵轴为 Axis Title，横轴三组为 Item 1、Item 2、Item 3，图例为 Item A、Item B、Item C、Item D。Item 1 四个柱值为 3、4、5、7，标注 p = 0.001；Item 2 四个柱值为 26、28、29、35，标注 p = NS；Item 3 四个柱值为 38、42、45、50，标注 p = 0.125。页脚引用 Smith et al., Eur Heart J. 2012;33:372-83。

### 备份表格页

DCA 与支架组的结果表，DCA n=381，Stent n=372。

页面题为“Table Slide”，副标题为“Subtitle text 18 pt Bold Ital”。表格如下：

| Outcome | DCA n = 381 | Stent n = 372 | P Value |
| --- | --- | --- | --- |
| Late loss (mm) | 25.0 | 13.0 | 0.28 |
| Binary restenosis | 26.7 | 22.1 | 0.24 |
| Optimal DCA (%) | 16.2 | 22.1 | 0.39 |
| TVR | 25.0 | 23.0 | 21.0 |
| 12-Month TVF (death, MI, TVR) (%) | 23.9 | 21.5 | 0.48 |

页脚引用 Smith et al., Eur Heart J. 2012;33:372-83。TVR 行的 P value 按原页显示为 21.0。
