import execjs

def get_js(path):
    f = open(path, 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr


path = r'C:\Users\Administrator\Desktop\temp_spider\qianyan\qianyan\spiders\crypto.js'
jsstr = get_js(path)
ctx = execjs.compile(jsstr) #加载JS文件
res = ctx.call('Md5JiaMi', '123')
print(res)

