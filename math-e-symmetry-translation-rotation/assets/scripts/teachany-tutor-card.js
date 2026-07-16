/* TeachAny AI Tutor Card - Self-contained for zstudy */
(function() {
  'use strict';

  const container = document.querySelector('[data-teachany-tutor-card]');
  if (!container) return;

  // ─── Knowledge base ───
  const KB = {
    topics: {
      '小数点对齐': {
        short: '小数加减法的核心规则：小数点对齐 = 相同数位对齐。把两个数的小数点上下对齐，个位对个位、十分位对十分位……',
        tip: '对齐小数点后，从最低位（最右边）开始算，满十进一，不够就向前一位借1。'
      },
      '整数减小数': {
        short: '整数减小数时，先把整数写成小数形式（如 5 = 5.0 = 5.00），补上小数点和足够的0，再按对齐规则减。',
        tip: '例如 5 - 2.3 → 写成 5.0 - 2.3，十分位 0-3 不够，向个位借1（1个=10个0.1），10-3=7，个位5→4，4-2=2，答案2.7。'
      },
      '进位': {
        short: '小数加法进位和整数加法一样：满十向前一位进1。从最低位开始加，如果某一位加起来≥10，就进1到前一位。',
        tip: '例如 0.7 + 0.5：十分位 7+5=12，写下2进1到个位，最终 1.2。'
      },
      '位数不同': {
        short: '位数不同时，在末尾补0让位数相同，对齐就更直观了。',
        tip: '如 3.08 + 0.9 → 把 0.9 写成 0.90（补一个0），3.08 + 0.90 = 3.98。补0不改变数的大小！'
      },
      '混合运算': {
        short: '小数加减混合运算按从左到右的顺序进行，也可以用小括号分组。',
        tip: '例：3.5 + 2.1 - 1.8 → 先算 3.5 + 2.1 = 5.6，再减 1.8 = 3.8。带括号时先算括号里面。'
      }
    },
    problems: {
      '3.5 + 2': '3.5 + 2 = 5.5。把2看成2.0，对齐小数点：3.5 + 2.0 = 5.5。不是3.7！因为不能末位对齐。',
      '1.35和1.4': '1.4 > 1.35，因为1.4 = 1.40（补0），1.40 > 1.35，高0.05米。',
      '超市': '2.5 + 3.08 + 0.9 → 2.50 + 3.08 + 0.90 = 6.48 元。'
    },
    general: '我是你的数学学伴！有小数加减法的问题都可以问我。我会先给你一个提示，不会直接给答案哦～'
  };

  const greetings = [
    '👋 有小数加减法的问题吗？先说说你卡在哪里～',
    '🤔 哪道题让你头疼了？试试描述一下你的思路～',
    '💡 小数加减法通关秘籍：小数点对齐！你有什么想问的？'
  ];

  // ─── Build UI ───
  container.innerHTML = `
    <style id="ta-tutor-inline-css">
      .ta-tutor-card {
        background: linear-gradient(135deg, #fffbf0 0%, #fff5e0 100%);
        border-radius: 16px;
        border: 2px solid #ffe66d;
        padding: 24px;
        max-width: 680px;
        margin: 0 auto;
        font-family: -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif;
      }
      .ta-tutor-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
        padding-bottom: 12px;
        border-bottom: 1px solid #ffe0a0;
      }
      .ta-tutor-avatar {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, #ff6b6b, #e84a4a);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        color: white;
        flex-shrink: 0;
      }
      .ta-tutor-title {
        font-weight: 700;
        font-size: 17px;
        color: #2d2d2d;
      }
      .ta-tutor-subtitle {
        font-size: 12px;
        color: #999;
      }
      .ta-tutor-chat {
        background: white;
        border-radius: 12px;
        padding: 16px;
        min-height: 80px;
        max-height: 280px;
        overflow-y: auto;
        margin-bottom: 12px;
        font-size: 15px;
        line-height: 1.7;
        color: #333;
      }
      .ta-tutor-msg {
        margin-bottom: 10px;
        padding: 10px 14px;
        border-radius: 12px;
        max-width: 90%;
        animation: taFadeIn 0.3s ease;
      }
      @keyframes taFadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
      .ta-tutor-msg.bot {
        background: #f0f9e8;
        align-self: flex-start;
        margin-right: auto;
      }
      .ta-tutor-msg.user {
        background: #e8f0ff;
        align-self: flex-end;
        margin-left: auto;
        text-align: right;
      }
      .ta-tutor-input-row {
        display: flex;
        gap: 8px;
      }
      .ta-tutor-input {
        flex: 1;
        padding: 10px 14px;
        border: 2px solid #ddd;
        border-radius: 10px;
        font-size: 15px;
        font-family: inherit;
        outline: none;
        transition: border-color 0.2s;
      }
      .ta-tutor-input:focus {
        border-color: #ff6b6b;
      }
      .ta-tutor-btn {
        padding: 10px 20px;
        background: linear-gradient(135deg, #ff6b6b, #e84a4a);
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        transition: opacity 0.2s;
        white-space: nowrap;
      }
      .ta-tutor-btn:hover { opacity: 0.88; }
      .ta-tutor-btn:active { transform: scale(0.97); }
      .ta-tutor-quick-qs {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 8px;
      }
      .ta-tutor-quick-q {
        padding: 5px 12px;
        background: #fff8e0;
        border: 1px solid #ffe66d;
        border-radius: 16px;
        font-size: 12px;
        color: #8a6d00;
        cursor: pointer;
        transition: background 0.15s;
      }
      .ta-tutor-quick-q:hover { background: #ffecb3; }
    </style>
    <div class="ta-tutor-card">
      <div class="ta-tutor-header">
        <div class="ta-tutor-avatar">🧑‍🏫</div>
        <div>
          <div class="ta-tutor-title">AI 数学学伴</div>
          <div class="ta-tutor-subtitle">小数加减法专属 · 先给提示不打答案</div>
        </div>
      </div>
      <div class="ta-tutor-chat" id="ta-tutor-chat"></div>
      <div class="ta-tutor-input-row">
        <input class="ta-tutor-input" id="ta-tutor-input" placeholder="说出你的问题，比如「3.5+2怎么算」…" />
        <button class="ta-tutor-btn" id="ta-tutor-send">➤</button>
      </div>
      <div class="ta-tutor-quick-qs" id="ta-tutor-quicks"></div>
    </div>
  `;

  const chat     = document.getElementById('ta-tutor-chat');
  const inputEl  = document.getElementById('ta-tutor-input');
  const sendBtn  = document.getElementById('ta-tutor-send');
  const quickRow = document.getElementById('ta-tutor-quicks');

  // ─── Quick questions ───
  const quickQs = [
    { label: '❶ 小数点对齐怎么对？', q: '小数点对齐' },
    { label: '❷ 整数减小数怎么做？', q: '整数减小数' },
    { label: '❸ 位数不同怎么办？', q: '位数不同' },
    { label: '❹ 3.5+2 是多少？',   q: '3.5 + 2' },
    { label: '❺ 混合运算顺序？',   q: '混合运算' },
    { label: '❻ 进位怎么处理？',   q: '进位' },
  ];
  quickRow.innerHTML = quickQs.map(q =>
    `<span class="ta-tutor-quick-q" data-q="${q.q}">${q.label}</span>`
  ).join('');

  // ─── Chat logic ───
  function addMsg(text, cls) {
    const div = document.createElement('div');
    div.className = 'ta-tutor-msg ' + (cls || 'bot');
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
  }

  function botReply(input) {
    const s = input.replace(/\s+/g, '').toLowerCase();
    let found = null;

    // Keyword matching
    for (const [kw, info] of Object.entries(KB.topics)) {
      if (s.includes(kw) || kw.includes(s) || s.includes(kw.replace(/[等怎]/g,''))) {
        found = info;
        break;
      }
    }
    // Problem matching
    if (!found) {
      for (const [p, ans] of Object.entries(KB.problems)) {
        if (s.includes(p.replace(/\s+/g,'')) || p.replace(/\s+/g,'').includes(s)) {
          found = { short: ans, tip: '' };
          break;
        }
      }
    }

    if (found) {
      addMsg(found.short + (found.tip ? '\n\n💡 ' + found.tip : ''), 'bot');
    } else if (s.length < 3) {
      addMsg('可以把问题再说详细一点吗？比如「小数点怎么对齐」「3.5+2.7等于多少」～', 'bot');
    } else {
      addMsg('这个问题很棒！试试这样想：\n1️⃣ 先对齐小数点（个位对个位、十分位对十分位）\n2️⃣ 从最低位开始加减\n3️⃣ 满十进一、不够借一\n\n你再试试看？卡在哪一步告诉我～', 'bot');
    }
  }

  function handleSend() {
    const txt = inputEl.value.trim();
    if (!txt) return;
    addMsg(txt, 'user');
    inputEl.value = '';
    setTimeout(() => botReply(txt), 400);
  }

  sendBtn.addEventListener('click', handleSend);
  inputEl.addEventListener('keydown', e => { if (e.key === 'Enter') handleSend(); });

  quickRow.addEventListener('click', e => {
    const el = e.target.closest('.ta-tutor-quick-q');
    if (!el) return;
    const q = el.dataset.q;
    addMsg(q, 'user');
    setTimeout(() => botReply(q), 400);
  });

  // ─── Init ───
  addMsg(greetings[Math.floor(Math.random() * greetings.length)], 'bot');
})();
