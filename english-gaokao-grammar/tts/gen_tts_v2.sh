#!/usr/bin/env bash
# v1.1：生成 15 个专题朗读音频 t01-t15，并重新生成 s13/s14（练习与总结更新版）
set -e
PY=/Users/playcrab/.workbuddy/binaries/python/versions/3.13.12/bin/python3
TTS=/Users/playcrab/.workbuddy/skills/teachany/scripts/tts-engine.py
DIR="$(cd "$(dirname "$0")" && pwd)"
VOICE="zh-CN-XiaoyiNeural"

gen() {
  local id="$1"; shift
  local text="$1"; shift
  echo "==> $id"
  "$PY" "$TTS" --text "$text" --voice "$VOICE" --output "$DIR/$id.mp3"
}

gen t01 "专题一，构词法。英语构词有三招：派生、合成、转化。派生是加词缀，比如 care 加 ful 变形容词 careful，再加 ly 变副词 carefully。合成是两词合一，比如 class 加 room。转化是词性直接变，比如 water 从名词变动词。高考语法填空的口诀是：先定句子成分，再选词性，最后变形。"
gen t02 "专题二，名词。可数名词变复数：一般加 s；s、x、ch、sh 结尾加 es；辅音加 y 变 ies；f 结尾常变 ves。不规则变化要死记：child 变 children，sheep 不变。高频不可数名词：information、advice、news、progress，永远不加 s。所有格记住：有生命用撇号 s，无生命用 of，还有双重所有格 a friend of mine。"
gen t03 "专题三，冠词。a 和 an 表泛指，an 看发音不看字母：an hour，但 a university。the 表特指，用于独一无二的事物、序数词、最高级和乐器前。零冠词用于球类、三餐、学科和 by 加交通工具。特别注意：in hospital 是住院，in the hospital 只是在医院里，一个 the 之差，意思完全不同。"
gen t04 "专题四，代词。人称代词四格：主格作主语，宾格作宾语，形容词性物主代词后接名词，名词性物主代词后不接名词。不定代词高频组：both、either、neither 用于两者；another、the other、others 要分清范围。it 有三大身份：指天气时间距离，作形式主语形式宾语，以及强调句的骨架。经典陷阱：its 是它的，it's 才是 it is。"
gen t05 "专题五，介词。介词后面必须接名词或代词作宾语。时间介词辨析是必考：in 接年月季节，on 接具体某天，at 接时刻点。固定搭配要成组记：depend on、succeed in、be famous for。介词加 which 或 whom 可以引导定语从句。语法填空没有提示词的空，优先考虑介词、冠词和连接词。"
gen t06 "专题六，时态。四种时间乘四种状态，等于十六个时态。高考高频七个：一般现在、现在完成、现在进行、一般过去、过去完成、过去进行和一般将来。必考辨析：有 since 或 so far 用现在完成时；有 yesterday、ago 等明确过去时间，用一般过去时；by 加过去时间用过去完成时。点击矩阵格子，可以看到每个时态的构成和例句。"
gen t07 "专题七，被动语态。公式是 be 加过去分词。十六个时态中只有十个有被动：四个完成进行时、将来进行时和过去将来进行时都没有被动，因为两个 be 连在一起没法读。特殊考点：The book sells well 主动形式表被动；need doing 等于 need to be done；系动词 taste、feel 没有被动；短语动词变被动时介词不能丢。"
gen t08 "专题八，非谓语动词。三步判断法：第一步找逻辑主语，第二步判主被动，主动用 doing 或 to do，被动用 done，第三步判时间，目的将来到用 to do，主动进行用 doing，被动完成用 done，先于谓语完成的主动动作用 having done。固定搭配要分类记：want、decide 接 to do；avoid、enjoy 接 doing。stop to do 是停下来去做，stop doing 是停止做，意思完全不同。"
gen t09 "专题九，三大从句。解题顺序：先划从句范围，再定从句类型，再看缺不缺成分，最后选连接词。名词性从句不缺成分用 that，缺什么用 what。定语从句修饰名词，先行词被最高级或 the only 修饰时，只用 that。状语从句按逻辑选词：条件用 if、unless，让步用 although，结果用 so that。"
gen t10 "专题十，虚拟语气。核心是三行表：与现在相反，从句 did 主句 would do；与过去相反，从句 had done 主句 would have done；与将来相反，从句 did 或 were to do。信号词：wish、if only、would rather 退一步时态；suggest、demand 后的宾语从句用 should 加动词原形，should 可省。难点是错综时间和 if 省略倒装：Had I known，就是 If I had known。"
gen t11 "专题十一，主谓一致。三大原则：语法一致、意义一致、就近就远。each、every 作主语用单数。集合名词看意思：强调整体用单数，强调成员用复数。最高频考点：A number of 加复数动词，是许多；The number of 加单数动词，是数量。主语后面跟 with、as well as 是干扰项，谓语只看真正的主语。"
gen t12 "专题十二，倒装句。全部倒装：here、there 开头或方位介词短语开头，谓语整体提前，但主语是代词时不倒装。部分倒装更重要：否定词开头、Only 加状语开头、So 加形容词开头，都要把助动词提前。比如 Not until midnight did he come back。注意：Only 修饰主语时不倒装。"
gen t13 "专题十三，强调句。结构是 It is 或 was 加被强调部分加 that。被强调的是人可以用 who。鉴别真伪的方法最重要：去掉 It is that 之后，句子仍然完整，才是真强调句；不完整就是定语从句。变形要会：一般疑问 Was it that，特殊疑问 Where was it that，以及 It was not until 的句型。强调谓语动词用 do、does、did 加原形。"
gen t14 "专题十四，省略。最高频的是状语从句省略：主从句主语一致，且从句含 be 动词，就省略主语加 be，比如 When asked, he smiled。不定式省略：前文出现过的动词，不定式只留 to，比如 I'd love to。定语从句中关系代词作宾语可以省略。语法填空遇到 When 加空格加动词，先判主动被动，主动填 doing，被动填 done。"
gen t15 "专题十五，独立主格。结构是名词或代词，加分词、不定式、形容词或介词短语。它不是句子，没有谓语，自带逻辑主语，用逗号和主句隔开。经典例子：Weather permitting, we will go，等于 If weather permits。with 复合结构是它的近亲：With the light on, he slept。判断关键：逗号前有自己的主语且没有谓语，就是独立主格，选分词形式。"
gen s13 "现在进入实战练习。十二道高考风格语法填空，每题对应一个专题，从构词法到强调句全覆盖。填入正确的词或形式，点击判定，立即获得解析。答完十二题，会显示你的总得分，九题以上算达标。"
gen s14 "总结一下十五个专题。词法八个：构词法定成分选词性，名词记复数和不可数，冠词分清 a、an、the 和零冠词，代词背四格，介词三分法，时态十六矩阵加标志词，被动语态 be 加 done，非谓语三步法。句法七个：从句先定类型再选词，虚拟背三行表，主谓一致三原则，倒装提助动词，强调去掉仍完整，省略省主语和 be，独立主格自带主语。三轮复习：第一轮默写规则，第二轮刷真题说依据，第三轮重做错题。坚持三轮，语法填空一定能提分。"

# 清理 v1.0 被替换的旧音频
rm -f "$DIR"/s05.mp3 "$DIR"/s06.mp3 "$DIR"/s07.mp3 "$DIR"/s08.mp3 "$DIR"/s09.mp3 "$DIR"/s10.mp3 "$DIR"/s11.mp3 "$DIR"/s12.mp3

echo "==> 全部完成"
ls -la "$DIR"
