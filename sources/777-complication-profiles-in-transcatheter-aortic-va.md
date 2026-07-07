# 经导管主动脉瓣置换并发症谱：56,806 份 FDA MAUDE 不良事件报告的自然语言处理分析（2012-2025）

## 核心要点

* 研究分析 openFDA MAUDE 中 2012年1月 至 2025年7月 的 TAVR 器械不良事件报告，共 56,806 份。
* 报告平台分布为 Edwards SAPIEN 30,141 份（53.1%）和 Medtronic Evolut 26,665 份（46.9%）。
* 规则型 NLP 可将 40,737 份报告（71.7%）映射到并发症域；不可分类 16,069 份（28.3%）。
* 全平台最常报告的并发症域为器械故障/释放问题 28.7%、结构性瓣膜退化 26.2%、传导障碍/起搏器 20.2%、瓣周漏/反流 18.3%。
* 平台信号有生物学一致性：Medtronic Evolut 的传导障碍/起搏器报告比例为 36.0%，Edwards SAPIEN 为 6.3%；Edwards 的结构性瓣膜退化报告比例为 31.8%，Medtronic 为 19.8%。
* 这些是报告信号，不是发生率、排名或因果证据；Edwards 不可分类报告 44.6%，Medtronic 9.8%，提示报告实践差异是主要混杂因素。

### 题目与作者

本研究题目为“经导管主动脉瓣置换并发症谱：56,806 份 FDA MAUDE 不良事件报告的自然语言处理分析（2012-2025）”。作者为 Bipul Mainali，BS，来自 UAB Heersink School of Medicine，Birmingham，AL；以及 Nicolas H. Pope，MD，来自 Medical University of South Carolina 心胸外科，Charleston，SC。会议信息为 TAVR: Conduction Complications，Moderated Abstracts Station 1，Presentation 814。

### 利益披露

报告作者 Bipul Mainali，BS，在此前 24 个月内担任 Ashlins Pharmaceuticals 顾问。共同作者 Nicolas H. Pope，MD，披露 Abbott（Tendyne）的 proctor 和 honoraria。页面说明：列出的关系均与本分析无关；本分析仅使用公开、去标识化 FDA 上市后数据（openFDA），无行业资助；教师披露信息也可在会议 app 中查看。

### 研究背景：TAVR 应用快于长期安全证据

TAVR 已从不能手术患者扩展到低风险患者，目前已成为美国主动脉瓣置换的大多数。关键随机试验如 PARTNER 和 Evolut 主要按疗效设计，不足以发现罕见或晚期器械失效。一旦器械进入广泛实践，上市后监测就成为观察真实世界安全性的主要窗口。

两大主导平台 Edwards SAPIEN（球囊扩张型）和 Medtronic Evolut（自膨型）具有不同机械特性和并发症特征。研究缺口是：此前没有覆盖两类 TAVR 平台、跨 13 年 MAUDE 叙述文本的大规模跨平台 NLP 分析。参考 VARC-3：Généreux P 等，J Am Coll Cardiol. 2021;77(21):2717-2746。

### MAUDE 是什么

MAUDE 指 FDA Manufacturer and User Facility Device Experience，是美国医疗器械不良事件报告的国家数据库。它收集 MDRs（Medical Device Reports），包括与器械相关的故障、严重伤害和死亡。

制造商、进口商和医院对器械死亡/严重伤害的报告为强制性，法规依据为 21 CFR 803；个人临床医生和患者可通过 MedWatch 自愿报告。每份报告以非结构化自由文本叙述为中心，内容丰富但不标准化。MAUDE 中有 >15M 份器械报告，并可通过 openFDA API 免费公开访问。其重要性在于，它是观察已获批器械上市后表现的最大真实世界窗口。

### 为何使用 MAUDE，以及为何不信任它

MAUDE 的优势包括：规模巨大、真实世界覆盖广；可捕捉临床试验遗漏的罕见或晚期故障；免费、公开、持续更新；可用于早期预警信号检测。

