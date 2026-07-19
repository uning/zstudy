# -*- coding: utf-8 -*-
import re, json, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "lesson-5", "index.html")
DST_DIR = os.path.join(ROOT, "lesson-6")

# 读取模板
T = open(SRC, encoding='utf-8').read()

# ---------- 各页替换内容 ----------
COVER = """
  <div class="slide-inner">
    <h1>最大公因数和最小公倍数</h1>
    <p class="subtitle">分最多用最大公约数，遇最少用最小公倍数——两个超好用的"最大/最小"工具</p>
    <figure class="ta-standard-figure" style="margin-top:20px">
      <svg style="max-width:680px;width:100%;height:auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" fill="none">
        <defs>
          <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFF5EE"/><stop offset="50%" stop-color="#E8F8F5"/><stop offset="100%" stop-color="#FFF5EE"/>
          </linearGradient>
          <linearGradient id="g6" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FF6B6B"/><stop offset="100%" stop-color="#4ECDC4"/>
          </linearGradient>
        </defs>
        <rect width="720" height="300" rx="20" fill="url(#bg6)"/>
        <rect x="250" y="120" width="220" height="64" rx="14" fill="url(#g6)"/>
        <text x="360" y="160" text-anchor="middle" fill="#fff" font-size="22" font-weight="700" font-family="system-ui,sans-serif">最大公约数 GCD</text>
        <rect x="40" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#FF6B6B" stroke-width="2"/>
        <text x="130" y="80" text-anchor="middle" fill="#FF6B6B" font-size="16" font-family="system-ui,sans-serif">公因数→取最大</text>
        <line x1="220" y1="74" x2="250" y2="150" stroke="#FF6B6B" stroke-width="2"/>
        <rect x="500" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#4ECDC4" stroke-width="2"/>
        <text x="590" y="80" text-anchor="middle" fill="#4ECDC4" font-size="16" font-family="system-ui,sans-serif">公倍数→取最小</text>
        <line x1="500" y1="74" x2="470" y2="150" stroke="#4ECDC4" stroke-width="2"/>
        <text x="360" y="225" text-anchor="middle" fill="#888" font-size="14" font-family="system-ui,sans-serif">分最多→GCD ｜ 遇最少→LCM</text>
        <text x="360" y="255" text-anchor="middle" fill="#FF6B6B" font-size="15" font-weight="600" font-family="system-ui,sans-serif">🍪分物 · 🧱铺砖 · 📚相遇</text>
      </svg>
    </figure>
  </div>
"""

ANCHOR = """
  <div class="slide-inner">
    <div class="card">
      <div class="section-header">
        <span class="phase-tag" data-variant="warn">Problem Anchor</span>
        <h2>今天想解决什么问题？</h2>
      </div>
      <p style="color:var(--text-secondary);line-height:1.7">选一个你关心的问题，后面的内容会围绕它展开。</p>
      <div style="display:flex;flex-direction:column;gap:10px;margin-top:10px">
        <div class="anchor-card">🍪 12块饼干和18颗糖，平均分给小朋友，<b>最多</b>能分给几个人，每人得几块？</div>
        <div class="anchor-card">🧱 用长6dm、宽4dm的地砖铺正方形地面，边长<b>最小</b>是多少才能正好铺满？</div>
        <div class="anchor-card">📚 甲每4天、乙每6天去图书馆，他们<b>最少</b>几天后又同一天相遇？</div>
      </div>
    </div>
  </div>
"""

OBJECTIVES = """
  <div class="slide-inner">
    <div class="card">
      <div class="section-header">
        <span class="phase-tag" data-variant="success">Objectives</span>
        <h2>学习目标</h2>
      </div>
      <ul class="obj-list">
        <li>理解 <b>公因数</b> 与 <b>最大公因数</b>，会求两个数的最大公约数（GCD）</li>
        <li>理解 <b>公倍数</b> 与 <b>最小公倍数</b>，会求两个数的最小公倍数（LCM）</li>
        <li>掌握 <b>列举法</b> 和 <b>短除法</b> 两种求法</li>
        <li>能用 GCD / LCM 解决 <b>分物、铺砖、周期相遇</b> 等实际问题</li>
      </ul>
    </div>
  </div>
"""

