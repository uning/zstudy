/* TeachAny AI Tutor Card - 平面直角坐标系 */
(function() {
  'use strict';
  var container = document.querySelector('[data-teachany-tutor-card]');
  if (!container) return;

  var KB = {
    topics: {
      'x轴': {short:'x轴是坐标系中水平的数轴（横轴）。向右为正方向，向左为负。x轴上的点y坐标恒为0。',tip:'口诀：x横→水平，y=0。比如(3,0)、(0,0)、(-5,0)都在x轴上。'},
      'y轴': {short:'y轴是坐标系中竖直的数轴（纵轴）。向上为正方向，向下为负。y轴上的点x坐标恒为0。',tip:'口诀：y纵→竖直，x=0。比如(0,4)、(0,-2)、(0,0)都在y轴上。'},
      '原点': {short:'原点O是x轴和y轴的交点，坐标是(0,0)。它是所有坐标的基准点。',tip:'任何点在原点右边→x为正；左边→x为负。上方→y为正；下方→y为负。'},
      '象限': {short:'两轴把平面分成四个象限，逆时针编号：Ⅰ(+,+)右上、Ⅱ(-,+)左上、Ⅲ(-,-)左下、Ⅳ(+,-)右下。',tip:'象限口诀：右上正正一，左上负正二，左下负负三，右下正负四。逆时针转一圈！'},
      '有序数对': {short:'(x,y)称为有序数对。x是横坐标在前，y是纵坐标在后，顺序不能换！(2,3)≠(3,2)。',tip:'类比电影票："5排8座"≠"8排5座"。排在前=横坐标，座在后=纵坐标。'},
      '描点': {short:'描点三步：①在x轴上找横坐标→画竖直线 ②在y轴上找纵坐标→画水平线 ③两条线的交点就是点！',tip:'口诀"先横后纵"：先在x轴找到x的值，画出过该点且垂直于x轴的直线；再到y轴找到y的值同理。'},
      '距离': {short:'水平两点的距离=|x₂-x₁|，竖直两点的距离=|y₂-y₁|。斜线上用勾股定理√(Δx²+Δy²)。',tip:'先判断是水平（y相同）、竖直（x相同）还是斜线，再选对应公式。别忘取绝对值！'},
      '符号规律': {short:'象限符号：Ⅰ(+,+) Ⅱ(-,+) Ⅲ(-,-) Ⅳ(+,-)。x轴y=0，y轴x=0。',tip:'y>0在上半平面，y<0在下半平面。x>0在右半平面，x<0在左半平面。'}
    },
    problems: {
      '(2,5)在哪个象限':'x=2>0, y=5>0 → (+,+) → 第一象限。',
      '(-3,4)':'x=-3<0, y=4>0 → (-,+) → 第二象限。',
      '(0,7)在哪个位置':'x=0说明在y轴上。y轴上的点不属于任何象限！',
      '(5,-2)和(5,3)的距离':'x都是5→竖直线。距离=|3-(-2)|=|5|=5。'
    }
  };

  var greetings = ['👋 坐标系有什么疑问？说说你在哪一步卡住了～','🤔 象限判断还是描点方法不熟悉？直接问！','💡 坐标系秘诀：先横后纵描点，逆时针记象限，x轴横y轴纵。你哪里不懂？'];

  container.innerHTML = '<style id="ta-tutor-inline-css">.ta-tutor-card{background:#fff;border-radius:14px;border:2px solid #e2e8f0;padding:24px;max-width:680px;margin:0 auto;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;box-shadow:0 1px 8px rgba(0,0,0,0.06)}.ta-tutor-header{display:flex;align-items:center;gap:12px;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid #e2e8f0}.ta-tutor-avatar{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#3b82f6,#1d4ed8);display:flex;align-items:center;justify-content:center;font-size:22px;color:#fff;flex-shrink:0}.ta-tutor-title{font-weight:700;font-size:17px;color:#1e293b}.ta-tutor-subtitle{font-size:12px;color:#94a3b8}.ta-tutor-chat{background:#f8fafc;border-radius:10px;padding:16px;min-height:80px;max-height:280px;overflow-y:auto;margin-bottom:12px;font-size:15px;line-height:1.7;color:#334155}.ta-tutor-msg{margin-bottom:10px;padding:10px 14px;border-radius:10px;max-width:90%;animation:taFI .3s ease}@keyframes taFI{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}.ta-tutor-msg.bot{background:#eff6ff;margin-right:auto}.ta-tutor-msg.user{background:#e8f0ff;margin-left:auto;text-align:right}.ta-tutor-input-row{display:flex;gap:8px}.ta-tutor-inp{flex:1;padding:10px 14px;border:2px solid #e2e8f0;border-radius:10px;font-size:15px;font-family:inherit;outline:0;transition:border-color .2s}.ta-tutor-inp:focus{border-color:#3b82f6}.ta-tutor-btn{padding:10px 20px;background:linear-gradient(135deg,#3b82f6,#2563eb);color:#fff;border:0;border-radius:10px;font-size:15px;font-weight:600;cursor:pointer;transition:opacity .2s;white-space:nowrap}.ta-tutor-btn:hover{opacity:.88}.ta-tutor-quick{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}.ta-tutor-q{padding:5px 12px;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:14px;font-size:12px;color:#475569;cursor:pointer;transition:background .15s}.ta-tutor-q:hover{background:#e0e7ff;border-color:#3b82f6}</style><div class="ta-tutor-card"><div class="ta-tutor-header"><div class="ta-tutor-avatar">🧑‍🏫</div><div><div class="ta-tutor-title">AI 数学学伴</div><div class="ta-tutor-subtitle">坐标系专属 · 先给提示不打答案</div></div></div><div class="ta-tutor-chat" id="ta-chat"></div><div class="ta-tutor-input-row"><input class="ta-tutor-inp" id="ta-inp" placeholder="问坐标问题，如「(2,5)在哪个象限」"><button class="ta-tutor-btn" id="ta-send">➤</button></div><div class="ta-tutor-quick" id="ta-quicks"></div></div>';

  var chat=document.getElementById('ta-chat'),inp=document.getElementById('ta-inp'),qr=document.getElementById('ta-quicks');
  var qqs=[{l:'❶ x轴和y轴是什么？',q:'x轴'},{l:'❷ 怎么判断象限？',q:'象限'},{l:'❸ (2,5)在哪个象限？',q:'(2,5)在哪个象限'},{l:'❹ 怎么描点？',q:'描点'},{l:'❺ (0,7)在什么位置？',q:'(0,7)在哪个位置'},{l:'❻ 两点间距离怎么算？',q:'距离'}];
  qr.innerHTML=qqs.map(function(q){return '<span class="ta-tutor-q" data-q="'+q.q+'">'+q.l+'</span>';}).join('');

  function add(t,c){var d=document.createElement('div');d.className='ta-tutor-msg '+(c||'bot');d.textContent=t;chat.appendChild(d);chat.scrollTop=chat.scrollHeight;}
  function reply(s){
    s=s.replace(/\s+/g,'').toLowerCase();
    var found=null,tk=Object.keys(KB.topics);
    for(var i=0;i<tk.length;i++){if(s.indexOf(tk[i])>=0||tk[i].indexOf(s)>=0){found=KB.topics[tk[i]];break;}}
    if(!found){var pk=Object.keys(KB.problems);for(var j=0;j<pk.length;j++){if(s.indexOf(pk[j].replace(/\s+/g,''))>=0){found={short:KB.problems[pk[j]],tip:''};break;}}}
    if(found) add(found.short+(found.tip?'\n\n💡 '+found.tip:''),'bot');
    else if(s.length<3) add('说详细一点好吗？比如「象限怎么记」「(2,5)在哪个象限」～','bot');
    else add('这个问题很好！坐标系核心：\n1️⃣ x轴横（水平），y轴纵（竖直），交于原点O(0,0)\n2️⃣ 四个象限逆时针编号，符号：Ⅰ(+,+) Ⅱ(-,+) Ⅲ(-,-) Ⅳ(+,-)\n3️⃣ 描点先横后纵，有序数对(x,y)不可交换\n\n你具体卡在哪一点？','bot');
  }
  function send(){var t=inp.value.trim();if(!t)return;add(t,'user');inp.value='';setTimeout(function(){reply(t);},400);}
  document.getElementById('ta-send').addEventListener('click',send);
  document.getElementById('ta-inp').addEventListener('keydown',function(e){if(e.key==='Enter')send();});
  qr.addEventListener('click',function(e){var el=e.target.closest('.ta-tutor-q');if(!el)return;var q=el.dataset.q;add(q,'user');setTimeout(function(){reply(q);},400);});
  add(greetings[Math.floor(Math.random()*greetings.length)],'bot');
})();
