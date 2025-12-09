import re
import urllib

def getHtml(url='https://google.com'):
    #page=urllib.urlopen(url) # ctrl + Alt +down to duplicate the currrent line
    page=urllib.request.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'src="(.*\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre, html)
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x +=1

#html=(getHtml("http://www.cnbeta.com/"))
html=(getHtml())
print(getImg(html))