PRETEST = """
  <div class="slide-inner">
    <div class="card">
      <div class="section-header">
        <span class="phase-tag" data-variant="warn">Pre-Test</span>
        <h2>先来试试看 👀</h2>
      </div>
      <p style="color:var(--muted);margin:0 0 12px">别担心，答错了也没关系，试试看！</p>
      <div style="margin-bottom:16px">
        <p style="font-weight:600;margin-bottom:6px">Q1: 12和18的公因数有哪些？</p>
        <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">A. 1,2,3</button>
        <button class="choice" data-quiz="pretest-q1" data-answer="correct" onclick="checkQuizBtn(this)">B. 1,2,3,6</button>
        <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 12,18</button>
        <p class="result" id="pretest-q1-fb" style="display:none;margin-top:8px"></p>
      </div>
      <div style="margin-bottom:16px">
        <p style="font-weight:600;margin-bottom:6px">Q2: 6和4的最小公倍数，下面哪项正确？</p>
        <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 2</button>
        <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 12不对，是24</button>
        <button class="choice" data-quiz="pretest-q2" data-answer="correct" onclick="checkQuizBtn(this)">C. 12</button>
        <p class="result" id="pretest-q2-fb" style="display:none;margin-top:8px"></p>
      </div>
      <div style="margin-bottom:8px">
        <p style="font-weight:600;margin-bottom:6px">Q3: 公因数里最大的那个，叫什么？</p>
        <button class="choice" data-quiz="pretest-q3" data-answer="correct" onclick="checkQuizBtn(this)">A. 最大公因数</button>
        <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 最小公倍数</button>
        <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 公约数</button>
        <p class="result" id="pretest-q3-fb" style="display:none;margin-top:8px"></p>
      </div>
    </div>
  </div>
"""

C1 = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 1</span><h2>先复习：因数和倍数 🔍</h2></div>
      <p style="line-height:1.7;color:var(--text-secondary)">如果 <b>a ÷ b</b> 能整除（没有余数），就说 <b>b 是 a 的因数</b>，<b>a 是 b 的倍数</b>。</p>
      <div class="example-box">
        <p><b>以 12 为例：</b></p>
        <p>12 ÷ 1 = 12，12 ÷ 2 = 6，12 ÷ 3 = 4，12 ÷ 4 = 3，12 ÷ 6 = 2，12 ÷ 12 = 1</p>
        <p>所以 <b>12 的因数</b>有：1, 2, 3, 4, 6, 12</p>
      </div>
      <p style="margin-top:10px;color:var(--text-secondary)">再看 <b>18 的因数</b>：1, 2, 3, 6, 9, 18</p>
      <p style="color:var(--brand);font-weight:600">👉 两个数<b>共同拥有</b>的因数，就是"公因数"。</p>
    </div>
  </div>
"""

C2 = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 2</span><h2>最大公约数 GCD（分物问题）🎁</h2></div>
      <p style="line-height:1.7;color:var(--text-secondary)"><b>公因数</b>里<b>最大</b>的那一个，叫 <b>最大公约数（GCD）</b>，也叫最大公因数。</p>
      <div class="example-box">
        <p><b>12 的因数</b>：1, 2, 3, 4, 6, 12</p>
        <p><b>18 的因数</b>：1, 2, 3, 6, 9, 18</p>
        <p><b>公因数</b>：1, 2, 3, 6</p>
        <p style="color:var(--brand);font-weight:700">→ 最大公约数 GCD(12,18) = <b>6</b></p>
      </div>
      <p style="margin-top:10px">🍪 <b>回到分物问题</b>：12块饼干、18颗糖最多平均分给 <b>6</b> 个小朋友（每人2块饼干+3颗糖），正是 GCD！</p>
      <p style="margin-top:8px;color:var(--muted);font-size:13px">📌 短除法：用公有的质因数同时除，直到互质，把左边除数相乘 = GCD。</p>
    </div>
  </div>
"""

