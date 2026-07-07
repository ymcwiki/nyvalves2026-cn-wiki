# 三叶主动脉瓣狭窄 TAVR 患者的纤维钙化组织分布表型与结局

## 核心要点

* 研究来自单中心 Duke TAVR registry，分析 1,129 例患者，平均年龄 78.3±8.7 岁，女性 44.9%；三叶瓣 1,014 例，二叶瓣 115 例。
* 钙化组织中位体积 359 mm³，IQR 213-546，indexed 73 mm³/cm²；纤维化组织中位体积 152 mm³，IQR 32-276。
* 无监督聚类在三叶瓣病例中识别出三个表型：leaflet-fibrotic 330 例（32.5%）、leaflet-calcific 477 例（47.0%）、periannular-calcific 207 例（20.4%）。
* Leaflet-fibrotic 组新 PPM 较高，aOR 1.99，p=0.010；periannular-calcific 组长期死亡率较高，aHR 1.33，p=0.008。
* 新的 periannular-calcific 模式表现为 LVOT 和 supra-commissural calcification 较高，虽总钙负荷较低，却携带更高长期死亡风险。

### 题目与讲者

幻灯片题目为“Fibrocalcific Tissue Distribution Phenotypes in Tricuspid & Bicuspid Aortic Stenosis”。讲者 Luke P. Dawson, MBBS, PhD，来自 Duke University Hospital。注意，幻灯片标题同时包含 tricuspid 与 bicuspid AS；本篇清单标题聚焦 tricuspid AS undergoing TAVR。

### 相关财务关系披露

Luke P. Dawson 声明没有与本报告相关的财务关系需要披露。页面注明 faculty disclosure information 可在会议 app 中查看。

### 背景

主动脉瓣狭窄的特征是 fibrocalcific remodeling。组织类型和空间分布会影响疾病严重程度与结局。瓣膜和主动脉根部的 fibrocalcific tissue 空间模式此前尚未被系统评估。

### 研究目的

研究目标包括：使用 polar bullseye 与 cylindrical wall projections 绘制 calcific 和 fibrotic tissue 的 3D 空间分布；使用 unsupervised machine learning 识别 fibrocalcific distribution phenotypes；评估 phenotypes、患者特征与 TAVR outcomes 之间的关系。

### 方法：标注与组织分类

半自动 CT 标注流程与组织分类示例。

研究使用单中心 Duke TAVR registry，时间为 2012-2020，影像为 ECG-gated cardiac CT。半自动标注 cusp nadirs、commissures、coaptation 和 STJ plane，用以定义 root、cusp 和 LVOT masks。组织分类基于每次扫描特异性的 blood-pool calibration，并经 histology 验证：calcific 定义为 mean + 3 SD；fibrotic 定义为 45 HU 到 mean - 3 SD。

右侧 9 个图依次示例 ROI Marker、TotalSegmentator、Cusp Nadir Annotations、Commissure Annotations、Central Coaptation、STJ Plane Adjustment、Cusp Masks、LVOT (4 mm slab) 和 Fibrocalcific Tissue。

### 方法：空间映射和聚类

瓣膜 bullseye 极坐标图与主动脉根壁圆柱展开图的示例。

瓣膜通过 polar bullseye projection 映射，主动脉根壁通过 cylindrical unwrap 映射；每种映射为 10×60 grid。每位患者生成 3 张 600-bin maps，并做归一化，以将 spatial pattern 与 total burden 分离。在三叶瓣病例中先进行 NMF，再进行 consensus clustering，样本量 N=1,014，不输入临床变量；k 值由 cophenetic correlation 和 silhouette width 决定。

示例图包含 Polar Maps 的 calcific 和 fibrotic 图，以及 Wall Unwrap 的 calcific 图。瓣叶标签包括 RCC、LCC、NCC；壁面展开标签包括 STJ、commissure、annulus、LVOT，以及 NCC、RCC、LCC 分区。

### 方法：TAVR 操作与结局

所有操作均由 high volume center 的 experienced operators 完成。院内结局包括 all-cause death、new PPM、stroke/TIA；术后 ECG 指标包括 new 1st degree AV block、new LBBB、PR/QRSD changes；TTE 指标包括 ≥mild 或 ≥moderate AR、mean gradient >10 mmHg 和 >20 mmHg。长期结局包括 all-cause death、new PPM 和 AV re-intervention。

### 研究队列

Duke TAVR Registry 队列筛选流程。

最终分析 1,129 例患者，平均年龄 78.3 岁，SD 8.7；女性 44.9%。瓣膜类型为 tricuspid 89.8%，n=1,014；bicuspid 10.2%，n=115。

