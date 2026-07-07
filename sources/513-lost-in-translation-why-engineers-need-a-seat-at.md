# 断译：为什么工程师需要坐到临床桌前

## 核心要点

* 讲者从工程研发视角指出，医疗器械从概念到临床的转化并非在产品锁定后结束，工程师和临床医生需要贯穿概念、早期可行性、关键研究、PMA 和商业化全生命周期。
* 所谓“lost in translation”主要发生在 Phase III 与 Phase IV 之间：临床研究被当成单纯执行，工程团队不再深度支持病例，现场经验和影像信号没有及时回流到设计和标准。
* ACURATE IDE 随机对照研究中，ACURATE neo2 在 1 年主要终点上未能证明对商业化瓣膜非劣效，后验中位差 6.63%，95% BCI 上限 10.20% 超过 8.0% 非劣效界值。
* 根因调查发现瓣膜欠扩张是重要问题，改进方向包括有效预扩、围术期双视角影像评估、可行时后扩，以优化 ACURATE neo2 扩张。
* 讲者主张把 bench testing imaging、透视/医学影像、PIV、FEA、blood loop、3D light scanning、material shedding 等工程工具转化进标准，推动工程、临床、产业、学术和监管共同学习。

### 标题与讲者身份

本讲题为“Lost in Translation: Why Engineers Need a Seat at the Clinical Table”，中文可译为“断译：为什么工程师需要坐到临床桌前”。讲者为 Aaron Chalekian, M.S.，职务为 Boston Scientific VP - R&D Emerging Therapies。会议标识为 CRF New York Valves, The Structural Heart Summit。

### 相关经济关系披露

讲者声明，在此前 24 个月内，与生产、营销、销售、转售或分销患者用医疗产品的公司存在经济关系；所有相关经济关系已被缓解，完整 faculty disclosure 可在会议 app 中查看。

| 经济关系性质 | 不合格公司 |
| --- | --- |
| 雇佣关系 | Boston Scientific Corporation |
| 董事会成员与投资者 | Veravas Inc. |

### 从概念到临床：早期工程教训

讲者用心脏外科和瓣膜发展史说明，产品成功的核心是工程、临床与使用场景协作。

本页题为“Concept to the Clinic”，副标题为“My Early Lesson as an Engineer in the Med Device Industry (~25yrs)”。左侧为 G. Wayne Miller 的书《King of Hearts》，副标题为“The True Story of the Maverick Who Pioneered Open Heart Surgery”。中间为 University of Minnesota 心血管医学历史“firsts”海报，列出世界首个心脏医院 1951、世界首例成功开放心脏手术 1952、世界首例使用 cross-circulation 的成功开放心脏手术 1954、世界首个功能性心肺机开发 1955、世界首例成功人工心脏瓣膜植入 1958、首个便携式起搏器开发 1958、首例 Minnesota 心脏移植 1978、首例 Minnesota ventricular-assist device 植入 1995。海报注释还提到首个电池供电外置起搏器由 Earl Bakken 开发，并由 C. Walton Lillehei 植入；右侧为“Legends of Heart Valves: Jeff & Jim ETL - St. Jude Medical”。底部写有“Rub Walt’s Nose for Luck”和“Collaboration is the Key to a Products Success!”。该页用历史经验提出主线：临床现场、工程实现和产品成功需要持续协作。

### 医疗器械开发旅程：工程视角

工程视角下的医疗器械开发包含五个阶段，从 idea 到 ideal product，并穿插早期可行性和 pivotal/PMA 临床工作。

本页题为“Medical Device Development Journey: An Engineering Point of View”。中央为“Phase of Medical Device Development Process”。Phase I 是 Initiation、Opportunity & Risk Analysis，对应“The Idea”。Phase II 是 Formulation、Concept & Feasibility，对应“CONCEPT”和 Clinical Work - Early Feasibility；左下强调“Iteration”，并写有“Perfection is the Enemy of Good Enough”。Phase III 是 Design & Development/Verification & Validation，对应“Lock the Design Down”。Phase IV 是 Final Validation/Product Launch preparation，对应 Clinical Work - Pivotal/PMA，并以“Design Refinement”和“Optimization to Perfection”提示临床前后的设计精炼。Phase V 是 Product Launch & Post launch Assessment，对应 LAUNCH 和“The Ideal Product”。这一页给出工程团队眼中的完整开发路径：想法、概念、验证、关键临床、上市和上市后评估是连续过程。

### Phase I-IV：理解需求、流程和解剖

