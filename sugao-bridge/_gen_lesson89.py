# -*- coding: utf-8 -*-
"""生成 lesson-8 / lesson-9：以干净的 lesson-7 为模板，只替换 15 个 section 的 inner + 唯一 COURSE_DATA。
绝不改动任何 <script> 块，从根避免重复 const 声明 bug。"""
import re, json, os

TMPL = "lesson-7/index.html"

def build(OUT, SECTIONS, COURSE_DATA, title_tag):
    h = open(TMPL, encoding="utf-8").read()
    def repl_sec(m):
        title = m.group(2)
        if title not in SECTIONS:
            return m.group(0)
        return f'<section{m.group(1)}>\n{SECTIONS[title]}\n  </section>'
    h = re.sub(r'<section([^>]*data-tsh="([^"]+)"[^>]*)>(.*?)</section>', repl_sec, h, flags=re.S)
    cd_json = json.dumps(COURSE_DATA, ensure_ascii=False)
    h = re.sub(r'const COURSE_DATA = \{.*?\};', f'const COURSE_DATA = {cd_json};', h, count=1, flags=re.S)
    h = h.replace('4升5衔接 · 五下因数和倍数', title_tag)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(h)
    hh = open(OUT, encoding="utf-8").read()
    n_s = len(re.findall(r'<script', hh)); n_c = hh.count('const COURSE_DATA')
    assert n_s == 2 and n_c == 1, f"{OUT}: script={n_s} cd={n_c}"
    return len(hh.encode('utf-8'))

