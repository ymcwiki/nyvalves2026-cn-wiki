# 个体化二尖瓣介入：从高级影像到AI预测工具

## 核心要点

* 讲者把AI定位为结构性心脏影像的过去、现在和未来，重点覆盖M-TEER、TMVR/TTVR规划、导航和介入。
* 瓣膜影像分割从人工到深度学习大幅提速：总分割时间由46小时降至70分钟再降至17分钟；用户时间由46小时降至60分钟再降至3.5分钟。
* LARALAB/Abbott相关工具展示了自动CT分割、自动CT测量、病例规划和AI二尖瓣叶重建，可分析动态瓣环、目标区和周围结构，例如RCA。
* ECHO-PREP提出全自动临床工作流：算法1处理TTE视图识别和质量，算法2处理TEE视图识别和M-TEER适合性，算法3通过图像测量支持M-TEER eligibility和M-TEER decision。
* Algorithm 3使用MVSEG2023 Challenge数据集，135个3D体积，70%/15%/15%划分，并采用MONAI Auto3DSeg分割瓣叶和瓣环。
* 未来工具包括digital twin、AI器械检测、AutoNavigate、增强现实、机器人、术中摄像训练集和适配AI创新速度的监管框架。

### 题目与机构

本报告题为“Personalized Mitral Intervention: From Advanced Imaging to AI based predictive Tools”。中文可译为“个体化二尖瓣介入：从高级影像到AI预测工具”。讲者为Ralph Stephan von Bardeleben, MD，来自Montreal Heart Institute Canada和University Medicine Mainz Germany。

### 相关财务利益披露

术者为Dr Ralph Stephan von Bardeleben。讲者披露，与Abbott、Edwards、Luxvalve、Medtronic、NeoChord、Leaflet Solutions、Philips、Siemens存在临床试验、proctor和讲者关系。学术研究者发起研究，即Academic IIT，与IZKS Göttingen和DZHK Germany相关。页面注明所有相关财务关系均已被缓解，讲者披露信息可在会议应用中查看。

### 结构性影像中的AI从何而来

本页提出问题：“AI in structural imaging: where do we come from?”，即结构性影像中的AI从何而来。左下角写有“Current and Future Role of Artificial Intelligence in Cardiac Imaging”，即人工智能在心脏影像中的当前和未来角色。右侧展示心脏影像切面与三维网格重建，提示从传统影像进入计算建模和AI辅助分析。

### 瓣膜影像深度学习的效率变化

AI深度学习用于瓣膜影像分割，从人工到2015分割算法再到2020深度学习，分割时间和用户时间显著缩短。

| 方式 | 时间节点 | 总分割时间 | 用户时间 |
| --- | --- | --- | --- |
| Manual，人工 | 01 | 46小时 | 46小时 |
| Segmentation algorithms，分割算法 | 2015 | 70分钟 | 60分钟 |
| Deep Learning，深度学习 | 2020 | 17分钟 | 3.5分钟 |

本页强调AI with Deep Learning在瓣膜影像中的应用，左侧展示心脏多结构彩色分割，右侧用流程图表示人工、传统分割算法和深度学习的演进。

### AI与二尖瓣介入影像

二尖瓣手术和介入中，AI影像可用于自动CT分割、自动CT测量、病例规划和二尖瓣叶自动重建。

本页标题为“AI and Imaging in Mitral Heart Valve Procedures”。列出的能力包括Automatic CT Segmentation，即自动CT分割；Automated CT Measurements，即自动CT测量；Case planning，即病例规划；Automatic AI based Reconstruction of Mitral Leaflets，即基于AI的二尖瓣叶自动重建。右侧图像显示重建出的二尖瓣瓣环、瓣叶和邻近结构。页面注明LARALAB GmbH现在已被Abbott SH收购。

### 二尖瓣和瓣膜装置重建

