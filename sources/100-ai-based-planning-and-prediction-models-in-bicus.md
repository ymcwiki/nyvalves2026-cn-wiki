# AI 规划与预测模型在二叶瓣 TAVR 中的应用

## 核心要点

* 讲者强调 AI 在 TAVR 规划中的角色是“预测”，专家负责解释，最终由 heart team 决策；尤其在二叶瓣和复杂解剖中，模型置信度必须与训练数据相似性一起判断。
* MSCT 一次采集可支持多项决策：诊断和 calcium score、二叶瓣 phenotype、冠脉高度/病变/通路、根部和主动脉外科策略、TAVR 瓣膜尺寸和器械选择、并发症风险、终身管理、AI/digital twins 模拟。
* PRECISE-TAVI 相关复杂解剖自动规划研究纳入 77 例复杂解剖，其中 17 例为二叶式主动脉瓣；接触压力指数与新 PPI 相关，No PPI 3.5% 对 New PPI 16.0%，p<0.01。
* 半自动规划 ROC 显示，新 PPI 预测 AUC 0.83，95% CI 0.72-0.94；>trace PVL 预测 AUC 0.69，95% CI 0.55-0.82。
* Mimics for TAVR 自动规划研究纳入 126 例，其中 50% 为复杂解剖、12 例二叶瓣；与 3-MENSIO 相比，SAPIEN sizing 一致率 90%，Navitor 87%，Evolut 88%，规划时间从 9 分钟降至 1 分钟。
* 当前 TAVR 规划可分为 4 层：自动测量、AI prediction、computational modeling、未来 hybrid digital twins；越罕见的解剖，越需要人类专家解释模型边界。

### 题目与讲者

本报告题为“AI Based Planning and Prediction Models in Bicuspid TAVR”，中文可译为“AI 规划与预测模型在二叶瓣 TAVR 中的应用”。讲者为 Nicolas M Van Mieghem, MD, PhD, FESC, FACC，页面显示 Ziekenhuis Oost-Limburg 标识。

### 财务利益披露

| 类别 | 公司 |
| --- | --- |
| Research Grant Support | Abbott、Boston Scientific、Medtronic、Meril、Pie Medical、Haemonetics。 |
| Consultancy/Advisory | Abbott、Abiomed、Adjust Medical、DockValve、Anteris、Approxima Srl、Boston Scientific、Daiichi Sankyo、Haemonetics、Materialise、Medtronic、Percassist、Pie Medical、Polares、PulseCath、Secure Closure、Siemens、Vivasure。 |

### AI 原理：预测、解释、团队决策

AI 生成预测，专家解释预测，heart team 决定治疗路径。

该页将 AI 工作流分为三步。第一步为 AI predicts：advanced algorithms and digital twin simulations generate predictions。左侧预测面板给出一个示例：Neo-LVOT area 165 mm2，标记为 high risk；LVOT obstruction 为 high risk；MR reduction 为 moderate；device stability 为 favorable；hemodynamics 为 acceptable。下方 data integration 包括 CT、Echo、Fluoroscopy、Clinical Data、Labs。

第二步为 experts interpret：专家使用临床知识、经验和上下文解释 AI predictions。专家需要 validate image quality & inputs；review anatomy nuances；consider patient factors & comorbidities；assess uncertainties & model limitations；integrate with procedural experience & outcomes data。页面显示 risk assessed by expert 的低、中、高风险色条。

第三步为 the heart team decides：以协作、患者为中心的决策平衡 risks、benefits 和 patient values。右侧会议屏幕再次显示 Neo-LVOT area 165 mm2 和 high risk，专家评估为 high risk，recommendation 为 proceed with TMVR。决策图标包括 clinical appropriateness、patient values & goals、risk vs. benefit assessment、plan & bailout strategy。底部总结为 better decisions、safer procedures、better outcomes；AI provides precision，experts provide perspective，heart team provides care。

### MSCT 的产出

MSCT 一次采集可支持诊断、解剖、TAVR、并发症预测和终身管理等多项决策。