C3 = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 3</span><h2>最小公倍数 LCM（铺砖问题）🧱</h2></div>
      <p style="line-height:1.7;color:var(--text-secondary)">一个数<b>所有倍数</b>里，两个数<b>共同</b>的倍数叫 <b>公倍数</b>；其中<b>最小</b>的，叫 <b>最小公倍数（LCM）</b>。</p>
      <div class="example-box">
        <p><b>6 的倍数</b>：6, 12, 18, 24, 30…</p>
        <p><b>4 的倍数</b>：4, 8, 12, 16, 20, 24…</p>
        <p><b>公倍数</b>：12, 24…</p>
        <p style="color:var(--brand);font-weight:700">→ 最小公倍数 LCM(6,4) = <b>12</b></p>
      </div>
      <p style="margin-top:10px">🧱 <b>回到铺砖</b>：6dm×4dm 地砖铺正方形，最小边长就是 LCM(6,4)=<b>12dm</b>（刚好用2×3块）。</p>
      <p style="margin-top:8px;color:var(--muted);font-size:13px">📌 两数互质时 LCM = 两数相乘；含倍数关系时 LCM = 较大数。</p>
    </div>
  </div>
"""

C4 = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 4</span><h2>怎么选？互质与实战 🚀</h2></div>
      <div class="example-box">
        <p><b>① 何时用 GCD？</b>——"最多分几份 / 最大边长 / 同时取完"</p>
        <p>· 分物(饼干糖)、截成等长小段、约分</p>
        <p><b>② 何时用 LCM？</b>——"最小几时后再次同时 / 最小铺满边长"</p>
        <p>· 周期相遇、铺正方形、通分</p>
        <p><b>③ 互质</b>：公因数只有1（如8和9）→ GCD=1，LCM=两数乘积</p>
      </div>
      <p style="margin-top:10px;color:var(--brand);font-weight:600">📚 相遇问题：甲每4天、乙每6天去图书馆 → 最少 LCM(4,6)=12 天后再同天相遇。</p>
    </div>
  </div>
"""

SCAFFOLD = """
  <div class="slide-inner">
    <div class="card">
      <div class="section-header"><span class="phase-tag" data-variant="success">Scaffold</span><h2>三步练习 ✍️</h2></div>
      <div style="margin-bottom:14px">
        <p style="font-weight:600">1 列举填空：求 GCD(15, 20)</p>
        <p style="color:var(--muted);font-size:14px">15的因数：1,3,5,15 ｜ 20的因数：1,2,4,5,10,20 ｜ 公因数：1,5 ｜ GCD = <b>5</b></p>
      </div>
      <div style="margin-bottom:14px">
        <p style="font-weight:600">2 列举填空：求 LCM(3, 5)（互质）</p>
        <p style="color:var(--muted);font-size:14px">3的倍数：3,6,9,12,15… ｜ 5的倍数：5,10,15… ｜ LCM = <b>15</b>（=3×5）</p>
      </div>
      <div style="margin-bottom:8px">
        <p style="font-weight:600">3 判断：两个数互质，它们的 GCD 和 LCM 分别是？</p>
        <p style="color:var(--muted);font-size:14px">GCD = <b>1</b>，LCM = <b>两数乘积</b></p>
      </div>
    </div>
  </div>
"""

