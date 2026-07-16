/* TeachAny AI Tutor Card - 分数四则运算 */
(function() {
  'use strict';

  const container = document.querySelector('[data-teachany-tutor-card]');
  if (!container) return;

  const KB = {
    topics: {
      '同分母加减': {
        short: '分母不变，分子直接相加减。比如3/8+2/8=5/8，分母8不变，分子3+2=5。',
        tip: '常见错误：把分母也加起来→3/8+2/8≠5/16！分母表示每份的大小，不变。'
      },
      '通分': {
        short: '异分母加减必须先通分：找两个分母的最小公倍数作为新分母。如1/2+1/3，2和3的最小公倍数是6，通分后=3/6+2/6=5/6。',
        tip: '通分方法：①找分母的最小公倍数LCM ②每个分数分子分母同乘一个数使其分母=LCM ③变成同分母后加减。'
      },
      '分数乘法': {
        short: '分子乘分子，分母乘分母。如2/3×1/2=(2×1)/(3×2)=2/6=1/3。结果要约成最简分数！',
        tip: '分数乘法不需要通分！直接分子×分子、分母×分母即可。这不同于加减法。'
      },
      '分数除法': {
        short: '除以一个分数=乘它的倒数！倒数就是把分子分母对调。如1/2÷2/3=1/2×3/2=3/4。',
        tip: '倒数口诀：分母↔分子。3/4的倒数是4/3，2的倒数是1/2，1/3的倒数是3。'
      },
      '约分': {
        short: '结果要化成最简分数：分子分母同时除以最大公约数。如2/4=1/2，6/8=3/4。',
        tip: '快速约分法：①分子分母都能被2整除→除以2 ②都能被3整除→除以3 ③直到不能约。'
      },
      '最小公倍数': {
        short: '通分时需要找两个分母的最小公倍数(LCM)。方法：列倍数表→找最小的共同倍数。如4和6的LCM是12（4的倍数：4,8,12；6的倍数：6,12）。',
        tip: '如果分母互质（没有公因数），公倍数就是乘积。如3和4互质，LCM=3×4=12。'
      },
      '混合运算': {
        short: '有括号先算括号，然后先乘除后加减。同级运算从左到右。',
        tip: '例：1/2+1/3×2=1/2+2/3=7/6。先算乘法1/3×2=2/3，再加。'
      },
      '分数比较': {
        short: '比较分数大小：分母相同→比分子；分母不同→先通分再比。',
        tip: '3/4和2/3谁大？通分：9/12 vs 8/12 → 3/4>2/3。'
      }
    },
    problems: {
      '1/2+1/3': '通分：3/6+2/6=5/6。不是2/5！分母不能直接相加。',
      '3/8+2/8': '同分母：分母8不变，分子3+2=5，答案是5/8。不是5/16！',
      '2/3×1/2': '乘法：2×1/3×2=2/6=1/3。',
      '1/2÷2/3': '除法变乘法：1/2×3/2=3/4。别忘了取倒数！'
    },
    general: '我是你的数学学伴！关于分数四则运算有什么问题都可以问我。我会先给提示，不直接给答案～'
  };

  const greetings = [
    '👋 分数运算有什么不懂的？先说说你卡在哪里～',
    '🤔 加减还是乘除分不清？试试描述一下题目～',
    '💡 分数运算秘诀：加减看分母，乘法直接乘，除法翻倒数！你有什么想问的？'
  ];

  container.innerHTML = '<style id="ta-tutor-inline-css">.ta-tutor-card{background:linear-gradient(135deg,#fffbf0,#fff5e0);border-radius:16px;border:2px solid #ffe66d;padding:24px;max-width:680px;margin:0 auto;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}.ta-tutor-header{display:flex;align-items:center;gap:12px;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid #ffe0a0}.ta-tutor-avatar{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#ff6b6b,#e84a4a);display:flex;align-items:center;justify-content:center;font-size:22px;color:white;flex-shrink:0}.ta-tutor-title{font-weight:700;font-size:17px;color:#2d2d2d}.ta-tutor-subtitle{font-size:12px;color:#999}.ta-tutor-chat{background:white;border-radius:12px;padding:16px;min-height:80px;max-height:280px;overflow-y:auto;margin-bottom:12px;font-size:15px;line-height:1.7;color:#333}.ta-tutor-msg{margin-bottom:10px;padding:10px 14px;border-radius:12px;max-width:90%;animation:taFadeIn .3s ease}@keyframes taFadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}.ta-tutor-msg.bot{background:#f0f9e8;margin-right:auto}.ta-tutor-msg.user{background:#e8f0ff;margin-left:auto;text-align:right}.ta-tutor-input-row{display:flex;gap:8px}.ta-tutor-input{flex:1;padding:10px 14px;border:2px solid #ddd;border-radius:10px;font-size:15px;font-family:inherit;outline:0;transition:border-color .2s}.ta-tutor-input:focus{border-color:#ff6b6b}.ta-tutor-btn{padding:10px 20px;background:linear-gradient(135deg,#ff6b6b,#e84a4a);color:white;border:0;border-radius:10px;font-size:15px;font-weight:600;cursor:pointer;transition:opacity .2s;white-space:nowrap}.ta-tutor-btn:hover{opacity:.88}.ta-tutor-btn:active{transform:scale(.97)}.ta-tutor-quick-qs{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}.ta-tutor-quick-q{padding:5px 12px;background:#fff8e0;border:1px solid #ffe66d;border-radius:16px;font-size:12px;color:#8a6d00;cursor:pointer;transition:background .15s}.ta-tutor-quick-q:hover{background:#ffecb3}</style><div class="ta-tutor-card"><div class="ta-tutor-header"><div class="ta-tutor-avatar">🧑‍🏫</div><div><div class="ta-tutor-title">AI 数学学伴</div><div class="ta-tutor-subtitle">分数四则运算专属 · 先给提示不打答案</div></div></div><div class="ta-tutor-chat" id="ta-tutor-chat"></div><div class="ta-tutor-input-row"><input class="ta-tutor-input" id="ta-tutor-input" placeholder="说出你的问题，比如「1/2+1/3怎么算」…"><button class="ta-tutor-btn" id="ta-tutor-send">➤</button></div><div class="ta-tutor-quick-qs" id="ta-tutor-quicks"></div></div>';

  var chat = document.getElementById('ta-tutor-chat');
  var inputEl = document.getElementById('ta-tutor-input');
  var quickRow = document.getElementById('ta-tutor-quicks');

  var quickQs = [
    { label: '❶ 同分母怎么加减？', q: '同分母加减' },
    { label: '❷ 什么是通分？', q: '通分' },
    { label: '❸ 1/2+1/3怎么算？', q: '1/2+1/3' },
    { label: '❹ 分数乘法怎么算？', q: '分数乘法' },
    { label: '❺ 分数除法怎么做？', q: '分数除法' },
    { label: '❻ 怎么约分？', q: '约分' },
  ];
  quickRow.innerHTML = quickQs.map(function(q) { return '<span class="ta-tutor-quick-q" data-q="'+q.q+'">'+q.label+'</span>'; }).join('');

  function addMsg(text, cls) {
    var div = document.createElement('div');
    div.className = 'ta-tutor-msg ' + (cls || 'bot');
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
  }

  function botReply(input) {
    var s = input.replace(/\s+/g,'').toLowerCase();
    var found = null;
    var tKeys = Object.keys(KB.topics);
    for (var i = 0; i < tKeys.length; i++) {
      if (s.indexOf(tKeys[i]) >= 0 || tKeys[i].indexOf(s) >= 0) { found = KB.topics[tKeys[i]]; break; }
    }
    if (!found) {
      var pKeys = Object.keys(KB.problems);
      for (var j = 0; j < pKeys.length; j++) {
        if (s.indexOf(pKeys[j].replace(/\s+/g,'')) >= 0) { found = { short: KB.problems[pKeys[j]], tip: '' }; break; }
      }
    }
    if (found) {
      addMsg(found.short + (found.tip ? '\n\n💡 ' + found.tip : ''), 'bot');
    } else if (s.length < 3) {
      addMsg('可以把问题再说详细一点吗？比如「分数加法怎么算」「通分是什么意思」～', 'bot');
    } else {
      addMsg('这个问题很棒！回顾一下：\n1️⃣ 同分母加减：分母不变，分子加减\n2️⃣ 异分母：先通分，再加减\n3️⃣ 乘法：分子×分子，分母×分母\n4️⃣ 除法：×倒数\n\n你具体卡在哪一步？', 'bot');
    }
  }

  function handleSend() {
    var txt = inputEl.value.trim();
    if (!txt) return;
    addMsg(txt, 'user');
    inputEl.value = '';
    setTimeout(function() { botReply(txt); }, 400);
  }

  document.getElementById('ta-tutor-send').addEventListener('click', handleSend);
  document.getElementById('ta-tutor-input').addEventListener('keydown', function(e) { if (e.key === 'Enter') handleSend(); });
  quickRow.addEventListener('click', function(e) {
    var el = e.target.closest('.ta-tutor-quick-q');
    if (!el) return;
    var q = el.dataset.q;
    addMsg(q, 'user');
    setTimeout(function() { botReply(q); }, 400);
  });

  addMsg(greetings[Math.floor(Math.random() * greetings.length)], 'bot');
})();
