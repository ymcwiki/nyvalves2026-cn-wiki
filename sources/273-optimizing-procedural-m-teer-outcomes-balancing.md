# 优化 M-TEER 术中结果：平衡残余 MR 与瓣膜压差

## 核心要点

* M-TEER 的核心权衡是降低 residual MR，同时避免医源性二尖瓣狭窄；常用狭窄替代指标是 MPG。
* REPAIR study 中最佳组定义为 residual MR ≤1+ 且 MPG <5 mmHg，占 59.4%；dual-suboptimal 组 residual MR ≥2+ 且 MPG ≥5 mmHg，占 7.0%，1 年死亡率最高。
* REPAIR 连续模型中，出院 MPG 每升高 1 mmHg 与死亡风险升高相关，HR 1.10，95% CI 1.00-1.21，P=0.048；但多变量模型中 residual MR ≤1+ 的保护作用更稳定。
* PRIME-MR 显示 residual MR 分级越低，免于全因死亡或心衰住院的比例越高；调整后 rMR ≥2+ 的风险信号 P=0.005，而 MPG >5 mmHg 的信号 P=0.84。
* 器械大小、第一枚夹子位置、是否形成 double/triple orifice 会影响 MVA 减少：MitraClip XTr MVA 减少 57%，NTr 52%；第二枚 device 后 double orifice 再减少 25%，triple orifice 34%。
* 术中指导不能只看 MR grade 或 MPG，应结合 LAP 和 pulmonary vein flow；mLAP ≤15 mmHg、PV flow 正常时，临床结局更好。

### 题目与讲者

题目为“Optimizing procedural M-TEER: Balancing residual MR and valve gradients”。讲者 Martin Swaans, MD, PhD, FESC, FEACVI, FSCAI，为荷兰 Nieuwegein 的 St. Antonius Hospital 心脏科医生。

### 财务利益披露

| Affiliation/Financial Relationship | Company |
| --- | --- |
| Grant/Research Support | ZonMW，包括 Efficacy studies grant, iCORONARY trial，以及 Promising care grant, TRACE-NL trial。 |
| Consulting Fees/Honoraria | Abbott Vascular、Anteris、Bioventrix inc.、Boston Scientific、Cardiac Dimensions、Edwards Lifesciences、GE Healthcare、Medtronic、Philips Healthcare、P&F、Siemens Healthcare。 |
| Major Stock Shareholder/Equity | None |
| Royalty Income | None |
| Ownership/Founder | None |
| Intellectual Property Rights | None |
| Other Financial Benefit | None |

披露时间范围为过去 12 个月。

### 问题引入：减少 MR 与避免狭窄

M-TEER 需要平衡残余 MR 与医源性二尖瓣狭窄；较少 rMR 与更好结局相关。

M-TEER 通过近似二尖瓣瓣叶实现反流减少，但必须在 residual MR (rMR) 和 iatrogenic mitral stenosis 之间取平衡。讲者指出，较少 rMR 与更好结局相关，这一点在不同 MPG 水平下仍成立；MPG 是临床常用的二尖瓣狭窄评价指标。

| 图示证据 | 关键读数 |
| --- | --- |
| Sorajja P et al. JACC 2017 | 随访 12 个月时，death or HF re-hospitalization 累积发生率按 MR 分级递增：Grade ≤I 最低，约 35%；Grade II 约 38-40%；Grade ≥III 最高，约 55%；P<0.0001。 |
| Hadjadj S et al. JASE 2022 | 生存曲线比较 mean TMG ≤5 mmHg 与 >5 mmHg。HR 3.42，95% CI 1.08-10.87，P=0.04。约 12 个月时，≤5 mmHg 组生存率接近 90%，>5 mmHg 组约 65-70%。 |

### Du meta-analysis：原发 MR 中梯度信号更强

Du 等 meta-analysis：M-TEER 后较高 MPVG 与 degenerative MR 患者不良结局相关，而 functional MR 中信号较弱。