CONCEPTTEST = """
  <div class="slide-inner">
    <div class="card">
      <div class="section-header"><span class="phase-tag" data-variant="warn">ConceptTest</span><h2>概念过关测试 🎯</h2></div>
      <div style="margin-bottom:14px">
        <p style="font-weight:600">第1题：GCD(8, 12) = ?</p>
        <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">A. 2</button>
        <button class="choice" data-quiz="ct-q1" data-answer="correct" onclick="checkQuizBtn(this)">B. 4</button>
        <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 8</button>
        <p class="result" id="ct-q1-fb" style="display:none;margin-top:8px"></p>
      </div>
      <div style="margin-bottom:14px">
        <p style="font-weight:600">第2题：LCM(2, 3) = ?（互质）</p>
        <button class="choice" data-quiz="ct-q2" data-answer="correct" onclick="checkQuizBtn(this)">A. 6</button>
        <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 1</button>
        <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 5</button>
        <p class="result" id="ct-q2-fb" style="display:none;margin-top:8px"></p>
      </div>
      <div style="margin-bottom:8px">
        <p style="font-weight:600">第3题：下列哪个问题用"最大公约数"？</p>
        <button class="choice" data-quiz="ct-q3" data-answer="correct" onclick="checkQuizBtn(this)">A. 把24块糖分给小朋友，最多几人正好分完</button>
        <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 两人几分钟后再次同时出发</button>
        <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 铺正方形最小边长</button>
        <p class="result" id="ct-q3-fb" style="display:none;margin-top:8px"></p>
      </div>
    </div>
  </div>
"""

INTERACTIVE = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="success">Interactive</span><h2>分类大挑战 🎮</h2></div>
      <p style="color:var(--muted);margin:0 0 8px">下面这些数，哪些既是 12 的因数、又是 18 的因数（公因数）？</p>
      <p style="color:var(--muted);margin:0 0 16px;font-size:13px">把它们拖到正确的分类里！（提示：公因数 = 1,2,3,6）</p>
      <div class="drop-zones">
        <div class="drop-zone" id="zone-match" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>✅ 公因数（12和18共有）</h4>
          <div id="zone-match-items" style="min-height:20px"></div>
        </div>
        <div class="drop-zone" id="zone-nomatch" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>❌ 不是公因数</h4>
          <div id="zone-nomatch-items" style="min-height:20px"></div>
        </div>
      </div>
      <div class="drop-items" id="drag-items">
        <div class="drag-item" draggable="true" data-correct="match" data-id="d1">2</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d2">3</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d3">6</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d4">1</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d5">9</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d6">12</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d7">4</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d8">18</div>
      </div>
      <div id="drag-score" style="text-align:center;margin-top:12px;font-weight:700;font-size:16px;color:var(--brand)"></div>
      <button class="check-btn" onclick="resetDragGame()" style="margin:8px auto;display:block">🔄 再来一次</button>
    </div>
  </div>
"""

POSTTEST = """
  <div class="slide-inner">
    <div class="card">
      <div class="section-header"><span class="phase-tag" data-variant="success">Post-Test</span><h2>学后检测 ✅</h2></div>
      <div style="margin-bottom:14px">
        <p style="font-weight:600">Q1: 把一根绳子截成等长小段（无剩余），要最长，用哪个？</p>
        <button class="choice" data-quiz="post-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 最大公约数</button>
        <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 最小公倍数</button>
        <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 平均数</button>
        <p class="result" id="post-q1-fb" style="display:none;margin-top:8px"></p>
      </div>
      <div style="margin-bottom:14px">
        <p style="font-weight:600">Q2: GCD(9, 15) = ?</p>
        <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 3不对，是1</button>
        <button class="choice" data-quiz="post-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 3</button>
        <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 45</button>
        <p class="result" id="post-q2-fb" style="display:none;margin-top:8px"></p>
      </div>
      <div style="margin-bottom:8px">
        <p style="font-weight:600">Q3: LCM(8, 9) = ?（互质）</p>
        <button class="choice" data-quiz="post-q3" data-answer="correct" onclick="checkQuizBtn(this)">A. 72</button>
        <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 1</button>
        <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 17</button>
        <p class="result" id="post-q3-fb" style="display:none;margin-top:8px"></p>
      </div>
    </div>
  </div>
