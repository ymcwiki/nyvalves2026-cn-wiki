# 左心耳封堵中患者特异性 CFD 的启示

## 核心要点

* LAAO 是房颤高卒中风险且不适合长期抗凝患者的既定预防手段，但 device-related thrombosis 仍可见，报告给出的发生率最高可达 7%。
* DRT 与流动有关，患者特异性 CFD 可把 CT、模型分割、边界条件和有限元/流体模拟连接起来，观察 LA 和 LAAO 器械周围的血流停滞。
* 本报告关注 TAWSS、OSI、RRT、ECAP 四个参数：低 TAWSS、高 RRT、高 ECAP 均提示更不利的近壁血流环境。
* Vogl et al. 2024 图中，DRT 组 TAWSS 低于对照组，p<0.01；OSI 差异 p=NS；ECAP 高于对照组，p<0.01。
* 深植入与不利流体动力学相关，RRT 高代表 poor washout，也就代表 DRT 可能性更高。
* 设备类型也会影响流动：Bshennaty et al. 2025 图示 Amulet 植入后更常出现血流动力学改善，但这种改善并未与 DRT 有无直接相关。

### 题目与讲者

本报告题为“Lessons From Patient-Specific Computational Fluid Dynamics in Left Atrial Appendage Occlusion: Implications for Device Selection, Implantation Strategy, and Thrombosis Risk”，中文可译为“左心耳封堵中患者特异性计算流体动力学的启示：对器械选择、植入策略和血栓风险的影响”。讲者为 Hoda Hatoum, PhD。

### 财务利益披露

讲者披露过去 24 个月内与 Dasi Sim 存在 Royalties/Patent Beneficiary 关系，所有相关财务关系均已缓解。

### LAAO 与器械相关血栓

LAAO 可用于卒中预防，但术后仍可能发生 DRT。

Left atrial appendage occlusion (LAAO) 是一种 established therapy，用于 elevated stroke risk 且存在 long-term anticoagulation contraindications 的 atrial fibrillation 患者。尽管 procedural success，device-related thrombosis (DRT) 仍是 clinically significant complication，prevalence 可达 7%。右侧示意图显示 before occlusion 的 LAA，封堵后无 DRT 的状态，以及封堵后器械表面出现 DRT 的状态。

### DRT 预测因素和血流机制

临床预测因素之外，讲者强调 thrombosis is related to flow。

临床研究已经发现 device type、implantation depth 和其他因素与 DRT 相关。页面明确写出：thrombosis is related to flow；DRT 的 underlying hemodynamic mechanisms remain poorly understood。

右上图总结 Published Predictors of DRT。Clinical Characteristics 包括 age、prior stroke or TIA、coagulopathy、permanent AF、low LVEF、renal failure、vascular disease。Procedural Factors 包括 LAA diameter、implant depth、procedural complications (effusion)。Post-Procedure Tx OAC/APT 部分提出“? Antiplatelets therapy only”。缩写说明：AF 为 atrial fibrillation，APT 为 antiplatelet therapy，DRT 为 device-related thrombus，LAA 为 left atrial appendage，LVEF 为 left ventricular ejection fraction，OAC 为 oral anticoagulation，TIA 为 transient ischemic attack。

右下图为 Virchow’s triad: recipe for thrombosis，三角包括 endothelial injury、stasis/turbulence、hypercoagulability。引用 Alkhouli et al. ACC: Advances. 2022。

### 与扰动流和停滞相关的流动参数

四个参数均由 wall shear stress 或近壁流动推导，用于描述血流停滞和内皮激活。

| 参数 | 定义 | 生理流 | 扰动/停滞流 | 公式 |
| --- | --- | --- | --- | --- |
| TAWSS | Time Averaged Wall Shear Stress，整个心动周期 WSS magnitude 的平均值。 | Higher TAWSS。 | Low TAWSS。 | TAWSS = 1/T ∫0T |WSS| dt。 |
| OSI | Oscillatory Shear Index，WSS vectors 在心动周期内偏转的程度。 | Lower OSI，约 0，单向流。 | High OSI，约 0.5，recirculation。 | OSI = 1/2 (1 - |∫0T WSS dt| / ∫0T |WSS| dt)。 |
| RRT | Relative Residence Time，血液颗粒在近壁区域停留时间。 | Lower RRT，good washout。 | High RRT，poor washout。 | RRT = 1 / ((1 - 2 × OSI) × TAWSS)。 |
| ECAP | Endothelial Cell Activation Potential，低 shear oscillatory flow 引起的内皮激活程度。 | Lower ECAP。 | High ECAP，endothelial activation。 | ECAP = OSI / TAWSS。 |

### 患者特异性 CFD 流程

流程从患者 CT 到模型分割、边界条件，再到 CFD 模拟的动态血流结果。

Procedural Framework 包含 4 个步骤。第一，Patients CT Scans：输入患者 CT 扫描。第二，Model Segmentation：从 pre-deployment 模型到 post-deployment 模型，通过 finite element simulations 模拟 Amulet Device 和 Watchman Device 的植入后形态。第三，Patient-Specific Boundary Conditions：生成 mesh 和 boundary conditions，图中标注 MV velocity。第四，Computational Simulations (CFD)：得到 simulated flow dynamic results。速度色标 V 为 0.0、0.3、0.6、0.9、1.2 m/s。

### DRT 是否与不利流动参数相关

DRT 组 TAWSS 较低、ECAP 较高；OSI 的组间差异未达显著。

