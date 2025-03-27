# favi_badapple

> 灵感来源：https://github.com/nolenroyalty/faviconic

> 视频演示：https://www.bilibili.com/video/BV1H393YCEce/

## 简介

实现原理比较简单，需要一个中间websocket服务器。打开web页面自动连接服务器，并依次标号排序。

当标签页全部打开并组合完成后，由服务端发送指令给每个网页，以控制标签页图标的颜色变化。

因此可以通过修改服务端与html来实现彩色等不同玩法。

网页使用静音音频进行保活，防止在后台时js性能被限制。

可自行使用*tool/row2bin.py*脚本解析其他视频

## 项目结构

- *http_server/start.bat* 运行后开启http小型服务器，承载指定的web网页
- *server.js* 运行后会自动读取当前目录下的*frames.txt*帧动画文件，并作为websocket服务端运行，控制播放与暂停
- *openChrome.py* 运行后会利用*chromedriver.exe*开启多个浏览器窗口，并自动依次打开web页面。当页面打开后会自动连接websocket服务端。耗时可能较久，中间出现弹窗、气泡提醒无需处理。
- *tool* 包含多个工具，创建静音音频、media内视频转frames、frames转为txt数据格式

## 使用方法

> 项目内已导出过bad apple视频的帧数据，无需转换可直接播放使用

需要使用nodejs=* python=3.10，项目已内置chromedriver

### 安装依赖

```
npm install ws

pip install selenium pillow

其他软件：
chrome
ffmpeg(可选)
```

### 运行项目

```
//运行http服务器
start-httpserver.bat

//运行websocket服务器
start-server.bat

//打开chrome及web页面
start-openChrome.bat

//等全部web页面加载完成后，在第二个窗口内输入“1”开始播放
```

### 自定义web窗口

修改根目录下的*openChrome.py*

默认配置：
```
# ==================== 配置 ====================
num_windows = 12  # 需要打开的窗口数量
num_tabs = 16  # 每个浏览器窗口打开的标签页数量
window_width = 800  # 每个窗口的宽度
window_height = 80  # 每个窗口的高度
gap = 32  # 窗口之间的间距
base_url = "http://localhost:888/"#http服务器地址
# ==================== 配置 ====================
```

### 自定义视频

- 安装ffmapeg，确保全局变量可用
- 下载视频为mp4格式，重命名为*video.mp4*并放到`tool/media`文件夹内
- （可选）修改`tool/[1]video2frames.bat`，其中"fps=10"为截取的帧数，当fps为10时，每秒会截取10张图片
- 运行`tool/[1]video2frames.bat`，等待截取完成，图片会出现在`tool/frames`文件夹内
- 运行`tool/[2]frames2data.bat`，等待转换完成，在`tool`文件夹内会出现一个*frame.txt*文件，注意文件大小不为0，否则为转换失败
- 将*frame.txt*文件移动至根目录下，再运行程序即可。

## 修改\开发建议

HTML文件：位于`web/index.html`，通过修改该文件可调整favi图标的颜色与内容，该项目中默认只有黑白两色(由函数updateFavicon控制)。

websocket服务端：位于`server.js`，可修改下发的指令等逻辑。

图像取模转换：位于`tool/convert_frames_to_data.py`，可修改处理图像逻辑，该项目中只截取图像的色彩为黑白两色。


## 补充

项目内用到的http-server为[simple-http-server](https://github.com/TheWaWaR/simple-http-server)

项目内所使用的chromedriver来自[Google Chromium](https://sites.google.com/chromium.org/driver/downloads)
