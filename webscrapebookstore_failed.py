import os
import requests 
from bs4 import BeautifulSoup as bs

r = requests.get("http://books.toscrape.com/")
soup = bs(r.text, 'html.parser')
category = soup.findAll("ul", {"class": "nav nav-list"})


print(category)
f = open("myfile.txt", "w")
f.write(str(category))
f.close()

f2 = open("myfile.txt", "r").read()


for genre in f2:
        category = genre.find('a').contents[0].strip()
        print(category)
        