中心为 CT。环形图列出 MSCT yield：Diagnosis，包括 confirm severity 和 calcium score；Anatomy，包括 bicuspid phenotype；Coronaries，包括 height、disease、access；Surgery，包括 root & aorta strategy；TAVR，包括 valve sizing 和 device selection；Complications，包括 coronary obstruction、annular rupture、conduction disturbances；Lifetime management，包括 coronary access、TAVR-in-TAVR、durability；AI & Digital Twins，包括 simulation、risk prediction、planning。

页面底部一句话是“One acquisition, multiple decisions.”，即一次 CT 采集服务多个治疗决策。

### AI 现实：置信度取决于数据相似性

模型置信度随解剖复杂度和训练数据相似性变化；罕见表型通常落在低置信度区域。

散点图纵轴为 anatomical complexity，从 low 到 high；横轴为 similarity to training data (population space)，从 low 到 high。AI model confidence 色标从 very low、low、moderate、good 到 very high，颜色依次为红、橙、黄、绿、蓝。

右下方常见表型 common phenotypes 处于 high data density 区域，数据点以蓝色为主，模型置信度 very high。中间区域标注 in between / less common anatomies，颜色为黄绿混合，表示中等到较好置信度。左上方 outlier / rare phenotypes 解剖复杂度高且与训练数据相似性低，数据点以红橙色为主，表示 very low 到 low confidence。二叶瓣 TAVR 中许多复杂表型会落入中间或罕见区域，因此不能只看 AI 输出。

### AI 现实：罕见解剖更依赖专家

AI 置信度来源分为模型经验之外、经验边缘和经验之内三类。

| 区域 | 含义 | 决策要求 |
| --- | --- | --- |
| Outside the model's experience | 训练数据中 very limited 或 no similar cases；predictions are uncertain；higher risk of model error。 | Expert judgment is critical。 |
| At the edge of experience | 存在 some similar cases；predictions are possible but less certain；expert interpretation essential。 | Human expertise adds context。 |
| Within the model's experience | 训练数据中 many similar cases；predictions are more reliable；AI tools provide high confidence support。 | AI + expertise = precision。 |

页面底部强调：the rarer the anatomy, the greater the value of human expertise。AI provides a map，experts decide the path。对于二叶瓣，尤其是钙化、raphe、水平主动脉、冠脉通路或瓣环形态异常时，专家解释模型边界是核心步骤。

### 复杂解剖中的自动规划研究

PRECISE-TAVI trial：CT-derived simulations 用于 challenging anatomies。

该页介绍“Automated Planning in complex anatomies”。研究纳入 77 例患者，全部为 complex anatomies，其中 N=17 为 bicuspid aortic valve。

右侧论文为 Wiley 发表的 Original Article - Basic Science，题为“Clinical value of CT-derived simulations of transcatheter-aortic-valve-implantation in challenging anatomies the PRECISE-TAVI trial”。稿件 received 30 March 2023，revised 28 July 2023，accepted 19 August 2023，DOI 10.1002/ccd.30816。

作者包括 Thijmen W. Hokken、Hendrik Wienemann、James Dargan、Dirk-Jan van Ginkel、Cameron Dowling、Axel Unbehaun、Johan Bosmans、Andreas Bader-Wolfe、Robert Gooley、Martin Swaans、Stephen J. Brecker、Matti Adam、Nicolas M. Van Mieghem。

### 风险预测：支架变形、接触面积和裙边贴合

自动规划可预测支架形态、钙化位移、传导异常风险和 PVL 风险。

该页题为“Risk Prediction”。左侧 frame deformation 用于 accurate prediction of frame morphology and calcium displacement，图像显示 CT 钙化和瓣架模拟。中间 contact area 用于 conduction abnormalities 的 risk assessment，图像以红色高亮瓣架与解剖结构接触压力/接触区域。右侧 skirt apposition 用于 PVL risk assessment，图像显示瓣膜裙边与局部解剖未贴合或泄漏区域。

引用为 Hokken, Van Mieghem et al., Catheterization and Cardiovascular Interventions 2023;102:1140-1148。

### 自动规划：PPI 和 PVL 的模拟指标

接触压力指数与新 PPI 相关，模拟 PVL 流量与临床 PVL 等级相关。

