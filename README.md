# PCTF_BASIC
Jarvis OJ上BASIC题的writeup<br>
[https://www.jarvisoj.com/challenges](https://www.jarvisoj.com/challenges)

## 段子<br>

程序猿圈子里有个非常著名的段子：

手持两把锟斤拷，口中疾呼烫烫烫。

请提交其中"锟斤拷"的十六进制编码。(大写)

FLAG: PCTF{你的答案}

    大部分出现这种问题的就是用gbk编码的文件用utf-8编码格式打开。当编码格式中出现utf-8无法解析的字节，那么这个字节就会被替换成 efbf bdef bfbd 这时我们会发现文件大小也发生了改变，因为未知字节全部变成三个未知字节。 而这时候再将其转换为gbk。
锟 (0xEFBF)，斤（0xBDEF），拷（0xBFBD）<br>

<img src="https://github.com/sunSUNQ/PCTF_BASIC/tree/master/picture/gbk.png" width="150" height="150" alt="gbk"/><br>

**PCTF{EFBFBDEFBFBD}**<br>

## 手贱<br>

某天A君的网站被日，管理员密码被改，死活登不上，去数据库一看，啥，这密码md5不是和原来一样吗？为啥登不上咧？

d78b6f302l25cdc811adfe8d4e7c9fd34

请提交PCTF{原来的管理员密码}

    对密文进行md5解密，发现不对，查位数33位，仔细看多余一位L，删除，重新md5解密

**PCTF{hack}**<br>

## 美丽的实验室logo<br>

出题人丢下个logo就走了，大家自己看着办吧

用010 editor打开，没发现什么。用stegsolve打开。<br>
<img src="https://github.com/sunSUNQ/PCTF_BASIC/tree/master/picture/stegsolve.png" width="150" height="150" alt="stegsolve"/><br>

**PCTF{You_are_R3ally_Car3ful}**<br>

## Secret <br>

传说中的签到题

题目入口：http://web.jarvisoj.com:32776/

Hint1: 提交格式PCTF{你发现的秘密}

F12 Network 看包头信息，有个secret标签，Welcome_to_phrackCTF_2016

**PCTF{Welcome_to_phrackCTF_2016}**<br>

## 取证 <br>

百度搜索内存取证软件，Volatility。

## help！！！<br>

出题人硬盘上找到一个神秘的压缩包，里面有个word文档，可是好像加密了呢~让我们一起分析一下吧

文件直接将。zip后边的去掉，可以解压，解压后发现一个word文档存在一个图片。
将word文档解压，获得文件夹，才word/media/下发现两个图片，其中一个是flag.<br>
<img src="https://github.com/sunSUNQ/PCTF_BASIC/tree/master/picture/help.png" width="150" height="150" alt="help"/><br>

## A Piece of cake <br>

nit yqmg mqrqn bxw mtjtm nq rqni fiklvbxu mqrqnl xwg dvmnzxu lqjnyxmt xatwnl, rzn nit uxnntm xmt zlzxuuk mtjtmmtg nq xl rqnl. nitmt vl wq bqwltwlzl qw yivbi exbivwtl pzxuvjk xl mqrqnl rzn nitmt vl atwtmxu xamttetwn xeqwa tsftmnl, xwg nit fzruvb, nixn mqrqnl ntwg nq gq lqet qm xuu qj nit jquuqyvwa: xbbtfn tutbnmqwvb fmqamxeevwa, fmqbtll gxnx qm fiklvbxu ftmbtfnvqwl tutbnmqwvbxuuk, qftmxnt xznqwqeqzluk nq lqet gtamtt, eqdt xmqzwg, qftmxnt fiklvbxu fxmnl qj vnltuj qm fiklvbxu fmqbtlltl, ltwlt xwg exwvfzuxnt nitvm twdvmqwetwn, xwg tsivrvn vwntuuvatwn rtixdvqm - tlftbvxuuk rtixdvqm yivbi evevbl izexwl qm qnitm xwvexul. juxa vl lzrlnvnzntfxllvldtmktxlkkqzaqnvn. buqltuk mtuxntg nq nit bqwbtfn qj x mqrqn vl nit jvtug qj lkwnitnvb rvquqak, yivbi lnzgvtl twnvnvtl yiqlt wxnzmt vl eqmt bqefxmxrut nq rtvwal nixw nq exbivwtl.

统计词频分析。拿到https://quipqiup.com/网站上跑一下就ok<br>
<img src="https://github.com/sunSUNQ/PCTF_BASIC/tree/master/picture/quipqiup.png" width="150" height="150" alt="quipqiup"/><br>

**PCTF{substitutepassisveryeasyyougotit}**<br>

## -.-字符串<br>

请选手观察以下密文并转换成flag形式

..-. .-.. .- --. ..... ..--- ..--- ----- .---- ---.. -.. -.... -.... ..... ...-- ---.. --... -.. .---- -.. .- ----. ...-- .---- ---.. .---- ..--- -... --... --... --... -.... ...-- ....- .---- -----

flag形式为32位大写md5

题目来源：CFF2016

直接找个网站在线解码摩斯密码。

**FLAG522018D665387D1DA931812B77763410** <br>

## 握手包 <br>

给你握手包，flag是Flag_is_here这个AP的密码，自己看着办吧。

提交格式：flag{WIFI密码}

使用aircrack_ng破解，用法百度，直接下载常用wifi密码词典，爆破。<br>
<img src="https://github.com/sunSUNQ/PCTF_BASIC/tree/master/picture/aircrack_ng.png" width="150" height="150" alt="aircrack_ng"/><br>
<img src="https://github.com/sunSUNQ/PCTF_BASIC/tree/master/picture/aircrack-ng.png" width="150" height="150" alt="aircrack-ng"/><br>

**flag{11223344}**