二尖瓣与瓣膜装置的三维重建示例，显示瓣环、瓣叶、左心房/左心室和邻近血管结构。

页面标题为“Reconstruction of the Mitral and valvular apparatus”。左侧三维图显示二尖瓣瓣叶、瓣环和周围结构，瓣叶呈黄色，瓣环/邻近结构以不同颜色区分。右侧图显示心脏外形和多腔室/血管重建，二尖瓣区域以黄色突出。底部标注“Confidential - LARALAB GmbH - 2023”。

### LARALAB/Abbott自动标注界面

LARALAB GmbH Germany now Abbott界面示例，显示多平面CT、D形二尖瓣瓣环、三角区、左心房中心、左心室中心和乳头肌距离等标注。

本页展示LARALAB GmbH Germany now Abbott的多视图规划界面。左上CT视图标有ANNULUS、LV CENTER、LA CENTER、LAA ORIFICE、TRIGONE LEFT、TRIGONE RIGHT，并显示“Mitral D Shaped Annulus”。右上视图标有2 CHAMBER、LVOT、4 CHAMBER、LAA ORIFICE、PAP DIST AL、PAP DIST PM、DTT、TRIGONE LEFT和TRIGONE RIGHT。左下和右下分别显示长轴/三维视图及粉色瓣环轨迹。屏幕角度标注包括RPO 38、CRA 17，RAO 55、CAU 10，LAO 7、CRA 70，以及RPO 45、CRA 22。

### CT几何量化工作流示例

从体积分割到舒张末/收缩末识别、瓣环几何、右冠到瓣环距离、组织架角度和统计分析的一整套量化流程。

本页展示A至H八个步骤。A为Volumetric segmentation，即体积分割。B为Identify and analyze the end-systolic and end-diastolic phases，即识别并分析收缩末期和舒张末期；上方RV Volume曲线显示容量随心动周期变化，纵轴至约400 ml，横轴为Phase 0%至100%。C为Quantify annular geometry，即量化瓣环几何。D为Quantify right coronary artery to annulus distance，即量化右冠状动脉至瓣环距离，图中多点距离标注约在3至12 mm范围。E为Quantify annular tissue shelf angles and lengths，即量化瓣环组织架角度和长度。F为Quantify size, position, and orientation of the inferior and superior vena cava，即量化上下腔静脉大小、位置和方向。G为Quantify annular excursion，即量化瓣环运动幅度。H为Statistical analysis of all measures between the studied groups，即对研究组间所有测量值做统计分析；示例柱状图标注p<0.05，纵轴刻度从0至40。

### AI在二尖瓣介入中的三个环节

本页标题为“AI and Mitral Heart Valve Procedures”。三个方块依次为Automatic CT Segmentation，即自动CT分割；Automated CT Measurements，即自动CT测量；Case planning，即病例规划。页面用三个模块概括AI在二尖瓣结构性介入前的基础工作流。

### 术前规划：动态瓣环和目标区域

术前规划示例：分析动态瓣环、目标区域及周围结构，并给出一键式AI自动测量。

本页标题为“Pre-procedural Planning”。文字说明包括：分析动态瓣环和目标区域，包括周围结构，例如RCA；使用one-click和AI based automatic方法。右侧显示三维心脏/瓣环重建。左下角自动测量小窗写有“Tricuspid 10% - projected”，并列出max(3d) 57.1，括号内57.2；min 46.1；mean 51.2，括号内51.1；Perim(3d) 160.6，括号内163.6；Area 1999.6。该页强调一键式测量和目标结构空间关系。

### AV和三尖瓣介入的4D融合

4D Fusion用于主动脉瓣和三尖瓣介入，透视影像和结构性影像/植入物规划相结合。

本页标题为“4D Fusion for AV and Tricuspid Valve Interventions”。左侧显示介入透视图像，右侧显示Structural Heart Valve Center、MHI AI Core Lab和Cardiac Implants标识。文字说明包括：反馈回路包含来自手术数据的学习；未来方向是4D live guidance，即4D实时引导。

