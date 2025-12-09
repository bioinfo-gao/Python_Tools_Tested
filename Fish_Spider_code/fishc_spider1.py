__author__ = "Alex Li"

import urllib.request
#response = urllib.request.urlopen("https://www.google.com")
#response = urllib.request.urlopen("https://www.fishc.com")
response = urllib.request.urlopen("https://www.google.com")
html = response.read() # take 5 min to get response from webpage
print(html) 