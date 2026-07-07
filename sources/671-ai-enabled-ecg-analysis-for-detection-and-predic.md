# AI 辅助 ECG 分析用于结构性心脏病的检测与预测

## 核心要点

* 研究把两个已部署的功能性 AI-ECG 二分类模型合成为一个 OR 规则：LVSD 阳性或 LVDD 阳性即为 composite AI-ECG 阳性，不重新训练、不重新校准。
* 横断面检测中，ISH 队列 n=46,082 的敏感性 71.8%、特异性 88.3%、NPV 95.6%；CUIMC 队列 n=36,286 的敏感性 76.1%、PPV 66.3%。
* 复合模型覆盖多种 SHD 表型：ISH 中 reduced LVEF、VHD、LVH、PH 的复合敏感性分别为 77.8%、72.2%、69.5%、79.7%。
* 新发 SHD 预测中，composite 阳性相对阴性的 HR 为 ISH 3.75、UKB 2.75；C-statistics 0.69–0.78，log-rank p<0.001。
* 同一 Youden 阈值跨韩国、美国、英国使用，未做站点特异性调参；作者定位为超声前分诊工具，不是疾病严重程度分期工具。

### 题目与讲者信息

本报告题为“A Composite AI-Enabled ECG for Detection and Prediction of Structural Heart Disease Across Multinational Cohorts”。中文可译为：复合 AI 辅助心电图用于跨国队列结构性心脏病的检测与预测。

讲者为 Hak Seung Lee, MD，来自 Digital Healthcare Institute、Sejong Medical Research Institute 和 Medical AI Co., Ltd.。会议为 CRF New York Valves, The Structural Heart Summit。

### 利益相关披露

讲者说明，在过去 24 个月内，与生产、营销、销售、转售或分销用于患者或作用于患者的医疗产品的公司存在财务关系。

| 财务关系性质 | 不合格公司 |
| --- | --- |
| 个人股票或股票期权 | Medical AI, Inc. |
| 版税或专利受益人 | Medical AI, Inc. |

### 结构性心脏病筛查缺口

Structural heart disease, SHD，即结构性心脏病，是 pre-HF Stage B 的结构基础，是心力衰竭和死亡的重要原因，但在临床中普遍诊断不足。

超声心动图可以给出确定诊断，但费用较高且可及性有限，不适合作为人群层面的普筛工具。AI-ECG 被视作广义心血管生物标志物，能够检测到超出名义训练目标的信号。

本研究提出的问题是：这种 AI-ECG 信号能否在多样化、跨国人群中，使用独立、已部署的模型，扩展到既往存在 SHD 和新发 SHD 的检测与预测。

页面引用：Elias et al., J Am Coll Cardiol. 2024 Jun 18;83(24):2472-2486；Croon, Khera et al., Circulation. 2025 Nov 4;152(18):1282-1294。

### SHD 的操作性定义

SHD 被定义为 4 类结构或功能异常中任意一类在超声心动图上存在。

结构性心脏病被描述为一组结构和功能性心脏异常，沿着连续谱进展至心力衰竭，常处于亚临床状态且诊断不足。

| 序号 | 表型 | 本研究标准 |
| --- | --- | --- |
| 1 | Reduced LVEF，左室射血分数降低 | 收缩功能障碍，LVEF <50% |
| 2 | Valvular Heart Disease，瓣膜性心脏病 | 中重度 AS、AR、MS、MR 或 TR |
| 3 | LV Hypertrophy，左室肥厚 | 最大左室壁厚度 ≥13 mm |
| 4 | Pulmonary Hypertension，肺动脉高压 | TR Vmax ≥3.2 m/s |

操作性定义为：上述四类中任何一类在超声心动图上存在，即判定为 SHD。标准来自 ASE/EACVI 与 ACC/AHA 指南中的超声心动图标准。

### 可部署的功能性复合 AI-ECG

Composite AI-ECG 的定义是：左室收缩功能障碍模型 LVSD 或左室舒张功能障碍模型 LVDD 任一阳性，即为复合阳性。该组合没有重新训练，也没有重新校准。

LVSD 模型训练目标为检测 LVEF ≤40%；LVDD 模型训练目标为检测室间隔 E/e′ >15。两个模型分别按预先定义的 Youden threshold 二值化。

两个模型均已在韩国获得监管批准并在临床部署，能够在照护现场输出可直接使用的二分类结果。

研究假设为：两个基于功能的 AI-ECG 模型只需一个简单 OR 规则，就可以捕捉完整 SHD 谱系，超越任一单模型的训练目标。

页面引用：Lee et al., Diagnostics (Basel). 2025 Jul 22;15(15):1837；Lim et al., J Am Heart Assoc. 2026 May 5;15(9):e046989。

### 为什么合并 LVSD 与 LVDD

LVSD 代表 reduced-EF 收缩通路，LVDD 代表充盈压/HFpEF 底物，OR 规则覆盖两条功能轴。

