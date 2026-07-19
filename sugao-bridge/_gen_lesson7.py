# -*- coding: utf-8 -*-
"""lesson-7 生成器：以已修复的 lesson-6 为干净模板，只替换 15 个 section 的 slide-inner 内容和唯一的 COURSE_DATA。
绝不改动任何 <script> 块，避免重复 const 声明 bug。"""
import re, json, os

SRC = "lesson-6/index.html"
OUT = "lesson-7/index.html"
os.makedirs("lesson-7", exist_ok=True)

h = open(SRC, encoding="utf-8").read()

# ---------- 各 section 的 slide-inner 内容 ----------
SECTIONS = {}

SECTIONS["封面"] = """
  <div class=\"slide-inner\">
    <h1>因数和倍数（进阶）</h1>
    <p class=\"subtitle\">认出 2·5·3 的倍数、分清质数合数、把数拆成质因数——打下五下因数与倍数的完整地基</p>
    <figure class=\"ta-standard-figure\" style=\"margin-top:20px\">
      <svg style=\"max-width:680px;width:100%;height:auto\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 720 300\" fill=\"none\">
        <defs>
          <linearGradient id=\"bg7\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"100%\">
            <stop offset=\"0%\" stop-color=\"#FFF5EE\"/><stop offset=\"50%\" stop-color=\"#E8F8F5\"/><stop offset=\"100%\" stop-color=\"#FFF5EE\"/>
          </linearGradient>
          <linearGradient id=\"g7\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"0%\">
            <stop offset=\"0%\" stop-color=\"#FF6B6B\"/><stop offset=\"100%\" stop-color=\"#4ECDC4\"/>
          </linearGradient>
        </defs>
        <rect width=\"720\" height=\"300\" rx=\"20\" fill=\"url(#bg7)\"/>
        <rect x=\"250\" y=\"120\" width=\"220\" height=\"64\" rx=\"14\" fill=\"url(#g7)\"/>
        <text x=\"360\" y=\"160\" text-anchor=\"middle\" fill=\"#fff\" font-size=\"22\" font-weight=\"700\" font-family=\"system-ui,sans-serif\">倍数特征 · 质数合数</text>
        <rect x=\"40\" y=\"50\" width=\"180\" height=\"48\" rx=\"12\" fill=\"#fff\" stroke=\"#FF6B6B\" stroke-width=\"2\"/>
        <text x=\"130\" y=\"80\" text-anchor=\"middle\" fill=\"#FF6B6B\" font-size=\"15\" font-family=\"system-ui,sans-serif\">2/5/3 倍数特征</text>
        <line x1=\"220\" y1=\"74\" x2=\"250\" y2=\"150\" stroke=\"#FF6B6B\" stroke-width=\"2\"/>
        <rect x=\"500\" y=\"50\" width=\"180\" height=\"48\" rx=\"12\" fill=\"#fff\" stroke=\"#4ECDC4\" stroke-width=\"2\"/>
        <text x=\"590\" y=\"80\" text-anchor=\"middle\" fill=\"#4ECDC4\" font-size=\"15\" font-family=\"system-ui,sans-serif\">质数 · 合数 · 分解</text>
        <line x1=\"500\" y1=\"74\" x2=\"470\" y2=\"150\" stroke=\"#4ECDC4\" stroke-width=\"2\"/>
        <text x=\"360\" y=\"225\" text-anchor=\"middle\" fill=\"#888\" font-size=\"14\" font-family=\"system-ui,sans-serif\">看末位 → 看各数位和 → 拆成质因数相乘</text>
        <text x=\"360\" y=\"255\" text-anchor=\"middle\" fill=\"#FF6B6B\" font-size=\"15\" font-weight=\"600\" font-family=\"system-ui,sans-serif\">🔢 快速判断 · 🧩 拆数 · ⚖️ 奇偶性</text>
      </svg>
    </figure>
  </div>
"""