图 A 为 TAWSS (Pa)，纵轴 0 到 10.0。DRT 组箱体约在 0.8-2.3 Pa，中位数约 1.7 Pa，须线约 0-4.4 Pa；CTL 组箱体约在 1.0-3.8 Pa，中位数约 2.9 Pa，须线最高约 8.1 Pa。组间 p<0.01。

图 B 为 OSI，纵轴 0.0 到 0.6。DRT 组中位数约 0.19，CTL 组中位数约 0.16，两组须线均可接近 0.50，差异 p=NS。

图 C 为 ECAP (Pa-1)，纵轴 -0.1 到 1.0。DRT 组箱体约 0.05-0.25，中位数约 0.23，须线最高约 0.55；CTL 组箱体约 0.02-0.17，中位数约 0.05，须线最高约 0.40。组间 p<0.01。页面结论写为：Patients with DRT are characterized by lower TAWSS and higher OSI and ECAP，但需注意 OSI 单独比较为 NS。引用 Vogl et al. JACC: Advances. 2024。

### 代表性患者的 TAWSS、OSI 和 ECAP 地图

代表性患者中，体内影像血栓位置与低/高流动参数区域叠加显示。

左侧三张表面图分别标注 TAWSS、OSI、ECAP，黑色轮廓和箭头标注 thrombus location from in-vivo imaging。颜色条从 Low 到 High，低值为蓝色，高值为红色。TAWSS 图中血栓附近有局部蓝白低剪切区和邻近红色高剪切区；OSI 和 ECAP 图显示血栓轮廓附近存在局部不均匀区域。右侧为患者特异性三维模型示意，显示封堵器附近的解剖结构。引用 Vogl et al. JACC: Advances. 2024。

### DRT 队列与对照队列的 TAWSS 分布

DRT 队列 19 例与 no DRT 对照队列 19 例的 TAWSS 表面地图。

左侧 DRT Cohort 包含 DRT 1 到 DRT 19，右侧 Control (no DRT) Cohort 包含 CTL 1 到 CTL 19。底部 TAWSS 色标单位为 Pa，刻度为 0.00、0.86、1.75、2.61、>3.50。蓝色代表低 TAWSS，红色代表高 TAWSS。DRT 组多图叠加了黑色血栓轮廓或小圆圈，显示血栓位置与局部异常近壁剪切环境相关。引用 Vogl et al. JACC: Advances. 2024。

### 植入深度是否影响流体动力学

深植入与更高 RRT、较差 washout 相关；近端植入通常更蓝，提示停留时间较低。

页面问题为“Can Implantation Depth of the LAAO Device Affect Flow Dynamics?” 文字结论有两点：High RRT indicates poor washout，进而表示 high likelihood of DRT；deep implants are associated with unfavorable flow dynamic parameters。

右侧显示 4 位患者，每位患者比较 distal 与 proximal 植入。Patient 1 distal 图红白区域明显，proximal 主要为蓝色；Patient 2 distal 有多个红色斑点，proximal 几乎全蓝；Patient 3 distal 大片红色，proximal 主要蓝色；Patient 4 distal 近半红色区域，proximal 红色范围较小。RRT 色标单位 Pa-1，刻度为 0.0、0.5、1.0、1.5、2.0、2.5、3.0、3.5、4.0。

### 设备类型是否影响流体动力学：流线图

Amulet 与 Watchman FLX 植入前后流线对比，速度色标均为 0.0-1.2 m/s。

页面问题为“Can the Type of the LAAO Device Affect Flow Dynamics?” 上半部分为 Amulet (Abbott)，Patient 1 到 Patient 6，每例都有 Pre-LAAO 和 Post-LAAO 流线。下半部分为 Watchman FLX (Boston Scientific)，Patient 7 到 Patient 12，同样展示 Pre-LAAO 与 Post-LAAO。速度 V 色标单位 m/s，刻度为 0.0、0.3、0.6、0.9、1.2。图中蓝色封堵器位于 LAA 口或腔内，不同设备和不同植入形态改变左房/LAA 周围流线。引用 Bshennaty et al. CCI. 2025。

### 设备类型是否影响流体动力学：TAWSS 柱状图

Amulet 植入后 TAWSS 改善更常见；Watchman FLX 图中植入后 TAWSS 整体下降。

左侧 Amulet 图纵轴为 TAWSS (Pa)，范围 0.0 到 4.5，蓝色为 With DRT，橙色为 No DRT。图中估读：With DRT 从 Pre-LAAO 约 1.75 Pa 到 Post-LAAO 约 1.85 Pa；No DRT 从 Pre-LAAO 约 2.25 Pa 到 Post-LAAO 约 3.85 Pa。箭头方向向上，表示植入后改善。

右侧 Watchman FLX 图纵轴为 TAWSS (Pa)，范围 0.0 到 2.0。图中估读：With DRT 从 Pre-LAAO 约 1.25 Pa 到 Post-LAAO 约 1.12 Pa；No DRT 从 Pre-LAAO 约 1.75 Pa 到 Post-LAAO 约 1.25 Pa。箭头方向向下，表示植入后 TAWSS 降低。页面结论为：More frequent post-implant hemodynamic improvement with Amulet；this improvement was not correlated to DRT or lack thereof。引用 Bshennaty et al. CCI. 2025。

### 总结

计算型患者特异性研究有助于理解 LAAO 植入前后左房内基本流动机制。DRT 与 flow dynamic parameters 相关。Deep implants 与不利流体动力学相关，可能导致 DRT。LAAO flow dynamics 取决于 device type。正在进行的研究将基于 flow 开发 predictive indices。