# =================== lesson-8 ===================
L8 = {}
L8["封面"] = """
  <div class="slide-inner">
    <h1>质因数与互质进阶</h1>
    <p class="subtitle">会分解质因数，就能秒算最大公因数和最小公倍数——再也不怕大数</p>
    <figure class="ta-standard-figure" style="margin-top:20px">
      <svg style="max-width:680px;width:100%;height:auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" fill="none">
        <defs>
          <linearGradient id="bg8" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFF5EE"/><stop offset="50%" stop-color="#E8F8F5"/><stop offset="100%" stop-color="#FFF5EE"/>
          </linearGradient>
          <linearGradient id="g8" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FF6B6B"/><stop offset="100%" stop-color="#4ECDC4"/>
          </linearGradient>
        </defs>
        <rect width="720" height="300" rx="20" fill="url(#bg8)"/>
        <rect x="250" y="120" width="220" height="64" rx="14" fill="url(#g8)"/>
        <text x="360" y="160" text-anchor="middle" fill="#fff" font-size="22" font-weight="700" font-family="system-ui,sans-serif">分解质因数 → 速算</text>
        <rect x="40" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#FF6B6B" stroke-width="2"/>
        <text x="130" y="80" text-anchor="middle" fill="#FF6B6B" font-size="15" font-family="system-ui,sans-serif">短除法求 GCD</text>
        <line x1="220" y1="74" x2="250" y2="150" stroke="#FF6B6B" stroke-width="2"/>
        <rect x="500" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#4ECDC4" stroke-width="2"/>
        <text x="590" y="80" text-anchor="middle" fill="#4ECDC4" font-size="15" font-family="system-ui,sans-serif">短除法求 LCM</text>
        <line x1="500" y1="74" x2="470" y2="150" stroke="#4ECDC4" stroke-width="2"/>
        <text x="360" y="225" text-anchor="middle" fill="#888" font-size="14" font-family="system-ui,sans-serif">互质 → GCD=1、LCM=两数乘积</text>
        <text x="360" y="255" text-anchor="middle" fill="#FF6B6B" font-size="15" font-weight="600" font-family="system-ui,sans-serif">🔢 互质判断 · 🧮 短除 · ⚡ 速算</text>
      </svg>
    </figure>
  </div>
"""
L8["问题锚点"] = """
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Problem Anchor</span>
      <h2>今天想解决什么问题？</h2>
    </div>
    <p style="color:var(--text-secondary);line-height:1.7">下面这些事，学完就能轻松搞定：</p>
    <div style="display:flex;flex-direction:column;gap:10px;margin-top:10px">
      <div class="anchor-card">🔢 求 GCD(48, 60)、LCM(12, 18)，列举法太慢，有没有快办法？</div>
      <div class="anchor-card">🤝 怎么一眼看出两个数<b>互质</b>？互质后能直接写出 GCD / LCM 吗？</div>
      <div class="anchor-card">🧩 一个数是另一个数的倍数时，GCD / LCM 怎么秒答？</div>
      <div class="anchor-card">🏭 分解质因数除了写式子，还能怎么用来算 GCD / LCM？</div>
    </div>
  </div>
"""
L8["学习目标"] = """
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="success">Objectives</span>
      <h2>学习目标</h2>
    </div>
    <ul class="obj-list">
      <li>会用 <b>短除法</b> 同时求两个数的 <b>最大公因数(GCD)</b> 和 <b>最小公倍数(LCM)</b></li>
      <li>理解 <b>互质</b>，能快速判断常见互质情形，并秒算 GCD / LCM</li>
      <li>掌握 <b>特殊情况</b>：互质、倍数关系时的速算规律</li>
      <li>会用 <b>分解质因数</b> 的方法求 GCD / LCM</li>
    </ul>
  </div>
"""
L8["前测"] = """
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Pre-Test</span>
      <h2>先来试试看 👀</h2>
    </div>
    <p style="color:var(--muted);margin:0 0 12px">别担心，答错了也没关系，试试看！</p>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q1: 8 和 9 这两个数（ ）</p>
      <button class="choice" data-quiz="pretest-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 互质</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 不互质</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 说不清</button>
      <p class="quiz-feedback" data-for="pretest-q1"></p>
    </div>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q2: 两个互质数的 GCD 是？</p>
      <button class="choice" data-quiz="pretest-q2" data-answer="correct" onclick="checkQuizBtn(this)">A. 1</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 两数乘积</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 较大数</button>
      <p class="quiz-feedback" data-for="pretest-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600;margin-bottom:6px">Q3: 48 = ?（分解质因数）</p>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 6×8</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 2×2×2×2×3</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 4×12</button>
      <p class="quiz-feedback" data-for="pretest-q3"></p>
    </div>
  </div>
"""
L8["概念1 - 什么情况用列举"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 1</span><h2>分解质因数的标准写法 🔍</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">把合数写成<b>几个质数相乘</b>，短除法最清楚：</p>
    <div class="example-box">
      <p>48 ÷ 2 = 24 → ÷2 = 12 → ÷2 = 6 → ÷2 = 3（质数止）</p>
      <p>所以 <b>48 = 2×2×2×2×3 = 2⁴×3</b></p>
      <p>📌 必须全部是质数！6×8、4×12 都<b>不是</b>分解质因数（含合数）。</p>
    </div>
  </div>
"""
L8["概念2 - 有序列举"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 2</span><h2>什么是互质？🤝</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)"><b>公因数只有 1</b> 的两个数叫 <b>互质</b>（互素）。</p>
    <div class="example-box">
      <p>🔹 8 和 9：公因数只有 1 → <b>互质</b></p>
      <p>🔹 常见的互质：<b>相邻自然数</b>(8,9)、<b>2 与奇数</b>、<b>两个不同的质数</b>(3,7)</p>
      <p>🔹 互质时：<b>GCD = 1</b>，<b>LCM = 两数乘积</b></p>
    </div>
  </div>
"""
L8["概念3 - 表格画图辅助"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 3</span><h2>短除法求 GCD / LCM 🧮</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">用<b>公有质因数</b>同时除，直到互质：</p>
    <div class="example-box">
      <p>求 GCD(18, 24)：公有质因数 2、3 → <b>GCD = 2×3 = 6</b></p>
      <p>求 LCM(18, 24)：公有(2,3) + 独有(3,4) → <b>LCM = 2×3×3×4 = 72</b></p>
      <p>📌 口诀：<b>左乘 = GCD，全乘 = LCM</b></p>
    </div>
  </div>
"""
L8["概念4 - 从列举中找最值"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 4</span><h2>特殊情况速算 ⚡</h2></div>
    <div class="example-box">
      <p><b>① 互质</b>：GCD = 1，LCM = 两数乘积（如 8 和 9 → LCM 72）</p>
      <p><b>② 倍数关系</b>：小数整除大数时</p>
      <p>· GCD = <b>较小数</b>（如 GCD(6, 18) = 6）</p>
      <p>· LCM = <b>较大数</b>（如 LCM(6, 18) = 18）</p>
      <p><b>③ 分解质因数法</b>：取公共质因数的最低次 → GCD；取所有质因数的最高次 → LCM</p>
    </div>
  </div>
"""
L8["脚手架练习"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Scaffold</span><h2>三步练习 ✍️</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">1 短除法求 GCD(12, 18)、LCM(12, 18)</p>
      <p style="color:var(--muted);font-size:14px">公有 2、3 → GCD=6；全乘 2×3×2×3=36 → LCM=36</p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">2 判断互质并速算：7 和 11</p>
      <p style="color:var(--muted);font-size:14px">不同质数→互质，GCD=1，LCM=7×11=77</p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">3 倍数关系：GCD(9, 27)、LCM(9, 27)</p>
      <p style="color:var(--muted);font-size:14px">GCD=9，LCM=27</p>
    </div>
  </div>
"""
L8["概念诊断"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="warn">ConceptTest</span><h2>概念过关测试 🎯</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第1题：GCD(15, 20) = ?</p>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">A. 60</button>
      <button class="choice" data-quiz="ct-q1" data-answer="correct" onclick="checkQuizBtn(this)">B. 5</button>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 1</button>
      <p class="quiz-feedback" data-for="ct-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第2题：两个互质数的 LCM 是？</p>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 1</button>
      <button class="choice" data-quiz="ct-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 两数乘积</button>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 较大数</button>
      <p class="quiz-feedback" data-for="ct-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">第3题：LCM(14, 21) = ?</p>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 7</button>
      <button class="choice" data-quiz="ct-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 42</button>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 294</button>
      <p class="quiz-feedback" data-for="ct-q3"></p>
    </div>
  </div>
"""
L8["互动 - 列举分类"] = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="success">Interactive</span><h2>互质对分类 🎮</h2></div>
      <p style="color:var(--muted);margin:0 0 8px">下面这些数对，哪些是<b>互质</b>？（公因数只有 1）</p>
      <p style="color:var(--muted);margin:0 0 16px;font-size:13px">把它们拖到正确的分类里！（提示：互质对 = (8,9)、(15,16)、(2,3)）</p>
      <div class="drop-zones">
        <div class="drop-zone" id="zone-match" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>✅ 互质对</h4>
          <div id="zone-match-items" style="min-height:20px"></div>
        </div>
        <div class="drop-zone" id="zone-nomatch" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>❌ 不互质（有公因数&gt;1）</h4>
          <div id="zone-nomatch-items" style="min-height:20px"></div>
        </div>
      </div>
      <div class="drop-items" id="drag-items">
        <div class="drag-item" draggable="true" data-correct="match" data-id="d1">(8, 9)</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d2">(15, 16)</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d3">(2, 3)</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d4">(6, 9)</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d5">(10, 15)</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d6">(12, 18)</div>
      </div>
      <div id="drag-score" style="text-align:center;margin-top:12px;font-weight:700;font-size:16px;color:var(--brand)"></div>
      <button class="check-btn" onclick="resetDragGame()">🔄 重置游戏</button>
    </div>
  </div>
"""
L8["后测"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Post-Test</span><h2>学后检测 ✅</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q1: GCD(7, 13) = ?（7、13 都是质数）</p>
      <button class="choice" data-quiz="post-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 1</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 91</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 7</button>
      <p class="quiz-feedback" data-for="post-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q2: 一个数是另一个的倍数时，LCM 等于？</p>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 较小数</button>
      <button class="choice" data-quiz="post-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 较大数</button>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 两数乘积</button>
      <p class="quiz-feedback" data-for="post-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">Q3: 分解质因数求 GCD：36=2²×3²，24=2³×3，GCD=?</p>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 72</button>
      <button class="choice" data-quiz="post-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 12</button>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 6</button>
      <p class="quiz-feedback" data-for="post-q3"></p>
    </div>
  </div>
"""
L8["课堂小结"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Summary</span><h2>课堂小结 📝</h2></div>
    <div class="summary-list">
      <div class="summary-item"><b>1 分解质因数</b>：必须全为质数（如 48 = 2⁴×3）。</div>
      <div class="summary-item"><b>2 互质</b>：公因数只有1；互质时 GCD=1、LCM=乘积。</div>
      <div class="summary-item"><b>3 短除法</b>：左乘=GCD，全乘=LCM。</div>
      <div class="summary-item"><b>4 特殊速算</b>：倍数关系取大/小；互质取1/乘积。</div>
    </div>
  </div>
"""
L8["知识图谱"] = """
  <div class="card card-glow">
    <div class="section-header">
      <span class="phase-tag" data-variant="purple">Knowledge Graph</span>
      <h2>知识图谱 🗺️</h2>
    </div>
    <p style="color:var(--muted);margin:0 0 4px">点击任意节点查看讲解，关联节点会自动高亮：</p>
    <div class="kg-wrap">
      <div class="kg-svg" id="kgSvg"></div>
      <div class="kg-info" id="kgInfo"><p style="color:var(--muted)">点击左侧节点查看详情 ↑</p></div>
    </div>
  </div>
"""
L8["AI学伴"] = """
  <div class="card card-glow">
    <div class="section-header">
      <span class="phase-tag" data-variant="purple">AI Tutor</span>
      <h2>AI 学伴 🤖</h2>
    </div>
    <div class="tutor-app">
      <div class="tutor-chat" id="tutorChat"></div>
      <div class="tutor-chips" id="tutorChips"></div>
      <div class="tutor-input">
        <input id="tutorInput" placeholder="问我任何关于互质、短除、GCD/LCM的问题…" />
        <button onclick="ask()">发送</button>
      </div>
    </div>
  </div>
"""
CD8 = {
  "faq": [
    {"q":"怎么用短除法求最大公因数和最小公倍数？",
     "keys":["短除法","怎么","求","GCD","LCM","算"],
     "a":"用公有的质因数同时除两个数，直到商互质。左边所有除数相乘=最大公因数(GCD)；左边除数和最后的商全部相乘=最小公倍数(LCM)。口诀：左乘得GCD，全乘得LCM。"},
    {"q":"什么是互质？互质时怎么算？",
     "keys":["互质","互素","公因数只有1","怎么算","乘积"],
     "a":"公因数只有1的两个数叫互质。互质时GCD=1，LCM=两数乘积。比如8和9互质，LCM(8,9)=72。"},
    {"q":"两个数有倍数关系时GCD/LCM怎么速算？",
     "keys":["倍数关系","速算","较大数","较小数"],
     "a":"若小数能整除大数：GCD=较小数，LCM=较大数。如GCD(6,18)=6，LCM(6,18)=18。"},
    {"q":"分解质因数时为什么必须全写成质数？",
     "keys":["分解质因数","质数","为什么","标准"],
     "a":"分解质因数的定义就是写成质数相乘，这样才唯一、规范。6×8或4×12含合数，不算分解质因数；48应写成2×2×2×2×3。"},
    {"q":"哪些数一定互质？",
     "keys":["哪些","互质","相邻","质数","2和奇数"],
     "a":"常见互质情形：相邻自然数(8和9)、2与任何奇数、两个不同的质数(3和7)。这些可以直接秒判互质。"}
  ],
  "quiz": [
    {"q":"GCD(15, 20) = ?", "options":["5","60","1"], "answer":0, "exp":"公有质因数只有5，GCD=5。"},
    {"q":"两个互质数的LCM是？", "options":["1","两数乘积","较大数"], "answer":1, "exp":"互质→GCD=1，LCM=两数乘积。"},
    {"q":"LCM(14, 21) = ?", "options":["7","42","294"], "answer":1, "exp":"公有7，独有2和3，LCM=7×2×3=42。"}
  ],
  "graph": {
    "w":720,"h":360,
    "nodes":[
      {"id":"n_dp","label":"分解质因数","x":285,"y":150,"w":150,"h":54,"color":"#FF6B6B",
       "desc":"把合数写成质数相乘（如48=2⁴×3），是求GCD/LCM的基础工具。","links":["n_cp","n_short","n_gcd"]},
      {"id":"n_cp","label":"互质","x":40,"y":80,"w":140,"h":44,"color":"#a78bfa",
       "desc":"公因数只有1。互质时GCD=1，LCM=两数乘积。","links":["n_dp","n_gcd"]},
      {"id":"n_short","label":"短除法","x":40,"y":240,"w":140,"h":44,"color":"#4ECDC4",
       "desc":"公有质因数除到互质：左乘=GCD，全乘=LCM。","links":["n_dp","n_gcd","n_lcm"]},
      {"id":"n_gcd","label":"最大公因数GCD","x":550,"y":80,"w":150,"h":44,"color":"#f59e0b",
       "desc":"两数公共因数里最大的。互质=1；倍数关系=较小数。","links":["n_dp","n_short","n_lcm"]},
      {"id":"n_lcm","label":"最小公倍数LCM","x":550,"y":240,"w":150,"h":44,"color":"#06b6d4",
       "desc":"两数公共倍数里最小的。互质=乘积；倍数关系=较大数。","links":["n_gcd","n_short"]}
    ]
  }
}

# =================== lesson-9 ===================
L9 = {}
L9["封面"] = """
  <div class="slide-inner">
    <h1>奇偶性综合应用</h1>
    <p class="subtitle">不用算，也能判断结果是奇数还是偶数——奇偶性的巧妙推理</p>
    <figure class="ta-standard-figure" style="margin-top:20px">
      <svg style="max-width:680px;width:100%;height:auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" fill="none">
        <defs>
          <linearGradient id="bg9" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFF5EE"/><stop offset="50%" stop-color="#E8F8F5"/><stop offset="100%" stop-color="#FFF5EE"/>
          </linearGradient>
          <linearGradient id="g9" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FF6B6B"/><stop offset="100%" stop-color="#4ECDC4"/>
          </linearGradient>
        </defs>
        <rect width="720" height="300" rx="20" fill="url(#bg9)"/>
        <rect x="250" y="120" width="220" height="64" rx="14" fill="url(#g9)"/>
        <text x="360" y="160" text-anchor="middle" fill="#fff" font-size="22" font-weight="700" font-family="system-ui,sans-serif">加 × 减 ÷ 奇偶</text>
        <rect x="40" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#FF6B6B" stroke-width="2"/>
        <text x="130" y="80" text-anchor="middle" fill="#FF6B6B" font-size="15" font-family="system-ui,sans-serif">加减：同偶异奇</text>
        <line x1="220" y1="74" x2="250" y2="150" stroke="#FF6B6B" stroke-width="2"/>
        <rect x="500" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#4ECDC4" stroke-width="2"/>
        <text x="590" y="80" text-anchor="middle" fill="#4ECDC4" font-size="15" font-family="system-ui,sans-serif">乘法：有偶则偶</text>
        <line x1="500" y1="74" x2="470" y2="150" stroke="#4ECDC4" stroke-width="2"/>
        <text x="360" y="225" text-anchor="middle" fill="#888" font-size="14" font-family="system-ui,sans-serif">翻杯子/开关灯：奇变偶不变</text>
        <text x="360" y="255" text-anchor="middle" fill="#FF6B6B" font-size="15" font-weight="600" font-family="system-ui,sans-serif">🔁 规律 · 💡 推理 · 🎯 巧解</text>
      </svg>
    </figure>
  </div>
"""
L9["问题锚点"] = """
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Problem Anchor</span>
      <h2>今天想解决什么问题？</h2>
    </div>
    <p style="color:var(--text-secondary);line-height:1.7">下面这些烧脑问题，用奇偶性轻松破解：</p>
    <div style="display:flex;flex-direction:column;gap:10px;margin-top:10px">
      <div class="anchor-card">🔢 不计算出结果，能判断 1+2+3+…+100 是奇数还是偶数吗？</div>
      <div class="anchor-card">🔁 10 个杯子全扣着，每次翻 2 个，能全部翻正吗？</div>
      <div class="anchor-card">💡 两个质数之和是奇数，说明什么？</div>
      <div class="anchor-card">🎯 奇数个奇数相加，和是奇是偶？</div>
    </div>
  </div>
"""
L9["学习目标"] = """
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="success">Objectives</span>
      <h2>学习目标</h2>
    </div>
    <ul class="obj-list">
      <li>掌握 <b>加法 / 减法</b> 的奇偶性规律（同加为偶、异加为奇）</li>
      <li>掌握 <b>乘法</b> 的奇偶性规律（有偶数则积为偶）</li>
      <li>会用奇偶性分析 <b>翻杯子 / 开关灯</b> 类问题（奇变偶不变）</li>
      <li>能利用奇偶性做简单 <b>推理</b>（如"两质数和为奇数→必含2"）</li>
    </ul>
  </div>
"""
L9["前测"] = """
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Pre-Test</span>
      <h2>先来试试看 👀</h2>
    </div>
    <p style="color:var(--muted);margin:0 0 12px">别担心，答错了也没关系，试试看！</p>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q1: 奇数 + 奇数 + 奇数 = ？</p>
      <button class="choice" data-quiz="pretest-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 奇数</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 偶数</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 质数</button>
      <p class="quiz-feedback" data-for="pretest-q1"></p>
    </div>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q2: 偶数 × 任何整数 = ？</p>
      <button class="choice" data-quiz="pretest-q2" data-answer="correct" onclick="checkQuizBtn(this)">A. 偶数</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 奇数</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 不一定</button>
      <p class="quiz-feedback" data-for="pretest-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600;margin-bottom:6px">Q3: 每次翻 2 个杯子（共10个），最终能全翻正吗？</p>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 能</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 不能</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 不一定</button>
      <p class="quiz-feedback" data-for="pretest-q3"></p>
    </div>
  </div>
"""
L9["概念1 - 什么情况用列举"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 1</span><h2>加减法的奇偶性 ➕</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">看参与运算的数的"奇偶个数"：</p>
    <div class="example-box">
      <p>🔹 奇 + 奇 = 偶 ｜ 偶 + 偶 = 偶（<b>同类相加为偶</b>）</p>
      <p>🔹 奇 + 偶 = 奇（<b>异类相加为奇</b>）</p>
      <p>🔹 减法同理：奇 - 奇 = 偶，偶 - 偶 = 偶，奇 - 偶 = 奇</p>
    </div>
    <p style="margin-top:10px">📌 <b>奇数个奇数相加 = 奇数；偶数个奇数相加 = 偶数</b>。</p>
  </div>
"""
L9["概念2 - 有序列举"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 2</span><h2>乘法的奇偶性 ✖️</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">只要因数里<b>有一个偶数</b>，积就是偶数：</p>
    <div class="example-box">
      <p>🔹 偶 × 偶 = 偶 ｜ 偶 × 奇 = 偶 ｜ 奇 × 奇 = <b>奇</b></p>
      <p>🔹 推论：连续自然数相乘（含2）→ 一定是偶数</p>
    </div>
    <p style="margin-top:10px">💡 例子：1×2×3×4×5 含 2 和 4 → 偶数。</p>
  </div>
"""
L9["概念3 - 表格画图辅助"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 3</span><h2>翻杯子 / 开关灯问题 🔁</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">核心规律：<b>奇数次操作会变状态，偶数次操作回到原状</b>。</p>
    <div class="example-box">
      <p>🔹 10 个杯子全扣着，每次翻 2 个（翻动总数是偶数次）</p>
      <p>🔹 要全翻正需每个翻奇数次 → 总翻动次数必为<b>奇数</b>×10 = 偶数…但每次翻2个只能产生偶数总次数</p>
      <p>🔹 结论：<b>无法从全扣变成全正</b>（奇偶性矛盾）</p>
    </div>
  </div>
"""
L9["概念4 - 从列举中找最值"] = """
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 4</span><h2>奇偶性推理 💡</h2></div>
    <div class="example-box">
      <p><b>① 两质数之和为奇数</b> → 必有一个是 <b>2</b>（唯一偶质数）</p>
      <p>· 例：a+b=21（奇），则 {2, 19}</p>
      <p><b>② 1+2+…+100</b>：1~100 有 50 个奇数，<b>偶数个奇数相加=偶数</b> → 总和是偶数</p>
      <p><b>③ 判断和奇偶</b>：只看计数对象里奇数的个数</p>
    </div>
  </div>
"""
L9["脚手架练习"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Scaffold</span><h2>三步练习 ✍️</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">1 判断：1+3+5+7+9（5个奇数）的和是？</p>
      <p style="color:var(--muted);font-size:14px">奇数个奇数相加=奇数 → 奇数</p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">2 判断：13 × 24 × 5 的积是？</p>
      <p style="color:var(--muted);font-size:14px">含偶数24 → 积为偶数</p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">3 推理：两个质数之和为 30，可能是哪两个？</p>
      <p style="color:var(--muted);font-size:14px">和为偶→两奇质数或含2；含2则另一为28(非质数)不行→两奇质数：7+23、11+19、13+17</p>
    </div>
  </div>
"""
L9["概念诊断"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="warn">ConceptTest</span><h2>概念过关测试 🎯</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第1题：偶数个奇数相加，和是？</p>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">A. 奇数</button>
      <button class="choice" data-quiz="ct-q1" data-answer="correct" onclick="checkQuizBtn(this)">B. 偶数</button>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 质数</button>
      <p class="quiz-feedback" data-for="ct-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第2题：奇 × 奇 × 偶 = ？</p>
      <button class="choice" data-quiz="ct-q2" data-answer="correct" onclick="checkQuizBtn(this)">A. 偶数</button>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 奇数</button>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 质数</button>
      <p class="quiz-feedback" data-for="ct-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">第3题：两质数之和为奇数，其中必有一个是？</p>
      <button class="choice" data-quiz="ct-q3" data-answer="correct" onclick="checkQuizBtn(this)">A. 2</button>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 3</button>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 5</button>
      <p class="quiz-feedback" data-for="ct-q3"></p>
    </div>
  </div>
"""
L9["互动 - 列举分类"] = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="success">Interactive</span><h2>结果奇偶分类 🎮</h2></div>
      <p style="color:var(--muted);margin:0 0 8px">下面这些算式，结果分别是<b>奇数</b>还是<b>偶数</b>？</p>
      <p style="color:var(--muted);margin:0 0 16px;font-size:13px">把它们拖到正确的分类里！（提示：奇数=3+5、7×9、13-2；偶数=2+4、11×2、8÷2）</p>
      <div class="drop-zones">
        <div class="drop-zone" id="zone-match" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>✅ 奇数结果</h4>
          <div id="zone-match-items" style="min-height:20px"></div>
        </div>
        <div class="drop-zone" id="zone-nomatch" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>❌ 偶数结果</h4>
          <div id="zone-nomatch-items" style="min-height:20px"></div>
        </div>
      </div>
      <div class="drop-items" id="drag-items">
        <div class="drag-item" draggable="true" data-correct="match" data-id="d1">3 + 5</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d2">7 × 9</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d3">13 - 2</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d4">2 + 4</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d5">11 × 2</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d6">8 ÷ 2</div>
      </div>
      <div id="drag-score" style="text-align:center;margin-top:12px;font-weight:700;font-size:16px;color:var(--brand)"></div>
      <button class="check-btn" onclick="resetDragGame()">🔄 重置游戏</button>
    </div>
  </div>
"""
L9["后测"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Post-Test</span><h2>学后检测 ✅</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q1: 1+2+3+…+99（50个奇数）的和是？</p>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">A. 奇数</button>
      <button class="choice" data-quiz="post-q1" data-answer="correct" onclick="checkQuizBtn(this)">B. 偶数</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 质数</button>
      <p class="quiz-feedback" data-for="post-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q2: 每次翻 3 个杯子（共9个，全扣），能全翻正吗？</p>
      <button class="choice" data-quiz="post-q2" data-answer="correct" onclick="checkQuizBtn(this)">A. 能</button>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 不能</button>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 不确定</button>
      <p class="quiz-feedback" data-for="post-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">Q3: 两个质数之和为 12，这两个质数可能是？</p>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 2 和 10</button>
      <button class="choice" data-quiz="post-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 5 和 7</button>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 3 和 9</button>
      <p class="quiz-feedback" data-for="post-q3"></p>
    </div>
  </div>
"""
L9["课堂小结"] = """
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Summary</span><h2>课堂小结 📝</h2></div>
    <div class="summary-list">
      <div class="summary-item"><b>1 加减</b>：同类(奇+奇/偶+偶)为偶，异类为奇；奇数个奇数相加为奇。</div>
      <div class="summary-item"><b>2 乘法</b>：有偶数因数则积为偶；奇×奇=奇。</div>
      <div class="summary-item"><b>3 翻动问题</b>：奇次变状态，偶次复原；用奇偶性判能否达成。</div>
      <div class="summary-item"><b>4 推理</b>：两质数和为奇数→必含2；看奇数个数判和之奇偶。</div>
    </div>
  </div>
"""
L9["知识图谱"] = """
  <div class="card card-glow">
    <div class="section-header">
      <span class="phase-tag" data-variant="purple">Knowledge Graph</span>
      <h2>知识图谱 🗺️</h2>
    </div>
    <p style="color:var(--muted);margin:0 0 4px">点击任意节点查看讲解，关联节点会自动高亮：</p>
    <div class="kg-wrap">
      <div class="kg-svg" id="kgSvg"></div>
      <div class="kg-info" id="kgInfo"><p style="color:var(--muted)">点击左侧节点查看详情 ↑</p></div>
    </div>
  </div>
"""
L9["AI学伴"] = """
  <div class="card card-glow">
    <div class="section-header">
      <span class="phase-tag" data-variant="purple">AI Tutor</span>
      <h2>AI 学伴 🤖</h2>
    </div>
    <div class="tutor-app">
      <div class="tutor-chat" id="tutorChat"></div>
      <div class="tutor-chips" id="tutorChips"></div>
      <div class="tutor-input">
        <input id="tutorInput" placeholder="问我任何关于奇偶性的问题（加减乘除、翻杯子、推理）…" />
        <button onclick="ask()">发送</button>
      </div>
    </div>
  </div>
"""
CD9 = {
  "faq": [
    {"q":"加减法的奇偶性怎么判断？",
     "keys":["加减","加法","减法","规律","奇偶"],
     "a":"同类相加为偶（奇+奇=偶，偶+偶=偶），异类相加为奇（奇+偶=奇）。减法同理。关键看参与的数里奇数的个数：奇数个奇数相加=奇数，偶数个奇数相加=偶数。"},
    {"q":"乘法的奇偶性怎么判断？",
     "keys":["乘法","乘","偶数","积","规律"],
     "a":"只要因数里有一个偶数，积就是偶数（偶×奇=偶，偶×偶=偶）；只有奇×奇才等于奇数。所以连续自然数相乘一定含2，结果必为偶数。"},
    {"q":"翻杯子/开关灯问题怎么用奇偶性？",
     "keys":["翻杯子","开关灯","奇偶","次数","变"],
     "a":"奇数次操作改变状态，偶数次操作回到原状。例如10个杯子全扣，每次翻2个，总翻动次数只能是偶数，而全翻正需要每个杯子翻奇数次（总次数=10个奇数之和=偶数）看似可行，但每次翻2个无法让单个杯子单独翻奇数次——实际不可行，需用奇偶性矛盾分析。"},
    {"q":"两个质数之和是奇数说明什么？",
     "keys":["质数","和为奇数","2","推理"],
     "a":"唯一的偶质数是2。两质数之和为奇数，说明其中一个必是2（另一个是奇数质数）。比如和为21→{2,19}；和为30(偶)→两个都是奇质数如{7,23}。"},
    {"q":"怎么判断1+2+…+n的奇偶性？",
     "keys":["求和","连续","奇偶","判断","1加到n"],
     "a":"只看1~n里奇数的个数：奇数个奇数相加得奇数，偶数个奇数相加得偶数。例如1~100有50个奇数→和为偶数；1~99也有50个奇数→和为偶数。"}
  ],
  "quiz": [
    {"q":"偶数个奇数相加，和是？", "options":["奇数","偶数","质数"], "answer":1, "exp":"偶数个奇数相加=偶数。"},
    {"q":"奇×奇×偶=？", "options":["奇数","偶数","质数"], "answer":1, "exp":"有偶数因数，积为偶数。"},
    {"q":"两质数和为奇数，必含哪个质数？", "options":["2","3","5"], "answer":0, "exp":"唯一偶质数是2，和为奇数必有一个是2。"}
  ],
  "graph": {
    "w":720,"h":360,
    "nodes":[
      {"id":"n_add","label":"加减法奇偶","x":285,"y":150,"w":150,"h":54,"color":"#FF6B6B",
       "desc":"同类(奇+奇/偶+偶)为偶，异类为奇；奇数个奇数相加为奇，偶数个为偶。","links":["n_mul","n_flip","n_infer"]},
      {"id":"n_mul","label":"乘法奇偶","x":40,"y":80,"w":140,"h":44,"color":"#4ECDC4",
       "desc":"有偶数因数则积为偶；仅奇×奇=奇。连续自然数乘积必为偶。","links":["n_add"]},
      {"id":"n_flip","label":"翻动问题","x":40,"y":240,"w":140,"h":44,"color":"#a78bfa",
       "desc":"奇次操作变状态，偶次复原；用奇偶性矛盾判断是否可达。","links":["n_add"]},
      {"id":"n_infer","label":"奇偶推理","x":550,"y":80,"w":140,"h":44,"color":"#f59e0b",
       "desc":"两质数和为奇数→必含2；看奇数个数判和之奇偶。","links":["n_add"]},
      {"id":"n_sum","label":"连加求和奇偶","x":550,"y":240,"w":150,"h":44,"color":"#06b6d4",
       "desc":"1~n 中若奇数个数为偶→和为偶；为奇→和为奇。","links":["n_add"]}
    ]
  }
}

# ===== 生成 =====
s8 = build("lesson-8/index.html", L8, CD8, "4升5衔接 · 五下因数和倍数")
s9 = build("lesson-9/index.html", L9, CD9, "4升5衔接 · 五下因数和倍数")
print(f"✅ lesson-8 生成 ≈{s8//1024}KB")
print(f"✅ lesson-9 生成 ≈{s9//1024}KB")