SECTIONS["问题锚点"] = """
  <div class=\"card\">
    <div class=\"section-header\">
      <span class=\"phase-tag\" data-variant=\"warn\">Problem Anchor</span>
      <h2>今天想解决什么问题？</h2>
    </div>
    <p style=\"color:var(--text-secondary);line-height:1.7\">下面这些困惑，学完这一课你都能轻松搞定：</p>
    <div style=\"display:flex;flex-direction:column;gap:10px;margin-top:10px\">
      <div class=\"anchor-card\">🔢 一堆数摆在面前，怎么<b>一眼</b>认出哪些是 2、5、3 的倍数？</div>
      <div class=\"anchor-card\">🧩 21 到底是不是质数？为什么 1 既不是质数也不是合数？</div>
      <div class=\"anchor-card\">⚖️ 奇数加奇数等于什么？偶数乘奇数呢？不用算也能判断吗？</div>
      <div class=\"anchor-card\">🏭 把 60 拆成几个质数相乘，怎么拆才对（分解质因数）？</div>
    </div>
  </div>
"""

SECTIONS["学习目标"] = """
  <div class=\"card\">
    <div class=\"section-header\">
      <span class=\"phase-tag\" data-variant=\"success\">Objectives</span>
      <h2>学习目标</h2>
    </div>
    <ul class=\"obj-list\">
      <li>掌握 <b>2、5、3 的倍数特征</b>，能快速判断一个数是不是它们的倍数</li>
      <li>理解 <b>质数与合数</b>，知道 1 既不是质数也不是合数，会判断一个数是质数还是合数</li>
      <li>会用 <b>短除法</b> 把合数 <b>分解质因数</b></li>
      <li>掌握 <b>奇数和偶数</b> 的运算规律（奇偶性）</li>
    </ul>
  </div>
"""

SECTIONS["前测"] = """
  <div class=\"card\">
    <div class=\"section-header\">
      <span class=\"phase-tag\" data-variant=\"warn\">Pre-Test</span>
      <h2>先来试试看 👀</h2>
    </div>
    <p style=\"color:var(--muted);margin:0 0 12px\">别担心，答错了也没关系，试试看！</p>
    <div style=\"margin-bottom:16px\">
      <p style=\"font-weight:600;margin-bottom:6px\">Q1: 下面哪个数一定是 3 的倍数？</p>
      <button class=\"choice\" data-quiz=\"pretest-q1\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">A. 123</button>
      <button class=\"choice\" data-quiz=\"pretest-q1\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">B. 321</button>
      <button class=\"choice\" data-quiz=\"pretest-q1\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 222</button>
      <p class=\"quiz-feedback\" data-for=\"pretest-q1\"></p>
    </div>
    <div style=\"margin-bottom:16px\">
      <p style=\"font-weight:600;margin-bottom:6px\">Q2: 下面哪个数是质数？</p>
      <button class=\"choice\" data-quiz=\"pretest-q2\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">A. 9</button>
      <button class=\"choice\" data-quiz=\"pretest-q2\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">B. 7</button>
      <button class=\"choice\" data-quiz=\"pretest-q2\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 21</button>
      <p class=\"quiz-feedback\" data-for=\"pretest-q2\"></p>
    </div>
    <div style=\"margin-bottom:8px\">
      <p style=\"font-weight:600;margin-bottom:6px\">Q3: 奇数 + 奇数 = ？</p>
      <button class=\"choice\" data-quiz=\"pretest-q3\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">A. 偶数</button>
      <button class=\"choice\" data-quiz=\"pretest-q3\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">B. 奇数</button>
      <button class=\"choice\" data-quiz=\"pretest-q3\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 不确定</button>
      <p class=\"quiz-feedback\" data-for=\"pretest-q3\"></p>
    </div>
  </div>
"""

SECTIONS["概念1 - 什么情况用列举"] = """
  <div class=\"card card-glow\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"blue\">Concept 1</span><h2>2 和 5 的倍数特征 🔍</h2></div>
    <p style=\"line-height:1.7;color:var(--text-secondary)\">看<b>个位</b>就够了：</p>
    <div class=\"example-box\">
      <p>🔹 <b>2 的倍数</b>：个位是 <b>0、2、4、6、8</b> → 都是<b>偶数</b></p>
      <p>🔹 <b>5 的倍数</b>：个位是 <b>0 或 5</b></p>
      <p>🔹 同时是 2 和 5 的倍数：个位一定是 <b>0</b></p>
    </div>
    <p style=\"margin-top:10px\"><b>快速判断：</b>130（✅2、✅5，个位0）｜ 47（❌2、❌5，个位7）｜ 85（❌2、✅5）</p>
  </div>
"""

