# AI 左室几何预测 TAVR 后重构：性别特异模型

## 核心要点

* 研究假设是：常规 pre-TAVR CT 中隐藏的 3D 左室几何信息，可以预测 TAVR 后左室质量回缩，而且这种预测具有性别特异性。
* 队列包含 339 例 BWH + MGH 患者，时间范围 2015-2023；女性 133 例（39%），男性 206 例（61%）。
* AI 分割平均 Dice 为 0.93，HD95 3.2 mm；模型将 300k 网格降采样到 5k 对应点，保留绝对左室大小。
* 1 年时 65% 患者出现 positive LVMR，女性为 66%；中位 LVMI 从 110 降至 99 g/m²，性别间回缩差异 P=0.99。
* 形态模型优于传统临床指标：交叉验证 R² 从 clinical baseline 0.16 到 female-specific modes 0.89；held-out general model R² 0.59，female-specific model R² 0.80。

### 题目与讲者

报告题为“Personalized Sex-Specific Post-TAVR Remodeling Prediction by AI-Driven Left Ventricular Geometry in Aortic Stenosis”，中文可译为“AI 驱动左室几何对主动脉狭窄 TAVR 后重构的个体化、性别特异预测”。副标题指出：routine pre-TAVR CT 提取的 3D LV shape 可预测 reverse remodeling，并且具有 sex-specific 特征。讲者为 Shahab Masoumi, MD，来自 Mass General Brigham、Brigham and Women’s Hospital、Harvard Medical School，Boston, MA。

### 相关经济关系披露

Shahab Masoumi 声明没有任何需要披露的经济关系。教师披露信息可在会议 app 中查看。

### 解除瓣膜狭窄不保证心室恢复

主动脉狭窄不仅是瓣膜病，也是心室病；问题是哪些患者会发生左室逆重构。

该页提出核心临床问题：relieving the valve does not guarantee the ventricle recovers。讲者强调主动脉狭窄是 ventricle 的疾病，而不仅是 valve 的疾病。流程为：severe aortic stenosis 导致 chronic LV pressure overload；TAVR 可解除 afterload；但最终可能发生 reverse remodeling（LVMR），也可能不发生。中间示意图显示主动脉瓣狭窄导致血流受阻、左室工作负荷增加和肥厚；右侧对比 SAVR 与 TAVR 后可能出现 LV reverse remodeled 或 LV adverse remodeled。页底问题为：谁会重构，谁不会？

### 传统指标的局限和研究假设

传统 LVMI、LVEF、舒张功能是二维和瓣膜中心指标，难以捕捉 3D 心室结构和性别差异。

当前指标被描述为 2D、valve-centric、male-dominated。第一，LV mass index、ejection fraction 和 diastolic function 会把 3D 结构压缩为标量平均值。第二，AS 不是 sex-neutral：女性更倾向向心性重构、腔室较小、低流量；男性更倾向离心性重构、扩张。第三，肥厚和纤维化具有区域异质性，两个质量相同的心室形态可能明显不同。

右侧“Sex disparities across AS care”示意图显示：男性更年轻，女性更年长且症状更多；解剖层面男性更常有瓣膜钙化，女性更常有弥漫心肌纤维化；LV remodeling 可呈 eccentric 或 concentric；TAVR 频率和生存也存在差异。研究假设为：pre-TAVR CT 中包含潜在 3D 几何信息，可改善 remodeling prediction，并且这种改善具有 sex-specific 特征。

### AI 与统计形态管线

从 pre-TAVR CT 到 AI 分割、3D digital twin、PLS 形态分析、SVR 模型和 post-TAVR LVMR 预测。

研究目的包括两点：重新定义重度 AS 患者 TAVR 后 LV remodeling 的预测因子；利用 3D LV geometry 和 sex-specific differences 预测术后 LVMR。研究假设包括三点：shape modes 优于 baseline clinical measures；SSA pre-op LV shape modes 可区分性别；几何特征在 SSA 和降维后仍可保留。

方法流程分为 5 步：1 AI segmentation；2 3D digital twin；3 shape analysis（PLS）；4 SVR model；5 post-TAVR LVMR。右侧流程图显示 pre-TAVR CT 经 AI-based segmentation 生成 STL 左室模型，经 mesh downsampling 后进入 statistical shape analysis，进行 center、align、reorder，并经 ML order reduction 生成 sex-specific shape scores，再进入 post-TAVR prediction 和 LVMI regression。

### 队列和基线特征

339 例患者，AI 左室分割平均 Dice 0.93，基线表显示男女在 LVMI 和 LVEF 上存在差异。