### TMVR和TTVR器械规划

TMVR和TTVR术前器械规划示例，三维重建中显示植入物与腔室/瓣环的空间关系。

本页标题为“TMVR and TTVR Procedural Planning”。左侧文字为Device Planning。右侧两幅三维体积渲染图显示拟植入器械、瓣环/腔室和参考红线的位置关系，上下两图均标注Volume Rendering并显示80.0%。该页强调在TMVR和TTVR中利用影像进行器械路径和位置规划。

### M-TEER的AI决策工具与ECHO-PREP流程

拟议的ECHO-PREP全自动临床流程：TTE筛查、TEE适合性判断和图像测量支持M-TEER决策。

本页标题为“AI decision tools M TEER Valve Interventions”和“Proposed fully automatic clinical workflow for ECHO-PREP”。左侧问题是“Suspect pathological Mitral valve?”，即是否怀疑二尖瓣病变。Algorithm 1以TTE为输入，包括View Identification、View Quality和Pathological MV?。Algorithm 2以TEE为输入，包括View Identification、View Quality和M-TEER eligible?。Algorithm 3分为两列：M-TEER eligible包括Valve area、Calcifications、Flail/gap width、Single vs Multi jets、Non image related clinical factors；M-TEER decision包括Leaflet thickness、Leaflet length、Device selection和Procedural planning。

### Algorithm 3：图像测量

Algorithm 3说明为何需要图像测量、使用的数据集，以及自动分割与测量提取流程。

左侧流程重复列出M-TEER eligible的Valve area、Calcifications、Flail/gap width、Single vs Multi jets、Non image related clinical factors，以及M-TEER decision的Leaflet thickness、Leaflet length、Device selection、Procedural planning。Why部分说明：除临床特征外，解剖测量是评估患者是否适合M-TEER的关键；测量需要标准化，因为不同术者可能略有差异；自动测量提供更精简且一致的解剖评估方法。

Dataset部分为MVSEG2023 Challenge dataset，会议为MICCAI 2023，共135个3D volumes，数据划分为70%/15%/15%。How部分包括：对相关解剖特征进行分割，特征为leaflets和annulus，方法为MONAI Auto3DSeg；识别mid-diastole frame；进行annulus post-processing；提取landmarks and measurements。

### 手工瓣环标注过程与病例示例

手工瓣环标注流程的上视图分析，展示10个代表病例，包含超声加分割、MVSEG瓣叶、控制点样条和增强数据集。

本页图题为“Manual Annulus Annotation Process: Superior View Analysis”。副标题说明：10个代表病例，上视图，top-down，B-spline interpolation，semi-automatic annotation pipeline。列出的病例包括Case 018、Case 190、Case 039、Case 022、Case 047、Case 073、Case 029、Case 077、Case 076和Case 069。A行显示Echo + Segmentation侧面视图。B行显示MVSEG Leaflets上视图，蓝色和红色代表瓣叶区域。C行显示Control Points + Spline，24个点。D行显示Enhanced Dataset with Annulus，加入瓣环轮廓后的增强数据。

### 3D平面可视化与峰值帧瓣膜投影

本页与前一页之后的病例投影页视觉内容重复，显示两个病例的3D plane visualization和peak frame valve projection。正文在下一节嵌入该非重复图并完整转写。

### 两个病例的峰值帧投影

多角度3D视图、PCA最优平面和峰值帧瓣膜投影示例，分别显示两个病例的瓣口面积。

左侧为Case 256466，图题为“3D Plane Visualization & Peak Frame Valve Projection”。副标题说明为Multi-Angle 3D Views、PCA-Based Optimal Plane、Peak Frame Valve Projection、real case，峰值帧为10。上方A1为Anterosuperior Corner View，A2为Posterosuperior Corner View，坐标轴单位为mm。下方B为Valve Plane Projection，标注Peak Frame 10，EA为692 mm²，下方包含Original Valve Projection、Inverted Mask (Label 4)和Final Segmentation三幅小图。