SECTIONS["概念2 - 有序列举"] = """
  <div class=\"card card-glow\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"blue\">Concept 2</span><h2>3 的倍数特征 🔢</h2></div>
    <p style=\"line-height:1.7;color:var(--text-secondary)\">3 的倍数<b>不看个位</b>，要看<b>各个数位上的数字之和</b>！</p>
    <div class=\"example-box\">
      <p><b>123</b>：1+2+3 = 6，6 是 3 的倍数 → <b>123 是 3 的倍数</b> ✅</p>
      <p><b>458</b>：4+5+8 = 17，17 不是 3 的倍数 → <b>458 不是</b> ❌</p>
    </div>
    <p style=\"margin-top:10px\">💡 小技巧：判断 9 的倍数也用同样方法，看<b>数位和是不是 9 的倍数</b>。</p>
  </div>
"""

SECTIONS["概念3 - 表格画图辅助"] = """
  <div class=\"card card-glow\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"blue\">Concept 3</span><h2>质数与合数 🧩</h2></div>
    <p style=\"line-height:1.7;color:var(--text-secondary)\">按<b>因数个数</b>给自然数分类：</p>
    <div class=\"example-box\">
      <p>🔹 <b>质数（素数）</b>：只有 <b>1 和它本身</b> 两个因数。如 2、3、5、7、11…</p>
      <p>🔹 <b>合数</b>：除了 1 和本身，<b>还有别的因数</b>。如 4、6、8、9、10…</p>
      <p>🔹 <b>1 既不是质数也不是合数</b>（只有 1 个因数）</p>
    </div>
    <p style=\"margin-top:10px\">⚠️ <b>2 是最小的质数，也是唯一的偶质数。</b></p>
  </div>
"""

SECTIONS["概念4 - 从列举中找最值"] = """
  <div class=\"card card-glow\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"blue\">Concept 4</span><h2>分解质因数 & 奇偶性 🚀</h2></div>
    <div class=\"example-box\">
      <p><b>① 分解质因数</b>：把合数写成几个质数相乘（用短除法）</p>
      <p>· 例：60 = 2×2×3×5（全部是质数）</p>
      <p><b>② 奇偶性运算规律</b>：</p>
      <p>· 奇+奇=偶｜偶+偶=偶｜奇+偶=奇</p>
      <p>· 奇×奇=奇｜偶×任何=偶</p>
    </div>
    <p style=\"margin-top:10px\">📌 <b>判断乘积奇偶性</b>：只要有一个因数是偶数，乘积就是偶数。</p>
  </div>
"""

SECTIONS["脚手架练习"] = """
  <div class=\"card\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"success\">Scaffold</span><h2>三步练习 ✍️</h2></div>
    <div style=\"margin-bottom:14px\">
      <p style=\"font-weight:600\">1 快速判断：下面哪些是 3 的倍数？</p>
      <p style=\"color:var(--muted);font-size:14px\">111（1+1+1=3 ✅）｜ 235（2+3+5=10 ❌）｜ 999（27 ✅）</p>
    </div>
    <div style=\"margin-bottom:14px\">
      <p style=\"font-weight:600\">2 判断质数/合数：2、9、13、15</p>
      <p style=\"color:var(--muted);font-size:14px\">2（质数）｜ 9=3×3（合数）｜ 13（质数）｜ 15=3×5（合数）</p>
    </div>
    <div style=\"margin-bottom:8px\">
      <p style=\"font-weight:600\">3 分解质因数：把 24 拆成质数相乘</p>
      <p style=\"color:var(--muted);font-size:14px\">24 = 2×2×2×3</p>
    </div>
  </div>
"""