MAUDE 使用不足的原因包括：没有分母，因此无法计算发生率；存在报告偏倚和重复偏倚，也存在自愿报告缺口；自由文本不一致且常含模板化 boilerplate；只能提示关联，不能证明因果。页面底部强调：报告反映的是“被报告的内容”，不是人群发生率。

### 研究目标与设计

研究问题是：基于规则的 NLP 分类器能否把 13 年 TAVR MDR 叙述文本分入 VARC-3 并发症域？Edwards SAPIEN 与 Medtronic Evolut 的报告谱是否不同？

研究设计为 openFDA MAUDE 上市后报告的回顾性分析，不接触患者。研究预先指定了锚定 VARC-3 的 18 域关键词分类体系，并允许多标签分类。研究明确为假设生成，目标是发现信号，而不是估计发生率。

为何需要 NLP：56,806 份自由文本叙述无法人工逐条审阅。作者采用透明、由作者定义的关键词分类器，不使用黑箱模型，以便可扩展、可审计、可复现。

### 队列构建：openFDA 查询到分析数据集

openFDA MAUDE 查询流程：NPT 产品代码、2012年1月至2025年7月、分离 SAPIEN 与 Evolut 报告。

研究从产品代码 NPT 开始，纳入所有经导管主动脉瓣报告；时间范围为 2012年1月 至 2025年7月，共 13 年上市后数据；最后分离两类平台报告：SAPIEN 和 Evolut。

分析报告总数为 56,806 份。平台分布为 Edwards SAPIEN 30,141 份（53.1%），Medtronic Evolut 26,665 份（46.9%）。分类前去除了制造商附加的使用说明书 IFU 模板文本，并进行了去重。页面底部注明：产品代码 NPT；报告提交时间为 2012年1月至2025年7月。

### NLP 分类体系：18 个 VARC-3 相关并发症域

18 个 VARC-3 相关并发症域，采用透明的作者定义关键词规则。

VARC-3 即 Valve Academic Research Consortium 3，是定义主动脉瓣试验终点的共识标准，因此研究域可映射到领域内已经接受的定义。该分类体系包括以下 18 个域：

| 编号 | 并发症域 | 中文解读 |
| --- | --- | --- |
| 1 | Device Malfunction / Deployment | 器械故障/释放问题 |
| 2 | Structural Valve Deterioration | 结构性瓣膜退化 |
| 3 | Conduction Disturbance / Pacemaker | 传导障碍/起搏器 |
| 4 | Paravalvular Leak / Regurgitation | 瓣周漏/反流 |
| 5 | Valve Embolization / Migration | 瓣膜栓塞/移位 |
| 6 | Death / Mortality | 死亡/病死 |
| 7 | Vascular Access Complication | 血管入路并发症 |
| 8 | Heart Failure / Hemodynamic | 心衰/血流动力学问题 |
| 9 | Valve Thrombosis | 瓣膜血栓 |
| 10 | Stroke / TIA | 卒中/TIA |
| 11 | Major Bleeding / Tamponade | 大出血/心包填塞 |
| 12 | Endocarditis / Infection | 心内膜炎/感染 |
| 13 | Myocardial Infarction | 心肌梗死 |
| 14 | Acute Kidney Injury | 急性肾损伤 |
| 15 | Conversion to Open Surgery | 转为开胸手术 |
| 16 | Coronary Obstruction | 冠脉阻塞 |
| 17 | Annular Rupture | 瓣环破裂 |
| 18 | Other Specified | 其它特定事件 |

页面强调：关键词规则透明、由作者定义，可审计到 VARC-3；不是黑箱模型。

### 报告量随采用增加，但信号质量未同步提高

年度 TAVR 不良事件报告量和 NLP 分类成功率：报告数量上升，分类率围绕总体均值波动。

