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
