import urllib.request
from bs4 import BeautifulSoup
#访问免费ip代理网址:http://www.youdaili.net/Daili/http/29381.html,处理得到所有的ip
def htmlParser(url):
    iplist=[]
    #设置头部
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {"User-Agent": user_agent}
    req = urllib.request.Request(url, headers=headers)
    #获取页面html
    html=urllib.request.urlopen(req).read()
    soup=BeautifulSoup(html,'html.parser')
    datas=soup.find("div",{"class":"content"}).findAll("p")
    for data in datas:
        ip=data.get_text().split("@")[0]
        iplist.apend(ip)
    return iplist
 
 
#检测ip是否可用
def confirm_ip(ip):
    #配置proxy
    proxy={'http':'http://%s'%ip}
    proxy_handler=urllib.request.ProxyHandler(proxy)
    proxy=urllib.request.bulid_handler(proxy_handler)
    urllib.request.install_handler(proxy)
 
    #用百度首页检测代理ip
    test_url="http://www.baidu.com"
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {"User-Agent": user_agent}
    req = urllib.request.Request(test_url, headers=headers)
 
    try:
        response=urllib.request.urlopen(req)
        content=response.read()
        #获取到内容
        if content:
            print("its a right ip")
            return ip
        #没有获取到
        else:
            return None
    #访问错误
    except urllib.request.URLError as e:
        print(e.reason)
        return None
 
trueIp=[]
url="http://www.youdaili.net/Daili/http/29381.html"
iplist=htmlParser(url)
for ip in iplist:
    if confirm_ip(ip)!=None:
       trueIp.append(ip)
 
print(trueIp)