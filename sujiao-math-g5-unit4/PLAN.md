# 苏教版五年级数学 几何综合课件 - 制作完成

## 单元信息
- **教材**: 苏教版五年级数学
- **单元**: 几何综合（垂线与平行线/三角形与四边形/变换/面积周长）
- **主节点ID**: math-e-area-calculation (Grade 4 geometry)
- **关联节点**: math-e-angle-concept, math-e-triangle-properties, math-e-triangles-quadrilaterals, math-e-symmetry-translation-rotation, math-e-perimeter
- **课时数**: 5 课时
- **格式**: TeachAny v2 分页课件 (每课 14 页)

## 课件结构

| 课时 | 标题 | 课型 | 核心内容 | 互动方式 |
|------|------|------|----------|----------|
| lesson-1 | 垂线与平行线（角的概念与度量） | 概念课 | 角的定义/分类/度量、垂线概念、平行线概念 | GeoGebra 几何画板、SVG 图示 |
| lesson-2 | 三角形（分类、性质、内角和） | 概念课 | 按角/按边分类、内角和=180°推导、稳定性 | Canvas 拖拽顶点动画、GeoGebra |
| lesson-3 | 平行四边形与梯形 | 概念课 | 特征对比、四边形家族关系图、特殊判定 | GeoGebra 几何画板、SVG 嵌套关系图 |
| lesson-4 | 平移、旋转和轴对称 | 概念课 | 三种变换定义与对比、轴对称画图互动 | Canvas 平移/旋转动画、对称轴画格子 |
| lesson-5 | 面积公式推导与综合练习 | 探究课 | 割补法（平行四边形）、拼接法（三角形/梯形）、分层练习 | Canvas 动画推导（3组）、9道分层练习题 |

## 文件清单
```
sujiao-math-g5-unit4/
├── index.html          (3KB) 单元目录页
├── manifest.json             课件清单
├── knowledge-context.json    知识图谱节点信息
├── lesson-1/
│   ├── index.html      (44KB) 垂线与平行线课件
│   └── tts/            4个 mp3 语音文件
├── lesson-2/
│   ├── index.html      (42KB) 三角形课件
│   └── tts/            4个 mp3 语音文件
├── lesson-3/
│   ├── index.html      (39KB) 平行四边形与梯形课件
│   └── tts/            4个 mp3 语音文件
├── lesson-4/
│   ├── index.html      (44KB) 平移旋转轴对称课件
│   └── tts/            4个 mp3 语音文件
└── lesson-5/
    ├── index.html      (47KB) 面积公式推导课件
    └── tts/            4个 mp3 语音文件
```

## 技术特点
- TeachAny v2 分页骨架：滚动吸附 + 播放模式 + 侧边导航
- 小学(elementary)学段视觉：暖白色调 + 各课独立配色方案
- 五件套模块：AI 学伴、TTS 旁白（Edge Neural）、知识图谱、侧边导航、播放工具栏
- 互动元素：
  - GeoGebra iframe 嵌入（L1/L2/L3/L4）
  - Canvas 拖拽三角形验证内角和（L2）
  - Canvas 平移按钮 + 旋转按钮动画（L4）
  - Canvas 轴对称画格子互动（L4）
  - Canvas 割补法/拼接法面积公式动画推导（L5）
  - 9道分层选择题练习（基础3+进阶3+挑战3）（L5）
- SVG 内嵌图示：角分类、四边形家族关系图、公式总表等
- TTS 语音：Edge Neural zh-CN-XiaoyiNeural 生成

## 制作日期
2026-07-13
