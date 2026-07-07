# TAVI Pilot 机器人瓣膜定位系统（Carvolix）

## 核心要点

* TAVIPILOT 的定位目标是减少 TAVI 瓣膜植入深度对术者经验和二维透视解读的依赖，降低起搏器、瓣周漏、冠脉阻塞和早期结构退化风险。
* AI-driven live “GPS” 不需要额外 markers 或 landmarks，可在透视中实时检测和追踪 non-coronary cusp 与 prosthetic valve，并对呼吸和心跳运动保持稳定。
* P4 界面示例中显示 Valve Implant: SAPIEN 3 Ultra，Size 26 mm，VLL Location 20%，并已检测 fluoroscopy、valve implant、contrast agent，同时进行 NCC and VLL tracking。
* 前期测试由 3 名 TAVI 专家执行，每个测试 60 次流程；AI augmented teleoperation 的定位误差分布最窄，图中标注约为 -0.3 至 0.5 mm。
* 临床项目显示 2024 年完成全球首个动物机器人 TAV 递送，first-in-human 从 2025 年 Q4 开始；ROTAO 1 澳大利亚阶段已达 9/10 例，procedural success 100%、complication 0、procedure time 31.7 min [SD 7.7]。
* 系统可作为 standalone software，也可整合到机器人系统，在 supervised control 下把实时 AI 引导与自动瓣膜定位闭环连接。

### 题目与讲者

首页标题为“Transforming TAVI Positioning With Real-Time AI, Augmented Reality and Robotics”，副标题为“First clinical use of TAVIPILOT Robot”。中文可译为“用实时 AI、增强现实和机器人改变 TAVI 定位：TAVIPILOT Robot 的首次临床使用”。讲者为 Stephen Worthley, MD, PhD，来自澳大利亚悉尼 Macquarie University Hospital。

### 利益关系披露

讲者说明过去 24 个月内存在相关财务关系。Consultant Fees/Honoraria 来自 Edwards Lifesciences、Abbott；Executive Role/Ownership Interest 为 Three Peaks Medical。Grant/Research Support、Individual Stock(s)/Stock Options、Royalties/Patent Beneficiary 和 Other Financial Benefit 未列出具体公司。所有相关财务关系已处理，披露信息可在会议 app 中查看。

### 未满足的临床需求

这一页题为“Unmet clinical need”。TAVI valve positioning 仍然依赖 operator。植入深度不理想可能导致 permanent pacemaker implantation、para-valvular leak、coronary obstruction 和 early structural deterioration。目前定位依赖 fluoroscopy 和 operator interpretation，因此需要实时、直观的 positioning support。由 AI software 驱动的 robotics 可以提高瓣膜放置精度和标准化程度。

### 全球首个 AI 驱动 TAVI 实时 GPS

左为原生透视，右为 TAVIPILOT 增强透视，界面显示实时 AI/AR 追踪和 20% 定位提示。

这一页标题为“1st in the World AI-driven live ‘GPS’ for TAVI”。左侧为 native fluoroscopy，右侧为 augmented fluoroscopy with TAVIPILOT。左下文字写明：No markers、No landmarks。右下文字列出三项功能：live non-coronary cusp detection and tracking with augmented reality；live prosthetic valve tracking with augmented reality；robust to breathing and heart-beat motion。

右侧 TAVIPILOT Solution 面板显示 Valve Implant 信息：Type 为 SAPIEN 3 Ultra，Size 为 26 mm，VLL Location 为 20%。Live Tasks Status 区域逐项打勾：Fluoroscopy detected、Valve implant detected、Contrast agent detected、NCC and VLL tracking。面板还用颜色图例标注 NCC、VLL、TAVIPILOT DIRECTOR，并显示 Live Confidence 栏和 End Live Tasks 按钮。增强透视图中瓣膜附近标注 20%，代表实时定位深度提示。

### TAVIPILOT Robot 首次临床使用

Macquarie University Hospital 首次临床使用 TAVIPILOT Robot 的设备和术者场景。