合并理由是两条结构性疾病的功能轴互补：LVSD 模型代表收缩功能障碍和 reduced-EF 通路；LVDD 模型代表舒张功能障碍、充盈压升高和 HFpEF 底物。OR 规则标记任一通路，从而共同覆盖 SHD 变得可由 ECG 电信号检测的功能谱。

讲者引用 Desai et al., JACC 2025/2026 的框架：在 FHS、CHS 和 MESA 三个美国人群队列中，使用相同的 LVSD+LVDD 二分类 OR 规则和预设阈值；composite 阳性个体的近期心衰风险升高 >20 倍；并优于 AHA 推荐的 PREVENT-HF 方程。

本研究把这一框架从心衰风险推广到完整 SHD 谱系，同时覆盖检测和预测，并在韩国、美国和英国的独立部署模型中验证。

页面引用：Desai et al., J Am Coll Cardiol. 2026 Mar 3;87(8):990-1005。

### 研究设计：三个跨国队列

ISH、CUIMC 和 UKB 三个队列用于横断面 SHD 检测和纵向新发 SHD 预测。

ISH 原始队列 n=141,690。排除 n=95,608：其中超声心动图数值缺失 n=85,568，ECG 与超声心动图间隔超过 14 天或 ECG 质量不合格 n=10,040。最终 ISH curated dataset 为 n=46,082。

CUIMC 队列 n=36,286，使用最近一对 ECG 与超声心动图，整理后数据集仍为 n=36,286。

UKB 队列 n=50,780。排除 n=9,554，原因是既往 HF 或 SHD 病史。最终 UKB curated dataset 为 n=41,226。

横断面 SHD detection 的输入数据集为 ISH 与 CUIMC；纵向 new-onset SHD prediction 的输入数据集为 ISH 与 UKB。

页面引用：Poterucha, Elias et al., Nature. 2025 Aug;644(8075):221-230。

### 既存 SHD 的检测性能

复合 AI-ECG 用于既存 SHD 检测；ISH 中每发现一例 SHD 需要的超声数约从 7.9 降至 2.1。

页面标题指出，在 ISH 队列中，每发现一例 SHD 所需的超声心动图数量约从 7.9 降至 2.1。

| 指标 | ISH，n=46,082 | CUIMC，n=36,286 |
| --- | --- | --- |
| 敏感性 Sensitivity | 71.8% | 76.1% |
| 特异性 Specificity | 88.3% | 70.1% |
| 阳性预测值 PPV | 47.2% | 66.3% |
| 阴性预测值 NPV | 95.6% | 79.1% |
| SHD 患病率 | 12.7% | 43.6% |

### 复合模型覆盖所有 SHD 表型

ISH 和 CUIMC 两个队列中，复合 AI-ECG 阳性在每一类 SHD 表型中均占多数。

图中蓝绿色为 AI-ECG composite positive，橙色为 AI-ECG composite negative；纵轴为占总队列的比例，横轴为 SHD、Reduced LVEF、VHD、LVH 和 PH。

| ISH 表型 | 占总队列比例 | composite 阳性 | composite 阴性 |
| --- | --- | --- | --- |
| SHD | 12.7% | 71.8% | 28.2% |
| Reduced LVEF | 7.5% | 77.9% | 22.1% |
| VHD | 3.7% | 72.2% | 27.8% |
| LVH | 1.7% | 69.5% | 30.5% |
| PH | 2.9% | 79.7% | 20.3% |

| CUIMC 表型 | 占总队列比例 | composite 阳性 | composite 阴性 |
| --- | --- | --- | --- |
| SHD | 43.6% | 76.0% | 24.0% |
| Reduced LVEF | 20.6% | 84.9% | 15.1% |
| VHD | 15.9% | 84.6% | 15.4% |
| LVH | 18.8% | 76.3% | 23.7% |
| PH | 13.4% | 79.6% | 20.4% |

讲者给出的解释是：在 reduced LVEF、VHD、LVH 和 PH 每一种表型内，复合阳性均占多数，因此信号覆盖完整 SHD 谱系。

### LVSD 与 LVDD 信号互补

CUIMC 队列中，按 LVSD 分数和 LVDD 分数分箱展示 SHD 及各表型患病率热图。

每份 ECG 同时由 LVSD 模型和 LVDD 模型打分，范围均为 0–100。图中纵轴为 AI-ECG LVSD score，横轴为 AI-ECG LVDD score，两个轴都按 [0,10)、[10,20)、[20,30)、[30,40)、[40,50)、[50,60)、[60,70)、[70,80)、[80,90)、[90,100] 分箱；单元格颜色代表患病率，色标为 0% 到约 90%。

