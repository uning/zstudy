# -*- coding: utf-8 -*-
import re, json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ============ 每课专属数据 ============
DATA = {
"lesson-1": {
  "faq": [
    {"q":"什么是负数？","keys":["负数","什么叫","是什么","定义","意思"],
     "a":"负数是比0小的数，用来表示相反意义的量。比如零下5℃记作-5℃、亏了200元记作-200元。前面带'-'号的数就是负数。"},
    {"q":"0是正数还是负数？","keys":["0","零","分界","既不是","正负"],
     "a":"0既不是正数也不是负数，它是正数和负数的分界点。"},
    {"q":"负数怎么比较大小？","keys":["比较","大小","比大小","谁大","排序"],
     "a":"在数轴上，右边的数总比左边大。负数离0越远数值越小，比如 -5 < -2，-1 > -3。"},
    {"q":"负数能加减吗？","keys":["加减","运算","加法","减法","算"],
     "a":"可以。同号相加取共同符号：(-3)+(-5)=-8；异号相加看绝对值大的定符号：(-3)+5=2。"},
    {"q":"生活里哪里用负数？","keys":["生活","应用","例子","实际","温度","海拔","例子"],
     "a":"温度计（零下）、海拔（海平面以下）、账本（亏损/欠债）、电梯（B1地下层）、比赛净胜球。"}
  ],
  "quiz": [
    {"q":"-3 和 -7 哪个大？","options":["-3 更大","-7 更大","一样大"],"answer":0,
     "exp":"数轴上-3在-7的右边，所以-3 > -7。"},
    {"q":"0 是？","options":["正数","负数","既不是正数也不是负数"],"answer":2,
     "exp":"0是正负数的分界，两者都不是。"},
    {"q":"零下5℃记作？","options":["5℃","-5℃","0℃"],"answer":1,
     "exp":"零下用负号表示，记作-5℃。"}
  ],
  "graph": {"w":720,"h":360,"nodes":[
    {"id":"n_neg","label":"负数","x":295,"y":155,"w":130,"h":54,"color":"#FF6B6B",
     "desc":"比0小的数，表示相反意义的量，是本单元核心。","links":["n_int","n_zero","n_opp","n_axis","n_app"]},
    {"id":"n_int","label":"整数","x":300,"y":22,"w":110,"h":44,"color":"#a78bfa",
     "desc":"像…-2,-1,0,1,2…这样的数，包含正整数、0、负整数。","links":["n_neg"]},
    {"id":"n_zero","label":"0（分界）","x":55,"y":157,"w":120,"h":44,"color":"#4ECDC4",
     "desc":"正数和负数的分界点，既不是正也不是负。","links":["n_neg"]},
    {"id":"n_opp","label":"相反意义的量","x":290,"y":290,"w":140,"h":44,"color":"#f59e0b",
     "desc":"用正负数表示一对相反的量，如收入/支出、上升/下降。","links":["n_neg"]},
    {"id":"n_axis","label":"数轴","x":555,"y":90,"w":120,"h":44,"color":"#FF8A65",
     "desc":"直观比较正负数大小的工具，右边总比左边大。","links":["n_neg"]},
    {"id":"n_app","label":"温度·海拔应用","x":545,"y":250,"w":150,"h":44,"color":"#06b6d4",
     "desc":"负数在生活中的典型应用：零下温度、海平面以下。","links":["n_neg"]}
  ]}
},
"lesson-2": {
  "faq": [
    {"q":"平行四边形面积怎么算？","keys":["平行四边形","面积","公式"],
     "a":"面积 = 底 × 高。把平行四边形沿高剪开平移，可拼成长方形，所以面积=底×高。"},
    {"q":"三角形面积为什么除以2？","keys":["三角形","除以2","一半","公式","为什么"],
     "a":"两个完全一样的三角形可以拼成一个平行四边形，所以一个三角形面积 = 底×高÷2。"},
    {"q":"梯形面积怎么算？","keys":["梯形","公式","上底","下底"],
     "a":"面积 =（上底＋下底）× 高 ÷ 2。两个一样的梯形可拼成平行四边形，底=上底+下底。"},
    {"q":"高怎么找？","keys":["高","垂直","底","对应"],
     "a":"高是从底边向对边作的垂直线段。不同底边对应不同的高，计算时底和高必须配套。"},
    {"q":"这些公式有什么联系？","keys":["联系","关系","转化","通用"],
     "a":"都可看成'面积=底×高'的变形：平行四边形直接底×高，三角/梯形因拼接要÷2。"}
  ],
  "quiz": [
    {"q":"底6cm、高4cm的平行四边形面积是？","options":["10","24","12"],"answer":1,
     "exp":"平行四边形面积=底×高=6×4=24cm²。"},
    {"q":"底8cm、高5cm的三角形面积是？","options":["40","20","13"],"answer":1,
     "exp":"三角形面积=8×5÷2=20cm²。"},
    {"q":"上底3、下底7、高4的梯形面积是？","options":["20","40","10"],"answer":0,
     "exp":"(3+7)×4÷2=20。"}
  ],
  "graph": {"w":720,"h":360,"nodes":[
    {"id":"n_area","label":"多边形面积","x":290,"y":150,"w":150,"h":54,"color":"#FF6B6B",
     "desc":"本单元核心：用'底×高'思想统一推导各类图形面积。","links":["n_par","n_tri","n_tra","n_rect"]},
    {"id":"n_rect","label":"长方形面积","x":285,"y":22,"w":140,"h":44,"color":"#a78bfa",
     "desc":"长×宽，是所有图形面积推导的起点。","links":["n_area"]},
    {"id":"n_par","label":"平行四边形","x":40,"y":150,"w":130,"h":44,"color":"#4ECDC4",
     "desc":"面积=底×高（剪拼成长方形）。","links":["n_area"]},
    {"id":"n_tri","label":"三角形","x":285,"y":290,"w":130,"h":44,"color":"#f59e0b",
     "desc":"面积=底×高÷2（两个拼成平行四边形）。","links":["n_area"]},
    {"id":"n_tra","label":"梯形","x":550,"y":150,"w":130,"h":44,"color":"#06b6d4",
     "desc":"面积=(上底+下底)×高÷2。","links":["n_area"]}
  ]}
},
"lesson-3": {
  "faq": [
    {"q":"小数乘法怎么点小数点？","keys":["乘法","乘","小数点","位数","点"],
     "a":"先当整数相乘，再看两个因数一共有几位小数，就从积的右边起数出几位点上小数点。"},
    {"q":"小数除法怎么算？","keys":["除法","除","移动","转化"],
     "a":"除数是小数时，先把除数变成整数（小数点右移几位，被除数也右移几位），再按整数除法算。"},
    {"q":"积的小数位数不够怎么办？","keys":["不够","补零","前面","0"],
     "a":"用0补足。例如0.2×0.3=0.06，积应有2位小数，前面补0占位。"},
    {"q":"被除数位数不够怎么办？","keys":["被除数","补零","末尾","商"],
     "a":"在被除数的末尾用0补足，继续除。商的小数点要和被除数的新小数点对齐。"},
    {"q":"怎么判断积比原数大还是小？","keys":["比较","大于","小于","判断","大小"],
     "a":"乘大于1的数，积比原数大；乘小于1的数，积比原数小。除以同理反过来。"}
  ],
  "quiz": [
    {"q":"0.3 × 0.2 = ?","options":["0.6","0.06","0.006"],"answer":1,
     "exp":"先算3×2=6，两个因数共2位小数，得0.06。"},
    {"q":"把 1.2 ÷ 0.3 转化为整数除法，被除数小数点移几位？","options":["1位","2位","不动"],"answer":0,
     "exp":"除数0.3右移1位变3，被除数1.2也右移1位变12，算12÷3。"},
    {"q":"一个非零数乘0.5，结果？","options":["比原数大","比原数小","不变"],"answer":1,
     "exp":"0.5<1，乘小于1的数，积比原数小。"}
  ],
  "graph": {"w":720,"h":360,"nodes":[
    {"id":"n_dec","label":"小数乘除","x":290,"y":150,"w":140,"h":54,"color":"#FF6B6B",
     "desc":"先按整数算，再处理小数点位置，是本单元核心。","links":["n_mul","n_div","n_int","n_point"]},
    {"id":"n_mul","label":"小数乘法","x":40,"y":80,"w":130,"h":44,"color":"#4ECDC4",
     "desc":"先当整数乘，再数总小数位数点小数点。","links":["n_dec"]},
    {"id":"n_div","label":"小数除法","x":40,"y":240,"w":130,"h":44,"color":"#f59e0b",
     "desc":"除数化整数（同移小数点），再除。","links":["n_dec"]},
    {"id":"n_int","label":"整数乘除","x":550,"y":80,"w":130,"h":44,"color":"#a78bfa",
     "desc":"小数乘除建立在整数乘除法则之上。","links":["n_dec"]},
    {"id":"n_point","label":"小数点位置","x":550,"y":240,"w":140,"h":44,"color":"#06b6d4",
     "desc":"积的位数、商的对齐都取决于小数点处理。","links":["n_dec"]}
  ]}
},
"lesson-4": {
  "faq": [
    {"q":"小数加减法怎么对齐？","keys":["对齐","小数点","数位","竖式"],
     "a":"小数点对齐，也就是相同数位对齐。缺位用0补齐，再按整数加减法计算。"},
    {"q":"小数减法不够减怎么办？","keys":["减法","退位","借","不够"],
     "a":"从前一位借1当10（十分位借1当10个千分位等），和整数退位一样。"},
    {"q":"得数末尾的0要去掉吗？","keys":["末尾","化简","0","去掉","约分"],
     "a":"通常把末尾的0去掉化简，如 3.20 写成 3.2；但表示精度时可保留。"},
    {"q":"连加连减有简便方法吗？","keys":["简便","连加","连减","运算律","结合律"],
     "a":"有！加法可用交换律/结合律凑整；连减可用 a-b-c=a-(b+c)。"},
    {"q":"小数加减和整数加减一样吗？","keys":["一样","区别","整数","关系"],
     "a":"算理相同，关键都是相同数位对齐——整数靠末位对齐，小数靠小数点对齐。"}
  ],
  "quiz": [
    {"q":"计算 3.2 + 4.58，小数点对齐后哪位要补0？","options":["3.2补0成3.20","4.58补0","都不补"],"answer":0,
     "exp":"3.2写成3.20，与4.58同为两位小数再相加。"},
    {"q":"5.1 - 2.35 = ?","options":["2.75","3.25","2.85"],"answer":0,
     "exp":"5.10-2.35，退位后得2.75。"},
    {"q":"简便计算 8.4 - 3.2 - 1.8 可用？","options":["8.4-(3.2+1.8)","8.4-3.2+1.8","直接减"],"answer":0,
     "exp":"连减性质：a-b-c=a-(b+c)=8.4-5=3.4。"}
  ],
  "graph": {"w":720,"h":360,"nodes":[
    {"id":"n_add","label":"小数加减法","x":290,"y":150,"w":150,"h":54,"color":"#FF6B6B",
     "desc":"小数点对齐=相同数位对齐，是本单元核心。","links":["n_align","n_borrow","n_simp","n_int"]},
    {"id":"n_align","label":"小数点对齐","x":40,"y":80,"w":140,"h":44,"color":"#4ECDC4",
     "desc":"竖式中小数点对齐，缺位补0。","links":["n_add"]},
    {"id":"n_borrow","label":"退位借1","x":40,"y":240,"w":130,"h":44,"color":"#f59e0b",
     "desc":"不够减时向前一位借1当10。","links":["n_add"]},
    {"id":"n_simp","label":"末尾化简","x":550,"y":80,"w":130,"h":44,"color":"#a78bfa",
     "desc":"去掉得数末尾无用的0。","links":["n_add"]},
    {"id":"n_int","label":"整数加减","x":550,"y":240,"w":130,"h":44,"color":"#06b6d4",
     "desc":"算理相同，只是对齐方式不同。","links":["n_add"]}
  ]}
},
"lesson-5": {
  "faq": [
    {"q":"什么时候用列举策略？","keys":["什么时候","何用","列举","策略","用"],
     "a":"当问题答案有多种可能、或要找'一共有几种'时，用一一列举把所有可能列出来。"},
    {"q":"列举要注意什么？","keys":["注意","有序","遗漏","重复","不重不漏"],
     "a":"要有顺序地列举，才能不重复、不遗漏。常用列表或画图帮助有序思考。"},
    {"q":"怎么做到不重复不遗漏？","keys":["不重复","不遗漏","有序","方法"],
     "a":"固定一个顺序（如从大到小），每步只变一个量，配合表格记录已列的项。"},
    {"q":"列举和搭配问题怎么算总数？","keys":["搭配","总数","乘法","乘"],
     "a":"分类列举后相加；若是分步选择（如上衣×裤子），可用乘法算总数。"},
    {"q":"怎么从列举里找最值？","keys":["最值","最大","最小","找","面积"],
     "a":"列出所有可能后比较，如围长方形时逐一算面积，取最大或最小的那组。"}
  ],
  "quiz": [
    {"q":"22根1米木条围长方形，求最大面积，最好用？","options":["一一列举","瞎猜","只算一种"],"answer":0,
     "exp":"长+宽=11，列举(1,10)(2,9)…(5,6)比较面积，最大30㎡。"},
    {"q":"上衣3件、裤子2件，搭配总数？","options":["5","6","3"],"answer":1,
     "exp":"分步选择用乘法：3×2=6种搭配。"},
    {"q":"列举最重要的是？","options":["快","有序不重不漏","多写"],"answer":1,
     "exp":"有序才能不重复、不遗漏，这是列举策略的精髓。"}
  ],
  "graph": {"w":720,"h":360,"nodes":[
    {"id":"n_list","label":"列举策略","x":290,"y":150,"w":140,"h":54,"color":"#FF6B6B",
     "desc":"把所有可能有序地列出来，解决'有几种'的问题。","links":["n_when","n_order","n_tool","n_best"]},
    {"id":"n_when","label":"何时用","x":40,"y":80,"w":130,"h":44,"color":"#4ECDC4",
     "desc":"答案有多种可能、求总数或最值时使用。","links":["n_list"]},
    {"id":"n_order","label":"有序不重不漏","x":40,"y":240,"w":150,"h":44,"color":"#f59e0b",
     "desc":"固定顺序列举，避免重复和遗漏。","links":["n_list"]},
    {"id":"n_tool","label":"列表/画图辅助","x":550,"y":80,"w":150,"h":44,"color":"#a78bfa",
     "desc":"用表格或画图让列举更清晰有序。","links":["n_list"]},
    {"id":"n_best","label":"找最值","x":550,"y":240,"w":130,"h":44,"color":"#06b6d4",
     "desc":"列举后比较，取最大/最小。","links":["n_list"]}
  ]}
}
}