该页提出问题：gradient 是否在 primary MR 中比 secondary MR 中更重要？Du 等 meta-analysis 纳入 7 项研究、2,730 例患者，其中 65% 为 functional MR。

| 森林图项目 | Hazard Ratio | 解读 |
| --- | --- | --- |
| Functional MR | 1.12，95% CI 0.74-1.71 | CI 跨越 1，高 MPVG 信号不明确。 |
| Degenerative MR | 1.37，95% CI 1.03-1.84 | 高 MPVG 与不良结局相关。 |
| Overall | 1.22，95% CI 0.95-1.56 | 总体趋势偏向高 MPVG 风险增加。 |
| MR ≥2+ 的 overall 分析 | 1.50，95% CI 1.10-2.03 | 当残余 MR ≥2+ 时，高 MPVG 方向的风险更明显。 |

引用 Du et al. Curr Probl Cardiol 2023。

### Functional MR 不同亚型：梯度主要影响 atrial FMR

Tanaka 等显示，在 atrial FMR 中 MPG ≥5 mmHg 与死亡或 HF 住院累积发生率较高相关；ventricular FMR 中 MPG 信号不明显。

| 图 | 比较 | Log-rank P | Number at risk |
| --- | --- | --- | --- |
| A | Residual MR ≤1+ vs residual MR >1+ | 0.021 | 蓝线 96, 79, 73, 67, 65；红线 29, 18, 16, 14, 14。 |
| B | MPG <5 mmHg vs MPG ≥5 mmHg | 0.021 | 蓝线 98, 79, 72, 67, 67；红线 27, 18, 17, 14, 12。 |
| C | Residual MR ≤1+ vs residual MR >1+ | 0.011 | 蓝线 228, 167, 153, 143, 136；红线 88, 61, 50, 41, 39。 |
| D | MPG <5 mmHg vs MPG ≥5 mmHg | 0.60 | 蓝线 274, 196, 174, 156, 148；红线 42, 32, 29, 28, 27。 |

A 和 B 对应 atrial FMR，C 和 D 对应 ventricular FMR。所有横轴为 days since procedure，终点为 all-cause mortality and HF hospitalization。该页结论是：functional MR 不能一概而论，MPG 的风险信号主要出现在 atrial FMR，而不是 ventricular FMR。引用 Tanaka et al. EuroIntervention 2024。

### 核心问题：能接受多少残余 MR，何时造成狭窄

该页提出临床决策问题：How much residual MR is acceptable and when have we created stenosis? 目标是在最大化 MR reduction 和避免 iatrogenic mitral stenosis 之间取得平衡。

### REPAIR study：分组定义与 1 年全因死亡

REPAIR study 按 residual MR 与 MPG 分成 4 组，主要终点为 1 年全因死亡。

| 分组 | 定义 | n | 比例 | 图中 360 天死亡读数 |
| --- | --- | --- | --- | --- |
| Optimal | Residual MR ≤1+ 且 MPG <5 mmHg | 1,290 | 59.4% | 8.7% |
| MPG-Suboptimal | Residual MR ≤1+ 且 MPG ≥5 mmHg | 267 | 12.3% | 9.8% |
| rMR-Suboptimal | Residual MR ≥2+ 且 MPG <5 mmHg | 462 | 21.3% | 14.4% |
| Dual-Suboptimal | Residual MR ≥2+ 且 MPG ≥5 mmHg | 153 | 7.0% | 20.1% |

Primary endpoint 为 1 年全因死亡。Kaplan-Meier 图显示 Log-rank P<0.001。引用 Mustafa D et al. Circ Cardiovasc Interv 2025。

### MPG 与死亡风险：连续模型

MPG 连续建模显示，出院 MPG 每升高 1 mmHg，1 年死亡 HR 增加。