热图包含 5 个面板：F 为 Composite SHD，G 为 Reduced LVEF，H 为 VHD，I 为 LVH，J 为 PH。复合 SHD 患病率随着两个轴上分数升高而升高，呈现分级梯度。Reduced LVEF 主要集中在 LVSD 分数较高的上方行，这是收缩功能信号。VHD、LVH 和 PH 在 LVDD 分数升高的右侧列更突出，说明舒张功能模型把检测范围扩展到 LVEF 以外的压力或容量负荷相关表型。

页面结论为：两个功能模型共同覆盖完整 SHD 谱系。

### 两个模型的分工

ISH 队列中按 SHD 表型分列的敏感性；CUIMC 中呈相同模式。

该页展示 ISH 队列中每个 SHD 表型的敏感性，单位为百分比。讲者注明 CUIMC 队列呈相同模式。

| SHD 表型 | AI-ECG LVSD | AI-ECG LVDD | Composite |
| --- | --- | --- | --- |
| Reduced LVEF | 68.9 | 57.9 | 77.8 |
| VHD | 36.8 | 68.5 | 72.2 |
| LVH | 28.7 | 65.2 | 69.5 |
| PH | 43.3 | 77.1 | 79.7 |

解读为：LVSD 主要负责 reduced LVEF；LVDD 模型驱动 VHD、LVH 和 PH 的检出，反映压力或容量负荷的电信号影子；复合模型把二者都纳入。

### 新发 SHD 的预测

ISH 与 UKB 中 composite 阳性组的新发 SHD 风险更高，曲线随访至约 6 年。

图 A 为 ISH，图 B 为 UKB。图例中橙色代表 AI-ECG composite negative，蓝绿色代表 AI-ECG composite positive。横轴为 Time，单位 year，从 0 到约 6 年；纵轴为 Survival probability。ISH 面板纵轴显示 0.00、0.25、0.50、0.75、1.00；UKB 面板聚焦于 0.85 到 1.00。

ISH 面板内标注 p<0.0001。页面底部汇总给出 composite 阳性相对阴性的 HR：ISH 为 3.75，UKB 为 2.75；C-statistics 为 0.69–0.78；log-rank p<0.001。

| ISH 风险人数 | 0 年 | 1 年 | 2 年 | 3 年 | 4 年 | 5 年 | 6 年 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| composite 阴性 | 3502 | 3175 | 2404 | 1702 | 1141 | 666 | 273 |
| composite 阳性 | 608 | 507 | 364 | 248 | 157 | 91 | 43 |

| UKB 风险人数 | 0 年 | 1 年 | 2 年 | 3 年 | 4 年 | 5 年 | 6 年 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| composite 阴性 | 34172 | 33810 | 30381 | 19948 | 13089 | 8205 | 4568 |
| composite 阳性 | 7054 | 6934 | 6069 | 3774 | 2026 | 1221 | 678 |

页面结论为：在基线无 SHD 的个体中，composite 阳性可识别新发 SHD 风险约 3–4 倍升高的人群，可用于临床前风险分层。

### 训练目标窄，检测范围广

模型训练在严格阈值上，但应用时检测到更宽的 SHD 谱系，并跨多个国家人群迁移。

训练目标较窄：LVSD 模型训练于 LVEF ≤40%，LVDD 模型训练于 E/e′ >15。检测目标则包括 SHD 谱系：LVEF <50% 的 reduced LVEF、中重度 VHD、LVH 和肺动脉高压。

跨人群迁移结果为：韩国 ISH 的检测敏感性 71.8%；美国 CUIMC 的检测敏感性 76.1%；英国 UKB 的预测 HR 2.75。

讲者强调，相同的 Youden-derived thresholds 未经重新校准直接应用，在 SHD 患病率相差 3.4 倍的范围内表现一致。

### 为何具有即时部署意义

该方法使用已有二分类模型输出，可以立即放入临床工作流，不需要原始概率，也不需要站点特异性调参。

其性能与在同一队列上训练的端到端 SHD 标签模型相当，没有明显检测损失。

该方法与 Desai 等人的底层逻辑一致：用 AI-ECG 输出的 OR 规则复合信号捕捉更广泛的心血管风险，并预测新发心力衰竭。

其最有价值的使用场景是影像和专科资源有限的环境，用于优先安排患者接受超声心动图和转诊。

### 局限性

第一，本研究为观察性设计，因果推断和结局获益仍需要前瞻性验证。

第二，新发 SHD 不是通过方案规定的影像随访时间表捕获；ISH 中来自临床指征，UKB 中来自 ICD 编码，因此可能存在 surveillance bias。

第三，composite 是筛查信号，不是疾病严重程度或疾病分期的量化指标。

### 带回信息

复合 AI-ECG，即 LVSD 或 LVDD 任一阳性，可以在韩国、美国和英国人群中检测既存 SHD 并预测新发 SHD。

其表现跨不同表型和不同人群保持一致，并具有较强的筛查效率。

该研究支持将 AI-ECG 作为可部署的广义心血管筛查工具，应用范围超出各单独模型原本的训练目标。
