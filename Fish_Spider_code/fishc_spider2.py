# https://realpython.com/python-web-scraping-practical-introduction/
from urllib.request import urlopen

#url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://placekitten.com/g/500/600"
#url = "https://www.cnbeta.com.tw/"
page = urlopen(url) # urlopen() #returns an HTTPResponse object:
#page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)