ENGINE = r"""
<script>
const COURSE_DATA = __DATA__;
(function(){
  const NS='http://www.w3.org/2000/svg';
  function el(t,a){const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);return e;}
  function findAnswer(text){
    text=(text||'').trim(); if(!text) return null;
    let best=null,bs=0;
    const low=text.toLowerCase();
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
    const f=findAnswer(v);
    bubble('user',v);
    if(f) bubble('bot',f.a);
    else bubble('bot','这个问题我还在学习～你可以先点下面的常见问题，或换个说法问我 😊');
  }
  function renderChips(){
    const c=document.getElementById('tutorChips'); if(!c)return; c.innerHTML='';
    COURSE_DATA.faq.forEach(f=>{ const b=document.createElement('button'); b.className='tutor-chip'; b.textContent=f.q; b.onclick=()=>showFaq(f); c.appendChild(b); });
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
      grp.addEventListener('click',()=>selectNode(n.id));
      svg.appendChild(grp);
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
  // init
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

TUTOR_SECTION = """
  <div class="slide-inner">
    <div class="card card-glow">
      <div class="section-header">
        <span class="phase-tag" data-variant="purple">AI Tutor</span>
        <h2>AI 学伴 🤖</h2>
      </div>
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
      <div class="section-header">
        <span class="phase-tag" data-variant="purple">Knowledge Graph</span>
        <h2>知识图谱 🗺️</h2>
      </div>
      <p style="color:var(--muted);margin:0 0 4px">点击任意节点查看讲解，关联节点会自动高亮：</p>
      <div class="kg-wrap">
        <div class="kg-svg" id="kgSvg"></div>
        <div class="kg-info" id="kgInfo"><p style="color:var(--muted);margin:0">👆 选择一个节点查看详情</p></div>
      </div>
    </div>
  </div>
"""

def replace_section(html, tsh, new_inner):
    pat = re.compile(r'<section([^>]*data-tsh="%s"[^>]*)>.*?</section>' % re.escape(tsh), re.S)
    return pat.sub(lambda m: '<section'+m.group(1)+'>'+new_inner+'</section>', html, count=1)

for L, d in DATA.items():
    path = os.path.join(ROOT, L, "index.html")
    if not os.path.exists(path):
        print("跳过(无文件):", L); continue
    html = open(path, encoding='utf-8').read()
    # 替换两页 inner
    html = replace_section(html, "AI学伴", TUTOR_SECTION)
    html = replace_section(html, "知识图谱", GRAPH_SECTION)
    # 注入 style（放在 </head> 前）
    html = html.replace("</head>", STYLE + "</head>", 1)
    # 注入 engine（含数据）放在 </body> 前
    engine = ENGINE.replace("__DATA__", json.dumps(d, ensure_ascii=False))
    html = html.replace("</body>", engine + "</body>", 1)
    open(path, 'w', encoding='utf-8').write(html)
    kb = len(html.encode('utf-8'))//1024
    print("✅ %s 注入完成 ≈%dKB" % (L, kb))
print("全部处理完毕")
