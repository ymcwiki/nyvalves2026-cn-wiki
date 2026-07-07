# 基于人工智能的软件用于全自动 TAVR 规划：真实世界队列中主动脉根部和髂股血管测量的外部验证

## 核心要点

* 本研究验证 4TAVR (Hi-D Imaging, Switzerland) 全自动 AI 软件在真实世界 TAVR CT 中的主动脉根部和髂股血管测量准确性。
* 队列包括 967 例连续严重 AS 患者的 TAVR CT，时间为 2015 至 2022 年，AI 结果与 Aquarius Intuition 或 3mensio 人工测量比较。
* 主动脉根部多数尺寸参数一致性良好，average ascending aorta diameter ICC 0.91、average SOV ICC 0.90、non-coronary SOV ICC 0.89；但 LMS height ICC 0.10、RCA height ICC 0.20，冠脉高度仍需改进。
* 髂股血管中，较大的近端 CIA 一致性较好，right CIA ICC 0.83、left CIA ICC 0.81；较小远端 CFA 一致性较中等，right CFA ICC 0.65、left CFA ICC 0.63。
* AI 推导瓣膜尺寸与人工解读高度一致，weighted κ 0.957，exact agreement 94.4%，overestimate 2.9%，underestimate 2.7%。

### 题目与讲者

本科学摘要题为“AI-based software for fully automated TAVR planning: external validation of aortic root and ilio-femoral vessel measurements in a real-world cohort”。讲者 Vitaliy Androshchuk, MBBCh MRes BSc (Hons.) PhD，来自 King’s College London, United Kingdom。

### 财务关系披露

讲者声明没有需要披露的相关财务关系。

### 引言

TAVR 是 severe AS 的主导治疗方式。CT imaging 对 TAVR planning 至关重要。TAVR CT interpretation 需要大量专业经验，耗时、重复且容易出现观察者间变异。全自动 AI 工具已出现，用于改善 TAVR CT analysis。潜在获益包括提高 planning efficiency、改善 cath lab patient flow、增加 throughput。

### 方法：4TAVR 软件与测量参数

4TAVR 从 CT 分割轮廓和重建平面计算 TAVR 规划参数。

4TAVR (Hi-D Imaging, Switzerland) 是 AI-powered、fully automated 的 TAVR CT image analysis 软件。TAVR planning 所需参数从 segmented CT contours 和 reconstructed planes 计算。测量包括 aortic annulus、LVOT、coronary heights、SoV、STJ、aorta、CIA、EIA、CFA。

### 方法：目的与设计

研究目的为验证 automated AI software 4TAVR 在真实世界 TAVR CT assessment 患者中，对 aortic root 和 ilio-femoral measurements 的准确性。设计为纳入 967 份 TAVR CT scans，来自连续严重 AS 并接受 TAVR 的患者；纳入时间为 2015 至 2022 年。4TAVR 测量与人工测量比较，人工软件为 Aquarius Intuition (TeraRecon, USA) 或 3mensio (Pie Medical Imaging, the Netherlands)。

### 结果：患者特征

研究队列 967 例 TAVR CT 的临床和超声基线特征。

| 特征 | Study cohort (n=967) |
| --- | --- |
| Age | 83 (78, 86) years |
| Female sex | 476 (49%) |
| Hypertension | 328 (34%) |
| AF | 379 (39%) |
| Diabetes mellitus | 281 (29%) |
| CAD | 493 (51%) |
| Chronic lung disease | 139 (14%) |
| CABG | 106 (11%) |
| Stroke | 133 (14%) |
| BMI | 26.5 (23.4, 30.1) kg/m² |
| LVEF | 52.91 ± 12.06% |
| Transaortic MG | 42 (33, 52) mmHg |
| AVA | 0.73 ± 0.21 cm² |

### 结果：TAVR CT 图像质量

主动脉根部和双侧髂股系统图像质量绝大多数为 good。

| 部位 | Poor | Fair | Good |
| --- | --- | --- | --- |
| Aortic root | 7 (0.7%) | 41 (4.2%) | 919 (95%) |
| Right ilio-femoral system | 3 (0.3%) | 19 (2.0%) | 945 (98%) |
| Left ilio-femoral system | 9 (0.9%) | 19 (2.0%) | 939 (97%) |

### 结果：TAVR 程序特征

TAVR 程序特征和钙化负荷。

| 特征 | Study cohort (n=967) |
| --- | --- |
| Listed electively | 877 (91%) |
| Tricuspid AV | 913 (94%) |
| BEV deployed | 840 (88%) |
| Valve size >23 mm | 593 (61%) |
| ≥ Moderate annular calcification | 154 (18%) |
| ≥ Moderate LVOT calcification | 93 (10%) |
| ≥ Moderate R CIA calcification | 432 (45%) |
| ≥ Moderate R EIA calcification | 125 (13%) |
| ≥ Moderate R CFA calcification | 278 (28%) |
| ≥ Moderate L CIA calcification | 461 (47%) |
| ≥ Moderate L EIA calcification | 117 (12%) |
| ≥ Moderate L CFA calcification | 282 (28%) |

### 结果：主动脉根部参数一致性

主动脉根部参数：4TAVR 与 expert observer 的散点一致性。