这一页标题为“TAVIPILOT Robot: first clinical use, Macquarie University Hospital”。左侧大图显示已覆盖无菌单的机器人/控制设备，画面左下角标注“Activate device”，右下角标注“illustrative footage”。右侧小图显示术者在导管室床旁操作，机器人组件位于患者身旁。该页强调系统已进入首次临床使用场景，而不仅是软件演示。

### 导管室现场图

导管室全景图，显示术者团队、C 臂、无菌覆盖设备和床旁机器人系统。

这一页没有文字标题，只显示导管室现场。画面中央可见术者团队在患者旁操作，右侧为透视设备，机器人或操作平台已用透明无菌套覆盖。该页作为上一页首次临床使用的现场补充，展示系统与常规 TAVI 导管室工作流的空间关系。

### AI 驱动机器人提高定位标准化精度

箱线图比较 manual actuation、manual augmented vision、teleoperation 和 AI augmented teleoperation 的定位误差。

这一页标题为“AI driven robotics allows for improved and standardized accuracy”。纵轴为 positioning error，单位 mm，范围约 -2 到 2。横轴四组为 Manual actuation、Manual augmented vision、Teleoperation、AI augmented teleoperation。右侧引用 Frontiers 文章“Towards autonomous robot-assisted transcatheter heart valve implantation”，下方写明 tests performed by 3 TAVI experts，60 procedures on each test。

箱线图标注读数如下。Manual actuation 的上须/上四分位/中位/下四分位/下须约为 -1.5、-0.8、-0.3、0.5、2.1 mm。Manual augmented vision 约为 -1.2、-0.1、0.2、0.5、1.2 mm。Teleoperation 约为 -0.8、-0.2、0.2、0.6、1.2 mm。AI augmented teleoperation 的标注约为上须 -0.3 mm、箱体上缘 0.0 mm、中位附近 0.1-0.2 mm、下须 0.5 mm，分布最窄。页底强调“AI driven software + robot”。

### TAVIPILOT Robot 临床项目

TAVIPILOT Robot clinical programme：动物实验、FIH、ROTAO 1、SAIRO 1B 和 ROTAO 2。

顶部进度条显示：Successful world first robotic TAV delivery in animal in 2024；First In Human start: Q4 2025。

左侧框为 ROTAO 1: Australia，状态 ONGOING，9/10 patients。技术为 TAVIPILOT (tele-operated robot)。说明文字为 robot remotely controlled by the operator during TAVI。适用 Edwards S3 and S3 ultra valves。结果列出 100% Procedural Success、0 Complication、Procedure time 31.7 min [SD 7.7]。底部写 High clinician satisfaction。

中间框为 SAIRO 1B: Australia，时间 Q2 2026。技术为 TAVIPILOT (tele-operated robot + guidance software)。说明为 combined use of robotic platform and real-time guidance software during TAVI。计划时间 April-May 2026，预计 10 patients。

右侧框为 ROTAO 2: Australia，时间 Q2 2026。技术为 TAVIPILOT autonomous。说明为 close-loop robot autonomously positions the valve under clinical supervision。计划时间 May-June 2026，预计 10 patients。

### 结论

结论有三条。第一，TAVIPILOT 可以作为 standalone software，也可以 fully integrated with the robotic system，机器人控制可为 manual 或 supervised control。第二，在 supervised control 下，AI-guided robotic system 会把瓣膜自动定位到 optimal depth，从 real-time guidance 到 automated valve positioning 形成闭环。第三，TAVIPILOT system 有潜力提高瓣膜放置的 precision and reproducibility，缩短 procedure times，并减少 fluoroscopy time 和 contrast usage。右侧配图为术中机器人使用场景。

### 致谢与联系方式

最后一页显示 THANK YOU 和 CARVOLIX 标识。文字为“Connect with us”，提示 follow us on LinkedIn and the web。页面包含两个二维码：LinkedIn 和 Website。网站文字为 carvolix.eu。
