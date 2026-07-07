# AI 驱动的 TAVR 图像增强与 3D 导航

## 核心要点

* 报告提出 Intelligent TAVR：自动 AI 驱动图像增强和 3D 导航，目标是在 TAVR 中改善可视化并减少造影剂使用。
* 当前 TAVR 影像短板包括软组织对比差、透视无法显示心脏解剖、平均每例约 152 mL造影剂、AKI 发生率 ≥10%，以及 2D 图像缺乏深度信息。
* 技术包含两部分：实时自动对比增强，以及将术中透视与术前 CT 对齐的 2D-3D多模态配准。
* 最佳增强方法为 Unsharp + CLAHE；荧光透视质量评分约 0.947，CT 质量评分约 0.994。
* 实时模式与离线模式质量接近，离线 score 0.946、time 1.12 s；实时 score 0.944、time 0.64 s，实时模式快 43%。
* CT-CT 配准验证中 Differential Evolution 的平移误差 0.0 mm、旋转误差 0.0°、运行时间 37.1 s；总结页报告 Fluoro-CT 配准精度 <3 mm。

### 技术题目与讲者

本报告题为“Intelligent TAVR: Automated AI-driven image Enhancement and 3D Navigation for better visualization and Contrast-Minimization in TAVR Procedure”，中文可译为“智能 TAVR：用于改善可视化并减少 TAVR 造影剂用量的自动 AI 驱动图像增强与 3D 导航”。讲者为 Shahab Masoumi, MD，来自 Brigham & Women’s Hospital 心血管 fellowship，Harvard Medical School, Boston, MA。

### 利益关系披露

Shahab Masoumi 声明无任何需要披露的经济关系。faculty disclosure 信息可在会议 app 中查看。

### 未满足的临床需求

未满足的临床需求：主动脉瓣狭窄流行病学、未治疗死亡率和外科不适合比例。

页面列出三项背景数据：年龄 >75 岁成人中主动脉瓣狭窄 AS 比例为 2-5%；未治疗 AS 的 2 年死亡率为 50%；超过 33%患者不适合开放手术。TAVR，即经主动脉瓣置换，已成为一种微创替代方案，并已用于所有患者风险分层。关键缺口是当前 TAVR 影像技术不足以提供安全引导。页脚注明所有相关经济关系已完成 mitigation，faculty disclosure 信息可在 app 中查看。

### 当前 TAVR 影像局限

当前透视下主动脉在无造影剂时不可见，主要局限为软组织对比差和仅有 2D 影像。

左侧两张透视图说明“Fluoroscopy: Aorta invisible without contrast dye”，即无造影剂时主动脉不可见。右侧总结主要 TAVR 影像局限。第一，软组织对比差：透视下心脏解剖不可见；每例平均使用 152 mL造影剂；肾毒性造影剂导致 AKI 的比例为 ≥10%；AKI 显著增加死亡风险。第二，只有 2D 影像：对 3D 解剖没有深度信息；术者必须在脑中重建 CT；术中认知负荷高；存在瓣膜位置不良风险。

### 技术差异化：从人工判断到自动叠加

当前实践与该技术的对照：造影剂需求、AKI 风险、3D 可视化、配准和认知负荷。

| Feature | Current Practice | Our Technology |
| --- | --- | --- |
| Contrast Requirement | 每例平均 152 mL | 显著减少 |
| AKI Risk | ≥10%患者 | 最小化 |
| 3D Visualization | 需要脑内重建 | 实时 3D overlay |
| Registration | 人工、耗时 | 自动化，<5 seconds |
| Cognitive Load | 术者负担高 | 降低 |

页脚引用 Smith et al. Eur Heart J. 2012;33:372-83。

### 技术概览：图像增强与 2D-3D 配准

技术流程：2D 实时透视扫描经 AI 增强后，与术前 CT 生成实时 3D 重建和主动脉根 3D 模型。

技术分为2个模块。第一是自动对比增强，包括实时图像优化、减少造影剂依赖、降低 AKI 风险。第二是 2D-3D 多模态配准，包括将透视与术前 CT 对齐、提供 3D 空间信息、降低认知负荷。底部流程从“2D RT fluoroscopy scan in OR”开始，经过第 1步“AI-Enhanced 2D fluoro scan”，再经第 2步“Real-Time 3D Reconstruction”，最终得到“Aortic root 3D RT model”。

### 对比增强方法：Unsharp + CLAHE

对比增强方法：先进行 Unsharp Masking，再做 CLAHE，并通过 64 个 tile 的双线性插值生成最终增强图像。

方法分为三层。第一层为 Unsharp Masking：Original(I) 减去 Gaussian Blur(I) 得到 Unsharp mask；增强图像由 Original(I) 加上权重 W 乘以 Unsharp mask 得到。第二层为 CLAHE：输入 Unsharp Masked Image，进行 Tile Division，随后计算 highlighted tile 的 local histogram，对 histogram 进行 clipping，再得到 clipped cumulative distribution function, CDF，最后生成 enhanced tile。