| 参数 | ICC | MAE |
| --- | --- | --- |
| Annular area | 0.85 | 36.16 |
| Annular perimeter | 0.86 | 2.89 |
| Area derived diameter | 0.85 | 0.96 |
| Perimeter derived diameter | 0.86 | 0.93 |
| Major diameter | 0.84 | 1.16 |
| Minor diameter | 0.75 | 1.32 |
| Eccentricity index | 0.46 | 4.71 |
| LMS height | 0.10 | 3.21 |
| RCA height | 0.20 | 3.99 |
| Left SOV | 0.85 | 1.66 |
| Right SOV | 0.85 | 1.44 |
| Non coronary SOV | 0.89 | 1.22 |
| Average SOV | 0.90 | 1.25 |
| Average STJ | 0.80 | 1.91 |
| Average Asc Ao diameter | 0.91 | 1.24 |

散点图横轴为 Expert observer，纵轴为 4TAVR。除冠脉高度和 eccentricity index 外，多数直径、周径、SOV、STJ、升主动脉参数 ICC 达到 0.75 至 0.91。

### 结果：主动脉根部 Bland-Altman

主动脉根部参数的 4TAVR minus expert 偏倚和 95% limits。

| 参数 | Mean | +1.96 SD | -1.96 SD |
| --- | --- | --- | --- |
| Annular area | 15.85 | 113.22 | -81.53 |
| Annular perimeter | 0.90 | 9.03 | -7.23 |
| Area derived diameter | 0.38 | 2.96 | -2.21 |
| Perimeter derived diameter | 0.29 | 2.90 | -2.32 |
| Major diameter | 0.54 | 3.53 | -2.46 |
| Minor diameter | 0.28 | 3.78 | -3.21 |
| Eccentricity index | 0.69 | 12.81 | -11.44 |
| LMS height | -2.06 | 4.79 | -8.91 |
| RCA height | 2.68 | 11.05 | -5.69 |
| Left SOV | 0.98 | 4.87 | -2.90 |
| Right SOV | 0.10 | 4.08 | -3.87 |
| Non coronary SOV | 0.45 | 3.68 | -2.78 |
| Average SOV | 0.53 | 3.52 | -2.46 |
| Average STJ | 1.85 | 5.17 | -1.48 |
| Average Asc Ao diameter | 0.94 | 3.96 | -2.09 |

图中纵轴为 4TAVR minus Expert，横轴为 Expert 与 4TAVR 的平均值。冠脉高度的偏倚和一致界限较宽，支持结论中“RCH 和 LCH 需进一步优化”。

### 结果：髂股参数一致性

髂股参数：4TAVR 与 expert observer 的散点一致性。

| 参数 | ICC | MAE |
| --- | --- | --- |
| Right CIA | 0.83 | 0.83 |
| Right EIA | 0.76 | 0.77 |
| Right CFA | 0.65 | 1.01 |
| Left CIA | 0.81 | 0.89 |
| Left EIA | 0.73 | 0.81 |
| Left CFA | 0.63 | 1.05 |

较大的 proximal vessels，尤其 CIA，ICC 达 0.81 至 0.83；较小远端 CFA 的 ICC 为 0.63 至 0.65，一致性较中等。

### 结果：髂股参数 Bland-Altman

髂股参数的偏倚和 95% 一致界限。

| 参数 | Mean | +1.96 SD | -1.96 SD |
| --- | --- | --- | --- |
| Right CIA | -0.16 | 2.17 | -2.49 |
| Right EIA | -0.01 | 2.14 | -2.17 |
| Right CFA | -0.24 | 2.43 | -2.91 |
| Left CIA | -0.17 | 2.36 | -2.70 |
| Left EIA | -0.13 | 2.16 | -2.41 |
| Left CFA | -0.49 | 2.15 | -3.13 |

髂股血管整体平均偏倚接近 0，左 CFA 偏倚最大，为 -0.49，下限至 -3.13。

### 结果：瓣膜尺寸选择一致性

Expert observer 与 4TAVR 推导瓣膜尺寸的混淆矩阵。

| Expert \\ 4TAVR (mm) | 20 | 23 | 25 | 26 | 27 | 29 | 34 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 34 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| 29 | 0 | 1 | 0 | 8 | 0 | 119 | 0 |
| 27 | 0 | 0 | 0 | 0 | 16 | 0 | 0 |
| 26 | 0 | 11 | 0 | 344 | 0 | 1 | 0 |
| 25 | 0 | 0 | 23 | 0 | 0 | 0 | 0 |
| 23 | 6 | 295 | 2 | 14 | 0 | 0 | 0 |
| 20 | 41 | 7 | 0 | 0 | 0 | 0 | 0 |

Weighted κ=0.957。Exact agreement 为 94.4%，overestimates 2.9%，underestimates 2.7%。对角线上的一致单元格包括 20 mm 41 例、23 mm 295 例、25 mm 23 例、26 mm 344 例、27 mm 16 例、29 mm 119 例、34 mm 4 例。

### 结论

对于主动脉根部，使用 fully automated AI-based software 获得的 TAVI CT measurements 与 expert manual measurements 一致性好，例外是 RCH 和 LCH。需要进一步改进冠脉高度评估，以反映当前指南。对于髂股血管，较大的 proximal vessels 一致性好，较小 distal vessels 一致性中等。基于 AI-derived measurements 的瓣膜 sizing 与人工解读总体一致性极佳。