SECTIONS["概念诊断"] = """
  <div class=\"card\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"warn\">ConceptTest</span><h2>概念过关测试 🎯</h2></div>
    <div style=\"margin-bottom:14px\">
      <p style=\"font-weight:600\">第1题：下面一定同时是 2 和 5 倍数的是？</p>
      <button class=\"choice\" data-quiz=\"ct-q1\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">A. 35</button>
      <button class=\"choice\" data-quiz=\"ct-q1\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">B. 60</button>
      <button class=\"choice\" data-quiz=\"ct-q1\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 12</button>
      <p class=\"quiz-feedback\" data-for=\"ct-q1\"></p>
    </div>
    <div style=\"margin-bottom:14px\">
      <p style=\"font-weight:600\">第2题：下面哪个是合数？</p>
      <button class=\"choice\" data-quiz=\"ct-q2\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">A. 17</button>
      <button class=\"choice\" data-quiz=\"ct-q2\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">B. 19</button>
      <button class=\"choice\" data-quiz=\"ct-q2\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">C. 51（=3×17）</button>
      <p class=\"quiz-feedback\" data-for=\"ct-q2\"></p>
    </div>
    <div style=\"margin-bottom:8px\">
      <p style=\"font-weight:600\">第3题：奇数 × 偶数 = ？</p>
      <button class=\"choice\" data-quiz=\"ct-q3\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">A. 偶数</button>
      <button class=\"choice\" data-quiz=\"ct-q3\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">B. 奇数</button>
      <button class=\"choice\" data-quiz=\"ct-q3\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 质数</button>
      <p class=\"quiz-feedback\" data-for=\"ct-q3\"></p>
    </div>
  </div>
"""

SECTIONS["互动 - 列举分类"] = """
  <div class=\"slide-inner\">
    <div class=\"card card-glow\">
      <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"success\">Interactive</span><h2>分类大挑战 🎮</h2></div>
      <p style=\"color:var(--muted);margin:0 0 8px\">下面这些数，哪些是<b>质数</b>？哪些是<b>合数</b>？</p>
      <p style=\"color:var(--muted);margin:0 0 16px;font-size:13px\">把它们拖到正确的分类里！（提示：质数=2,11,13；合数=4,9,15）</p>
      <div class=\"drop-zones\">
        <div class=\"drop-zone\" id=\"zone-match\" ondrop=\"handleDrop(event)\" ondragover=\"handleDragOver(event)\" ondragleave=\"handleDragLeave(event)\">
          <h4>✅ 质数（只有两个因数）</h4>
          <div id=\"zone-match-items\" style=\"min-height:20px\"></div>
        </div>
        <div class=\"drop-zone\" id=\"zone-nomatch\" ondrop=\"handleDrop(event)\" ondragover=\"handleDragOver(event)\" ondragleave=\"handleDragLeave(event)\">
          <h4>❌ 合数</h4>
          <div id=\"zone-nomatch-items\" style=\"min-height:20px\"></div>
        </div>
      </div>
      <div class=\"drop-items\" id=\"drag-items\">
        <div class=\"drag-item\" draggable=\"true\" data-correct=\"match\" data-id=\"d1\">2</div>
        <div class=\"drag-item\" draggable=\"true\" data-correct=\"match\" data-id=\"d2\">11</div>
        <div class=\"drag-item\" draggable=\"true\" data-correct=\"match\" data-id=\"d3\">13</div>
        <div class=\"drag-item\" draggable=\"true\" data-correct=\"nomatch\" data-id=\"d4\">4</div>
        <div class=\"drag-item\" draggable=\"true\" data-correct=\"nomatch\" data-id=\"d5\">9</div>
        <div class=\"drag-item\" draggable=\"true\" data-correct=\"nomatch\" data-id=\"d6\">15</div>
      </div>
      <div id=\"drag-score\" style=\"text-align:center;margin-top:12px;font-weight:700;font-size:16px;color:var(--brand)\"></div>
      <button class=\"check-btn\" onclick=\"resetDragGame()\">🔄 重置游戏</button>
    </div>
  </div>
"""