左图为 all rMR grades，横轴 MPG 从 0 到 10 mmHg，纵轴为 HR for 1-year mortality，虚线 HR=1。曲线在 MPG 约 3-4 mmHg 附近穿过 HR=1，到 10 mmHg 时 HR 约 2.0，置信区间上界超过 5。

右图按 rMR 分层：rMR ≤1+ 的绿色曲线整体较低，MPG 10 mmHg 时约接近 HR 1.0；rMR ≥2+ 的紫色曲线随 MPG 增加而上升，MPG 10 mmHg 时约 2.3，置信区间上界接近 6。页脚结论为：modeled continuously，每增加 1 mmHg discharge MPG 与更高死亡率相关，HR 1.10，95% CI 1.00-1.21，P=0.048。

### REPAIR 多变量模型：rMR 信号强于 MPG

多变量模型中 residual MR ≤1+ 保持显著保护作用，MPG 指标未达统计学显著。

| MPG as a continuous variable | | |
| --- | --- | --- |
| Variable | HR (95% CI) | P-Value |
| Residual MR ≤1+ | 0.56 (0.41-0.77) | <0.001 |
| MPG per mmHg | 1.07 (0.98-1.18) | 0.145 |

| MPG as a dichotomized variable | | |
| --- | --- | --- |
| Variable | HR (95% CI) | P-Value |
| Residual MR ≤1+ | 0.55 (0.40-0.76) | <0.001 |
| MPG <5 mmHg vs ≥5 mmHg | 0.77 (0.54-1.10) | 0.158 |

这页支持讲者的主线：若必须二选一，残余 MR 的长期预后驱动作用常强于 MPG 增加。

### PRIME-MR：术后结果与结局

PRIME-MR 显示 residual MR 分级与免于死亡或 HF 住院相关，MPG spline 风险在高值处上升。

| Post-procedural rMR 曲线 | 0 月 | 6 月 | 12 月 | 18 月 | 24 月 | 24 月读数 |
| --- | --- | --- | --- | --- | --- | --- |
| rMR ≤1+ | 951 | 733 | 599 | 462 | 358 | 免于 all-cause mortality or HF hospitalization 约 70% |
| rMR 2+ | 336 | 250 | 192 | 148 | 115 | 约 58% |
| rMR ≥3+ | 117 | 64 | 49 | 41 | 37 | 约 45% |

左图 P<0.0001。右侧 unadjusted spline analysis 以 MPG 为横轴，范围 1-10 mmHg，纵轴 hazard ratio。HR 在 MPG 1 时约 0.7，3 时约 1.0，5-7 时约 1.3-1.5，9 时约 2.0，10 时约 3.0，高 MPG 区域置信区间明显变宽。

### PRIME-MR：rMR 与 MPG 的组合影响

PRIME-MR 组合分析中，rMR ≥2+ 的 adjusted Cox 信号明显，MPG >5 mmHg 信号不明显。

| 分组曲线 | 0 月 | 6 月 | 12 月 | 18 月 | 24 月 | 24 月约读数 |
| --- | --- | --- | --- | --- | --- | --- |
| Optimal result / Low gradient | 688 | 533 | 427 | 321 | 243 | 免于死亡或 HF 住院约 70% |
| Optimal result / High gradient | 35 | 29 | 22 | 15 | 12 | 约 60% |
| Suboptimal result / Low gradient | 247 | 189 | 145 | 112 | 91 | 约 60% |
| Suboptimal result / High gradient | 35 | 21 | 14 | 9 | 7 | 约 43-45% |

左图 P=0.0002。右侧 fully adjusted Cox regression 中，rMR ≥2+ 的 HR 点估计位于 1 右侧，约 1.6-1.8，P=0.005；MPG >5 mmHg 的点估计约 1.0-1.1，95% CI 横跨 1，P=0.84。模型调整变量包括 age、sex、atrial fibrillation、LVEF <30%、CKD、COPD，并分别加入 rMR 或 MPG。

### 器械位置和大小影响二尖瓣口面积减少