|  |  |
| --- | --- |
| Duke TAVR Registry | Apr 2012-Jul 2020，n=1,305 |
| 第一轮排除 | Excluded n=169：prior aortic valve replacement n=114；pre-procedural CT not available n=55。 |
| Pre-procedural CT segmented | n=1,136 |
| 第二轮排除 | Excluded n=7：inadequate CT quality。 |
| Phenotyping cohort | n=1,129，其中 tricuspid n=1,014，bicuspid n=115。 |
| Outcomes cohort | TAVR implanted，n=1,123。 |
| Outcomes 排除 | Excluded from outcomes n=6：TAVR aborted。 |

### 纤维钙化组织体积

Calcific tissue：中位体积 359 mm³，IQR 213-546；indexed 73 mm³/cm²。分布为 NCC-dominant，顺序为 NCC > LCC > RCC。男性钙化体积高于女性，468 vs 243 mm³。

Fibrotic tissue：中位体积 152 mm³，IQR 32-276；各 cusp 间相似。女性 fibrotic-to-calcific ratio 较高，0.66 vs 0.39。二叶瓣的 calcific 和 fibrotic burden 均高于三叶瓣。

### 纤维钙化组织关联

组织空间特征与临床、传导、超声和解剖指标的 Spearman 相关热图。

热图使用 Spearman ρ 色阶，范围约为 -0.4 到 +0.4，蓝色为负相关，红色为正相关，星号标示统计显著性。列包括 calcific vol. index、calcific % RCC、calcific % LCC、calcific % NCC、calcific LVOT、LVOT RCC、LVOT LCC、LVOT NCC、calcific supra-comm.、fibrotic vol. index、fibrotic % RCC、fibrotic % LCC、fibrotic % NCC。行包括 age、women、BMI、HTN、DM、prior MI、PVD、prior stroke、dialysis、AF、1° AVB、RBBB、LBBB、QRSD、PR interval、LVEF、mean gradient、valve area、AR 3+、MR 3+、TR 3+、annular area index、annular ellipticity、annular tilt、RCC rotation、commissural height ratio、commissural tilt、STJ/annulus ratio、STJ height ratio、STJ tilt、root volume index、LVOT/annulus ratio、LVOT ellipticity、LVOT offset ratio。

作者总结的主要关联为：calcific tissue 与男性性别、更高 mean gradient、BMI 和 conduction delay 相关；LVOT 和 supra-commissural calcium 与 conduction disease 和 vascular comorbidity 相关；fibrotic tissue 与 older age、prior MI、AF 和 concomitant valve disease 相关；不同关联谱提示 calcific 和 fibrotic pathways 部分独立。

### 聚类表型

NMF/共识聚类得到三个三叶瓣纤维钙化分布表型。

共识聚类得到三个表型：leaflet-fibrotic，n=330，32.5%；leaflet-calcific，n=477，47.0%；periannular-calcific，n=207，20.4%。这些 cluster 分离良好且 ambiguity 低，PAC 0.086，mean silhouette 0.29；bootstrap resampling 稳定，Jaccard 0.94-0.99。

右侧 A 图为 z-score heatmap，色阶从 -3 到 +3，列为 Polar Calc 1、Polar Calc 2、Polar Fib 1、Polar Fib 2、Wall Calc 1、Wall Calc 2。B 图为 consensus matrix，色阶 0.00-1.00。C 图为 silhouette width：cluster 1，n=330，约 0.28；cluster 2，n=477，约 0.25；cluster 3，n=207，约 0.38。

### 三叶瓣纤维钙化分布表型

三叶瓣三种表型在 P50、P75、P90 和 wall P90 上的钙化分布。

本页按三叶瓣 cluster 展示 calcific distribution phenotypes。三行分别为 tricuspid cluster 1 leaflet-fibrotic，N=330；tricuspid cluster 2 leaflet-calcific，N=477；tricuspid cluster 3 periannular-calcific，N=207。列为 P50、P75、P90 和 Wall P90。polar maps 标注 RCC、LCC、NCC；wall unwrap 标注 STJ、commissure、annulus、LVOT，并在底部标注 NCC、RCC、LCC。

图例为 calcific burden，单位 mm³/cm²，色阶从 0.00 到约 0.35。Leaflet-fibrotic 和 leaflet-calcific 的 P90 均可见瓣叶钙化热点；periannular-calcific 的 wall P90 显示更突出的 STJ/supra-commissural 区域以及 LVOT/annulus 相关钙化，符合 periannular 表型定义。

### 二叶瓣 AS 的纤维钙化分布

二叶瓣 AS 按形态类型展示 P50、P75、P90 和 wall P90 分布。

本页题为“Fibrocalcific distribution in bicuspid AS”。三行分别为 bicuspid type 0，N=9；bicuspid type 1 (L-R)，N=83；bicuspid type 1 (R-N)，N=20。列为 P50、P75、P90 和 Wall P90。Type 0 的 polar maps 使用 Ant/Post 标签；Type 1 图上标注 RCC、LCC、NCC。wall P90 图标注 STJ、commissure、annulus、LVOT；Type 0 底部为 Ant/Post，Type 1 底部为 NCC、RCC、LCC。

