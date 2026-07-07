# 自动化 AI TAVR 规划器的验证

## 核心要点

* 研究验证 Mimics for TAVR 在真实临床流程中相对半自动 3Mensio 的准确性，纳入 126例连续患者。
* 样本复杂度较高：中位年龄 80 岁，男性 56%，中位 STS 5.5，复杂解剖 50%。
* 与 3Mensio 比较，AI 对 annulus、LVOT、STJ 面积有小幅低估，平均百分误差约 -1.9% 到 -2.7%，冠脉高度 -3.5% 到 -3.9%。
* 几乎所有参数 ICC 均 >0.90，annulus area ICC 0.976，LVOT area ICC 0.970，STJ area ICC 0.953。
* Mimics 平均分析时间 1.03 ± 0.15 分钟，3Mensio 为 9.55 ± 3.16 分钟，约 9 倍更快，P=0.001。

### 题目与作者

本研究题为《自动化 AI TAVR 规划器的验证》。讲者为 Thoraxcenter, Erasmus MC, Rotterdam, NL 的 L. Uchoa de Assis, MD。作者包括 M.M.P. van den Dorpel、L. Uchoa de Assis、J. van Niekerk、S. Deckx、I. Kardys、A. Hirsch、J. Daemen、R.J. Nuis、N.M. Van Mieghem。

### 利益披露

Lucas Uchoa de Assis 声明无任何需要披露的经济关系。Faculty disclosure 信息可在会议 app 查看。

### MSCT 是 TAVR 成功的前提

多层螺旋 CT（MSCT）是成功 TAVR 的前提，用于主动脉根部 sizing、冠脉阻塞风险评估和入路策略。半自动软件已经简化流程，但仍有明显不足：第一，耗时，人工分割和测量每例都需要专家时间；第二，观察者间变异，读片者不同可能导致结果差异，降低可重复性；第三，容易发生人为错误，系统性人工干预仍留有出错空间。

### 以往自动规划器验证的局限

人工智能可能使分析更快且更可重复。然而，以往自动化规划器验证有重要局限：常排除二叶瓣、重度钙化或生物瓣等解剖变异；很少报告实际选择的经导管瓣膜尺寸；研究多为回顾性，且来自选择性人群。

### Mimics for TAVR 与研究目的

Mimics for TAVR 从匿名 DICOM 建立患者特异性 3D 模型，并在网页界面中提供主动脉根部测量。

Mimics for TAVR 生成来自匿名 DICOM 的患者特异性 3D 解剖模型。自动测量来自 3D U-Net，该网络用 449份 CT 训练，并用 200份验证。系统为网页界面，可在 heart-team 讨论期间实时访问。本研究目的为在常规临床实践中，以半自动 3Mensio 为参照验证 Mimics for TAVR。

### 研究方法

研究纳入 2024 年 6 月至 11 月的 126例连续患者。匿名 DICOM 通过 Ambra/PACS 上传至 Mimics for TAVR。AI 分析包括自动 3D 模型和主动脉根部测量。3名评阅者确认输出，必要时手动调整。参照标准为 3Mensio v10 上 3次测量的平均值。测量项目包括 annulus、LVOT、STJ、sinus of Valsalva、冠脉高度、membranous septum，并记录 SAPIEN 3、Evolut FX、Navitor 的建议尺寸。统计学使用 ICC（two-way mixed）和 Bland-Altman，并记录每例分析时间。

### 患者构成与复杂解剖

研究人群有一半为复杂解剖，常见复杂因素为重度钙化、小瓣环和二叶瓣。

患者中位年龄 80 岁，四分位范围 74-85岁；男性 56%；中位 STS score 5.5，四分位范围 2.4-8.4；复杂解剖占 50%。复杂解剖分解为重度钙化 30例、二叶瓣 12例、小瓣环 14例、失败生物瓣 7例。

### 测量误差

Mimics 相比 3Mensio 的平均百分误差总体较小，但多为负值，提示轻度低估。

| 参数 | 平均百分误差 ± SD，相对 3Mensio |
| --- | --- |
| Annulus area | -1.9 ± 3.3% |
| LVOT area | -2.7 ± 3.8% |
| STJ area | -2.6 ± 4.2% |
| Coronary heights | -3.5% 到 -3.9% |
| Membranous septum | -5.0 ± 9.2% |

图中横向列出 annulus、LVOT、STJ、SOV 以及 coronary/MS 的多个测量点，纵轴为 mean error (%) ± SD；多数点在 0 以下，误差棒主要落在约 -10% 到 +5%区间，membranous septum 的离散度最大。

### ICC 与 Bland-Altman

Annulus 与 LVOT 的相关和 Bland-Altman 图显示高度一致性，右侧列出 ICC。

| 参数 | ICC (95% CI) |
| --- | --- |
| Annulus area | 0.976（0.966-0.984） |
| LVOT area | 0.970（0.957-0.983） |
| STJ area | 0.953（0.921-0.971） |
| Sinus of Valsalva | 0.922-0.949 |
| Coronary heights | 0.900-0.928 |
| Membranous septum | 0.919（0.880-0.940） |

几乎所有参数 ICC >0.90，全部 P<0.001。左侧相关和 Bland-Altman 图展示 annulus 与 LVOT：散点沿一致性线分布，Bland-Altman 图标出平均差异及 ±1.96 SD 界限。

### 复杂解剖与观察者间一致性

复杂病例的 ICC 略低于非复杂病例，但仍保持较高一致性。

| 参数 | 非复杂病例 ICC | 复杂病例 ICC |
| --- | --- | --- |
| Annulus area | 0.981 | 0.972 |
| LVOT area | 0.979 | 0.963 |
| STJ area | 0.964 | 0.939 |

观察者间一致性方面，Mimics annulus-area ICC 为 0.994，3Mensio 为 0.992，两者均 P<0.001。

### 分析时间与瓣膜尺寸选择

Mimics 分析时间约为 3Mensio 的九分之一，三类瓣膜尺寸选择一致性约 90% 或更高。

Mimics for TAVR 平均分析时间为 1.03 ± 0.15 分钟，3Mensio 为 9.55 ± 3.16 分钟，约 9 倍更快，P=0.001。右侧柱图分别展示 SAPIEN、Navitor、Evolut 的建议尺寸选择，纵轴为病例百分比，颜色区分较小尺寸、相同尺寸、较大尺寸。图上未标每段具体百分比，但三类瓣膜的“same size”蓝色段均占主体，约为 90%或更高；较小尺寸和较大尺寸仅占少数。尺寸选择差异检验 P=0.001。

### 讨论：优势与局限

优势包括：前瞻性真实世界临床实践；纳入复杂解剖且未损失准确性；针对实际假体尺寸选择进行验证；一致性界限比既往工具更紧，约 ±37 mm²；速度明显更快，浏览器界面，可实时访问。局限包括：单中心、高容量三级中心；只纳入高质量 MSCT 数据集；没有独立核心实验室判读；参考标准本身也是半自动测量。

### 结论

Mimics for TAVR 是半自动术前规划的准确替代方案，可能改善工作流效率。具体结论为：主动脉根部各测量准确，几乎所有测量 ICC >0.90；经导管瓣膜 sizing 在约 90%病例中一致；在复杂解剖中表现稳定。