SECTIONS["后测"] = """
  <div class=\"card\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"success\">Post-Test</span><h2>学后检测 ✅</h2></div>
    <div style=\"margin-bottom:14px\">
      <p style=\"font-weight:600\">Q1: 一个数各个数位和是 12，它（ ）是 3 的倍数。</p>
      <button class=\"choice\" data-quiz=\"post-q1\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">A. 一定</button>
      <button class=\"choice\" data-quiz=\"post-q1\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">B. 不一定</button>
      <button class=\"choice\" data-quiz=\"post-q1\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 一定不</button>
      <p class=\"quiz-feedback\" data-for=\"post-q1\"></p>
    </div>
    <div style=\"margin-bottom:14px\">
      <p style=\"font-weight:600\">Q2: 把 30 分解质因数，正确的是？</p>
      <button class=\"choice\" data-quiz=\"post-q2\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">A. 2×3×5</button>
      <button class=\"choice\" data-quiz=\"post-q2\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">B. 2×15</button>
      <button class=\"choice\" data-quiz=\"post-q2\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 5×6</button>
      <p class=\"quiz-feedback\" data-for=\"post-q2\"></p>
    </div>
    <div style=\"margin-bottom:8px\">
      <p style=\"font-weight:600\">Q3: 偶数 + 奇数 = ？</p>
      <button class=\"choice\" data-quiz=\"post-q3\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">A. 偶数</button>
      <button class=\"choice\" data-quiz=\"post-q3\" data-answer=\"correct\" onclick=\"checkQuizBtn(this)\">B. 奇数</button>
      <button class=\"choice\" data-quiz=\"post-q3\" data-answer=\"wrong\" onclick=\"checkQuizBtn(this)\">C. 质数</button>
      <p class=\"quiz-feedback\" data-for=\"post-q3\"></p>
    </div>
  </div>
"""

SECTIONS["课堂小结"] = """
  <div class=\"card\">
    <div class=\"section-header\"><span class=\"phase-tag\" data-variant=\"success\">Summary</span><h2>课堂小结 📝</h2></div>
    <div class=\"summary-list\">
      <div class=\"summary-item\"><b>1 倍数特征</b>：2/5看个位（0/2/4/6/8；0/5）；3看数位和。</div>
      <div class=\"summary-item\"><b>2 质数合数</b>：质数只有1和本身两个因数；1 既不是质数也不是合数。</div>
      <div class=\"summary-item\"><b>3 分解质因数</b>：用短除法把合数拆成质数相乘（如 60=2×2×3×5）。</div>
      <div class=\"summary-item\"><b>4 奇偶性</b>：同加为偶、异加为奇；乘式中有偶数则积为偶。</div>
    </div>
  </div>
"""

SECTIONS["知识图谱"] = """
  <div class=\"card card-glow\">
    <div class=\"section-header\">
      <span class=\"phase-tag\" data-variant=\"purple\">Knowledge Graph</span>
      <h2>知识图谱 🗺️</h2>
    </div>
    <p style=\"color:var(--muted);margin:0 0 4px\">点击任意节点查看讲解，关联节点会自动高亮：</p>
    <div class=\"kg-wrap\">
      <div class=\"kg-svg\" id=\"kgSvg\"></div>
      <div class=\"kg-info\" id=\"kgInfo\"><p style=\"color:var(--muted)\">点击左侧节点查看详情 ↑</p></div>
    </div>
  </div>
"""

SECTIONS["AI学伴"] = """
  <div class=\"card card-glow\">
    <div class=\"section-header\">
      <span class=\"phase-tag\" data-variant=\"purple\">AI Tutor</span>
      <h2>AI 学伴 🤖</h2>
    </div>
    <div class=\"tutor-app\">
      <div class=\"tutor-chat\" id=\"tutorChat\"></div>
      <div class=\"tutor-chips\" id=\"tutorChips\"></div>
      <div class=\"tutor-input\">
        <input id=\"tutorInput\" placeholder=\"问我任何关于倍数、质数、奇偶性的问题…\" />
        <button onclick=\"ask()\">发送</button>
      </div>
    </div>
  </div>
"""