"""

SUMMARY = """
  <div class="slide-inner">
    <div class="card">
      <div class="section-header"><span class="phase-tag" data-variant="success">Summary</span><h2>课堂小结 📝</h2></div>
      <div class="summary-list">
        <div class="summary-item"><b>1 公因数 / 最大公约数</b>：共同因数里最大的 = GCD，用来解决"最多分几份"。</div>
        <div class="summary-item"><b>2 公倍数 / 最小公倍数</b>：共同倍数里最小的 = LCM，用来解决"最小几时后再相遇"。</div>
        <div class="summary-item"><b>3 两种求法</b>：列举法（列因数/倍数找公共）、短除法（除到互质）。</div>
        <div class="summary-item"><b>4 互质</b>：公因数只有1，GCD=1，LCM=两数乘积。</div>
      </div>
      <p style="margin-top:12px;color:var(--brand);font-weight:600">🎯 一句话：分最多→最大公约数；遇最少→最小公倍数。</p>
    </div>
  </div>
"""

# 占位（将被注入引擎替换）
GRAPH = "<placeholder-kg/>"
TUTOR = "<placeholder-tutor/>"

# 需要替换的 tsh -> 新 inner
REPL = {
    "封面": COVER, "问题锚点": ANCHOR, "学习目标": OBJECTIVES, "前测": PRETEST,
    "概念1 - 什么情况用列举": C1, "概念2 - 有序列举": C2, "概念3 - 表格画图辅助": C3,
    "概念4 - 从列举中找最值": C4, "脚手架练习": SCAFFOLD, "概念诊断": CONCEPTTEST,
    "互动 - 列举分类": INTERACTIVE, "后测": POSTTEST, "课堂小结": SUMMARY,
}

def replace_section(html, tsh, new_inner):
    pat = re.compile(r'<section([^>]*data-tsh="%s"[^>]*)>.*?</section>' % re.escape(tsh), re.S)
    return pat.sub(lambda m: '<section'+m.group(1)+'>'+new_inner+'</section>', html, count=1)

out = T
for tsh, inner in REPL.items():
    before = out
    out = replace_section(out, tsh, inner)
    if out == before:
        print("⚠️ 未匹配:", tsh)

# 改 H1 标题已在 COVER 中处理

# 替换封面 hero 短语（列举策略→GCD/LCM）已在 COVER 处理；删原 hero? COVER 无 img
# 替换 AI学伴 / 知识图谱占位
TUTOR_SECTION = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="purple">AI Tutor</span><h2>AI 学伴 🤖</h2></div>
      <div class="tutor-app">
        <div class="tutor-chat" id="tutorChat"></div>
        <div class="tutor-chips" id="tutorChips"></div>
        <div class="tutor-input">
          <input id="tutorInput" placeholder="问我任何关于本课的问题…" />
          <button id="tutorAsk">问</button>
          <button id="tutorQuiz">🎲 随机考我</button>
        </div>
      </div>
    </div>
  </div>
"""
GRAPH_SECTION = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="purple">Knowledge Graph</span><h2>知识图谱 🗺️</h2></div>
      <p style="color:var(--muted);margin:0 0 4px">点击任意节点查看讲解，关联节点会自动高亮：</p>
      <div class="kg-wrap">
        <div class="kg-svg" id="kgSvg"></div>
        <div class="kg-info" id="kgInfo"><p style="color:var(--muted);margin:0">👆 选择一个节点查看详情</p></div>
      </div>
    </div>
  </div>