| 指标 | 分组 | 数值 | p 值 |
| --- | --- | --- | --- |
| Contact Pressure Index (%) | No PPI | 3.5 (0.0-11.3) | <0.01 |
| Contact Pressure Index (%) | New PPI | 16.0 (12.0-21.0) |
| Paravalvular Leakage (mL/s) | None/Trace | 5.7 (1.3-11.1) | 0.04 |
| Paravalvular Leakage (mL/s) | Mild | 12.7 (5.5-19.1) |
| Paravalvular Leakage (mL/s) | Moderate | 17.7 (3.6-19.4) |

左侧箱线图纵轴为 contact pressure index (%)，范围约 0-40。No PPI 组中位数较低，New PPI 组中位数约 16%。右侧箱线图纵轴为 paravalvular leakage (mL/s)，none/trace、mild、moderate 三组随 PVL 等级升高而模拟泄漏量上升。

### 半自动规划：ROC 曲线

半自动规划的 ROC 曲线：预测新 PPI 的 AUC 高于预测 >trace PVL。

| ROC 曲线 | AUC | Cut-Off | Sensitivity | Specificity |
| --- | --- | --- | --- | --- |
| (A) 预测 new PPI | 0.83 (0.72-0.94) | 11.5 | 0.86 | 0.76 |
| (B) 预测 >trace PVL | 0.69 (0.55-0.82) | 12.2 | 0.59 | 0.79 |

两幅图纵轴均为 sensitivity，横轴为 1 - specificity，并画出对角参考线。PPI 曲线在低假阳性区域快速上升，提示预测性能较好；PVL 曲线与对角线距离较小，说明预测能力中等。

### Mimics for TAVR 自动规划

Vd Dorpel、Van Mieghem 等在 press 的 Mimics for TAVR 自动规划研究。

该页题为“Automated Planning”。平台为 Mimics for TAVR。研究纳入 126 例患者，其中 50% 为 complex anatomies，N=12 为 bicuspid aortic valve。右侧截图显示软件内的主动脉根部和左室三维重建，并可在 CT 多平面视图和 3D 模型之间联动。引用为 Vd Dorpel, Van Mieghem et al., in press。

### 自动与半自动 sizing 对比

Mimics for TAVR 与 3-MENSIO 的 sizing 结果高度一致，同时节省规划时间。

该页比较 Mimics for TAVR 与 3-MENSIO。中央堆叠柱状图纵轴为 percentage of cases，范围 0-100%；横轴为 SAPIEN、Navitor、Evolut。图例为绿色 smaller size、蓝色 same size、红色 larger size。

底部文字给出一致率：SAPIEN 按 area-based sizing，一致率 90%；Navitor 按 perimeter-based sizing，一致率 87%；Evolut 按 perimeter-based sizing，一致率 88%。右侧标注 time saving from 9 to 1 minutes。柱状图显示不一致部分主要为 smaller size 或 larger size，比例均约为个位数百分比。

引用为 Vd Dorpel, Van Mieghem et al., in press。

### 自动规划示例

示例展示三维解剖分割、钙化标注和 Materialise/FEops 虚拟瓣膜植入。

左侧为主动脉根部三维分割模型，紫色半透明结构显示主动脉/根部，绿色、黄色和其他彩色区域标示瓣叶钙化、LVOT 或邻近结构，瓣架示意位于瓣环区域。右侧为 Materialise FEops 软件截图，显示虚拟瓣膜置入后与患者特异性解剖的关系。页面无新增数字，但强调自动规划的输出不是单一测量，而是可视化解剖、钙化、器械位置和潜在相互作用。

### 机器学习与计算建模

机器学习回答“相似患者发生过什么”，计算建模回答“物理机制将如何发生”。

该页对比 DASI AI-driven digital twin 与 FEops/Materialise physics-based virtual implantation。中央为 bicuspid aortic valve patient-specific CT，heart team 的角色是 informed、confident、patient-specific decisions。底部总结为“AI predicts ↔ Physics explains”。

