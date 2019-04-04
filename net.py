import urllib.request
import urllib.parse
import json
import easygui as gui
content=gui.enterbox("请输入你想要翻译的内容","by John M")
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
data={}
data['type']='AUTO'
data['i']=content
data['doctype']='json'
data['xmlVersion']='1.6'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['typoResult']='true'
data=urllib.parse.urlencode(data).encode('utf-8')
req=urllib.request.Request(url,data)
req.add_header('referer','http://fanyi.youdao.com')
req.add_header('User-Agent','Mozilla/5.0(Macintosh;Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML,like Gecko) Chrome/39.0.2171.95 Safari/537.36X-Requested-With:XMLHttpRequest')
res=urllib.request.urlopen(url,req)
html=res.read().decode('utf-8')
target=json.loads(html)
gui.msgbox(target,"net","OK")
print("done")

