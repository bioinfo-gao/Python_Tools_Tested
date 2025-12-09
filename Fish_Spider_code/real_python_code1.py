# https://realpython.com/python-web-scraping-practical-introduction/
from urllib.request import urlopen

#url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url) # urlopen() #returns an HTTPResponse object:
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)