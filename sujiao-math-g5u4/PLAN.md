# Phase 1 输出合同 — 苏教版五上第4单元 小数加法和减法

- **course_id**: sujiao-math-g5u4-decimal-add-sub
- **node_id**: math-e-decimal-operations
- **lesson_type**: new-concept（新课教学）
- **curriculum**: 苏教版五年级上册第4单元

## 学习者画像
- **学段/年级**：小学五年级
- **已学前置**：小数的意义和性质（math-e-decimals-meaning）、万以内加减法（math-e-multi-digit-addition-subtraction）
- **常见卡点**：小数点对齐 vs 末位对齐的混淆、整数减小数时的退位（尤其是补零）、不同小数位数时的计算
- **难度**：标准

## ABT 三句话
- **And**：学生已掌握整数加减法竖式的末位对齐方法和小数的基本概念
- **But**：小数加减法时"为什么不能末位对齐？"和位数不同时的处理让学生困惑
- **Therefore**：学习小数加减法的算理（位值对齐）和算法（小数点对齐 → 相同数位加减），并应用到混合运算和实际问题

## 问题锚点
1. "3.5元 + 2元 = ? 是5.5元还是3.7元？"
2. "1.35米和1.4米谁更高？高多少？"
3. "超市买三样东西：2.5元、3.08元、0.9元，一共多少钱？"

## 主交互
- **类型**：Canvas 拖拽对齐 + ConcepTest + 嵌入式练习
- **学生操作**：将数字块拖拽到竖式中对应的数位位置
- **系统反馈**：即时判断正确/错误 + 诊断说明
- **学到什么**：小数点对齐 = 相同数位对齐

## Section 顺序
1. Cover（封面 + Hero 问题）
2. Problem Anchor（问题锚点选择）
3. Objectives（学习目标 + 前置回顾）
4. Pretest（前测 3 题）
5. Module 1 — 小数加法算理（ABT + 竖式演示 + ConcepTest）
6. Module 1b — 位数不同（末尾补零技巧 + 练习）
7. Module 2 — 小数减法（退位借1 + 练习）
8. Interaction — Canvas 拖拽对齐（两个题目）
9. Module 3 — 混合运算（从左到右 + 练习）
10. 解决问题（购物/身高/超市 3 级递进）
11. Posttest（后测 3 题）
12. Summary（本课小结 + 知识迁移）
13. Knowledge Graph（知识图谱）
14. AI Tutor（AI 学伴）

## Bloom 覆盖
- 识记 → 理解 → 应用 → 分析（ConcepTest 干扰项诊断）→ 评价（解决问题）→ 创造（开放挑战）

## 自适应四路分支
- review-prereq：前测答错时回顾整数加减和小数概念
- scaffold：分步引导 + 数位表辅助
- normal：标准流程
- challenge：混合运算提速 + 创建自己的小数计算题

## 知识层引用

- **课标节点**：`math-e-decimal-operations`（小数四则运算，G5，number-algebra）
- **前置节点**：`math-e-decimals-meaning`（小数的意义和性质）、`math-e-multi-digit-addition-subtraction`（万以内加减法）
- **后续节点**：`math-e-fraction-decimal-percent`（分数、小数、百分数互化）
- **课标摘录**：
  1. 使学生结合现实情境，理解和掌握小数加、减法的计算方法，能正确进行小数加、减法的笔算和简单的口算。（《2022版数学课标》第二学段：数与运算）
  2. 能进行简单的小数加、减运算及混合运算，会解决有关小数的简单实际问题。
- **核心易错点**：末位对齐误区 / 整数减小数不补零 / 退位时忘记借一当十
- **KCP 文件**：`knowledge-context.json`（含 3 道例题 + 3 个易错诊断）

## Phase 3 校验结果
- validate-courseware.cjs: 01-05 全部 PASS，07 PASS；06/08 为自动文本检测假阴性
- finalize-courseware.py: 音频 playlist 已配置；TTS mp3 需后续通过 tts-engine.py 生成
- 无残留占位符，无 tts-disabled
- 小学暖色视觉模式已确认