需求理解必须覆盖使用场景、工作流、解剖和生理，包括术者使用、患者植入与恢复，以及血管通路解剖。

本页题为“Phase I-IV. Understanding the Requirements: Use Cases, Workflow, Anatomy & Physiology”。左侧展示导管室、病房和恢复场景，蓝色箭头标注“Operator Use & Patient Implantation → Recovery”。恢复阶段被分为 Flat in Recovery、Sitting Up in Recovery、Walking to Recovery，提示产品需求不能只考虑植入瞬间，也要考虑术后卧床、坐起、行走等状态。右侧为 CT 三维重建，Anterior View 标注 Axillary Artery (Left) 和 Femoral Artery (R & L)，Lateral View (off axis) 标注 Overall Artery (3D Tortuosity)。这一页强调，工程需求应来自真实使用流程和真实解剖，而不是只来自抽象规格。

### Phase II-III：迭代与优化

标准可指导有效设计迭代、系统评估和优化，但产品使用的直接经验仍是关键输入。

本页题为“Phase II - III. Iteration and Optimization”。中间横幅写着“Standards Help Guide Effective Design Iteration, Optimization over the life cycle of medical device development”。三个板块分别是“Apples to Apples Evaluations”，即用一致条件进行对照评估；“System Assessments”，即系统层面的台架、人体模型或解剖模拟评估；“Optimization”，即通过专用台架和计算模型调整产品几何与性能。底部引用语为“The direct experience with product use is still the best way to iterate and optimize” - GF。该页核心是：标准重要，但不能替代使用者和临床现场带来的直接反馈。

### Phase III-IV：断译发生的位置

讲者认为 Phase III 与 Phase IV 之间常出现工程与临床连接断裂，现场学习没有进入设计反馈。

本页题为“Medical Device Development Journey: Lost in Translation Between Phase III & IV”。左侧复用开发阶段图，箭头指向 Phase III 设计/验证和 Phase IV 最终验证/上市准备之间。右侧列出“Phase III & IV. Lost in Translation”中的 4种错误认识：工程师不再需要支持病例；设计已经锁定，所以临床研究只是执行；匿名化数据并把事情管紧是临床研究最重要的事；我们学到了一些东西，但试验很难停止和重新启动。底部总结为“Somewhere in this Phase (III & IV) the connection between engineering and the clinic is lost”。该页是全讲的论点核心：关键研究阶段仍然需要工程和临床的双向学习。

### ACURATE-TAVR：失败临床研究案例

ACURATE-TAVR 作为案例，说明早期境外经验没有充分转化到美国临床试验产品采用中。

本页标题为“ACURATE - TAVR: A Failed Clinical Study”，副标题为“What was Learned & How BSC Decided to Do Better”。Why The Trial Failed：早期 OUS，即美国以外早期使用经验中的关键产品学习，没有被转化到美国试验中的产品采用。BSC Consciously Decided to Move Forward：Boston Scientific 决定退役该产品，从错误中学习，并与整个社区分享。该页将“断译”具体化为产品和试验策略层面的案例。

### ACURATE IDE 结果：非劣效未达成

ACURATE IDE RCT 中，ACURATE neo2 对商业化瓣膜在 1 年主要终点上未证明非劣效。

本页题为“What Were the Results?”。ACURATE IDE 随机对照研究中，ACURATE neo2 未能在 1 年主要终点上证明对商业可用瓣膜非劣效；主要终点为全因死亡、卒中或再住院。脚注说明再住院指 valve-related symptoms 或 worsening congestive heart failure，NYHA III或 IV级，按 VARC-2 定义。

| 设计/分组 | 信息 |
| --- | --- |
| 总样本 | N=1500 TAVR 患者 |
| 入组病种 | 有症状重度原生主动脉瓣狭窄 |
| 对照瓣膜选择 | 术者在若随机到 Control 前预先指定要使用的瓣膜类型 |
| 随机方式 | 1:1 随机 |
| ACURATE neo2 | N=752 |
| Mixed Control | N=748，其中 Evolut N=244，SAPIEN N=504 |

| 贝叶斯分析项目 | 结果 |
| --- | --- |
| ACURATE neo2 后验中位数 [95% BCI] | 16.16% [13.38%, 19.07%] |
| Control 后验中位数 [95% BCI] | 9.53% [7.47%, 11.89%] |
| 后验中位差 [95% BCI] | 6.63% [3.04%, 10.20%] |
| 非劣效界值 | 8.0% |
| 非劣效后验概率 | 77.9%，低于非劣效检验阈值 97.5% |

