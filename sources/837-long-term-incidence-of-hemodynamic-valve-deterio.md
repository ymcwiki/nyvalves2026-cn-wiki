# Evolut TAVR 后血流动力学瓣膜退化的长期发生率

## 核心要点

* 研究为单机构 Evolut TAVR 数据库分析，排除 valve-in-valve 病例，并以出院后全因死亡作为竞争事件。
* 7 年时 HVD 累计发生率较低：Stage 2 HVD 为 5.42%，Stage 3 HVD 为 2.50%。
* 同期竞争死亡率很高：3、5、7 年分别为 24.4%、41.9%、57.8%，因此解释瓣膜退化时必须考虑竞争风险。
* 按 Evolut 亚型比较，Stage 2 HVD 差异未达显著，Gray 检验 p = 0.076；Stage 3 HVD 按亚型差异显著，p = 0.041，Evolut Pro+ 最高。
* 按 TVT 瓣膜尺寸比较，Stage 2 与 Stage 3 HVD 均未见显著差异，Gray 检验分别为 p = 0.412 和 p = 0.866。

### 题目与作者

本报告题为“Evolut TAVR 后血流动力学瓣膜退化的长期发生率”。作者包括 Mangesh Kritya, MD；Mohak Gupta, MD；Chloe Kharsa, MD；Karl Abou-Zeid, MD；Marcell Szekely, MD；Hanad Bashir, MD；Davis Leaphart, MD；Saliha Erdem, MD；Nadeen N. Faza, MD；Stephen H. Little, MD；Marvin D. Atkins, MD；Joe Aoun, MD；Michael J. Reardon, MD；Neal S. Kleiman, MD；Sachin S. Goel, MD。

### 利益声明

讲者 Mangesh Kritya 声明无任何需要披露的财务关系。

### 研究背景

血流动力学瓣膜退化，HVD，反映 TAVR 后瓣膜性能随时间下降。Evolut TAVR 后真实世界长期 HVD 数据仍有限。本研究拟描述最长 7 年的 HVD 发生率、进展和亚组模式。

### 研究方法

研究使用单机构 Evolut TAVR 患者数据库，排除 valve-in-valve 手术。Stage 2 HVD 使用改良 VARC-3 标准定义。出院后全因死亡被作为竞争事件处理。研究使用累积发生函数估计 3 年、5 年和 7 年的 Stage 2 与 Stage 3 HVD。按 Evolut 亚型和 TVT 瓣膜尺寸进行亚组比较，采用 Gray 检验，分析在 R 中完成。

### VARC-3 生物瓣功能障碍框架

VARC-3 中生物瓣功能障碍和生物瓣失败的框架，用于理解 HVD 分期。

中心图来自 Généreux 等，J Am Coll Cardiol 2021;77(21)，题为“Bioprosthetic Valve Dysfunction and Bioprosthetic Valve Failure”。图中首先询问生物瓣功能障碍类型，再判断是否有血流动力学改变和临床后果。

| 分类 | 完整内容 |
| --- | --- |
| 结构性瓣膜退化 | 指假体瓣膜内在、永久性改变，包括磨损，瓣叶破裂，瓣叶脱垂或翻转，瓣叶纤维化和/或钙化，支架断裂或变形。 |
| 非结构性瓣膜功能障碍 | 指非假体瓣膜内在异常但导致瓣膜功能障碍的情况，包括瓣周反流、患者-假体不匹配，以及其他原因，例如瓣叶被 pannus、组织或缝线牵拉，瓣膜定位或尺寸不合适，支架less 生物瓣或保留主动脉瓣手术后主动脉根部扩张，瓣膜栓塞或移位。 |
| 患者-假体不匹配，BMI <30 kg/m² | 按 indexed EOA cm²/m²：不显著 >0.85；中度 0.65-0.85；重度 <0.65。 |
| 患者-假体不匹配，BMI ≥30 kg/m² | 按 indexed EOA cm²/m²：不显著 >0.70；中度 0.55-0.70；重度 <0.55。 |
| 血栓形成 | 亚临床血栓形成为影像有 HALT/RLM，且血流动力学改变缺如或轻微、无症状或后遗症。临床显著血栓形成包括有血栓栓塞事件临床后果，或 AS/AR 恶化并达到 HVD Stage 2-3 且有确认影像 HALT/RLM；若无临床后果，则需同时有 HVD Stage 3 与确认影像 HALT/RLM。 |
| 感染性心内膜炎 | 至少满足以下之一：Duke 心内膜炎标准；再手术时组织学或微生物学研究证实脓肿、脓液或赘生物由感染导致；尸检确认脓肿、脓液或赘生物。 |
| Stage 1 | 形态学瓣膜退化：有结构性瓣膜退化、非结构性瓣膜功能障碍，除外瓣周反流或患者-假体不匹配，血栓或心内膜炎证据，但无显著血流动力学改变。 |
| Stage 2 | 中度 HVD：具体阈值见下一页。 |
| Stage 3 | 重度 HVD：具体阈值见下一页。 |
| 生物瓣失败 BVF | Stage 1 为任何生物瓣功能障碍伴临床表达标准，例如新发或加重症状、左室扩张/肥厚/功能障碍或肺高压，或不可逆 Stage 3 HVD；Stage 2 为主动脉瓣再干预；Stage 3 为瓣膜相关死亡。 |