上方图 A 显示 2012-2025 年按年份和平台分层的 TAVR 不良事件报告。横轴为年份，左轴为单平台不良事件报告数量，刻度从 0 到约 5,000；右轴为年度总报告量，刻度从 0 到 10,000。青色代表 Edwards SAPIEN，紫红色代表 Medtronic Evolut，黑色折线代表总报告量。

年度总量从 2012 年低位逐步增加，2019 年低风险适应证批准后明显上升；2023 年总量约 7,000，2024 年接近 9,500-10,000，2025 年因只到 7 月，约为 6,500-7,000。平台柱状图显示 Edwards 2024 年约 4,000+ 份，Medtronic 2024 年约 5,000+ 份；2025 年 Medtronic 仍约 4,000+ 份，Edwards 约 2,500 份。

下方图 B 显示 NLP 分类成功率。纵轴为分类率，范围 0-100%；虚线为总体均值 71.7%。2012 年分类率约 90%，2013 年约 80%，2014 年约 74%，2015-2016 年降至约 60-62%，随后回升并多数年份保持在约 69-78%。页面结论为：报告量追随市场采用增加，在 2019 年低风险批准后激增；但可用、可分类叙述大致保持稳定，数据更多并不等于数据更好。单份报告可映射到多个域。

### 分类产出率按制造商显著不同

总体分类比例和按制造商分类成功率：Edwards 不可分类比例明显高于 Medtronic。

总体报告分类图显示总样本量 N=56,806。其中可分类报告为 40,737 份（71.7%），不可分类报告为 16,069 份（28.3%）。

按制造商分层：Edwards SAPIEN（n=30,141）中，可分类 55.4%，不可分类 44.6%。Medtronic Evolut（n=26,665）中，可分类 90.2%，不可分类 9.8%。页面右侧突出总体可分类率为 71.7%，并指出 Edwards 不可分类 44.6% 对 Medtronic 9.8% 的不对称更可能是报告实践差异，而非临床差异；作者把它当作局限而不是研究发现。

### 全平台最常报告并发症域

56,806 份 FDA MAUDE TAVR 报告中各并发症域频率，多标签分类。

分母为 56,806 份报告，允许多标签。所有平台中最常报告的是器械故障/释放问题、结构性瓣膜退化和传导障碍/起搏器。右侧信息框强调：器械故障/释放问题 28.7%；结构性瓣膜退化 26.2%；提及死亡的报告 12.9%，n=7,305，且不代表可归因于器械。

| 并发症域 | 比例 | 报告数 |
| --- | --- | --- |
| 器械故障/释放问题 | 28.7% | 16,277 |
| 结构性瓣膜退化 | 26.2% | 14,859 |
| 传导障碍/起搏器 | 20.2% | 11,488 |
| 瓣周漏/反流 | 18.3% | 10,373 |
| 瓣膜栓塞/移位 | 13.5% | 7,678 |
| 死亡/病死 | 12.9% | 7,305 |
| 血管入路并发症 | 8.6% | 4,859 |
| 心衰/血流动力学问题 | 6.5% | 3,704 |
| 瓣膜血栓 | 6.5% | 3,700 |
| 卒中/TIA | 6.5% | 3,696 |
| 大出血/心包填塞 | 4.7% | 2,658 |
| 心内膜炎/感染 | 4.1% | 2,331 |
| 其它特定事件 | 3.2% | 1,819 |
| 心肌梗死 | 2.9% | 1,624 |
| 急性肾损伤 | 2.5% | 1,446 |
| 转为开胸手术 | 2.4% | 1,350 |
| 冠脉阻塞 | 1.9% | 1,082 |
| 瓣环破裂 | 1.8% | 1,027 |

### 平台信号在传导障碍和 SVD 上分化

Edwards SAPIEN 与 Medtronic Evolut 前 6 个并发症域比例对比。