右侧为Case 381643，同样为多角度3D视图和峰值帧瓣膜投影，峰值帧为7。下方B标注Peak Frame 7，EA为37 mm²，同样展示Original Valve Projection、Inverted Mask (Label 4)和Final Segmentation。

### 下一步

本页为过渡页，标题为“WHAT IS NEXT?”，即“下一步是什么？”背景为红紫渐变，无其他数据或图表。

### Laza Procedure

Laza Medical系统概念图：术者手持探头，床旁设备带有超声屏幕。

本页标题为“Laza Procedure”，右上角标注LAZA Medical。图中术者手持柔性探头/导管，患者仰卧，床旁设备屏幕显示超声图像。底部声明为：©2024 Laza Medical；免责声明称Laza Medical System仍在开发中，未在美国或全球任何地区获准使用。

### Probe Navigation探头导航

Laza Medical探头导航示意，显示机器人臂、柔性探头、控制屏和右侧导航圆形视野。

本页标题为“Probe Navigation”。图中显示设备机械臂伸出柔性探头，控制屏上有瓣环样界面和黄色扇形超声视野，右侧有圆形导航空间与探头头端。底部同样声明：©2024 Laza Medical；该系统处于开发阶段，未在美国或全球任何地区获批。

### Laza场景中的手术室显示

手术室场景概念图：床旁探头、介入团队、超声图像和三维解剖显示整合在大屏幕中。

本页显示Laza Medical相关手术室场景。患者位于手术床上，左侧设备插入探头，床旁有控制屏；大屏幕左侧显示TEE图像，右侧显示粉色三维解剖/操作示意。两名术者站在床旁观察屏幕。底部继续标注©2024 Laza Medical及开发中、未获批的免责声明。

### 三维瓣膜近景示意

暗背景下的三维瓣膜/腔内结构近景，呈蓝色和橙色高亮。

本页无标题和文字说明，主要显示一个暗背景下的三维瓣膜或腔内结构近景，结构边缘以蓝色高亮，中央开口周围有橙色区域，像是Laza或增强现实显示中的局部解剖视图。

### Philips与Edwards Pascal的AI器械检测

AI器械检测示例：Philips平台结合Edwards Pascal，融合超声、3D和透视图像。

本页标题为“AI Device detection Philips with Edwards Pascal”。屏幕左侧显示多个超声视图和三维瓣膜图像，右侧显示透视影像；超声和透视图上有彩色线条标记器械轴线或识别结果。该页展示AI在M-TEER器械识别和多模态导航中的应用。

### 瓣膜模型中的流场/力学可视化

三幅二尖瓣/心室模型的流线和颜色图，展示不同状态下的流场或应力分布。

本页左上角编号为23。三幅模型图展示类似心室或瓣膜装置的流线/颜色场，蓝色到红色表示不同强度区域。左图显示相对规则的流线和两个局部涡旋；中图显示更复杂的多涡旋；右图显示靠近瓣膜装置或流入口处的高强度红黄色区域。该页用于说明计算模型可视化在个体化评估中的作用。

### 速度场可视化

两幅速度场图，色标从0到0.7，显示瓣膜/腔室模型内速度分布。

本页左上角编号为24。左图为较完整的半透明心室/瓣膜模型，右侧有速度色标，标注Velocity(m/2)，范围从0到0.7，中间刻度为0.1、0.2、0.3、0.4、0.5、0.6。右图为点云样模型，也有相同的速度色标0至0.7。多数区域呈蓝色低速，局部区域有绿色到黄色更高速度。

### 治疗规划用二尖瓣digital twin

从CT或3D超声生成二尖瓣装置digital twin，用于治疗策略、器械选择尺寸和优化结果。