队列包括 339 例患者，来自 BWH + MGH，时间为 2015-2023。女性 133 例，占 39%；男性 206 例，占 61%。AI 分割与专家相比平均 Dice 为 0.93，HD95 为 3.2 mm。网格从 300k 点降采样到 5k 对应点。Segmentation 使用 TotalSegmentator deep learning；结局为 1 年 echo LV mass index（ASE）；形态来自 pre-TAVR CT。关键方法选择是保留绝对 LV size，不做标准化，因为 size 本身是 remodeling 的临床特征。

| 变量 | 全体 | 男性 | 女性 |
| --- | --- | --- | --- |
| 年龄，岁 | 78.4 | 77.4 | 79.2 |
| LV mass index，g/m² | 113 | 117 | 107 |
| LVEF，% | 59.6 | 58.6 | 61.0 |
| 高血压 | 90% | 90% | 91% |
| 糖尿病 | 30% | 31% | 29% |

### 1 年左室质量回缩分布

多数心室在 1 年发生回缩，男女相似；总体中位 LVMI 从 110 到 99 g/m²。

该页标题为“Most ventricles regress at one year, equally in both sexes”。左上方总结：positive LVMR 为 65%，女性为 66%；中位 regression 约 10%，男性 10.1%，女性 9.4%；性别间 regression 无差异，P=0.99；总体中位 LVMI 从 110 降至 99 g/m²。

左侧直方图横轴为 LVMI regression，范围约 -0.6 到 0.7；纵轴为全体人群百分比，最高柱约 16%。图内标注 ΔLVMI≥0 为 74%，ΔLVMI<0 为 26%。右侧 violin plot 显示 pre 和 post TAVR 的整个群体 LVMI 分布，pre 中位数标注 108.8，post 中位数标注 101.2；旁注 median regression = 8%。

### 性别差异的几何成分可视化

显著性别差异的 general shape modes：Mode 1、2、4、6、12，颜色条为距离变化约 -0.4 到 +0.4 mm。

该页展示 significant modes，包括 Mode 1、Mode 2、Mode 4、Mode 6 和 Mode 12。每列包含 inner distance 和 thickness 两行热图。坐标说明为 base 到 apex，lateral 到 anterior。颜色条为 Δ Distance，范围约 -0.4 到 +0.4 mm。图例显示最高 shape score 的性别：粉色代表 women，蓝色代表 men。模式含义为：Mode 1 对应 global LV size 降低；Mode 2 对应 global LV size 升高；Mode 4 和 Mode 6 反映 local remodeling，即 spherical to ovoidal ratio；Mode 12 对应 wall thickness。脚注说明这些为 Welch’s t-test 中 score 存在显著性别差异的 general shape modes，P<0.05。

### 性别特异 3D 几何优于传统指标

一般人群形态模型、女性特异模型和临床基线模型性能比较。

左侧 held-out 拟合图中，一般人群模型 accuracy 87%，R²=0.59，RMSE=0.13。女性特异模型 accuracy 91%，R²=0.80，RMSE=0.09。页底给出 clinical baseline 模型，使用 pre-TAVR LVMI、LVEF、LVDD，accuracy 53%，R²=0.19，RMSE=0.47。

| 模型/特征 | 交叉验证 R² |
| --- | --- |
| Clinical baseline | 0.16 |
| General shape modes | 0.59 |
| Male-specific modes | 0.80 |
| Female-specific modes | 0.89 |

图中标注 cross-validated R² 的 mean ± SD 分别为 0.16±0.02、0.59±0.07、0.80±0.01、0.89±0.01。相较临床基线，解释方差增加超过 4 倍，R² 从 0.16 到 0.89；RMSE 下降 59%，从 0.22 到 0.09。讲者强调 regional signal 反映肥厚位于何处，而不是平均大小。

### 结论、局限和下一步

结论页：形态预测优于传统指标，且男女形态模式不同；局限包括回顾性、双中心和仅内部交叉验证。

第一，shape-based predictors 优于 conventional metrics。基于 3D LV geometry 的工具预测 post-TAVR LV reverse remodeling，R²=0.8，明显高于 baseline clinical predictor 的 R²=0.19。该方法可能用于严重 AS 人群的干预时机优化。第二，sex-specific LV shape modes 在女性和男性之间不同，并具有不同预测价值，R²=0.8 对 R²=0.59。第三，shape analysis 揭示了参与 LVMR 的左室几何变化，包括局部和全局 LV size、球形到卵圆形比例、以及壁厚变化，这些都可由 shape modes 解释。

局限和下一步包括：研究为回顾性、双中心队列；形态来自 CT，但结局来自依赖操作者的 echo LVMI；要求 1 年随访导致 survivor/attrition 偏倚；目前仅有内部交叉验证。临床使用前还需要前瞻性外部验证、与硬临床结局关联，以及 CMR/组织学层面的组织表征。通信邮箱为 [邮箱已隐去]；基金包括 NIH R21HL173731、AHA 25CDA1452999、NIH F32 和 NSF ACCESS。
