/* TeachAny AI Tutor Card - DeepSeek V4-Pro powered (self-contained) */
(function() {
  'use strict';

  const container = document.querySelector('[data-teachany-tutor-card]');
  if (!container) return;

  // ═══════════════════════════════════════════════════════════════
  //  DeepSeek API 配置
  //  ⚠️ 安全提示：此 Key 会随前端源码公开，切勿用于生产环境。
  //  生产环境应通过后端（如 CloudBase 云函数）中转，Key 只存服务端。
  // ═══════════════════════════════════════════════════════════════
  const CONFIG = {
    endpoint: 'https://api.deepseek.com/chat/completions',
    apiKey: 'sk-a276267cef5c4e92a61cd9f376d3240e',
    model: 'deepseek-v4-pro',
    maxTokens: 600,
    temperature: 0.7
  };

  // 系统提示词：把学伴约束为「小数加减法」专属数学老师
  const SYSTEM_PROMPT = [
    '你是一位耐心的小学五年级数学学伴，正在辅导学生《小数加法和减法》（苏教版五年级上册第4单元）。',
    '教学原则：',
    '1. 先引导学生思考，不要直接给答案；先给一个提示或反问他"第一步该做什么"。',
    '2. 学生明显卡住或反复求助时，再分步骤讲解。',
    '3. 核心知识点：小数点对齐＝相同数位对齐（不是末位对齐）；位数不同时末尾补0；整数减小数要补小数点和0（如5＝5.0）；满十进一、不够借一当十；混合运算从左到右、有括号先算括号。',
    '4. 常见易错点：末位对齐误区、整数减小数忘记补0、退位忘记借1。',
    '5. 语气活泼亲切，适合小学生，适当用emoji，回答简洁，一次不要超过120字。'
  ].join('\n');

  // ─── 本地知识库（离线兜底 + 高频问题秒回）───
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
    }
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
        white-space: pre-wrap;
        word-break: break-word;
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
      .ta-tutor-msg.thinking {
        background: #f5f5f5;
        color: #999;
        font-style: italic;
        align-self: flex-start;
        margin-right: auto;
      }
      .ta-tutor-msg.error {
        background: #fff0f0;
        color: #c0392b;
        align-self: flex-start;
        margin-right: auto;
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
      .ta-tutor-btn:disabled { opacity: 0.5; cursor: not-allowed; }
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
          <div class="ta-tutor-subtitle">DeepSeek V4-Pro · 小数加减法专属 · 先给提示不打答案</div>
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
    return div;
  }

  // 本地知识库匹配，命中返回内容，未命中返回 null
  function matchLocal(input) {
    const s = input.replace(/\s+/g, '').toLowerCase();
    for (const [kw, info] of Object.entries(KB.topics)) {
      if (s.includes(kw) || kw.includes(s)) {
        return info.short + (info.tip ? '\n\n💡 ' + info.tip : '');
      }
    }
    for (const [p, ans] of Object.entries(KB.problems)) {
      const pp = p.replace(/\s+/g, '');
      if (s.includes(pp) || pp.includes(s)) {
        return ans;
      }
    }
    return null;
  }

  // 调用 DeepSeek API
  async function callDeepSeek(input) {
    const resp = await fetch(CONFIG.endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + CONFIG.apiKey
      },
      body: JSON.stringify({
        model: CONFIG.model,
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: input }
        ],
        stream: false,
        max_tokens: CONFIG.maxTokens,
        temperature: CONFIG.temperature,
        thinking: { type: 'disabled' }
      })
    });

    if (!resp.ok) {
      const code = resp.status;
      if (code === 401) throw new Error('auth');
      if (code === 402) throw new Error('balance');
      if (code === 429) throw new Error('rate');
      throw new Error('http_' + code);
    }

    const data = await resp.json();
    const content = data.choices && data.choices[0] && data.choices[0].message
      ? data.choices[0].message.content
      : '';
    return (content || '').trim();
  }

  async function botReply(input) {
    // 1) 本地知识库秒回（高频问题）
    const local = matchLocal(input);
    if (local) {
      addMsg(local, 'bot');
      return;
    }

    // 2) 调用 DeepSeek API
    const thinkingEl = addMsg('🤔 思考中…', 'thinking');
    sendBtn.disabled = true;
    try {
      const answer = await callDeepSeek(input);
      thinkingEl.remove();
      if (answer) {
        addMsg(answer, 'bot');
      } else {
        addMsg('我一时没想好，换个问法再试试？或者点下面的快捷问题～', 'bot');
      }
    } catch (err) {
      thinkingEl.remove();
      const map = {
        auth: '⚠️ 学伴的钥匙失效了，请联系老师更新。',
        balance: '⚠️ 学伴的余额用完了，请联系老师充值。',
        rate: '⚠️ 学伴太忙了，稍等一下再问我～',
      };
      addMsg(map[err.message] || '⚠️ 网络开小差了，先点下面的快捷问题试试，或稍后重试～', 'error');
    } finally {
      sendBtn.disabled = false;
    }
  }

  function handleSend() {
    const txt = inputEl.value.trim();
    if (!txt) return;
    addMsg(txt, 'user');
    inputEl.value = '';
    setTimeout(() => botReply(txt), 300);
  }

  sendBtn.addEventListener('click', handleSend);
  inputEl.addEventListener('keydown', e => { if (e.key === 'Enter') handleSend(); });

  quickRow.addEventListener('click', e => {
    const el = e.target.closest('.ta-tutor-quick-q');
    if (!el) return;
    const q = el.dataset.q;
    addMsg(q, 'user');
    setTimeout(() => botReply(q), 300);
  });

  // ─── Init ───
  addMsg(greetings[Math.floor(Math.random() * greetings.length)], 'bot');
})();
