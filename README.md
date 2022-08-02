## m3u8-Streaming-Server
-------------
在互联网快速发展的今天，有成千上万个用户都有观看电视的需求，而我，
想打造一个让每个人都拥有自己的电视频道的目标，每个人都可以根据自己的喜欢去筛选喜欢的节目，
并且拥有免费且流畅的观看体验。

---
**[演示地址](https://vs.naihe.repl.co/channel.m3u8) 演示部分接口**
---

### 核心功能:  
- 生成m3u列表
- 生成m3u8视频文件
- 下载视频
- 流媒体转发
- 视频中转
- 生成epg节目单(developing)
- 数据分流


---

### 实现效果：
#### ios软件观看效果

<img height="300" src="https://github.com/239144498/m3u8-Streaming-Server/blob/gh-pages/image/a1.png?raw=true" title="播放效果" width="600"/>

<img height="600" src="https://github.com/239144498/m3u8-Streaming-Server/blob/gh-pages/image/a2.jpg?raw=true" title="节目单" width="300"/>

---

### 原理介绍
该项目根据分析4gtv网站的接口，通过算法得到生成ts视频的一些关键参数，省去请求网站
从而得到m3u8文件的通信时长等开销，针对海外视频网站被墙隔离，以下简单几种观看方式：
- 使用翻墙软件观看
- 通过反向代理观看
- 通过套CDN观看

该项目使用的是反向代理+CDN方式，通过搭建中转服务器，在客户端不使用翻墙软件情况下，
得到稳定流畅的观看体验。

---

### 使用方式
#### 方式1：
本地部署:  
``` code
git clone https://github.com/239144498/m3u8-Server.git
```
安装依赖
``` code
pip install -r requirements.txt
```
运行
``` code
python3 main.py
```

---

## License
Released under the MIT license.

Copyright, 2022, by naihe.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