图中曲线显示 95% BCI 上限超过预设 8% 非劣效界值，因此页面结论为：ACURATE neo2 相对 Control 的主要终点非劣效未达成。

### 发现瓣膜欠扩张：瓣膜应该是什么样

随访 CT 清楚显示 ACURATE 欠扩张，提示术后评估和图像判读需要更明确标准。

本页题为“Valve Under Expansion Found: Lost in Translation - How should the valve look?”。左侧 Pre-Screening 显示术前 CT/模拟横断面，标注 RC、LC、NC。中间“Angulated commissure Posts”透视图用绿色和红色虚线提示交界柱角度偏斜。右侧 Post Implant Assessment 显示三维重建和瓣架模型，绿色框写着“Follow Up CT’s Clearly Showed Under Expansion”，底部红条写着“Under Expanded ACURATE”。该页说明，欠扩张并非抽象质量问题，而是术后 CT 能清楚显示的形态问题；问题在于临床、工程和标准之间是否对“正确展开形态”形成一致语言。

### 研究教训：工程和临床共同根因调查

根因调查提出预扩、双视角围术期影像评估和后扩作为 procedural optimization 机会。

本页题为“What are the lessons learned from this study? A Root Cause Investigation - Collaboration: Engineering & Clinical”。页面列出 3个总教训：此类 root cause investigation 需要工程团队和临床团队共同参与；最佳瓣膜扩张对于降低临床结局风险至关重要；研究识别出 procedural optimization 的机会。

| 优化方向 | 具体内容 |
| --- | --- |
| Routine use of effective pre-dilation | 推荐对 ACURATE neo2 进行预扩；BAV 球囊尺寸应比瓣环直径小 1 mm。 |
| Peri-procedural imaging assessment in two views | 欠扩张更容易通过 2个造影视角识别，例如 3-cusp 和 cusp overlap。 |
| Post-dilation when feasible | 可行时应进行后扩，以改善扩张；页面右侧用 before post-dilation 和 after post-dilation 透视图对比，后扩后绿色参考线显示框架更接近平行和充分展开。 |

### 从台架到医学影像：弥合影像差距

台架测试影像与医学透视影像之间应建立可翻译的对应关系，帮助术者识别瓣膜展开状态。

本页题为“Bench to Medical Imaging (Ex. Fluoroscopy): Bridging the Imaging Gap”。左侧为 Bench Testing Imaging，注释写明视频是 ACURATE 在 pulse duplicator 上评估瓣膜性能的测试。中间用等号连接台架影像和医学影像，并以红线、绿线、黄框示意瓣架纵轴、交界柱和横断面观察窗口。右侧为 Medical Imaging，透视横断面图中标注 N、L、R，对应无冠、左冠、右冠方位。底部结论为“Translational Imaging = Engineering to Medical Imaging”，并建议将这种转化影像方法纳入下一次 ISO 标准更新。该页的含义是，工程测试中看到的结构表现必须能被临床透视语言识别，否则现场学习无法回到标准和设计。

### 工具转化为标准：增强瓣膜设计

工程工具包括 PIV、计算建模、FEA、blood loop、3D light scanning 和 material shedding，可转化为改进瓣膜设计的标准化工具。

本页题为“Tools Translated to Standards”，副标题为“Ways to enhance valve design!!!”。左侧为 Particle Image Velocimetry (PIV) & Computational Modelling，展示流场装置、bioprosthesis 附近 flow distribution、velocity magnitude 和 velocity vectors。中间上方为 FEA Modelling，显示瓣膜有限元模型；中间下方为 Blood loop Testing，展示血液循环测试中的瓣膜。右侧上方为 3D Light Scanning，显示瓣叶或瓣膜结构三维扫描；右侧下方为 Material Shedding，显示材料脱落/颗粒或表面变化相关图像。该页主张把这些工程评估工具变成可共享、可监管、可迭代的设计标准。

### 结论：下一阶段可以做得更好

结论页标题为“Conclusion: We’re at the Next Phase of Evolution”，核心句为“We Can Do Better”。讲者指出，工程师和医生需要参与整个开发周期，包括 Concept、Early Feasibility、Pivotal Study、PMA，以及商业化产品的全生命周期。原因是临床试验只是学习使用者交互、解剖交互、观察趋势和临床结局关系的起点。关键责任方包括 Academia、Industry、Clinicians 和 Regulatory Agencies。具体行动包括通过增强标准带来更可靠产品，以及推动临床医生与产业界协作学习和持续参与。

### 致谢

最后一页为“Thank You!”致谢页，会议标识为 CRF New York Valves, The Structural Heart Summit。