本页标题为“Digital twin of the mitral valve apparatus derived from CT or 3D echo for therapy planning”。流程从影像估计二尖瓣解剖开始，输入可为US、MRI、CT和DynaCT。随后创建患者特异性二尖瓣生物力学模型，包含leaflets、chordae、mitral annulus、papillary tips和fiber directions。下方目标包括：为患者规划治疗策略；进行器械选择和尺寸确定；优化获得良好结局的机会。

### 患者特异性瓣膜闭合计算

digital twin中的二尖瓣闭合、应力和不同心动周期状态计算，包含峰收缩和早舒张。

本页左上角编号为26。左侧显示Peak Systole和Early Diastole两种状态，旁边有应力色标S1，单位kPa，范围从0到500，中间刻度250。右侧展示多角度二尖瓣模型和瓣叶/腱索样结构，既有解剖表面也有蓝绿色应力分布。该页对应digital twin中“Personalized Computation of Valve Closure”的概念。

### AI驱动AutoNavigate瓣膜介入

AI driven AutoNavigate Valve Interventions示意，左侧为第一视角画面，右侧为三维心腔与器械轨迹/目标区域。

本页标题为“AI driven AutoNavigate Valve Interventions”。左侧画面像内镜或仿真第一视角，中央有黑色十字准星。右侧显示三维心腔、蓝色瓣膜/目标结构、红色球形目标区域和器械轨迹。左上角界面显示ROS IP: 192.168.0.100:10003。该页用于说明AI导航可把解剖、器械和目标点整合到实时路径引导中。

### 增强现实/空间显示示例

本页无标题文字，显示一幅增强现实或空间可视化画面：大量蓝色半透明方块构成类似空间地图/点云，黑色器械或摄像对象位于其中，底部有界面按钮，包括“BACK”等。该页作为AutoNavigate或增强现实场景的视觉过渡。

### 明日二尖瓣介入工具箱

未来二尖瓣介入工具包括自动化、AI、医学教育、基因组学、机器人、增强现实和大数据可视化。

本页标题为“The tools of (Mitral) Heart Valve interventions tomorrow”。列出的工具包括Automation、Artificial Intelligence、Medical Education、Genomics、Robotics、Augmented Reality和Big Data Visualization。中间背景图展示未来医疗场景，包含全息人体、医生、机器人设备、虚拟屏幕和增强现实眼镜。

### 基于介入摄像的训练

术中摄像训练集示例，人体姿态和手部关键点被彩色骨架线标注。

本页标题为“Interventional Camera based Training”。正文写明：收集高质量、标准化和术中数据集，用于训练AI算法并验证新技术。配图中两名穿手术衣人员的手臂、手部和身体关键点被绿色、黄色、红色、橙色、蓝色等线条标注，显示AI可从术中摄像数据学习操作动作。

### 监管规则需要适应AI创新速度

欧盟和北美监管规则需要适应医学中AI创新速度，同时评估安全性、有效性和伦理影响。

本页标题为“EU, North American Regulatory Rules will have to adapt to AI speed of innovation in medicine”。右侧文字说明，法规和指南需要评估这些技术整合进入临床实践时的安全性、有效性和伦理影响。左侧显示英国报告封面“A pro-innovation approach to AI regulation”，说明该报告于2023年3月由Secretary of State for Science, Innovation and Technology以His Majesty名义提交议会，编号为CP 815。右下图为机器人手指触碰光点。

### 带回家的信息

最后总结为“Take Home: Advanced Tools in Mitral Structural Imaging”。要点包括：AI是过去、现在和未来；AI将显著影响M-TEER和TMVR的规划、导航和介入；AI为可重复性和培训机会增加潜力；介入影像将从knobology，即依赖手动旋钮操作的技能，转向autoNavigate；讲者邀请听众为AI未来做好准备，参加MOSAIC Montreal Structural AI Course，日期为2026年10月1日至3日。