右侧图例标示 fibrotic burden，单位 mm³/cm²，范围 0.00-0.10。图中同时可见红橙色钙化和蓝色纤维化分布，用以说明二叶瓣不同解剖类型中 fibrocalcific tissue 的空间差异。

### 表型特征表

三叶瓣三种表型的临床、超声和组织体积特征。

表格标题为“Phenotype characteristics”，对象为 tricuspid phenotypes，N=1,014；数值为 median 或 mean。带星号项目为 indexed to annular area，单位 mm³/cm²。

| Variable | Leaflet-fibrotic (n=330) | Leaflet-calcific (n=477) | Periannular-calcific (n=207) | P |
| --- | --- | --- | --- | --- |
| Age, years | 80.5 | 78.2 | 78.2 | <0.001 |
| Women, % | 47.6 | 36.3 | 62.3 | <0.001 |
| Diabetes, % | 36.7 | 46.3 | 45.4 | 0.027 |
| STS-PROM | 5.3 | 5.4 | 6.5 | <0.001 |
| Mean gradient, mmHg | 43.4 | 46.3 | 40.8 | <0.001 |
| Calcific volume index\* | 67 | 82 | 65 | <0.001 |
| Fibrotic volume index\* | 43 | 19 | 39 | <0.001 |
| LVOT calcific index\* | 0 | 0 | 7 | <0.001 |
| Supra-commissural calcific\* | 7 | 8 | 29 | <0.001 |

### TAVR 后结局按表型分层

三叶瓣表型和二叶瓣组的长期死亡、主动脉瓣再干预和起搏器植入曲线。

院内结局：leaflet-fibrotic 组 higher PPM，aOR 1.99，p=0.010；leaflet-fibrotic 和 periannular-calcific 组 post-TAVR gradient 更低。长期结局中位随访 4.4 年：periannular-calcific 组 higher mortality，aHR 1.33，p=0.008；reintervention 或 long-term pacemaker 在组间无差异。所有结果均调整 age、sex、STS。

右侧 A 图为 all-cause mortality，对应纵轴 survival probability，横轴 time (years) 0-10；log-rank p=0.001。B 图为 aortic valve reintervention，对应纵轴 cumulative incidence 0%-10%，Gray test p=0.847。C 图为 pacemaker implantation，对应纵轴 cumulative incidence 0%-40%，Gray test p=0.322。图例颜色为 cluster 1 leaflet-fibrotic 蓝色、cluster 2 leaflet-calcific 绿色、cluster 3 periannular-calcific 橙色、bicuspid 紫色；生存曲线中 orange periannular-calcific 走低，符合更高长期死亡率。

### 纤维钙化分布表型汇总

四类形态的 CT、root mask、polar maps 和 wall unwrap 汇总。

本页汇总列标题为 CT en face、CT outflow、Root Mask fibrocalcific tissue、Polar Maps calcific、Polar Maps fibrotic、Wall Unwrap calcific。Leaflet-fibrotic，N=330：年龄较高、女性较多、fibrotic 增加、calcific 减少、新起搏器增加。Leaflet-calcific，N=477：男性较多、糖尿病较多、calcific 增加、fibrotic 减少、post-TAVR gradient 增加。Periannular-calcific，N=207：女性较多、STS 较高、LVOT/STJ calcific 增加、长期死亡率增加。Bicuspid，N=115：年龄较低、calcific 增加、fibrotic 增加，结局相似。脚注说明示例为 R-L bicuspid。

### 结论

研究仅从 spatial pattern 识别出三个可重复三叶瓣表型：leaflet-fibrotic、leaflet-calcific 和 periannular-calcific。新的 periannular-calcific 模式，即 LVOT 和 supra-commissural calcification，虽总钙负荷较低，却携带更高长期死亡率。Fibrocalcific tissue 的空间模式具有超越 total burden 的预后意义，可能反映不同疾病机制。

本套幻灯片未单独列出局限；从方法页可确认，研究基于单中心 Duke TAVR registry、2012-2020 年 ECG-gated CT 和观察性结局关联，因此外推到其他中心、不同 CT 方案或新一代 TAVR 实践时需要进一步验证。

### 致谢、代码与联系方式

共同作者为 A Vekstein、L Huckaby、L Hurwitz、F Alenezi、S Vemulapalli、A Wang、A Pineda、Z Wegermann、Y B Pride、J G Gaca、A Williams、G C Hughes、J K Harrison。代码地址为 github.com/ludaws/aortic-root-phenotyping。联系方式为 [邮箱已隐去]。
