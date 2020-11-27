import os, sys, requests, csv, pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel
from bs4 import BeautifulSoup as bs

if os.path.exists("Books.xlsx"):
  print("Books.xlsx exists")
else:
  crtBooks = open("Books.xlsx", "x")
  print("Books.xlsx has been created")
  crtBooks.close()
url = "http://books.toscrape.com/"
r = requests.get(url)
link = []
buk_genre = []
soup = bs(r.text, 'lxml')
for category_list in soup.findAll("ul", {"class": "nav nav-list"}):#finds the category list
    for tag in category_list.findAll('a'):    #find all the anchor tags in the category list
        link.append(tag.get('href'))        #gets the links from the the list 
        buk_genre.append(tag.string.strip())        #gets the genre names/string from the list
csvBook = pd.Series(buk_genre, name="genre") #convert buk_genre to a pd series
csvlink = pd.Series(link, name="url") #convert buk_genre to a pd series
data = {"Genre":csvBook, "URL":csvlink}
df = pd.DataFrame(data, columns=['Genre','URL']) #makes it into a dataframe
df.to_excel(r'Books.xlsx', sheet_name='Genres',index=False)
read_df=pd.read_excel('Books.xlsx', sheet_name='Genres') #reads the file 
i_index =1
for i in link:
	if (i_index >= len(link)):
		break
	else:
		URL2 = read_df.iloc[i_index]['URL']
		link_url = url+URL2
		i_index += 1
		r_books=requests.get(link_url)
		soup_book = bs(r_books.text, 'html.parser')
		names_book= []
		genre_book = []
		prices = []
		for book_prod in soup_book.findAll('article', {"class": "product_pod"}):
			genre_book.append(buk_genre[i_index])
			names_book.append(book_prod.find('h3').text.encode('UTF-8'))
			prices.append(book_prod.find('p', class_="price_color").text[2:])
	csvNames = pd.Series(names_book, name="Book Names")
	csvGenres = pd.Series(genre_book, name="genre")
	csvPrice = pd.Series(prices, name="Price")
	data_columns = {"Genre":csvGenres, "Book Names":csvNames, 'Price':csvPrice}
	df2 = pd.DataFrame(data_columns, columns=['Genre','Book Names','Price'])
	header_row = 1
	df2.columns = df2.iloc[header_row]
	df2 = df2.drop(header_row)
	df2.to_excel(r'Books.xlsx', sheet_name='books',index=False)
	read_df2=pd.read_excel('Books.xlsx', sheet_name='books')
	print(read_df2)