MitraClip 与 Pascal 数据提示，device 尺寸、第一枚夹子位置和瓣口数会影响 MVA 减少。

| 器械/研究 | 样本与关键数字 |
| --- | --- |
| MitraClip | 116 例患者，包括 primary MR 55 例、secondary MR 61 例。 |
| MVA reduction by clip type | XTr 减少 57%，NTr 减少 52%。 |
| 第一枚 device 位置 | P2 centre 减少 50%；P2 border 减少 57%；commissure 减少 43%。 |
| 第二枚 device 后进一步减少 | Double orifice 25% vs triple orifice 34%。 |
| Pascal | 72 例 secondary MR；ACE device 减少 56%；P10 device 减少 46%，P10 带 spacer。 |

右侧示意显示一枚 MitraClip 后不同热区位置对瓣口面积的影响，下方对比 double orifice 与 triple-orifice 结构。

### M-TEER 后二尖瓣口面积

MVA sum ≥2 cm2 是术后规划重点，3D MVA 较小时预后较差。

该页左侧强调 post M-TEER 的 MVA sum 应 ≥2 cm2。左下 Kaplan-Meier 图来自 entire study cohort n=92，比较 MVApost >1.94 cm2 与 MVApost ≤1.94 cm2，Log-rank χ2=5.427，P=0.02；结论为 post MTEER 3D MVA <1.94 预示较差结局，若术前已有 PH 则更差。

中间示例显示 individually optimise and trace each orifice：上方 MVA 1.18，下方 MVA 2.22，MVA sum=3.4 cm2。右侧关于 MVA 对死亡率影响的研究：N=279，retrospective，5 年随访；primary MR 占 51%，其中 38/142 MVA ≤1.5；secondary MR 占 49%，其中 42/137 MVA ≤1.5。图中结论为：degenerative MR 且 MVA ≤1.5 时预后更差；secondary MR group 未见差异。

### MR 评估应结合左房压 LAP

Hemodynamic profiling 用 residual MR 和 mLAP 共同定义 optimal、mixed 与 poor。

Hemodynamic profiling 定义为：residual MR ≤1+ 加 mLAP ≤15 mmHg。两者都满足为“Optimal” Type I；只满足其中一个为“Mixed” Type II；两者都不满足为“Poor” Type III。

| 左图：Survival with TEER | 读数 |
| --- | --- |
| MR ≤1+ and mLAP ≤15 mmHg | 生存率 91.6% |
| MR >1+ or mLAP ≥15 mmHg | 生存率 82.6% |
| MR ≥1+ and mLAP ≥15 mmHg | 生存率 67.9% |
| 统计 | Log-rank test P<0.001；HR 2.13，95% CI 1.44-3.15，P<0.001 per 1 category。以 Optimal 为参照，Mixed HR 2.16，95% CI 1.10-4.22，P=0.03；Poor HR 4.55，95% CI 2.07-9.96，P<0.001。 |

| 右图：≤1+ MR 患者中 LAP 影响 | 0 月 | 4 月 | 8 月 | 12 月 | 12 月生存率 |
| --- | --- | --- | --- | --- | --- |
| mLAP ≤15 mmHg | 148 | 137 | 130 | 116 | 91.6% |
| mLAP 16-20 mmHg | 97 | 83 | 78 | 72 | 85.5% |
| mLAP >20 mmHg | 66 | 53 | 47 | 43 | 80.0% |

右图统计：Log-rank test P=0.06；HR 1.60，95% CI 1.08-2.37，P=0.02 per 1 category。以 Optimal 为参照，Mixed HR 1.77，95% CI 0.81-3.88，P=0.15；Poor HR 2.56，95% CI 1.15-5.70，P=0.02。引用 Sato H et al. JACC Cardiovasc Interv 2022。

### Pulmonary vein flow：异常 PV-flow 的提示

低 Svti/Dvti 与较高 MACE、较少 NYHA 改善和短期 MR 加重相关。

