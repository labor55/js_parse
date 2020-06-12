#1 目标url：
http://api.geetest.com/ajax.php?

参数：
gt: b46d1900d0a894591916ea94ea91bd2c
challenge: 4899dab4ecfe3473d923001b1337d580f2
w: "轨迹参数"
callback: geetest_1587365857834

gt？
challenge ？

# 2 gt and challenge 参数url：
http://api.geetest.com/get.php?

请求参数：
gt: b46d1900d0a894591916ea94ea91bd2c
challenge: 4899dab4ecfe3473d923001b1337d580
product: popup
offline: false
protocol: http://
maze: /static/js/maze.1.0.1.js
path: /static/js/geetest.6.0.9.js
pencil: /static/js/pencil.1.0.3.js
type: slide
voice: /static/js/voice.1.2.0.js
beeline: /static/js/beeline.1.0.1.js
callback: geetest_1587365847103


#3 疑似
http://api.geetest.com/gettype.php?

gt: b46d1900d0a894591916ea94ea91bd2c
callback: geetest_1587365846107

响应：
geetest_1587365846107({"status": "success", "data": {"static_servers": ["static.geetest.com"], "maze": "/static/js/maze.1.0.1.js", "path": "/static/js/geetest.6.0.9.js", "pencil": "/static/js/pencil.1.0.3.js", "type": "slide", "voice": "/static/js/voice.1.2.0.js", "beeline": "/static/js/beeline.1.0.1.js"}})

#4 gt and challenge url
http://localhost:5000/pc-geetest/register?t=1587369439884

难点 cookie
Cookie: session=eyJndF9zZXJ2ZXJfc3RhdHVzIjoxLCJ1c2VyX2lkIjoidGVzdCJ9.Xp1UoQ.He11Q1zKzFhxsuKbIGGsqcrr1O4

请求结果：
{"success": 1, "gt": "b46d1900d0a894591916ea94ea91bd2c", "challenge": "a1e7785349223d719664f8dd449ed5ba"}


介绍
http://www.wisedream.net/2016/12/02/spider/crack-geetest/