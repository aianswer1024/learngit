'''
import requests
url = "http://dnf.qq.com/main.shtml"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:10000])
except:
    print("爬取失败")
'''
'''
import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'user-agent' : 'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败')
'''
'''
import requests
keyword = 'Python'
flag = input()
try:
    if flag == 'b' or flag == 'B':
        kv = {'wd' : keyword}
        print("正在使用百度搜索引擎")
        r = requests.get('http://www.baidu.com/s',params = kv)
    elif flag == 3 :
        kv = {'q' : keyword}
        print("正在使用360搜索引擎")
        r = requests.get('http://www.so.com/s',params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
'''
'''
import requests
import os

url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "D://fanju//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open (path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
'''
'''
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
'''
'''
import requests
from bs4 import BeautifulSoup
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
'''
from bs4 import BeautifulSoup
import requests
import bs4
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
   
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if  isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string]) 

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
        
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()