图中以平台内报告百分比为分母：Edwards SAPIEN n=30,141，Medtronic Evolut n=26,665。右侧信息框强调，传导障碍/起搏器方面，Medtronic 为 36.0%，Edwards 为 6.3%，与已知器械生物学一致；结构性退化方面，Edwards 为 31.8%，Medtronic 为 19.8%，作者认为仅为方向性信号。

| 并发症域 | Edwards SAPIEN | Medtronic Evolut |
| --- | --- | --- |
| 器械故障/释放问题 | 23.7% | 34.3% |
| 结构性瓣膜退化 | 31.8% | 19.8% |
| 传导障碍/起搏器 | 6.3% | 36.0% |
| 瓣周漏/反流 | 13.5% | 23.7% |
| 瓣膜栓塞/移位 | 6.6% | 21.3% |
| 死亡/病死 | 8.8% | 17.4% |

### 解释：报告信号追踪已知器械生物学

Medtronic Evolut 的传导障碍/起搏器报告更高，与自膨瓣架更深坐落于 LVOT 时永久起搏器负担较高的已知现象一致。研究中 Edwards 的比例 6.3%，正好接近 PARTNER 3 SAPIEN 起搏器率约 6%。

更多 Edwards 报告映射到结构性退化，但这只是一个假设，不是耐久性裁决：MAUDE 关键词命中并非经过 VARC-3 adjudication 的 SVD，而且 Edwards 的叙述文本更稀疏，会偏倚比较。总体并发症域频率符合临床预期的 TAVR 并发症层级。

页面 takeaway 为：重现预期传导信号支持 NLP 方法的表面效度，但仍需要正式的 precision/recall 验证。

### 核心警示：报告实践不等于临床真相

Edwards 与 Medtronic 在不可分类报告上的差距，44.6% 对 9.8%，很可能反映报告实践，而非安全性差异。MAUDE 没有分母，因此更高的计数可能意味着使用更多、报告更多或事件更多。表面上的平台差异可能部分反映各制造商如何提交叙述文本。

右侧信息框要求：把每一个信号都读作一个需要检验的假设，而不是发生率、不是排名，也不是因果证明。

### 局限性：本分析不能声称什么

局限包括：被动、自愿报告导致选择偏倚和漏报；没有分母，因此只能给出比例，不能给出发生率；即使去重后仍可能存在重复报告；关键词 NLP 的 precision/recall 尚未正式验证；品牌归因依赖自由文本字段；只能提示关联，不能推断因果或比较疗效。

下一步是人工标注验证 NLP 准确性，并与 STS/ACC TVT 等注册数据库链接，以补足缺失的分母。

### 结论与影响

MAUDE 叙述文本的 NLP 分类具有可扩展性和可行性：跨 13 年的 56,806 份报告中，有 71.7% 映射到并发症域。平台信号具有临床一致性：Medtronic 指向传导障碍/起搏器，Edwards 指向结构性退化。

制造商报告异质性是主要混杂因素，任何基于 MAUDE 的监测都必须承认这一点。强制 MAUDE 采用结构化叙述字段，将显著改善 TAVR 上市后监测。底线是：NLP 可以把 MAUDE 的自由文本叙述转化为结构化信号，但数据基础设施必须跟上。

### 致谢与参考文献

页面致谢并列出参考文献：1. openFDA Device Adverse Event (MAUDE) API，https://open.fda.gov/device/event，访问时间为 2025年7月。2. Généreux P 等，Valve Academic Research Consortium 3 (VARC-3)，J Am Coll Cardiol. 2021;77(21):2717-2746。3. Mack MJ 等，PARTNER 3: TAVR in low-risk patients，N Engl J Med. 2019;380:1695-1705。4. Popma JJ 等，Evolut Low Risk Trial，N Engl J Med. 2019;380:1706-1715。5. Mack MJ 等，PARTNER 3 五年结局，N Engl J Med. 2023;389:1949-1960。

页脚再次列出作者：Bipul Mainali，BS，UAB Heersink School of Medicine；Nicolas H. Pope，MD，MUSC Cardiothoracic Surgery。
