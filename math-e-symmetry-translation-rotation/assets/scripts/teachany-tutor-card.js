/* TeachAny AI Tutor Card - 旋转、对称与平移 */
(function() {
  'use strict';

  const container = document.querySelector('[data-teachany-tutor-card]');
  if (!container) return;

  // ─── Knowledge base ───
  const KB = {
    topics: {
      '轴对称': {
        short: '轴对称是指图形沿一条直线（对称轴）对折后，两边能完全重合。就像蝴蝶的两只翅膀，关于身体中线完全对称！',
        tip: '判断一个问题：对折后两边能完全重合吗？能→轴对称，不能→不是轴对称。'
      },
      '对称轴': {
        short: '对称轴就是对折的那条"线"。正方形有4条对称轴（横、竖、两条对角线），长方形有2条，等边三角形有3条，圆形有无数条！',
        tip: '判断对称轴数量的方法：横着折、竖着折、斜着折……逐一检查，看折完后两边是否重合。'
      },
      '平移': {
        short: '平移是图形沿直线方向移动，只改变位置，大小、形状、方向都不变。就像推箱子——箱子换了位置，但大小还是那么大！',
        tip: '平移三不变：大小不变、形状不变、方向不变。只有一个变了：位置。考试常考："平移后图形变大了对吗？"——当然不对！'
      },
      '旋转': {
        short: '旋转是图形绕着一个固定点（旋转中心）转动。旋转后图形方向变了，但大小和形状不变。关键要素：旋转中心、旋转方向、旋转角度。',
        tip: '时钟指针、风车、摩天轮都是旋转的例子。旋转三要素：①绕哪个点转？②顺时针还是逆时针？③转了多少度？'
      },
      '区分三种变换': {
        short: '平移：物体沿直线滑动，只看位置变了没。旋转：物体绕点转动，看方向变了没。轴对称：对折后两边重合，看有没有对称轴。',
        tip: '分不清时用三问法：①位置变了吗？→平移 ②方向变了吗？→旋转 ③两边能对折重合吗？→轴对称。注意：三种变换都不改变图形大小和形状！'
      },
      '旋转中心': {
        short: '旋转中心就是图形旋转时绕着的那个固定点。同一个图形，绕不同的中心点旋转，结果完全不一样！在GeoGebra页面试试看~',
        tip: '比如一个三角形绕顶点旋转和绕中心旋转，画出来的图形完全不同。所以描述旋转时一定要说清楚"绕哪个点转"。'
      },
      '方格纸平移': {
        short: '在方格纸上平移图形时，先数清楚每个顶点要移几格，然后把每个顶点都移到新位置，最后连线。所有顶点移动的格数和方向都一样！',
        tip: '关键步骤：①选一个顶点 ②数方格移过去 ③其他顶点照着移相同格数 ④连线成形。记住：所有顶点移动的距离和方向必须一致！'
      },
      '旋转画法': {
        short: '画出旋转后的图形：①找到旋转中心 ②连接中心和关键顶点 ③将连线按指定方向和角度旋转 ④在新位置画出顶点 ⑤连线成形。',
        tip: '在GeoGebra里拖动滑块观察每个点的运动轨迹，这样比纸上画更直观！'
      }
    },
    problems: {
      '正方形有几条对称轴': '正方形有4条对称轴！横着1条、竖着1条、两条对角线各1条。长方形只有2条（横竖各1），因为长方形对角线不对折重合。',
      '电梯是什么变换': '电梯上下是平移现象！电梯沿垂直方向直线移动，只改变位置，大小、形状、方向都不变。这就是典型的平移。',
      '摩天轮是什么变换': '摩天轮是旋转！摩天轮上的小房子绕着摩天轮中心转动——有旋转中心、有转动方向、有角度。小房子的方向一直在变，但大小不变。',
      '蝴蝶翅膀': '蝴蝶翅膀是轴对称的经典例子！把蝴蝶沿身体中线对折，左边翅膀和右边翅膀完全重合，这条中线就是对称轴。',
      '推窗是旋转还是平移': '推窗多数是旋转——窗户绕着合页（铰链）这个轴转动。但也有推拉窗是平移哦。判断方法：看窗户是"转"还是"滑"。'
    },
    general: '我是你的数学学伴！关于轴对称、平移和旋转有什么问题都可以问我。我会先给你一个提示，帮你理清思路～'
  };

  const greetings = [
    '👋 图形变换有什么不懂的？先说说你卡在哪里～',
    '🤔 平移、旋转、对称分不清？试试描述一下你看到的现象～',
    '💡 图形变换的秘诀：平移看位置，旋转看方向，对称看对折！你有什么想问的？'
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
          <div class="ta-tutor-subtitle">图形变换专属 · 先给提示不打答案</div>
        </div>
      </div>
      <div class="ta-tutor-chat" id="ta-tutor-chat"></div>
      <div class="ta-tutor-input-row">
        <input class="ta-tutor-input" id="ta-tutor-input" placeholder="说出你的问题，比如「正方形有几条对称轴」…" />
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
    { label: '❶ 什么是轴对称？', q: '什么是轴对称' },
    { label: '❷ 正方形有几条对称轴？', q: '正方形有几条对称轴' },
    { label: '❸ 平移和旋转怎么区分？', q: '平移和旋转怎么区分' },
    { label: '❹ 电梯是什么变换？', q: '电梯是什么变换' },
    { label: '❺ 旋转有哪些要素？', q: '旋转有哪些要素' },
    { label: '❻ 蝴蝶是什么变换？', q: '蝴蝶翅膀是什么变换' },
  ];
  quickRow.innerHTML = quickQs.map(function(q) {
    return '<span class="ta-tutor-quick-q" data-q="'+q.q+'">'+q.label+'</span>';
  }).join('');

  // ─── Chat logic ───
  function addMsg(text, cls) {
    var div = document.createElement('div');
    div.className = 'ta-tutor-msg ' + (cls || 'bot');
    div.textContent = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
  }

  function botReply(input) {
    var s = input.replace(/\s+/g, '').toLowerCase();
    var found = null;

    // Topic matching
    var topicKeys = Object.keys(KB.topics);
    for (var i = 0; i < topicKeys.length; i++) {
      var kw = topicKeys[i];
      if (s.indexOf(kw) >= 0 || kw.indexOf(s) >= 0 || s.indexOf(kw.replace(/[等怎]/g,'')) >= 0) {
        found = KB.topics[kw];
        break;
      }
    }
    // Problem matching
    if (!found) {
      var probKeys = Object.keys(KB.problems);
      for (var j = 0; j < probKeys.length; j++) {
        var p = probKeys[j];
        if (s.indexOf(p.replace(/\s+/g,'')) >= 0 || p.replace(/\s+/g,'').indexOf(s) >= 0) {
          found = { short: KB.problems[p], tip: '' };
          break;
        }
      }
    }

    if (found) {
      addMsg(found.short + (found.tip ? '\n\n💡 ' + found.tip : ''), 'bot');
    } else if (s.length < 3) {
      addMsg('可以把问题再说详细一点吗？比如「对称轴怎么找」「平移有什么特点」～', 'bot');
    } else {
      addMsg('这个问题很棒！试试这样想：\n1️⃣ 它是不是沿直线滑动？→ 平移\n2️⃣ 它是不是绕着点转动？→ 旋转\n3️⃣ 对折后两边能不能重合？→ 轴对称\n\n三种变换的共同点是：都不改变图形的大小和形状！你再想想看～', 'bot');
    }
  }

  function handleSend() {
    var txt = inputEl.value.trim();
    if (!txt) return;
    addMsg(txt, 'user');
    inputEl.value = '';
    setTimeout(function() { botReply(txt); }, 400);
  }

  sendBtn.addEventListener('click', handleSend);
  inputEl.addEventListener('keydown', function(e) { if (e.key === 'Enter') handleSend(); });

  quickRow.addEventListener('click', function(e) {
    var el = e.target.closest('.ta-tutor-quick-q');
    if (!el) return;
    var q = el.dataset.q;
    addMsg(q, 'user');
    setTimeout(function() { botReply(q); }, 400);
  });

  // ─── Init ───
  addMsg(greetings[Math.floor(Math.random() * greetings.length)], 'bot');
})();
