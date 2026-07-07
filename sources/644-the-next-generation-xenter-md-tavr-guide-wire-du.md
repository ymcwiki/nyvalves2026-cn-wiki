# 下一代 Xenter MD TAVR 导丝：双传感器血流动力学评估与无线云端数据采集

## 核心要点

* Guru TAVR guidewire 设计为 2 个压力传感器：主动脉传感器和左室传感器，导丝 coil tip 标注为 3 cm。
* 该系统用于快速评估 TAVR 前后跨瓣压差、术后 PVL，并试图减少对超声的依赖，从而节省时间和成本。
* 页面引用 dicrotic AR index 证据：预测显著 PVR 的 AUC 为 0.829（95% CI 0.747-0.911，p<0.001），优于传统 AR index 的 AUC 0.602。
* HARVi 计算模型将用不同程度主动脉反流并叠加心率、容量状态、血管张力、收缩力和残余瓣膜梯度等变量来预填充 AI 引擎。
* Xenter 生态由 Xenter smart devices、XenFi 无线网络、XMD 全球医疗云和 XenME 患者/医生软件组成，目标是把血流动力学监测变成无线、移动、可接入 AI 的数据流。

### 题目与讲者

幻灯片题目为“Next-Generation TAVR Guidewire”。讲者 William A. Gray MD FACC MSCAI，为 Main Line Health 心血管科系统主任、Thomas Jefferson University 医学教授、Phillip D. Robinson Endowed Chair in Cardiovascular Medicine。

### 利益披露

讲者在过去 24 个月内与一家生产、营销、销售、转售或分销患者使用医疗产品的公司存在财务关系。财务关系包括 consultant fees/honoraria，涉及公司 Xenter；individual stock(s)/stock options，涉及公司 Xenter。所有相关财务关系均已处理。Faculty disclosure information 可在 app 中查看。

### Guru 双传感器导丝

Guru 双传感器导丝：心脏示意图中标出两个 pressure sensors，一个位于主动脉侧，一个位于左室侧。

Guru two-sensor guidewire 的目标是快速评估 TAVR 术前和术后 procedural gradients，并评估术后 PVL。讲者称其可减少对 echo 的需求，从而节省成本和时间；还可在不需要资本设备的情况下，对操作成功进行客观、准确评估。图中导丝连接无线模块，压力传感器在心脏示意图中分别位于主动脉和左室相关位置。

### 传感器尺寸

传感器尺寸与一枚美国 10 美分硬币对比，传感器位于白色圆圈内。

该页用一枚 dime 作为参照展示传感器尺寸。白色圆圈内可见两个很小的传感器部件，意在说明传感器可以整合到导丝尺寸范围内。

### Guru TAVR 导丝的血流动力学功能

Guru Guidewire for TAVR：两个压力传感器分别采集主动脉和左室压力，并无线传输至 data hub，用于 xAR 和 xPR。

Guru Guidewire for TAVR 标注 2 个 pressure sensors：aortic sensor 和 left ventricle sensor。导丝远端标注 3 cm coil tip。压力数据通过无线方式传输到 data hub。输出包括 xAR，即 real-time aortic regurgitation measurement；以及 xPR，即 wireless continuous aortic pressure register。示意界面显示同步压力波形和实时数值，图中可辨认的面板示例包括 CaO 约 96.7/50.2、LV 约 96.4/0.0、ΔP 0.3、xAR 1，用于说明同时测量主动脉与左室压力差及反流相关指标。

### 空白过渡页

该页为空白过渡页，无文字、图表或数据。

### Dicrotic AR index 证据

研究通讯“A New Hemodynamic Index Predicting Paravalvular Regurgitation After TAVR”：dicrotic AR index 用于预测 TAVR 后显著 PVR。

该页引用 Jeehoon Kang、Jun Pil Yun、You-Jeong Ki、Hak Seung Lee、Jung-Kyu Han、Han-Mo Yang、Kyung Woo Park、Hyun-Jae Kang、Bon-Kwon Koo、Hyo-Soo Kim 等来自 Seoul National University Hospital 的研究通讯，题为“A New Hemodynamic Index Predicting Paravalvular Regurgitation After TAVR”。图 1 标题为 Dicrotic AR Index。上方波形示意中标注 systolic BP、dicrotic notch BP、diastolic BP、LV end diastolic BP，用于说明 dicrotic AR index 取决于返流造成的压力下降，并用主动脉与左室压力差标准化。

