1. 访问一个国内免费ip代理的网站(注意要获取高匿的ip)，这里我们以网站有代理 (http://www.youdaili.net) 为例，进入后找到http代理点击进入，然后点击列表中最新日期的免费代理，就可以看到很多最新的免费ip代理;
2. 用Python的BeautifulSoup解析这个页面，从页面中获取所有的ip地址及端口号，组合(ip:port的形式)起来存入一个列表中;
3. 获得了所有的ip后，接下来我么要验证这些ip能不能用，因为免费的ip代理大部分都是不能用的，所以我们就要从这些在网页上爬取的ip进行检查，去掉那些不能用的，具体方法是(注意一点Python中代理参数的格式是proxy={'http':'http://ip:port'}) 。首先我们将ip配置为Python中代理参数的默认格式，然后我们用urllib.request.ProxyHandler方法将proxy传入，接着用`urllib.request.build.opener`和`urllib.request.install_opener()`一次处理，代理参数就配置好了，然后我们以百度为测试网站，测试看看我们的代理ip能不能，用`urllib.request.urlopen()`如果能返回则证明可用反之不能用。能用的话我们就添加到一个新的列表中加一保存。
#### Note: 
出入讲解的缘故，代码只爬取的免费代理网站上面的首页所有ip和port ，没进行翻页处理。
