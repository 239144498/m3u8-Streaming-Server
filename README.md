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
- 生成EPG节目单(completed)  [EPG节目单](https://agit.ai/239144498/demo/raw/branch/master/4gtvchannel.xml) 每日实时更新
- 数据分流


---

### 实现效果：
#### ios软件观看效果

<img height="300" src="https://ik.imagekit.io/naihe/github/1.png?ik-sdk-version=javascript-1.4.3&updatedAt=1660959995410" title="播放效果" width="600"/>

<img height="600" src="https://ik.imagekit.io/naihe/github/2.png?ik-sdk-version=javascript-1.4.3&updatedAt=1660959995410" title="频道表" width="300"/>

<img height="600" src="https://ik.imagekit.io/naihe/github/3.png?ik-sdk-version=javascript-1.4.3&updatedAt=1660959995410" title="节目单" width="300"/>

---

### 原理介绍
该项目根据分析4gtv网站的接口，通过算法得到生成ts视频的一些关键参数，省去请求网站
从而得到m3u8文件的通信时长等开销，针对海外视频网站被墙隔离，以下简单几种观看方式：
- 使用翻墙软件观看
- 通过反向代理观看
- 通过套CDN观看

该项目使用的是反向代理+CDN方式，通过搭建中转服务器，在客户端不使用翻墙软件情况下，
得到稳定流畅的观看体验。

**已做出更优方式，核心原理：通过服务器定时更新将核心参数缓存到redis，服务器端接收客户端请求后，通过核心参数生成多个时间片.ts链接，将链接分布式到多个脚本程序预下载，再将.ts文件上传到mysql，而服务器端读取数据库内容发送给客户端。mysql使用事件调度器做了定时删除数据功能，最后根据实际使用体验来看，看1080甚至4k都不是问题！源码后续发布，敬请期待！欢迎关注(●'◡'●)**
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

### 现已支持频道

- [x] 民视第一台
- [x] 民视台湾台
- [x] 民视
- [x] 大爱电视
- [x] 中视
- [x] 中视经典台
- [x] 华视
- [x] 三立综合台
- [x] 客家电视台
- [x] 八大综艺台
- [x] 中视菁采台
- [x] TVBS精采台
- [x] 爱尔达娱乐台
- [x] 靖天综合台
- [x] 靖天日本台
- [x] 新唐人亚太台
- [x] 中天综合台
- [x] ARIRANG阿里郎频道
- [x] Global Trekker
- [x] LiveABC互动英语频道
- [x] 达文西频道
- [x] ELTV生活英语台
- [x] Nick Jr. 儿童频道
- [x] 尼克儿童频道
- [x] 靖天卡通台
- [x] 靖洋卡通Nice Bingo
- [x] i-Fun动漫台
- [x] MOMO亲子台
- [x] CN卡通
- [x] 东森购物一台
- [x] 镜电视新闻台
- [x] 东森新闻台
- [x] 华视新闻
- [x] 民视新闻台
- [x] 三立财经新闻iNEWS
- [x] TVBS新闻
- [x] 东森财经新闻台
- [x] 中视新闻
- [x] 中天新闻台
- [x] 寰宇新闻台
- [x] SBN全球财经台
- [x] TVBS
- [x] 东森购物二台
- [x] 民视综艺台
- [x] 猪哥亮歌厅秀
- [x] 靖天育乐台
- [x] KLT-靖天国际台
- [x] Nice TV 靖天欢乐台
- [x] 靖天资讯台
- [x] 中天全民最大党
- [x] TVBS欢乐台
- [x] 韩国娱乐台 KMTV
- [x] Lifetime 娱乐频道
- [x] 电影原声台CMusic
- [x] TRACE Urban
- [x] MTV Live HD 音乐频道
- [x] Mezzo Live HD
- [x] CLASSICA 古典乐
- [x] 博斯高球台
- [x] 博斯运动一台
- [x] 博斯无限台
- [x] 博斯网球台
- [x] TRACE Sport Stars
- [x] 智林体育台
- [x] 时尚运动X
- [x] 车迷TV
- [x] GINX Esports TV
- [x] TechStorm
- [x] Pet Club TV
- [x] 民视旅游台
- [x] 滚动力rollor
- [x] 亚洲旅游台
- [x] 幸福空间居家台
- [x] Love Nature
- [x] History 历史频道
- [x] HISTORY 2 频道
- [x] Smithsonian Channel
- [x] 爱尔达生活旅游台
- [x] LUXE TV Channel
- [x] TV5MONDE STYLE HD 生活时尚
- [x] 中天美食旅游
- [x] 公视戏剧
- [x] 民视影剧台
- [x] 龙华戏剧台
- [x] HITS频道
- [x] 龙华日韩台
- [x] 八大精彩台
- [x] 靖天戏剧台
- [x] 靖洋戏剧台
- [x] CI 罪案侦查频道
- [x] 视纳华仁纪实频道
- [x] 影迷数位纪实台
- [x] 金光布袋戏
- [x] ROCK Extreme
- [x] 采昌影剧台
- [x] 靖天映画
- [x] 靖天电影台
- [x] 龙华电影台
- [x] 影迷数位电影台
- [x] amc最爱电影
- [x] CinemaWorld
- [x] CATCHPLAY Beyond
- [x] CATCHPLAY电影台
- [x] My Cinema Europe HD 我的欧洲电影
- [x] 好消息2台
- [x] 好消息
- [x] 大爱二台
- [x] 人间卫视
- [x] 半岛国际新闻台
- [x] VOA美国之音
- [x] CNBC Asia 财经台
- [x] DW德国之声
- [x] CNN头条新闻台
- [x] CNN国际新闻台
- [x] 国会频道1
- [x] 国会频道2
- [x] 经典电影台
- [x] 经典卡通台
- [x] 精选动漫台
- [x] 华语戏剧台
- [x] 华语综艺台

---

## License
Released under the MIT license.

Copyright, 2022, by naihe,239144498@qq.com .

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