"""
out = out.replace(TUTOR, TUTOR_SECTION)
out = out.replace(GRAPH, GRAPH_SECTION)

DATA = {
 "faq": [
   {"q":"什么是最大公约数？","keys":["最大公约数","最大公因数","GCD","公因数","最大"],
    "a":"两个数公因数里最大的那个，叫最大公约数(GCD)。比如12和18的公因数有1,2,3,6，最大是6，所以GCD(12,18)=6。分物、截绳、约分都用它。"},
   {"q":"什么是最小公倍数？","keys":["最小公倍数","LCM","公倍数","最小"],
    "a":"两个数公倍数里最小的那个，叫最小公倍数(LCM)。比如6和4的公倍数有12,24…，最小是12，所以LCM(6,4)=12。铺砖、周期相遇、通分用它。"},
   {"q":"怎么求最大公约数？","keys":["求","算","怎么","方法","列举","短除"],
    "a":"两种方法：①列举法——分别列出两个数的因数，找公共的再取最大；②短除法——用公有的质因数同时除到互质，左边除数相乘就是GCD。"},
   {"q":"怎么求最小公倍数？","keys":["求","算","怎么","方法","列举","短除","倍数"],
    "a":"①列举法——列倍数找第一个公共的；②短除法——公有质因数和各自独有质因数全相乘=LCM；③互质时直接两数相乘；含倍数关系时取较大数。"},
   {"q":"什么是互质？互质时怎么算？","keys":["互质","互素","乘积","1"],
    "a":"公因数只有1的两个数叫互质(如8和9)。互质时GCD=1，LCM=两数乘积。例如LCM(8,9)=72。"},
   {"q":"什么时候用最大公约数，什么时候用最小公倍数？","keys":["区别","用","选","分","相遇","铺"],
    "a":"要「分最多/最长无剩余/最大边长」用GCD；要「最少几天后再相遇/最小铺满边长」用LCM。口诀：分最多→GCD，遇最少→LCM。"}
 ],
 "quiz": [
   {"q":"GCD(10, 15) = ? 即最大公因数是？","options":["5","1","30"],"answer":0,"exp":"10因数1,2,5,10；15因数1,3,5,15；公因数1,5，最大是5。"},
   {"q":"LCM(4, 10) = ?","options":["20","40","2"],"answer":0,"exp":"4倍数4,8,12,16,20…；10倍数10,20…；最小公共20。"},
   {"q":"两数互质时 GCD 是？","options":["1","两数乘积","较大数"],"answer":0,"exp":"互质=公因数只有1，所以GCD=1。"}
 ],
 "graph": {"w":720,"h":360,"nodes":[
   {"id":"n_gcd","label":"最大公约数","x":285,"y":150,"w":150,"h":54,"color":"#FF6B6B",
    "desc":"公因数里最大的，解决「分最多/最长无剩余」。GCD(12,18)=6。","links":["n_fac","n_lcm","n_app","n_short"]},
   {"id":"n_fac","label":"因数与公因数","x":40,"y":80,"w":140,"h":44,"color":"#a78bfa",
    "desc":"两数共同拥有的因数叫公因数；最大那个是GCD。","links":["n_gcd"]},
   {"id":"n_lcm","label":"最小公倍数","x":40,"y":240,"w":140,"h":44,"color":"#4ECDC4",
    "desc":"公倍数里最小的，解决「最少几天后再相遇」。LCM(6,4)=12。","links":["n_gcd"]},
   {"id":"n_app","label":"分物·铺砖·相遇","x":550,"y":80,"w":150,"h":44,"color":"#f59e0b",
    "desc":"GCD用于分最多/截最长；LCM用于铺最小/周期相遇。","links":["n_gcd"]},
   {"id":"n_short","label":"短除法","x":550,"y":240,"w":130,"h":44,"color":"#06b6d4",
    "desc":"用公有质因数除到互质，左乘=GCD，全乘=LCM。","links":["n_gcd"]}
 ]}
}

ENGINE = r"""
<script>
const COURSE_DATA = __DATA__;
(function(){
  const NS='http://www.w3.org/2000/svg';
  function el(t,a){const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);return e;}
  function findAnswer(text){
    text=(text||'').trim(); if(!text) return null;
    let best=null,bs=0; const low=text.toLowerCase();
    for(const f of COURSE_DATA.faq){
      let s=0; const hay=(f.q+' '+(f.keys||[]).join(' ')).toLowerCase();
      if(f.q && low.includes(f.q.toLowerCase().slice(0,3))) s+=3;
      for(const k of (f.keys||[])){ if(text.includes(k)) s+=2; }
      for(const ch of new Set(text.split(''))){ if(ch.trim() && f.q.includes(ch)) s+=0.15; }
      if(s>bs){bs=s;best=f;}
    }
    return bs>=1?best:null;
  }
  function bubble(role,text){
    const c=document.getElementById('tutorChat'); if(!c)return;
    const d=document.createElement('div'); d.className='tutor-bubble '+(role==='bot'?'bot':'user');
    d.textContent=text; c.appendChild(d); c.scrollTop=c.scrollHeight;
  }
  function showFaq(f){ bubble('user',f.q); bubble('bot',f.a); }
  function ask(){
    const inp=document.getElementById('tutorInput'); const v=inp.value.trim(); if(!v)return; inp.value='';
    const f=findAnswer(v); bubble('user',v);
    if(f) bubble('bot',f.a);
    else bubble('bot','这个问题我还在学习～你可以先点下面的常见问题，或换个说法问我 😊');
  }
  function quiz(){
    const c=document.getElementById('tutorChips'); if(!c||!COURSE_DATA.quiz)return;
    const q=COURSE_DATA.quiz[Math.floor(Math.random()*COURSE_DATA.quiz.length)];
    bubble('bot','🎲 考考你：'+q.q);
    q.options.forEach((opt,i)=>{
      const b=document.createElement('button'); b.className='tutor-chip'; b.textContent=opt;
      b.onclick=()=>{ if(i===q.answer){ bubble('user',opt); bubble('bot','✅ 答对啦！'+q.exp); }
        else { bubble('user',opt); bubble('bot','❌ 再想想～正确答案：'+q.options[q.answer]+'。'+q.exp); } };
      c.appendChild(b);
    });
  }
  function renderChips(){
    const c=document.getElementById('tutorChips'); if(!c)return; c.innerHTML='';
    COURSE_DATA.faq.forEach(f=>{ const b=document.createElement('button'); b.className='tutor-chip'; b.textContent=f.q; b.onclick=()=>showFaq(f); c.appendChild(b); });
  }
  function renderGraph(){
    const wrap=document.getElementById('kgSvg'); if(!wrap||!COURSE_DATA.graph)return;
    const g=COURSE_DATA.graph, W=g.w||720, H=g.h||360;
    const svg=el('svg',{viewBox:'0 0 '+W+' '+H,class:'kg-canvas',width:'100%'});
    g.nodes.forEach(n=>{(n.links||[]).forEach(t=>{ const m=g.nodes.find(x=>x.id===t); if(!m)return;
      const ln=el('line',{x1:n.x+n.w/2,y1:n.y+n.h/2,x2:m.x+m.w/2,y2:m.y+m.h/2,stroke:'#e2d5cf','stroke-width':2,class:'kg-edge'});
      ln.dataset.a=n.id; ln.dataset.b=t; svg.appendChild(ln); });});
    g.nodes.forEach(n=>{
      const grp=el('g',{class:'kg-node',style:'cursor:pointer'}); grp.dataset.id=n.id;
      const r=el('rect',{x:n.x,y:n.y,width:n.w,height:n.h,rx:10,fill:'#fff',stroke:n.color||'#FF6B6B','stroke-width':2});
      r.dataset.id=n.id;
      const t=el('text',{x:n.x+n.w/2,y:n.y+n.h/2+5,'text-anchor':'middle','font-size':13,fill:'#333','font-family':'system-ui,sans-serif'});
      t.textContent=n.label; grp.appendChild(r); grp.appendChild(t);
      grp.addEventListener('click',()=>selectNode(n.id)); svg.appendChild(grp);
    });
    wrap.innerHTML=''; wrap.appendChild(svg);
  }
  function selectNode(id){
    const g=COURSE_DATA.graph; const n=g.nodes.find(x=>x.id===id); if(!n)return;
    document.querySelectorAll('.kg-edge').forEach(e=>{ const on=(e.dataset.a===id||e.dataset.b===id); e.setAttribute('stroke',on?'#FF6B6B':'#eee'); e.setAttribute('stroke-width',on?3:2); });
    document.querySelectorAll('.kg-node').forEach(grp=>{ const on=(grp.dataset.id===id)||(n.links||[]).includes(grp.dataset.id);
      const r=grp.querySelector('rect'); r.setAttribute('stroke',on?'#FF6B6B':'#ccc'); r.setAttribute('opacity',on?1:0.45); });
    const info=document.getElementById('kgInfo'); if(!info)return;
    let html='<h3 style="color:#FF6B6B;margin:0 0 6px">'+n.label+'</h3><p style="margin:0 0 8px;color:#444;line-height:1.6">'+n.desc+'</p>';
    if(n.links&&n.links.length){ html+='<p style="font-size:13px;color:#888">关联：'+n.links.map(l=>{const m=g.nodes.find(x=>x.id===l);return m?m.label:l;}).join('、')+'</p>'; }
    info.innerHTML=html;
  }
  renderChips();
  const askBtn=document.getElementById('tutorAsk'); if(askBtn) askBtn.onclick=ask;
  const inp=document.getElementById('tutorInput'); if(inp) inp.addEventListener('keydown',e=>{ if(e.key==='Enter') ask(); });
  const qz=document.getElementById('tutorQuiz'); if(qz) qz.onclick=quiz;
  renderGraph();
  const c0=document.getElementById('tutorChat'); if(c0) bubble('bot','我是本课 AI 学伴 🤖 点下面的常见问题，或输入你的问题，也可以点「🎲随机考我」！');
})();
</script>
"""

STYLE = """
<style>
.tutor-app{display:flex;flex-direction:column;gap:12px}
.tutor-chat{max-height:300px;overflow-y:auto;display:flex;flex-direction:column;gap:8px;padding:10px;background:#fff8f0;border-radius:14px}
.tutor-bubble{max-width:88%;padding:10px 14px;border-radius:14px;font-size:14px;line-height:1.55;white-space:pre-wrap}
.tutor-bubble.user{align-self:flex-end;background:#FF6B6B;color:#fff;border-bottom-right-radius:4px}
.tutor-bubble.bot{align-self:flex-start;background:#fff;color:#333;border:1px solid #ffe0d0;border-bottom-left-radius:4px}
.tutor-chips{display:flex;flex-wrap:wrap;gap:8px}
.tutor-chip{background:#fff;border:1px solid #ffd0c0;color:#FF6B6B;padding:8px 12px;border-radius:20px;font-size:13px;cursor:pointer;transition:.15s}
.tutor-chip:hover{background:#fff0ea}
.tutor-input{display:flex;gap:8px;flex-wrap:wrap}
.tutor-input input{flex:1;min-width:150px;padding:10px 14px;border:1px solid #ffd0c0;border-radius:12px;font-size:14px}
.tutor-input button{padding:10px 16px;border:none;border-radius:12px;background:#FF6B6B;color:#fff;font-size:14px;cursor:pointer}
.tutor-input button#tutorQuiz{background:#4ECDC4}
.kg-wrap{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-start;margin-top:8px}
.kg-svg{flex:1;min-width:300px}
.kg-canvas{width:100%;height:auto;background:#fffdfb;border-radius:14px}
.kg-node rect{transition:.15s}
.kg-node:hover rect{filter:brightness(.97)}
.kg-info{flex:1;min-width:240px;background:#fff8f0;border-radius:14px;padding:16px;min-height:120px}
</style>
"""

out = out.replace("</head>", STYLE + "</head>", 1)
engine = ENGINE.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
out = out.replace("</body>", engine + "</body>", 1)

# 统一用语：苏教版标准"最大公因数"（保留GCD缩写）
out = out.replace("最大公约数", "最大公因数")

# 写文件
os.makedirs(DST_DIR, exist_ok=True)
open(os.path.join(DST_DIR,"index.html"),'w',encoding='utf-8').write(out)
print("✅ lesson-6 生成完成, 大小≈%dKB, 页型数=%d" % (len(out.encode('utf-8'))//1024, out.count('class="slide-page"')))
