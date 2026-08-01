# 走进信息世界 · 课件设计文档

## 基本信息

- **course_id**: `info-e-online-basics`
- **node_id**: `it-e-online-experience`（小学信息科技·在线体验与信息获取）
- **学科**: info-tech（信息科技）
- **年级**: 小学三年级（G3）
- **课型**: new-concept（新授课）
- **版本**: 1.0.0
- **日期**: 2026-08-01

## Phase 1 输出合同

### 学习者画像
- **学段/年级**: 小学三年级
- **已学前置**: 无（本课为信息科技起点课）
- **常见卡点**: 对"信息"概念抽象难理解；分不清古代/现代信息工具；缺乏信息安全意识
- **本课默认难度**: 基础

### ABT 三句话
- **And**: 学生每天都在用手机、看电视、听广播，已经接触过大量信息工具
- **But**: 但不知道"信息"到底是什么，也不清楚信息是怎么传到设备上的，更不知道网上哪些信息不能随便告诉别人
- **Therefore**: 所以本课要认识信息的本质，了解信息的传递方式，体验在线工具，并学会保护个人信息

### 问题锚点
1. 信息到底是什么？
2. 信息是怎么"跑"到手机上的？
3. 我的信息会被别人看到吗？

### 主交互
- **类型**: SVG 拖拽/匹配 + 步骤排序
- **学生操作**: 将信息工具拖到"古代"或"现代"类别；将在线搜索步骤按正确顺序排列
- **系统反馈**: 即时判断对错，给出鼓励或提示
- **学到什么**: 信息工具的时代差异；在线查找信息的标准流程

### Section 顺序
1. hero（封面）
2. problem-anchor（问题锚点）
3. objectives（学习目标）
4. concept-what-is-info（什么是信息）
5. concept-info-sources（信息来源·古今对比）
6. interaction-drag-classify（互动：工具分类）
7. concept-info-transfer（信息传递原理）
8. concept-online-tools（在线工具体验）
9. interaction-sort-steps（互动：搜索步骤排序）
10. concept-security（信息安全）
11. quiz（练习）
12. ai-tutor（AI 学伴）
13. summary（课堂总结）
14. knowledge-graph（知识图谱）

### Bloom 覆盖
- 记忆：说出信息的定义
- 理解：举例说明生活中的信息
- 应用：将工具分类、按步骤操作
- 分析：判断信息安全行为的对错

### ConcepTest 位置
- Slide 11：2 道选择题（概念辨析 + 安全判断）

### 自适应四路分支
- review-prereq: 无前置，直接进入
- scaffold: 拖拽/排序错误时显示提示
- normal: 标准流程
- challenge: 鼓励学生提出自己的信息问题并搜索答案

## 页面清单（14 页）

| 页码 | 类型 | data-tts | 内容 |
|------|------|----------|------|
| 1 | cover | s01 | 封面：走进信息世界 |
| 2 | interactive | s02 | 问题锚点：选择感兴趣的问题 |
| 3 | objectives | s03 | 学习目标 |
| 4 | concept | s04 | 什么是信息 |
| 5 | concept | s05 | 信息来源：古今对比 |
| 6 | interactive | s06 | 互动：信息工具分类（拖拽） |
| 7 | concept | s07 | 信息传递原理（发送者→通道→接收者） |
| 8 | concept | s08 | 在线工具体验 |
| 9 | interactive | s09 | 互动：搜索步骤排序 |
| 10 | concept | s10 | 信息安全小卫士 |
| 11 | quiz | s11 | 练一练（2 题） |
| 12 | concept | s12 | AI 学伴 |
| 13 | summary | s13 | 课堂总结 |
| 14 | summary | s14 | 知识图谱 |

## TTS 规划

共 14 段，每段对应一页，使用 `zh-CN-XiaoyiNeural`，`--rate=-8%`。

## 视觉规范

- **学段**: `teachany-elementary`
- **背景**: 暖白 `#fffbf0`
- **主色**: 紫 `#8b5cf6` → 青 `#06b6d4` → 橙 `#f59e0b`
- **卡片**: 白底圆角，柔和阴影
- **互动**: 拖拽分类 + 步骤排序

## 依赖与资源

- CSS/JS: `https://www.teachany.cn/assets/scripts/`（CDN）
- TTS: edge-tts CLI
- Hero 图: 内嵌 SVG（信息流动示意图）
- 知识图谱: `data-teachany-kg="it-e-online-experience"`

## 发布路径

- 本地: `/Users/playcrab/WorkBuddy/Claw/community/info-e-online-basics/`
- zstudy: `https://uning.github.io/zstudy/community/info-e-online-basics/`
- teachany.cn: 待用户确认后走 `hang_tree.py publish`