| 维度 | DASI，机器学习 | FEops/Materialise，计算建模 |
| --- | --- | --- |
| 类比 | Like ChatGPT。 | Like a flight simulator。 |
| 学习来源 | 从 experience 学习：thousands of prior patients、training dataset、neural networks、predictions/probabilities。 | 从 physics 学习：CT anatomy、3D reconstruction、finite element mesh、virtual valve deployment、biomechanical behavior。 |
| 核心问题 | What happened in similar patients? | What does the physics predict in this patient? |
| Characteristics | Data-driven；learns from examples；statistical intelligence；continuously improves with more data；fast and scalable；black-box tendencies。 | Physics-driven；solves mechanical equations；explainable mechanisms；device-specific simulation；does not require prior outcome data；computationally intensive。 |
| Strengths | Speed、scalability、standardized risk prediction。 | Mechanistic understanding、device-specific behavior、optimal strategy in complex anatomy。 |
| Limitations | Dependent on quality and breadth of training data；less explainable。 | More computationally intensive；requires high-quality models and expertise。 |

FEops 输出的 biomechanical behavior 包括 deformation、contact pressure、PVL、coronary access、implant depth。底部流程显示 CT scan 进入 DASI AI engine 后生成 risk prediction & recommendations；另一侧 3D model 进入 FEops virtual implantation 后输出 biomechanical insight & strategy optimization，最终 converge for best decision。

### AI 规划的 4 个层级

从自动测量到未来混合数字孪生，TAVR 规划可分为 4 个层级。

| 层级 | 工具/概念 | 核心问题 | 输出 |
| --- | --- | --- | --- |
| Tier 1：Imaging & Automated Measurements | 3mensio、CIRCLE、Siemens Healthineers、PHILIPS。 | What does the anatomy look like? | Annulus、LVOT、coronaries、calcium；standardized measurements、calcium assessment、anatomical landmarks。示例数字包括 annulus area 439 mm2、perimeter 74.1 mm、distance to LCA 12.4 mm、LVOT area 437 mm2、distance to RCA 15.2 mm。 |
| Tier 2：AI Prediction | DASI simulations，machine learning like ChatGPT。 | What is likely to happen? | Risk assessment dashboard：PVL low risk、coronary obstruction low risk、pacemaker implantation moderate risk、annular rupture very low risk、coronary access future favorable、redo TAVR feasibility good、overall confidence high。Recommended strategy：preferred valve 29 Evolut FX+；implant depth 3-4 mm；commissural alignment recommended。 |
| Tier 3：Computational Modeling | Materialise、FEops，physics engine like a flight simulator。 | Why and how will it happen? | Contact pressure implant depth comparison；predicted PVL 2.1 mL/s 与 6.4 mL/s；other analyses 包括 skirt apposition、frame deformation、membranous septum contact、coronary access after TAVR，示例 LCA 11.8 mm、RCA 14.6 mm。 |
| Tier 4：Hybrid Digital Twins，future platforms | Machine learning + computational modeling + CFD hemodynamics。 | How can treatment be optimized? | Multi-dimensional optimization，整合 structural physics、hemodynamics CFD、AI outcomes prediction、patient-specific goals，用于个体化治疗和长期结局预测。 |

### 当前 TAVR 规划工具版图

当前工具按商业可及性和技术成熟度分布，从研究原型到标准照护平台。

纵轴为 commercial availability，从 research only/not commercially available，到 limited availability/limited rollout/expert centers，再到 widely available/global commercial availability。横轴为 technology maturity，从 research concept/proof of concept least developed，到 pilot feasibility/pilot studies，到 early adoption initial commercial rollout/expert centers，再到 standard of care widespread adoption/global market most developed。

| 工具/平台 | 图中定位 | 说明 |
| --- | --- | --- |
| 3mensio、CIRCLE、Siemens Healthineers、PHILIPS | 高商业可及性，高技术成熟度，standard of care 区域。 | Mature imaging platforms，standard of care in TAVR centers worldwide。 |
| DASI simulations | limited availability 到 early adoption 附近。 | AI prediction platform，early commercial with selective rollout。 |
| Materialise FEops | limited availability 和 early adoption 区域。 | Computational modeling (FEA/FE) for TAVR planning，early adoption in expert centers。 |
| CardioVision | pilot/research 附近。 | AI-powered digital twin，research / pilot studies。 |
| TAVR-AID | research only，research concept 区域。 | AI + CFD + physics，research prototype。 |
| HeartFlow Structural (Future) | research only，future 概念区域。 | Hybrid digital twin，conceptual / future，not yet available。 |

### 致谢

最后一页为“Thank You”，背景图为奖杯样式图片，没有新增医学数据或模型参数。
