---
version: 1
updated: 2026-06-29
auto_suggestion_count: 0
---

# Wiki Schema 配置

本文件规定 LLM 如何构建和维护你的 Wiki，可以自由编辑。
（注意：枚举值、路径、字段名、链接格式等"契约词"必须保留英文原样，否则系统会判为非法并丢弃。）

## Wiki 结构
- 实体页：`实体/`（person、organization、project、product、event、place、other）
- 概念页：`概念/`（theory、method、field、phenomenon、standard、term、other）
- 来源页：`来源/`
- 索引：`index.md`
- 日志：`log.md`

## 实体页模板
`实体/` 下的页面必须遵循以下结构：

**Frontmatter 字段：**
- `type: entity` — 页面类别（必须正好是 "entity"）
- `created:` — 首次创建的 ISO 日期
- `sources:` — 来源文件 wiki 链接的数组
- `tags:` — 实体子类型，必须是以下之一：person、organization、project、product、event、place、other
- `aliases:`（可选）— 别名（译名、缩写）
- `reviewed:`（可选）— 为 true 时表示该页已人工核验并受保护

**章节：**
1. **基本信息**：类型、来源文件链接
2. **描述**：3-6 句具体事实，带双向链接
3. **相关实体**：用 [[实体/...]] 链接到相关实体
4. **相关概念**：用 [[概念/...]] 链接到相关概念
5. **来源提及**：带来源标注的逐字引用 — 见下方[来源提及格式](#来源提及格式)

## 概念页模板
`概念/` 下的页面必须遵循以下结构：

**Frontmatter 字段：**
- `type: concept` — 页面类别（必须正好是 "concept"）
- `created:` — 首次创建的 ISO 日期
- `sources:` — 来源文件 wiki 链接的数组
- `tags:` — 概念子类型，必须是以下之一：theory、method、field、phenomenon、standard、term、other
- `aliases:`（可选）— 别名（译名、缩写）
- `reviewed:`（可选）— 为 true 时表示该页已人工核验并受保护

**章节：**
1. **定义**：清晰、简洁的定义
2. **关键特征**：定义性特征的要点列表
3. **应用**：真实世界的使用场景
4. **相关概念**：用 [[概念/...]] 链接
5. **相关实体**：用 [[实体/...]] 链接
6. **来源提及**：带来源标注的逐字引用 — 见下方[来源提及格式](#来源提及格式)

## 命名约定
- 文件名：小写加连字符（slug 化）
- 实体/概念名称：保留来源原文语言，**绝不翻译**
- Wiki 链接：使用完整路径 [[实体/page-name|显示名]] 或 [[概念/page-name|显示名]]

## 来源页模板
`来源/` 下的页面必须遵循以下结构：

**Frontmatter 字段：**
- `type: source` — 页面类别（必须正好是 "source"）
- `tags:` — 从来源笔记的 frontmatter **继承**（不要用 LLM 提取的概念名）。系统会从来源文件以程序方式填充该字段，LLM 不得用提取出的概念名覆盖它。这样可保留用户已有的标签词汇，并防止 LLM 幻觉污染。
- `sources:` — 由本来源创建的相关 wiki 页链接的数组
- `created:` / `updated:` — 由系统设置，见下方"日期字段"

**章节：**
1. **摘要**：来源内容的简要描述（2-4 句）
2. **关键要点**：主要洞见的要点列表
3. **提及的页面**：由本来源创建的 [[实体/...]] 和 [[概念/...]] 页面列表

## 日期字段
- `created:` 和 `updated:` 由系统以程序方式填充 — **绝不由 LLM 生成**
- LLM 在提取时可能产生错误日期；系统会在写入后覆盖以确保正确
- 合并时 `created:` 保留（保留较早的值）；`updated:` 始终设为当前日期
- `source_note:`（可选）— 指向原始来源文件的 wiki 链接

## 来源提及格式
"来源提及"条目采用学术脚注式的来源标注，格式为：
- "原文逐字引用（可选译文）" — [[source-name|显示名]]

规则：
- 引用必须**逐字**——绝不改写、概括或翻译掉原文
- 必须带来源 wiki 链接，以便将来页面合并时能把每条引用追溯到出处
- 同一来源的多条引用放在同一块中，用换行分隔

## 内容规则
- mentions_in_source 必须是**逐字**引用——绝不改写或翻译
- 摘要/描述应使用 wiki 输出语言
- 实体/概念名称必须与来源文件的原文语言完全一致
- 所有页面在相关处都必须包含双向链接

## 分类规则
- **type 字段：** entity | concept | source — 页面类别
- **tags 字段：** 存储子类型（entity_type 或 concept_type）
- 实体子类型（type=entity 的有效 tags）：person、organization、project、product、event、place、other
- 概念子类型（type=concept 的有效 tags）：theory、method、field、phenomenon、standard、term、other
- 来源类型：document、conversation、note
- **规则：** tags 只能包含上述对应子类型列表中的值。不在有效列表中的标签会被系统移除。

## 多来源合并规则
- Sources 数组：追加新来源，绝不覆盖
- Aliases：追加别名（译名、缩写），不覆盖已有
- reviewed 标志：为 true 时，保留全部已有内容，只追加确属新增的信息
- 矛盾：双方都保留并标注，加入 ## 矛盾 章节
- NO_NEW_CONTENT：若来源没有带来任何新内容，返回此信号

## 维护策略
- 陈旧阈值：90 天未更新
- 矛盾严重度：warning、conflict、error
- 孤立页：没有来自其他 wiki 页面的入链
- 缺失页：被 [[link]] 引用但不存在