图中央显示对 64 tiles 逐个增强，得到 64 enhanced tiles，再通过 Bilinear Interpolation 合成最终图像。插值公式写为：T(p) = (1-α)(1-β)TBL + α(1-β)TBR + (1-α)βTTL + αβTTR。其中图中还标注 tile centre 和 pixel P。右侧方法框列出：离线优化测试了 8种增强方法、多种优化算法和 5-metric复合目标；实时调参为患者特异性适配，使用 Differential Evolution algorithm，优化时间 <5 seconds；术中使用为实时增强，透视 0.82 sec/frame，CT 2.96 sec total。两种模态最佳方法均为 Unsharp + CLAHE。

### 对比增强结果：质量与实时速度

对比增强结果：Original、Unsharp+CLAHE Offline 与 Unsharp+CLAHE RT 三图比较，并列出质量分数和时间。

左侧 key findings 列出：质量分数为 Fluoroscopy 0.947、CT 0.994；5-metric目标优于 entropy，数值为 0.946 vs 0.610；实时性能为 <5 sec收敛，所有配置质量均 >0.75。

右侧三张图分别为 Original、Unsharp + CLAHE Offline、Unsharp + CLAHE RT。离线增强 score 为 0.946，time 为 1.12 s；实时增强 score 为 0.944，time 为 0.64 s。下方总结为质量相当，Δ=0.5%，实时模式快 43%。

### 对比增强结果：5 参数优化是否值得

优化算法比较：质量分数与计算时间的散点图，以及 3 参数和 5 参数在质量与处理时间上的比较。

左侧散点图纵轴为 normalized quality score，范围约 0.3-1.0；横轴为 computation time，范围 0-5 s。虚线给出质量阈值 0.75 和实时阈值 1 s。图例包括 Interior-Point、Grid Search、Bayesian Opt、Diff. Evolution，以及 Entropy 与 5-Metrics 两类目标。红框标出最佳平衡点：quality 0.946，time 0.82 s/frame。左下文字明确写出“Fluoroscopy: Diff. Evolution: With 5-Metrics (0.946, 0.82 s)”。

| 比较 | 3-Parameter | 5-Parameter | 结论 |
| --- | --- | --- | --- |
| Bayesian Opt 质量 | 0.946 | 0.947 | 几乎无提升 |
| Diff. Evolution 质量 | 0.946 | 0.945 | 无提升 |
| Bayesian Opt 时间 | 4.3 s | 5.6 s | +29% slower |
| Diff. Evolution 时间 | 0.6 s | 1.4 s | +134% slower |

页脚问题为“Is optimizing the 5-parameters worth the complexity?”，答案是“No”。含义是：5 参数优化带来极小质量收益，却显著增加处理时间，因此不值得增加复杂度。

### 2D-3D 配准：CT-CT 验证

CT-CT 验证：目标为平移精度 <1 mm、旋转精度 <1°、处理时间 <60 s，Differential Evolution 表现最佳。

本页给出 2D-3D Registration 的 CT-CT validation。顶部目标为 translation accuracy <1 mm、rotation accuracy <1°、processing time <60 s。右侧图像比较 corresponding CT slice pose 的 ground-truth angles 和 predicted CT slice pose。

| Algorithm | Translation Error | Rotation Error | Runtime |
| --- | --- | --- | --- |
| Differential Evolution | 0.0 mm | 0.0° | 37.1 sec |
| Powell | 10.9 mm | 9.9° | 46.5 sec |
| Genetic Algorithm | 1.8 mm | 3.4° | 244.4 sec |

### 完整系统集成

系统集成：增强透视与注册后的 3D CT 结合，用于更安全的瓣膜定位。

本页说明完整系统将增强后的透视与配准后的 3D CT 结合，用于更安全的瓣膜定位。流程从左侧增强透视图出发，经箭头进入自动 3D 重建，随后生成有彩色分层轮廓的模型，最终形成“Aortic Root 3D RT model”。这对应前文两项核心技术：增强 2D 透视图像，以及把术前 CT 的 3D 空间信息注册到术中透视坐标系。

### 临床影响总结

临床影响被分为三类。第一是患者安全：通过减少造影剂用量降低 AKI 风险，提高瓣膜定位准确性，降低并发症发生率。第二是临床效率：减少手术时间，降低术者认知负荷，减少重复干预。第三是经济获益：降低 OR 成本，降低并发症管理费用，提高患者周转。

已验证的性能指标包括：N=50名患者验证并有专家临床复核；质量分数为透视 0.947、CT 0.994；配准精度为 CT-CT <1 mm、Fluoro-CT <3 mm；实时性能为透视 <1 sec、CT <3 sec。