| 指标/阈值 | 显著 PVR 比例 | 统计结果 |
| --- | --- | --- |
| 传统 AR index <25 | 15.5% (20/129) | P=0.125 |
| 传统 AR index ≥25 | 9.2% (12/130) |
| Dicrotic AR index <3.3 | 31.7% (26/82) | P<0.001 |
| Dicrotic AR index ≥3.3 | 3.4% (6/177) |

ROC 曲线显示，dicrotic AR index 预测显著 PVR 的 AUC 为 0.829（95% CI 0.747-0.911，p<0.001）；传统 AR index 的 AUC 为 0.602（95% CI 0.490-0.713，p=0.063）。两者 AUC 比较的 p 值为 <0.001。dicrotic AR index 的 cutoff value 为 3.3，显示对显著 PVL/PVR 的区分能力更强。

### HARVi 计算模型与 AI 输出

HARVi 计算模型用不同程度 AR/PVL 和多种血流动力学变量模拟压力容量环与波形，为临床 AI 输出提供训练基础。

该页标题说明：Predictive analytics using HARVi computational modeling will inform clinical AI outputs。HARVi 正用于模拟 PVL，模拟包括不同程度的主动脉反流，并与以下变量耦合：heart rate、volume status、vascular tone、contractility、residual valvular gradient。右侧模型图包含 RA、LA、RV、LV 的压力-容量图，下面显示 LVP/LAP/AOP、LVV/LAV、MVF/AOF 等波形。讲者的设想是先用 HARVi 预填充 AI engine，等临床使用开始后，只需要验证 HARVi 输出即可。

### Xenter 生态系统

Xenter Ecosystem：智能器械、XenFi 无线网络、XMD 云端和 XenME 软件应用。

Xenter Ecosystem 由四部分组成。Xenter smart devices with AI clinical decision tools 负责采集和处理器械端数据；XenFi 是 wireless network；XMD 是 Global Healthcare Cloud；XenME 是 patient and provider software applications。整体结构显示导丝等智能设备经无线网络连接到云端和软件端，用于临床决策工具。

### 无线医疗器械理念

该页标题为 Wireless Medical Devices。核心定义是：“smart” medical devices transmitting real-time Physical Intelligence (PI) data that will make AI a reality in healthcare。中文理解为，智能医疗器械实时传输“物理智能”数据，使医疗 AI 能够基于真实、高频、连续的生理信号运行。

### Reveal 三传感器导丝

Reveal 三传感器导丝：图中三个蓝圈标出 pressure sensors，用于多种介入场景和即时病变压差信息。

Reveal three-sensor guidewire 被描述为可用于多种操作的 versatile workhorse guidewire。其功能包括：提供即时 lesion gradient information；具有形成新临床终点的潜力。图中三个蓝色圆圈标出压力传感器位置，提示该平台可以从 TAVR 扩展到更多介入场景。

### Avara 无线重症监测

Avara 无线重症监测：将动脉压力监测无线化，目标是节省护理时间、减少资本设备并为临床 AI 捕获高保真数据。

Avara Wireless Critical Care Monitoring 页面列出三个价值点。Staffing：节省大量时间且无需培训，使护士从重复操作中释放出来。Costs：消除昂贵资本设备，为 ICU 节省数千美元。Enables Clinical AI：直接从设备采集高保真数据，用于决策工具开发和研究。图像中展示前臂动脉导管连接无线模块的示意。

### 总结

总结页指出，Xenter Guru wire 将提供一种新的术中决策工具，通过快速分析同步压力波形，并安全连接到 AI 引擎，几乎即时评估 PVL 程度。支持 Guru wire 的 Xenter 生态还可扩展到医院内其他血流动力学监测场景，例如 arterial lines 和 PA catheters，使这些监测设备变得 smart 和 mobile。