### Stage 2 与 Stage 3 HVD 定义

研究采用的改良 VARC-3 Stage 2 与 Stage 3 HVD 阈值。

| 分期 | 定义 |
| --- | --- |
| Stage 2，中度 HVD | 平均跨瓣压差较术后 1-3 个月超声评估增加 ≥10 mmHg，并导致平均压差 ≥20 mmHg，同时伴有效瓣口面积 EOA 下降 ≥0.3 cm² 或 ≥25%，和/或 Doppler velocity index 下降 ≥0.1 或 ≥20%；或者新出现或增加 ≥1 级瓣内 AR，最终达到 ≥中度 AR。 |
| Stage 3，重度 HVD | 平均跨瓣压差较术后 1-3 个月超声评估增加 ≥20 mmHg，并导致平均压差 ≥30 mmHg，同时伴 EOA 下降 ≥0.6 cm² 或 ≥50%，和/或 Doppler velocity index 下降 ≥0.2 或 ≥40%；或者新出现或增加 ≥2 级瓣内 AR，最终达到重度 AR。 |

### Stage 2 与 Stage 3 HVD 累积发生率

3、5、7 年 Stage 2 HVD、Stage 3 HVD 与竞争死亡的累积发生率。

| 指标 | 3 年 | 5 年 | 7 年 |
| --- | --- | --- | --- |
| Stage 2 HVD | 1.60% | 2.66% | 5.42% |
| Stage 3 HVD | 0.37% | 0.83% | 2.50% |
| 竞争死亡 | 24.4% | 41.9% | 57.8% |

图中两张曲线的横轴为 TAVR 后时间，单位月，显示 0、12、24、36、48、60、72、84 月。纵轴为累积发生率，刻度从 0% 到 70%。Stage 2 HVD 风险表在上述时间点分别为 1210、1030、865、711、497、350、228、108 例；Stage 3 HVD 风险表分别为 1211、1034、872、718、503、354、233、110 例。

### 按 Evolut 亚型分层的 HVD

Stage 2 与 Stage 3 HVD 按 Evolut 亚型分层的累积发生曲线，采用 Gray 检验。

左图为 Stage 2 HVD by Evolut subgroup，Gray 检验 p = 0.076，提示亚型间差异未达到统计学显著性。右图为 Stage 3 HVD by Evolut subgroup，Gray 检验 p = 0.041，提示亚型间差异达到统计学显著性。图例包括 CoreValve Evolut、Evolut FX、Evolut Pro、Evolut Pro+ 和 Evolut R。页面底部说明：Evolut Pro+ 的 7 年发生率最高，Stage 2 为 6.51%，Stage 3 为 3.51%；Stage 2 HVD 在亚型间无显著差异，而 Stage 3 HVD 有显著差异，p = 0.041。

### 7 年 HVD 按亚型和瓣膜尺寸分层

7 年 Stage 2 与 Stage 3 HVD 的柱状图，左侧按 Evolut 亚型，右侧按 TVT 瓣膜尺寸。

| Evolut 亚型 | Stage 2 HVD | Stage 3 HVD |
| --- | --- | --- |
| CoreValve | 1.01% | 0.00% |
| Pro | 2.05% | 0.70% |
| Pro+ | 6.51% | 3.51% |
| R | 4.09% | 0.40% |

按亚型比较的 Gray 检验：Stage 2 HVD p = 0.076，Stage 3 HVD p = 0.041。

| TVT 瓣膜尺寸 | Stage 2 HVD | Stage 3 HVD |
| --- | --- | --- |
| 23 mm | 5.56% | 0.00% |
| 26 mm | 2.30% | 0.75% |
| 29 mm | 4.91% | 1.21% |
| 34 mm | 6.14% | 2.75% |

按瓣膜尺寸比较的 Gray 检验：Stage 2 HVD p = 0.412，Stage 3 HVD p = 0.866。因此，本页数据显示尺寸分层并未带来统计学显著差异。

### 结论

作者总结：Evolut TAVR 后 HVD 至 7 年总体少见，但进展和竞争死亡均需要纳入解释。第一，Stage 2 和 Stage 3 HVD 在 Evolut TAVR 后 7 年内发生率低。第二，Evolut Pro+ 的 Stage 3 HVD 更高；Stage 2 HVD 在 Evolut 亚型或瓣膜尺寸之间没有差异，Stage 3 HVD 按亚型有差异，p = 0.041，以 Evolut Pro+ 最高。第三，竞争死亡率高；在进展前死亡很常见，5 年为 36.2%，提示该人群中竞争风险的重要性。

### 致谢

最后一页为 Thank You，无额外研究数据。
