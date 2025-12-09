# https://realpython.com/python-web-scraping-practical-introduction/
from urllib.request import urlopen

#url = "http://olympus.realpython.org/profiles/aphrodite"
#url = "https://www.cnbeta.com.tw/"
#url = "http://placekitten.com/g/500/600" 
#url = "http://placekitten.com/200/300"
url = "http://placekitten.com/408/287"
page = urlopen(url) # urlopen() #returns an HTTPResponse object:
#page
cat_image = page.read()

with open("cat_500_600.jpg", 'wb') as f:
    #f.write(cat_image) # C:\Users\zhen-\Documents\Python Scripts\Lynnda_Exercise_Files\12 Classes\cat_500_600.jpg
    f.write(cat_image) # C:\Users\zhen-\Documents\Python Scripts\Lynnda_Exercise_Files\12 Classes\cat_408_287.jpg