示例频谱显示：低 Svti/Dvti 组 Svti=7.5 cm、Dvti=14 cm、Svti/Dvti ratio=0.54；高 Svti/Dvti 组 Svti=23 cm、Dvti=10 cm、ratio=2.3。

| MACE 累积发生率 | 0 月 | 3 月 | 6 月 | 9 月 | 12 月 | 结果 |
| --- | --- | --- | --- | --- | --- | --- |
| Low Svti/Dvti | 91 | 68 | 60 | 52 | 45 | 12 月累积 MACE 约 28%；Log-rank P<0.001 |
| High Svti/Dvti | 209 | 173 | 165 | 159 | 141 | 12 月累积 MACE 约 7% |

| NYHA III/IV rate | Low Svti/Dvti | High Svti/Dvti | P 值 |
| --- | --- | --- | --- |
| 1-month | 33%，n=61 | 17%，n=179 | P=0.005 |
| 12-month | 28%，n=60 | 12%，n=156 | P=0.006 |

| MR 3+ or 4+ rate | Low Svti/Dvti | High Svti/Dvti | P 值 |
| --- | --- | --- | --- |
| After MitraClip | 5.5%，n=91 | 0%，n=209 | P<0.001 |
| 1-month | 26%，n=61 | 5.2%，n=176 | P<0.001 |
| 12-month | 18%，n=50 | 5.3%，n=149 | P=0.008 |

该页结论为：abnormal PV-flow 与 NYHA 改善较少相关，也预测短期 MR 加重。引用 Ikenaga H et al. JACC Int 2019。

### 有时保留少量 MR 优于制造明显 MS

多个研究图示共同强调：轻度或中度 MR 与低梯度的组合，可能优于更低 MR 但较高梯度的组合。

左上 Neuss/Butter 图比较 MVPG <5 mmHg 与 MVPG >5 mmHg 的 combined endpoint。Number at risk：MVPG <5 mmHg 为 148, 94, 78, 56, 41；MVPG >5 mmHg 为 48, 23, 14, 8, 5。两组差异 P=0.001，高 MVPG 组曲线下降更快。

右上图按 PG 与 MR 组合分层，图例包括 PG <5, MR=1+；PG <5, MR=2+；PG >5, MR=1+；PG <5, MR=3+；PG >5, MR >1+。红框特别比较 PG <5, MR=2+ 与 PG >5, MR=1+，提示残余 2+ MR 但低梯度的结果未必比轻 MR 但高梯度差。

| Makkar/Leon JAMA 2023 图中分组 | 相对 unsuccessful 的调整 HR |
| --- | --- |
| Mild MR or less / gradient ≤5 mmHg | 0.35，95% CI 0.30-0.41，P=.02 |
| Mild MR or less / gradient >5 to <10 mmHg | 0.65，95% CI 0.54-0.78，P<.001 |
| Moderate MR / gradient ≤5 mmHg | 0.53，95% CI 0.44-0.63，P<.001 |
| Moderate MR / gradient >5 to <10 mmHg | 0.77，95% CI 0.62-0.96，P<.001 |

下方 12 个月图显示 mortality at 1 year 和 heart failure readmission at 1 year 均按结果分层；heart failure readmission 图 Log-rank P<.001。图中约读数显示 unsuccessful 曲线最高，12 个月再住院约 17%；mild MR/MG ≤5 最低，约 6%；moderate MR/MG ≤5 约 9%；mild MR/MG 5-10 约 12%；moderate MR/MG 5-10 约 15%。

### 总结

Prognosis：residual MR 驱动长期结局；MR reduction 往往超过 gradient increase 的影响。Planning：MVA 可在 clipping 前预判；策略取决于病变位置、器械和形成的瓣口。Guidance：应联合 MR grade、LAP 和 PV flow。讲者最后强调，完美结果并非每次都必须达到，但仍应以 best achievable result 为目标。
