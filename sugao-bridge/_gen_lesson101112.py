# -*- coding: utf-8 -*-
"""生成 lesson-10/11/12：以干净的 lesson-9 为模板，只替换 15 个 section 的 inner + 唯一 COURSE_DATA。
绝不改动任何 <script> 块，从根避免重复 const 声明 bug。"""
import re, json, os

TMPL = "lesson-9/index.html"

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

# ============== lesson-10 小数的意义和性质 ==============
L10 = {}
L10["封面"] = '''
  <div class="slide-inner">
    <h1>小数的意义和性质</h1>
    <p class="subtitle">0.1 就是 1/10——把分数写成分数点右边，测量世界更精确</p>
    <figure class="ta-standard-figure" style="margin-top:20px">
      <svg style="max-width:680px;width:100%;height:auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" fill="none">
        <defs>
          <linearGradient id="bg10" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFF5EE"/><stop offset="50%" stop-color="#E8F8F5"/><stop offset="100%" stop-color="#FFF5EE"/>
          </linearGradient>
          <linearGradient id="g10" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FF6B6B"/><stop offset="100%" stop-color="#4ECDC4"/>
          </linearGradient>
        </defs>
        <rect width="720" height="300" rx="20" fill="url(#bg10)"/>
        <rect x="250" y="120" width="220" height="64" rx="14" fill="url(#g10)"/>
        <text x="360" y="160" text-anchor="middle" fill="#fff" font-size="22" font-weight="700" font-family="system-ui,sans-serif">分数 ⇄ 小数</text>
        <rect x="40" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#FF6B6B" stroke-width="2"/>
        <text x="130" y="80" text-anchor="middle" fill="#FF6B6B" font-size="15" font-family="system-ui,sans-serif">1/10 = 0.1</text>
        <line x1="220" y1="74" x2="250" y2="150" stroke="#FF6B6B" stroke-width="2"/>
        <rect x="500" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#4ECDC4" stroke-width="2"/>
        <text x="590" y="80" text-anchor="middle" fill="#4ECDC4" font-size="15" font-family="system-ui,sans-serif">0.3 = 0.30</text>
        <line x1="500" y1="74" x2="470" y2="150" stroke="#4ECDC4" stroke-width="2"/>
        <text x="360" y="225" text-anchor="middle" fill="#888" font-size="14" font-family="system-ui,sans-serif">计数单位 · 读写 · 性质 · 比较改写</text>
        <text x="360" y="255" text-anchor="middle" fill="#FF6B6B" font-size="15" font-weight="600" font-family="system-ui,sans-serif">🔢 意义 · ✍️ 读写 · ⚖️ 性质</text>
      </svg>
    </figure>
  </div>
'''
L10["问题锚点"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Problem Anchor</span>
      <h2>今天想解决什么问题？</h2>
    </div>
    <p style="color:var(--text-secondary);line-height:1.7">下面这些困惑，学完这一课你都能轻松搞定：</p>
    <div style="display:flex;flex-direction:column;gap:10px;margin-top:10px">
      <div class="anchor-card">🔢 0.1 元到底是多少钱？它和 1/10 有什么关系？</div>
      <div class="anchor-card">📏 身高 1 米 3 分米，怎么用小数写成 1.3 米？</div>
      <div class="anchor-card">⚖️ 0.3 和 0.30 相等吗？为什么末尾能添 0？</div>
      <div class="anchor-card">🔁 3.05 米和 305 厘米，谁大？怎么比较和换算？</div>
    </div>
  </div>
'''
L10["学习目标"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="success">Objectives</span>
      <h2>学习目标</h2>
    </div>
    <ul class="obj-list">
      <li>理解 <b>小数的意义</b>：分母是 10、100、1000 的分数可写成小数</li>
      <li>掌握小数的 <b>计数单位</b>（0.1、0.01、0.001）和数位顺序</li>
      <li>会正确 <b>读写</b> 小数，理解 <b>小数性质</b>（末尾添 0 去 0 大小不变）</li>
      <li>会比较小数大小，并进行 <b>单位改写</b>（米/厘米、元/角分）</li>
    </ul>
  </div>
'''
L10["前测"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Pre-Test</span>
      <h2>先来试试看 👀</h2>
    </div>
    <p style="color:var(--muted);margin:0 0 12px">别担心，答错了也没关系，试试看！</p>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q1: 0.1 等于几分之几？</p>
      <button class="choice" data-quiz="pretest-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 1/10</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 1/100</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 1/1</button>
      <p class="quiz-feedback" data-for="pretest-q1"></p>
    </div>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q2: 0.3 和 0.30 的大小关系是？</p>
      <button class="choice" data-quiz="pretest-q2" data-answer="correct" onclick="checkQuizBtn(this)">A. 相等</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 0.3 大</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 0.30 大</button>
      <p class="quiz-feedback" data-for="pretest-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600;margin-bottom:6px">Q3: 小数的计数单位不包含？</p>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 0.1</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 0.01</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="correct" onclick="checkQuizBtn(this)">C. 0.2</button>
      <p class="quiz-feedback" data-for="pretest-q3"></p>
    </div>
  </div>
'''
L10["概念1 - 什么情况用列举"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 1</span><h2>小数的意义 🔍</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">小数是<b>分母为 10、100、1000… 的分数</b>的另一种写法：</p>
    <div class="example-box">
      <p>🔹 1/10 = <b>0.1</b>（一位小数），计数单位 0.1</p>
      <p>🔹 1/100 = <b>0.01</b>（两位小数），计数单位 0.01</p>
      <p>🔹 1/1000 = <b>0.001</b>（三位小数），计数单位 0.001</p>
      <p>🔹 例：0.7 = 7/10，0.25 = 25/100，0.138 = 138/1000</p>
    </div>
  </div>
'''
L10["概念2 - 有序列举"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 2</span><h2>小数的读写 ✍️</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">读小数：先读<b>整数部分</b>（按整数），再读<b>小数点</b>（读作"点"），最后依次读出<b>小数部分的每个数字</b>。</p>
    <div class="example-box">
      <p>🔹 3.14 读作：三点一四</p>
      <p>🔹 0.05 读作：零点零五（中间的 0 要读出来）</p>
      <p>🔹 10.08 读作：十点零八</p>
    </div>
    <p style="margin-top:10px">📌 写小数：对应数位写数字，缺位用 0 占位。</p>
  </div>
'''
L10["概念3 - 表格画图辅助"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 3</span><h2>小数的性质 ⚖️</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)"><b>小数的末尾</b>添上 0 或去掉 0，小数的<b>大小不变</b>。</p>
    <div class="example-box">
      <p>🔹 0.3 = 0.30 = 0.300</p>
      <p>🔹 化简：0.70 = 0.7，10.0 = 10（整数末尾 0 一般去掉）</p>
      <p>🔹 改写：0.4 = 0.40（凑两位小数），便于比较、计算</p>
    </div>
    <p style="margin-top:10px">⚠️ 是<b>末尾</b>的 0，中间的 0 不能去（0.05 ≠ 0.5）。</p>
  </div>
'''
L10["概念4 - 从列举中找最值"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 4</span><h2>比较大小与单位改写 🔁</h2></div>
    <div class="example-box">
      <p><b>① 比较大小</b>：先比整数部分，再依次比十分位、百分位…</p>
      <p>· 例：3.14 ＞ 3.08（整数相同，十分位1＞0）</p>
      <p><b>② 单位改写</b>（进率 10、100、1000）：</p>
      <p>· 米↔厘米：×100 / ÷100，如 1.2 米 = 120 厘米</p>
      <p>· 元↔分：×100，如 3.05 元 = 305 分</p>
    </div>
  </div>
'''
L10["脚手架练习"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Scaffold</span><h2>三步练习 ✍️</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">1 分数化小数：7/10、53/100、9/1000</p>
      <p style="color:var(--muted);font-size:14px">0.7、0.53、0.009</p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">2 化简与改写：0.60 = ?，把 0.8 写成三位小数</p>
      <p style="color:var(--muted);font-size:14px">0.60 = 0.6；0.8 = 0.800</p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">3 单位改写：2.5 米 = ? 厘米，4 元 8 分 = ? 元</p>
      <p style="color:var(--muted);font-size:14px">250 厘米；4.08 元</p>
    </div>
  </div>
'''
L10["概念诊断"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="warn">ConceptTest</span><h2>概念过关测试 🎯</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第1题：0.25 里面有（ ）个 0.01。</p>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">A. 5</button>
      <button class="choice" data-quiz="ct-q1" data-answer="correct" onclick="checkQuizBtn(this)">B. 25</button>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 250</button>
      <p class="quiz-feedback" data-for="ct-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第2题：下面（ ）的 0 去掉后大小不变。</p>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 3.05</button>
      <button class="choice" data-quiz="ct-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 3.50</button>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 0.03</button>
      <p class="quiz-feedback" data-for="ct-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">第3题：比较 0.9 和 0.87，结果是？</p>
      <button class="choice" data-quiz="ct-q3" data-answer="correct" onclick="checkQuizBtn(this)">A. 0.9 ＞ 0.87</button>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 0.9 ＜ 0.87</button>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 相等</button>
      <p class="quiz-feedback" data-for="ct-q3"></p>
    </div>
  </div>
'''
L10["互动 - 列举分类"] = '''
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="success">Interactive</span><h2>相等配对 🎮</h2></div>
      <p style="color:var(--muted);margin:0 0 8px">下面这些数中，哪些和 <b>0.3</b> 相等？（利用小数性质）</p>
      <p style="color:var(--muted);margin:0 0 16px;font-size:13px">把它们拖到"相等"区！（提示：相等的是 0.30、0.300、0.3000）</p>
      <div class="drop-zones">
        <div class="drop-zone" id="zone-match" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>✅ 与 0.3 相等</h4>
          <div id="zone-match-items" style="min-height:20px"></div>
        </div>
        <div class="drop-zone" id="zone-nomatch" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>❌ 不相等</h4>
          <div id="zone-nomatch-items" style="min-height:20px"></div>
        </div>
      </div>
      <div class="drop-items" id="drag-items">
        <div class="drag-item" draggable="true" data-correct="match" data-id="d1">0.30</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d2">0.300</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d3">0.3000</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d4">0.03</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d5">3.0</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d6">0.33</div>
      </div>
      <div id="drag-score" style="text-align:center;margin-top:12px;font-weight:700;font-size:16px;color:var(--brand)"></div>
      <button class="check-btn" onclick="resetDragGame()">🔄 重置游戏</button>
    </div>
  </div>
'''
L10["后测"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Post-Test</span><h2>学后检测 ✅</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q1: 0.8 里面有（ ）个 0.1。</p>
      <button class="choice" data-quiz="post-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 8</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 80</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 0.8</button>
      <p class="quiz-feedback" data-for="post-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q2: 把 3.6 米改写成厘米是？</p>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 36 厘米</button>
      <button class="choice" data-quiz="post-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 360 厘米</button>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 3.6 厘米</button>
      <p class="quiz-feedback" data-for="post-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">Q3: 0.207 读作？</p>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 零点二百零七</button>
      <button class="choice" data-quiz="post-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 零点二零七</button>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 零点二七</button>
      <p class="quiz-feedback" data-for="post-q3"></p>
    </div>
  </div>
'''
L10["课堂小结"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Summary</span><h2>课堂小结 📝</h2></div>
    <div class="summary-list">
      <div class="summary-item"><b>1 意义</b>：分母是10/100/1000的分数写成一位/两位/三位小数。</div>
      <div class="summary-item"><b>2 计数单位</b>：0.1、0.01、0.001，对应十分位/百分位/千分位。</div>
      <div class="summary-item"><b>3 性质</b>：末尾添0去0大小不变；化简与改写靠它。</div>
      <div class="summary-item"><b>4 比较改写</b>：先整数后小数位；单位换算用进率。</div>
    </div>
  </div>
'''
L10["知识图谱"] = '''
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
'''
L10["AI学伴"] = '''
  <div class="card card-glow">
    <div class="section-header">
      <span class="phase-tag" data-variant="purple">AI Tutor</span>
      <h2>AI 学伴 🤖</h2>
    </div>
    <div class="tutor-app">
      <div class="tutor-chat" id="tutorChat"></div>
      <div class="tutor-chips" id="tutorChips"></div>
      <div class="tutor-input">
        <input id="tutorInput" placeholder="问我任何关于小数意义、读写、性质、比较的问题…" />
        <button onclick="ask()">发送</button>
      </div>
    </div>
  </div>
'''
CD10 = {
  "faq": [
    {"q":"小数和分数有什么关系？",
     "keys":["小数","分数","意义","关系","怎么"],
     "a":"小数是分母为10、100、1000…的分数的另一种写法。一位小数表示十分之几（0.1=1/10），两位小数表示百分之几（0.01=1/100），三位小数表示千分之几。例如0.7=7/10，0.25=25/100。"},
    {"q":"小数的计数单位是什么？",
     "keys":["计数单位","0.1","0.01","数位"],
     "a":"小数的计数单位依次是0.1（十分之一）、0.01（百分之一）、0.001（千分之一）……分别对应十分位、百分位、千分位。例如0.25里有25个0.01。"},
    {"q":"小数的性质是什么？",
     "keys":["性质","末尾","添0","相等"],
     "a":"小数的末尾添上0或去掉0，小数的大小不变。所以0.3=0.30=0.300。注意是末尾的0，中间的0不能去掉，0.05≠0.5。"},
    {"q":"小数怎么读、怎么写？",
     "keys":["读写","读作","怎么读","写法"],
     "a":"读法：先读整数部分（按整数），小数点读“点”，再依次读出小数部分的每个数字。例如3.14读三点一四，0.05读零点零五。写法：对应数位写数字，缺位用0占位。"},
    {"q":"怎么比较小数大小和单位改写？",
     "keys":["比较","大小","改写","单位","换算"],
     "a":"比较：先比整数部分，再依次比十分位、百分位……单位改写用进率：米↔厘米×100/÷100（1.2米=120厘米），元↔分×100（3.05元=305分）。"}
  ],
  "quiz": [
    {"q":"0.25 里有几个 0.01？", "options":["5","25","250"], "answer":1, "exp":"0.25=25/100，有25个0.01。"},
    {"q":"下面哪个去掉0后大小不变？", "options":["3.05","3.50","0.03"], "answer":1, "exp":"只有末尾的0可去：3.50=3.5；3.05中间0不能去。"},
    {"q":"0.9 和 0.87 比较？", "options":["0.9大","0.87大","相等"], "answer":0, "exp":"十分位9>8，所以0.9>0.87。"}
  ],
  "graph": {
    "w":720,"h":360,
    "nodes":[
      {"id":"n_mean","label":"小数意义","x":285,"y":150,"w":150,"h":54,"color":"#FF6B6B",
       "desc":"分母是10/100/1000的分数写成一位/两位/三位小数，如0.1=1/10。","links":["n_unit","n_rw","n_prop"]},
      {"id":"n_unit","label":"计数单位","x":40,"y":80,"w":140,"h":44,"color":"#a78bfa",
       "desc":"0.1、0.01、0.001对应十分/百分/千分位。","links":["n_mean"]},
      {"id":"n_rw","label":"读写","x":40,"y":240,"w":140,"h":44,"color":"#4ECDC4",
       "desc":"先读整数，点读点，再依次读小数位数字；缺位0占位。","links":["n_mean"]},
      {"id":"n_prop","label":"小数性质","x":550,"y":80,"w":140,"h":44,"color":"#f59e0b",
       "desc":"末尾添0去0大小不变；用于化简与改写。","links":["n_mean","n_cmp"]},
      {"id":"n_cmp","label":"比较与改写","x":550,"y":240,"w":150,"h":44,"color":"#06b6d4",
       "desc":"先整数后小数位比大小；单位换算用进率10/100/1000。","links":["n_prop"]}
    ]
  }
}

# ============== lesson-11 统计 ==============
L11 = {}
L11["封面"] = '''
  <div class="slide-inner">
    <h1>统计：复式表与折线图</h1>
    <p class="subtitle">一张表看清两组数据，一条线看见变化趋势——统计让数据会说话</p>
    <figure class="ta-standard-figure" style="margin-top:20px">
      <svg style="max-width:680px;width:100%;height:auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" fill="none">
        <defs>
          <linearGradient id="bg11" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFF5EE"/><stop offset="50%" stop-color="#E8F8F5"/><stop offset="100%" stop-color="#FFF5EE"/>
          </linearGradient>
          <linearGradient id="g11" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FF6B6B"/><stop offset="100%" stop-color="#4ECDC4"/>
          </linearGradient>
        </defs>
        <rect width="720" height="300" rx="20" fill="url(#bg11)"/>
        <rect x="250" y="120" width="220" height="64" rx="14" fill="url(#g11)"/>
        <text x="360" y="160" text-anchor="middle" fill="#fff" font-size="22" font-weight="700" font-family="system-ui,sans-serif">表 → 图</text>
        <rect x="40" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#FF6B6B" stroke-width="2"/>
        <text x="130" y="80" text-anchor="middle" fill="#FF6B6B" font-size="15" font-family="system-ui,sans-serif">复式统计表</text>
        <line x1="220" y1="74" x2="250" y2="150" stroke="#FF6B6B" stroke-width="2"/>
        <rect x="500" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#4ECDC4" stroke-width="2"/>
        <text x="590" y="80" text-anchor="middle" fill="#4ECDC4" font-size="15" font-family="system-ui,sans-serif">折线统计图</text>
        <line x1="500" y1="74" x2="470" y2="150" stroke="#4ECDC4" stroke-width="2"/>
        <text x="360" y="225" text-anchor="middle" fill="#888" font-size="14" font-family="system-ui,sans-serif">合并对比 · 看趋势 · 选对图</text>
        <text x="360" y="255" text-anchor="middle" fill="#FF6B6B" font-size="15" font-weight="600" font-family="system-ui,sans-serif">📊 复式表 · 📈 折线 · 🔍 读图</text>
      </svg>
    </figure>
  </div>
'''
L11["问题锚点"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Problem Anchor</span>
      <h2>今天想解决什么问题？</h2>
    </div>
    <p style="color:var(--text-secondary);line-height:1.7">下面这些场景，学完就能选对工具：</p>
    <div style="display:flex;flex-direction:column;gap:10px;margin-top:10px">
      <div class="anchor-card">📊 想同时比较甲、乙两班每个月的体温数据，用一张表还是两张？</div>
      <div class="anchor-card">📈 想看一周气温是升是降、哪天最热，用什么图最直观？</div>
      <div class="anchor-card">🔍 有两组成绩，想直接对比谁高谁低，选条形还是折线？</div>
      <div class="anchor-card">🧩 为什么有时用复式折线，比单式折线更清楚？</div>
    </div>
  </div>
'''
L11["学习目标"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="success">Objectives</span>
      <h2>学习目标</h2>
    </div>
    <ul class="obj-list">
      <li>认识 <b>复式统计表</b>，会把多张单式表合并，便于对比</li>
      <li>认识 <b>单式折线统计图</b>，能从点和线读出数量与变化趋势</li>
      <li>认识 <b>复式折线统计图</b>，能对比两组数据的变化</li>
      <li>会根据问题 <b>选择合适的统计图</b>（比较多少用条形，看趋势用折线）</li>
    </ul>
  </div>
'''
L11["前测"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Pre-Test</span>
      <h2>先来试试看 👀</h2>
    </div>
    <p style="color:var(--muted);margin:0 0 12px">别担心，答错了也没关系，试试看！</p>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q1: 想看"气温一周变化趋势"，最好用？</p>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">A. 统计表</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="correct" onclick="checkQuizBtn(this)">B. 折线统计图</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 象形图</button>
      <p class="quiz-feedback" data-for="pretest-q1"></p>
    </div>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q2: 要同时对比男、女生身高，用？</p>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 单式表</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 复式统计表</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 折线图</button>
      <p class="quiz-feedback" data-for="pretest-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600;margin-bottom:6px">Q3: 折线统计图的"点"表示？</p>
      <button class="choice" data-quiz="pretest-q3" data-answer="correct" onclick="checkQuizBtn(this)">A. 数量的多少</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 类别名称</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 总数</button>
      <p class="quiz-feedback" data-for="pretest-q3"></p>
    </div>
  </div>
'''
L11["概念1 - 什么情况用列举"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 1</span><h2>复式统计表 📊</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">把<b>几张单式统计表</b>合并成<b>一张</b>，加上"类别"列，就能同时对比多组数据。</p>
    <div class="example-box">
      <p>🔹 单式：男生身高表、女生身高表（各看各的）</p>
      <p>🔹 复式：一张表里分"男生/女生"两列，一眼比出谁高</p>
      <p>📌 好处：信息集中、便于比较、避免来回翻看</p>
    </div>
  </div>
'''
L11["概念2 - 有序列举"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 2</span><h2>单式折线统计图 📈</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">用<b>点</b>表示各数量多少，用<b>线段</b>按顺序连起来，就能看出<b>变化趋势</b>。</p>
    <div class="example-box">
      <p>🔹 点高 = 数量多；点低 = 数量少</p>
      <p>🔹 线<b>上升</b> = 增加；线<b>下降</b> = 减少；线平 = 不变</p>
      <p>🔹 例：一周气温 20→22→25→23→21，先升后降</p>
    </div>
  </div>
'''
L11["概念3 - 表格画图辅助"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 3</span><h2>复式折线统计图 🔍</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">在同一图上画<b>两条折线</b>（常用不同颜色），分别标图例，就能<b>对比两组数据的变化</b>。</p>
    <div class="example-box">
      <p>🔹 红线 = 甲班，蓝线 = 乙班</p>
      <p>🔹 看两条线谁在上、谁升得快、何时交叉</p>
      <p>📌 比单式折线信息更丰富，适合对比</p>
    </div>
  </div>
'''
L11["概念4 - 从列举中找最值"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 4</span><h2>选对统计图 🧭</h2></div>
    <div class="example-box">
      <p><b>① 想比较各类数量的多少</b> → 用 <b>条形统计图</b></p>
      <p><b>② 想看数量随时间的变化趋势</b> → 用 <b>折线统计图</b></p>
      <p><b>③ 想同时对比两组数据的多少/变化</b> → 用 <b>复式统计表 / 复式折线</b></p>
    </div>
    <p style="margin-top:10px">📌 没有"最好"的图，只有"最合适"的图。</p>
  </div>
'''
L11["脚手架练习"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Scaffold</span><h2>三步练习 ✍️</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">1 下面数据选什么图？"各小组人数"</p>
      <p style="color:var(--muted);font-size:14px">比较多少 → 条形统计图</p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">2 "近6个月销售额变化" 选什么图？</p>
      <p style="color:var(--muted);font-size:14px">看趋势 → 折线统计图</p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">3 "甲乙两店每天营业额对比" 选什么？</p>
      <p style="color:var(--muted);font-size:14px">两组对比 → 复式折线统计图</p>
    </div>
  </div>
'''
L11["概念诊断"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="warn">ConceptTest</span><h2>概念过关测试 🎯</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第1题：折线统计图中，线段上升表示数量（ ）。</p>
      <button class="choice" data-quiz="ct-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 增加</button>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 减少</button>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 不变</button>
      <p class="quiz-feedback" data-for="ct-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第2题：合并多张单式表用（ ）。</p>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 条形图</button>
      <button class="choice" data-quiz="ct-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 复式统计表</button>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 象形图</button>
      <p class="quiz-feedback" data-for="ct-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">第3题：想看"两国人口随时间变化"，最好用？</p>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 单式折线</button>
      <button class="choice" data-quiz="ct-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 复式折线</button>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 统计表</button>
      <p class="quiz-feedback" data-for="ct-q3"></p>
    </div>
  </div>
'''
L11["互动 - 列举分类"] = '''
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="success">Interactive</span><h2>选图大挑战 🎮</h2></div>
      <p style="color:var(--muted);margin:0 0 8px">下面这些统计需求，该用哪种图？</p>
      <p style="color:var(--muted);margin:0 0 16px;font-size:13px">拖到正确的分类里！（提示：条形=比多少；折线=看趋势；复式=两组对比）</p>
      <div class="drop-zones">
        <div class="drop-zone" id="zone-match" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>✅ 折线统计图</h4>
          <div id="zone-match-items" style="min-height:20px"></div>
        </div>
        <div class="drop-zone" id="zone-nomatch" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>❌ 条形/复式表</h4>
          <div id="zone-nomatch-items" style="min-height:20px"></div>
        </div>
      </div>
      <div class="drop-items" id="drag-items">
        <div class="drag-item" draggable="true" data-correct="match" data-id="d1">气温一周变化</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d2">销售额6个月走势</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d3">体重每月变化</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d4">各班人数比较</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d5">男女身高对比表</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d6">各类图书数量</div>
      </div>
      <div id="drag-score" style="text-align:center;margin-top:12px;font-weight:700;font-size:16px;color:var(--brand)"></div>
      <button class="check-btn" onclick="resetDragGame()">🔄 重置游戏</button>
    </div>
  </div>
'''
L11["后测"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Post-Test</span><h2>学后检测 ✅</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q1: 折线图里"点"的主要作用是？</p>
      <button class="choice" data-quiz="post-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 表示数量多少</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 表示时间</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 表示类别</button>
      <p class="quiz-feedback" data-for="post-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q2: 比较"三种饮料销量多少"，选？</p>
      <button class="choice" data-quiz="post-q2" data-answer="correct" onclick="checkQuizBtn(this)">A. 条形统计图</button>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">B. 折线统计图</button>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 复式表</button>
      <p class="quiz-feedback" data-for="post-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">Q3: 复式折线比单式折线多了一个什么？</p>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 更多的点</button>
      <button class="choice" data-quiz="post-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 第二条数据线(对比)</button>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 图例无关</button>
      <p class="quiz-feedback" data-for="post-q3"></p>
    </div>
  </div>
'''
L11["课堂小结"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Summary</span><h2>课堂小结 📝</h2></div>
    <div class="summary-list">
      <div class="summary-item"><b>1 复式统计表</b>：合并单式表，便于多组数据对比。</div>
      <div class="summary-item"><b>2 单式折线</b>：点表数量、线表趋势（升/降/平）。</div>
      <div class="summary-item"><b>3 复式折线</b>：两条线+图例，对比两组变化。</div>
      <div class="summary-item"><b>4 选图</b>：比多少→条形；看趋势→折线；两组对比→复式。</div>
    </div>
  </div>
'''
L11["知识图谱"] = '''
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
'''
L11["AI学伴"] = '''
  <div class="card card-glow">
    <div class="section-header">
      <span class="phase-tag" data-variant="purple">AI Tutor</span>
      <h2>AI 学伴 🤖</h2>
    </div>
    <div class="tutor-app">
      <div class="tutor-chat" id="tutorChat"></div>
      <div class="tutor-chips" id="tutorChips"></div>
      <div class="tutor-input">
        <input id="tutorInput" placeholder="问我任何关于复式表、折线图、选图的问题…" />
        <button onclick="ask()">发送</button>
      </div>
    </div>
  </div>
'''
CD11 = {
  "faq": [
    {"q":"复式统计表是什么？有什么用？",
     "keys":["复式统计表","合并","对比","单式"],
     "a":"把几张单式统计表合成一张，增加类别列（如男生/女生），就能在同一张表里同时对比多组数据，信息集中、便于比较。"},
    {"q":"折线统计图怎么读？",
     "keys":["折线","读","点","线","趋势"],
     "a":"点表示数量的多少（点高数量多），线段按顺序连接表示变化趋势：上升=增加，下降=减少，水平=不变。能直观看出增减变化。"},
    {"q":"单式折线和复式折线有什么区别？",
     "keys":["单式","复式","区别","两条","对比"],
     "a":"单式折线只有一组数据的一条线；复式折线在同一图上有两条线（不同颜色+图例），可以对比两组数据的变化，信息更丰富。"},
    {"q":"什么时候用条形图、什么时候用折线图？",
     "keys":["选图","条形","折线","比较","趋势"],
     "a":"想比较各类数量的多少→用条形统计图；想看数量随时间或顺序的变化趋势→用折线统计图；想同时对比两组数据→用复式统计表或复式折线。"},
    {"q":"折线图里的点代表什么？",
     "keys":["点","表示","数量","含义"],
     "a":"折线图中的每个点代表某一时刻或某一类别对应的具体数量多少；点的位置高低直接反映数量大小。"}
  ],
  "quiz": [
    {"q":"线段上升表示数量？", "options":["增加","减少","不变"], "answer":0, "exp":"上升=增加。"},
    {"q":"合并多张单式表用？", "options":["条形图","复式统计表","象形图"], "answer":1, "exp":"复式表把多组合并对比。"},
    {"q":"两国人口随时间变化，最好用？", "options":["单式折线","复式折线","统计表"], "answer":1, "exp":"两组对比→复式折线。"}
  ],
  "graph": {
    "w":720,"h":360,
    "nodes":[
      {"id":"n_table","label":"复式统计表","x":285,"y":150,"w":150,"h":54,"color":"#FF6B6B",
       "desc":"合并多张单式表，加类别列，便于多组数据对比。","links":["n_line","n_choose"]},
      {"id":"n_line","label":"单式折线图","x":40,"y":80,"w":140,"h":44,"color":"#4ECDC4",
       "desc":"点表数量，线表趋势（升/降/平）。","links":["n_table","n_dline"]},
      {"id":"n_dline","label":"复式折线图","x":40,"y":240,"w":140,"h":44,"color":"#a78bfa",
       "desc":"两条线+图例，对比两组数据变化。","links":["n_line","n_table"]},
      {"id":"n_choose","label":"选对统计图","x":550,"y":150,"w":150,"h":54,"color":"#06b6d4",
       "desc":"比多少→条形；看趋势→折线；两组对比→复式。","links":["n_table","n_line","n_dline"]}
    ]
  }
}

# ============== lesson-12 小数实际问题 ==============
L12 = {}
L12["封面"] = '''
  <div class="slide-inner">
    <h1>小数实际问题</h1>
    <p class="subtitle">单价×数量、单位换算、分段计费——把小数算进真实生活里</p>
    <figure class="ta-standard-figure" style="margin-top:20px">
      <svg style="max-width:680px;width:100%;height:auto" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" fill="none">
        <defs>
          <linearGradient id="bg12" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#FFF5EE"/><stop offset="50%" stop-color="#E8F8F5"/><stop offset="100%" stop-color="#FFF5EE"/>
          </linearGradient>
          <linearGradient id="g12" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FF6B6B"/><stop offset="100%" stop-color="#4ECDC4"/>
          </linearGradient>
        </defs>
        <rect width="720" height="300" rx="20" fill="url(#bg12)"/>
        <rect x="250" y="120" width="220" height="64" rx="14" fill="url(#g12)"/>
        <text x="360" y="160" text-anchor="middle" fill="#fff" font-size="22" font-weight="700" font-family="system-ui,sans-serif">生活 → 算式</text>
        <rect x="40" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#FF6B6B" stroke-width="2"/>
        <text x="130" y="80" text-anchor="middle" fill="#FF6B6B" font-size="15" font-family="system-ui,sans-serif">单价×数量</text>
        <line x1="220" y1="74" x2="250" y2="150" stroke="#FF6B6B" stroke-width="2"/>
        <rect x="500" y="50" width="180" height="48" rx="12" fill="#fff" stroke="#4ECDC4" stroke-width="2"/>
        <text x="590" y="80" text-anchor="middle" fill="#4ECDC4" font-size="15" font-family="system-ui,sans-serif">单位换算</text>
        <line x1="500" y1="74" x2="470" y2="150" stroke="#4ECDC4" stroke-width="2"/>
        <text x="360" y="225" text-anchor="middle" fill="#888" font-size="14" font-family="system-ui,sans-serif">数量关系 · 分段计费 · 估算检验</text>
        <text x="360" y="255" text-anchor="middle" fill="#FF6B6B" font-size="15" font-weight="600" font-family="system-ui,sans-serif">🛒 购物 · 📏 测量 · 🚕 计费</text>
      </svg>
    </figure>
  </div>
'''
L12["问题锚点"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Problem Anchor</span>
      <h2>今天想解决什么问题？</h2>
    </div>
    <p style="color:var(--text-secondary);line-height:1.7">下面这些生活题，学完就能列式算清：</p>
    <div style="display:flex;flex-direction:column;gap:10px;margin-top:10px">
      <div class="anchor-card">🛒 苹果 3.5 千克，每千克 8.6 元，一共要付多少？</div>
      <div class="anchor-card">🚕 打车起步价 10 元（3千米内），超过每千米 2.4 元，8千米多少钱？</div>
      <div class="anchor-card">📏 一根 1.2 米布做上衣，做 5 件够吗（每件 0.25 米）？</div>
      <div class="anchor-card">🔍 算出来 41.9 元，怎么快速检验合不合理？</div>
    </div>
  </div>
'''
L12["学习目标"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="success">Objectives</span>
      <h2>学习目标</h2>
    </div>
    <ul class="obj-list">
      <li>掌握常见 <b>数量关系</b>：单价×数量=总价、速度×时间=路程</li>
      <li>会用 <b>单位换算</b> 处理元角分、米分米厘米的实际问题</li>
      <li>会解决 <b>分段计费</b> 问题（起步价 + 超出部分）</li>
      <li>养成 <b>估算与检验</b> 的习惯，判断结果是否合理</li>
    </ul>
  </div>
'''
L12["前测"] = '''
  <div class="card">
    <div class="section-header">
      <span class="phase-tag" data-variant="warn">Pre-Test</span>
      <h2>先来试试看 👀</h2>
    </div>
    <p style="color:var(--muted);margin:0 0 12px">别担心，答错了也没关系，试试看！</p>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q1: 单价 5 元，买 4 个，总价 = ？</p>
      <button class="choice" data-quiz="pretest-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 20 元</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 9 元</button>
      <button class="choice" data-quiz="pretest-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 1.25 元</button>
      <p class="quiz-feedback" data-for="pretest-q1"></p>
    </div>
    <div style="margin-bottom:16px">
      <p style="font-weight:600;margin-bottom:6px">Q2: 1.5 米 = ? 厘米</p>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 15 厘米</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 150 厘米</button>
      <button class="choice" data-quiz="pretest-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 1500 厘米</button>
      <p class="quiz-feedback" data-for="pretest-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600;margin-bottom:6px">Q3: 分段计费：起步 10 元(含3km)，超 1km 加 2 元，走 5km 付？</p>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 10 元</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 14 元</button>
      <button class="choice" data-quiz="pretest-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 12 元</button>
      <p class="quiz-feedback" data-for="pretest-q3"></p>
    </div>
  </div>
'''
L12["概念1 - 什么情况用列举"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 1</span><h2>基本数量关系 🛒</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">把生活语言翻成算式，关键是找对<b>数量关系</b>：</p>
    <div class="example-box">
      <p>🔹 <b>单价 × 数量 = 总价</b>（如 8.6 元/kg × 3.5 kg）</p>
      <p>🔹 <b>速度 × 时间 = 路程</b>（如 60 km/h × 1.5 h）</p>
      <p>🔹 已知两个量可求第三个：总价 ÷ 数量 = 单价</p>
    </div>
  </div>
'''
L12["概念2 - 有序列举"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 2</span><h2>单位换算应用 📏</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">实际问题中常要先统一单位再计算，记住进率：</p>
    <div class="example-box">
      <p>🔹 1 元 = 10 角 = 100 分；3 元 5 角 = 3.5 元 = 350 分</p>
      <p>🔹 1 米 = 10 分米 = 100 厘米；1.2 米 = 120 厘米</p>
      <p>🔹 大化小 ×进率，小化大 ÷进率</p>
    </div>
    <p style="margin-top:10px">📌 列式前先看单位是否一致！</p>
  </div>
'''
L12["概念3 - 表格画图辅助"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 3</span><h2>分段计费 🚕</h2></div>
    <p style="line-height:1.7;color:var(--text-secondary)">先算"起步内"，再算"超出部分"，最后相加：</p>
    <div class="example-box">
      <p>例：起步 10 元(3km 内)，超 1km 加 2 元，走 8km</p>
      <p>· 超出：8 - 3 = 5 km</p>
      <p>· 超出费：5 × 2 = 10 元</p>
      <p>· 总费：10 + 10 = <b>20 元</b></p>
    </div>
  </div>
'''
L12["概念4 - 从列举中找最值"] = '''
  <div class="card card-glow">
    <div class="section-header"><span class="phase-tag" data-variant="blue">Concept 4</span><h2>估算与检验 🔍</h2></div>
    <div class="example-box">
      <p><b>① 估算</b>：8.6×3.5 ≈ 9×3.5 = 31.5，结果应比 31.5 略小</p>
      <p><b>② 检验合理性</b>：单价、数量都为正，总价应是正数；数量翻倍总价也应翻倍</p>
      <p><b>③ 单位检查</b>：总价单位应是"元"，不是"千克"</p>
    </div>
    <p style="margin-top:10px">📌 算完多问一句："这个答案合理吗？"</p>
  </div>
'''
L12["脚手架练习"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Scaffold</span><h2>三步练习 ✍️</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">1 笔 2.5 元/支，买 4 支，总价？</p>
      <p style="color:var(--muted);font-size:14px">2.5×4 = 10 元</p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">2 0.8 米布做 1 个书包，3 米够做几个？</p>
      <p style="color:var(--muted);font-size:14px">3 ÷ 0.8 = 3.75 → 最多 3 个（去尾）</p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">3 水费：前 10 吨 2 元/吨，超出 3 元/吨，用 15 吨付？</p>
      <p style="color:var(--muted);font-size:14px">10×2 + 5×3 = 20+15 = 35 元</p>
    </div>
  </div>
'''
L12["概念诊断"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="warn">ConceptTest</span><h2>概念过关测试 🎯</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第1题：每千克 4.2 元，买 2.5 千克，总价列式？</p>
      <button class="choice" data-quiz="ct-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 4.2×2.5</button>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 4.2÷2.5</button>
      <button class="choice" data-quiz="ct-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 4.2+2.5</button>
      <p class="quiz-feedback" data-for="ct-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">第2题：2.4 米 = ? 厘米</p>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 24</button>
      <button class="choice" data-quiz="ct-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 240</button>
      <button class="choice" data-quiz="ct-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 2400</button>
      <p class="quiz-feedback" data-for="ct-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">第3题：起步 8 元(含2km)，超 1km 加 1.5 元，走 6km 付？</p>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">A. 8 元</button>
      <button class="choice" data-quiz="ct-q3" data-answer="correct" onclick="checkQuizBtn(this)">B. 14 元</button>
      <button class="choice" data-quiz="ct-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 9 元</button>
      <p class="quiz-feedback" data-for="ct-q3"></p>
    </div>
  </div>
'''
L12["互动 - 列举分类"] = '''
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header"><span class="phase-tag" data-variant="success">Interactive</span><h2>方法归类 🎮</h2></div>
      <p style="color:var(--muted);margin:0 0 8px">下面这些生活问题，主要用到哪种方法？</p>
      <p style="color:var(--muted);margin:0 0 16px;font-size:13px">拖到正确分类！（提示：单价数量 / 单位换算 / 分段计费）</p>
      <div class="drop-zones">
        <div class="drop-zone" id="zone-match" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>✅ 单价×数量</h4>
          <div id="zone-match-items" style="min-height:20px"></div>
        </div>
        <div class="drop-zone" id="zone-nomatch" ondrop="handleDrop(event)" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)">
          <h4>❌ 单位换算/分段计费</h4>
          <div id="zone-nomatch-items" style="min-height:20px"></div>
        </div>
      </div>
      <div class="drop-items" id="drag-items">
        <div class="drag-item" draggable="true" data-correct="match" data-id="d1">苹果3kg每千克6元</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d2">笔2元买5支</div>
        <div class="drag-item" draggable="true" data-correct="match" data-id="d3">书25.8元买3本</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d4">1.5米化厘米</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d5">打车8km计费</div>
        <div class="drag-item" draggable="true" data-correct="nomatch" data-id="d6">水费分段算</div>
      </div>
      <div id="drag-score" style="text-align:center;margin-top:12px;font-weight:700;font-size:16px;color:var(--brand)"></div>
      <button class="check-btn" onclick="resetDragGame()">🔄 重置游戏</button>
    </div>
  </div>
'''
L12["后测"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Post-Test</span><h2>学后检测 ✅</h2></div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q1: 牛奶每盒 3.5 元，买 6 盒，共？</p>
      <button class="choice" data-quiz="post-q1" data-answer="correct" onclick="checkQuizBtn(this)">A. 21 元</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">B. 9.5 元</button>
      <button class="choice" data-quiz="post-q1" data-answer="wrong" onclick="checkQuizBtn(this)">C. 3.5 元</button>
      <p class="quiz-feedback" data-for="post-q1"></p>
    </div>
    <div style="margin-bottom:14px">
      <p style="font-weight:600">Q2: 0.6 米布做一个娃娃，2.5 米最多做几个？</p>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">A. 4 个</button>
      <button class="choice" data-quiz="post-q2" data-answer="correct" onclick="checkQuizBtn(this)">B. 4 个（2.5÷0.6≈4.16，去尾4）</button>
      <button class="choice" data-quiz="post-q2" data-answer="wrong" onclick="checkQuizBtn(this)">C. 5 个</button>
      <p class="quiz-feedback" data-for="post-q2"></p>
    </div>
    <div style="margin-bottom:8px">
      <p style="font-weight:600">Q3: 检验 8.6×3.5≈30.1 是否合理，可用？</p>
      <button class="choice" data-quiz="post-q3" data-answer="correct" onclick="checkQuizBtn(this)">A. 估算 9×3.5=31.5 对照</button>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">B. 直接相信</button>
      <button class="choice" data-quiz="post-q3" data-answer="wrong" onclick="checkQuizBtn(this)">C. 不用检验</button>
      <p class="quiz-feedback" data-for="post-q3"></p>
    </div>
  </div>
'''
L12["课堂小结"] = '''
  <div class="card">
    <div class="section-header"><span class="phase-tag" data-variant="success">Summary</span><h2>课堂小结 📝</h2></div>
    <div class="summary-list">
      <div class="summary-item"><b>1 数量关系</b>：单价×数量=总价；速度×时间=路程。</div>
      <div class="summary-item"><b>2 单位换算</b>：先统一单位再算，进率10/100。</div>
      <div class="summary-item"><b>3 分段计费</b>：起步内 + 超出部分，分别算再相加。</div>
      <div class="summary-item"><b>4 估算检验</b>：用近似估大小、查单位与正负合理性。</div>
    </div>
  </div>
'''
L12["知识图谱"] = '''
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
'''
L12["AI学伴"] = '''
  <div class="card card-glow">
    <div class="section-header">
      <span class="phase-tag" data-variant="purple">AI Tutor</span>
      <h2>AI 学伴 🤖</h2>
    </div>
    <div class="tutor-app">
      <div class="tutor-chat" id="tutorChat"></div>
      <div class="tutor-chips" id="tutorChips"></div>
      <div class="tutor-input">
        <input id="tutorInput" placeholder="问我任何小数应用题、单位换算、分段计费的问题…" />
        <button onclick="ask()">发送</button>
      </div>
    </div>
  </div>
'''
CD12 = {
  "faq": [
    {"q":"小数实际问题常用什么数量关系？",
     "keys":["数量关系","单价","总价","数量","路程"],
     "a":"最常用：单价×数量=总价，速度×时间=路程。已知其中两个量可求第三个，例如总价÷数量=单价。把生活语言先翻译成这样的关系式再列式。"},
    {"q":"单位不统一怎么办？",
     "keys":["单位","换算","统一","进率","米厘米"],
     "a":"列式前先统一单位：1米=100厘米、1元=100分等。大单位化小单位乘进率，小化大除以进率。例如1.2米=120厘米，3元5角=3.5元。"},
    {"q":"分段计费怎么算？",
     "keys":["分段","计费","起步","超出","出租车"],
     "a":"分两段：先算起步价涵盖的部分，再算超出部分×单价，最后相加。例：起步10元(3km内)，超1km加2元，走8km：超出5km×2=10元，总10+10=20元。"},
    {"q":"怎么估算和检验答案？",
     "keys":["估算","检验","合理","怎么"],
     "a":"估算：把小数近似成整数先算个大概范围，如8.6×3.5≈9×3.5=31.5，结果应略小于它。检验：看单位对不对、正负是否合理、数量翻倍结果是否也翻倍。"},
    {"q":"去尾法和进一法什么时候用？",
     "keys":["去尾","进一","最多","最少","余数"],
     "a":"求“最多能做几个”用去尾法（舍去余数，如3÷0.8=3.75→最多3个）；求“至少需要多少容器”用进一法（余数进1）。根据问题情境选择。"}
  ],
  "quiz": [
    {"q":"每千克4.2元买2.5千克，总价列式？", "options":["4.2×2.5","4.2÷2.5","4.2+2.5"], "answer":0, "exp":"单价×数量=总价。"},
    {"q":"2.4米=?厘米", "options":["24","240","2400"], "answer":1, "exp":"米化厘米×100。"},
    {"q":"起步8元(含2km)超1km加1.5元，走6km付？", "options":["8元","14元","9元"], "answer":1, "exp":"超出4km×1.5=6，8+6=14。"}
  ],
  "graph": {
    "w":720,"h":360,
    "nodes":[
      {"id":"n_rel","label":"数量关系","x":285,"y":150,"w":150,"h":54,"color":"#FF6B6B",
       "desc":"单价×数量=总价；速度×时间=路程。先翻译生活语言再列式。","links":["n_unit","n_fee","n_check"]},
      {"id":"n_unit","label":"单位换算","x":40,"y":80,"w":140,"h":44,"color":"#4ECDC4",
       "desc":"先统一单位再算；1米=100厘米，1元=100分。","links":["n_rel"]},
      {"id":"n_fee","label":"分段计费","x":40,"y":240,"w":140,"h":44,"color":"#a78bfa",
       "desc":"起步价 + 超出部分×单价，分别算再相加。","links":["n_rel"]},
      {"id":"n_check","label":"估算与检验","x":550,"y":150,"w":150,"h":54,"color":"#06b6d4",
       "desc":"用整数估算范围、查单位与正负，判断结果是否合理。","links":["n_rel","n_unit"]}
    ]
  }
}

# ===== 生成 =====
s10 = build("lesson-10/index.html", L10, CD10, "4升5衔接 · 五上小数与统计")
s11 = build("lesson-11/index.html", L11, CD11, "4升5衔接 · 五上小数与统计")
s12 = build("lesson-12/index.html", L12, CD12, "4升5衔接 · 五上小数与统计")
print(f"✅ lesson-10 生成 ≈{s10//1024}KB")
print(f"✅ lesson-11 生成 ≈{s11//1024}KB")
print(f"✅ lesson-12 生成 ≈{s12//1024}KB")