# ---------- 唯一 COURSE_DATA ----------
COURSE_DATA = {
  "faq": [
    {"q":"怎么快速判断一个数是2或5的倍数？",
     "keys":["2的倍数","5的倍数","判断","个位","特征"],
     "a":"看个位：2的倍数个位是0/2/4/6/8（就是偶数）；5的倍数个位是0或5。同时是2和5的倍数个位一定是0。"},
    {"q":"3的倍数怎么判断？",
     "keys":["3的倍数","数位和","特征","怎么"],
     "a":"不看个位，把各个数位上的数字相加，和是3的倍数，这个数就是3的倍数。比如123：1+2+3=6，所以123是3的倍数。"},
    {"q":"质数和合数怎么区分？1呢？",
     "keys":["质数","合数","1","区分","什么是"],
     "a":"质数只有1和它本身两个因数（如2,3,5,7）；合数除了1和本身还有别的因数（如4,6,9）。1只有一个因数，既不是质数也不是合数。"},
    {"q":"怎么分解质因数？",
     "keys":["分解质因数","怎么","短除","拆"],
     "a":"用短除法：用质数依次除，直到商为质数，把所有除数和最后的商写成相乘形式。如60=2×2×3×5，全部都是质数。"},
    {"q":"奇数加奇数、偶数乘奇数分别是什么？",
     "keys":["奇偶性","奇数","偶数","规律","加","乘"],
     "a":"奇数+奇数=偶数，偶数+偶数=偶数，奇数+偶数=奇数；乘法中只要有一个因数是偶数，积就是偶数（奇×奇=奇）。"}
  ],
  "quiz": [
    {"q":"下面同时是2和5的倍数的是？", "options":["35","60","12"], "answer":1, "exp":"个位必须是0，只有60符合。"},
    {"q":"下面哪个是合数？", "options":["17","19","51(=3×17)"], "answer":2, "exp":"51有因数1,3,17,51，是合数；17、19是质数。"},
    {"q":"奇数×偶数=？", "options":["偶数","奇数","质数"], "answer":0, "exp":"乘法中只要有一个偶数，积就是偶数。"}
  ],
  "graph": {
    "w":720,"h":360,
    "nodes":[
      {"id":"n_feat","label":"倍数特征","x":285,"y":150,"w":150,"h":54,"color":"#FF6B6B",
       "desc":"2/5看个位，3看数位和。快速判断一个数是不是它们的倍数。","links":["n_25","n_3","n_odd"]},
      {"id":"n_25","label":"2与5的倍数","x":40,"y":80,"w":140,"h":44,"color":"#a78bfa",
       "desc":"2的倍数个位0/2/4/6/8；5的倍数个位0/5；同时是2和5倍数→个位0。","links":["n_feat"]},
      {"id":"n_3","label":"3的倍数","x":40,"y":240,"w":140,"h":44,"color":"#4ECDC4",
       "desc":"把各数位数字相加，和是3的倍数，这个数就是3的倍数。","links":["n_feat"]},
      {"id":"n_pc","label":"质数与合数","x":550,"y":80,"w":150,"h":44,"color":"#f59e0b",
       "desc":"质数只有1和本身两个因数；合数有更多因数；1既不是质数也不是合数。","links":["n_feat","n_prime"]},
      {"id":"n_prime","label":"分解质因数","x":550,"y":240,"w":140,"h":44,"color":"#06b6d4",
       "desc":"用短除法把合数拆成质数相乘，如60=2×2×3×5。","links":["n_pc"]},
      {"id":"n_odd","label":"奇偶性","x":290,"y":280,"w":140,"h":44,"color":"#ef6ea8",
       "desc":"同加为偶、异加为奇；乘法中有偶数则积为偶。","links":["n_feat"]}
    ]
  }
}

# ---------- 执行替换 ----------
# 1) 替换每个 section 的 slide-inner
def repl_sec(m):
    title = m.group(2)
    if title not in SECTIONS:
        return m.group(0)
    return f'<section{m.group(1)}>\n{SECTIONS[title]}\n  </section>'

h = re.sub(r'<section([^>]*data-tsh="([^"]+)"[^>]*)>(.*?)</section>', repl_sec, h, flags=re.S)

# 2) 替换唯一 COURSE_DATA
cd_json = json.dumps(COURSE_DATA, ensure_ascii=False)
h = re.sub(r'const COURSE_DATA = \{.*?\};', f'const COURSE_DATA = {cd_json};', h, count=1, flags=re.S)

# 3) 标题/页脚标签（4升5衔接 -> 五下）
h = h.replace('4升5衔接 · 五下预告', '4升5衔接 · 五下因数和倍数')
# 移除封面 phase-tag 里的"五下预告"若包含（保留即可，不强制）

open(OUT, "w", encoding="utf-8").write(h)

# 验证
hh = open(OUT, encoding="utf-8").read()
types = re.findall(r'data-tsh="([^"]+)"', hh)
n_script = len(re.findall(r'<script', hh))
n_cd = hh.count('const COURSE_DATA')
print(f"✅ lesson-7 生成完成, 大小≈{len(hh.encode('utf-8'))//1024}KB, 页型数={len(types)}, script={n_script}, COURSE_DATA={n_cd}")
assert n_script == 2, "script数异常"
assert n_cd == 1, "COURSE_DATA重复"
