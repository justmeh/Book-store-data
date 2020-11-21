import requests 
from bs4 import BeautifulSoup as bs
r = requests.get("http://books.toscrape.com/")
soup = bs(r.text, 'html.parser')
soup = bs(r.text, 'html.parser')
for category_list in soup.findAll("ul", {"class": "nav nav-list"}):
    #finds the category list
    for tag in category_list.findAll('a'):
    #find all the anchor tags in the category list
        link = tag.get('href')
        #gets the links from the the list 
        buk_genre = (tag.string.strip())
        #gets the genre names/string from the list
        print (buk_genre, ' : ',link )
       
