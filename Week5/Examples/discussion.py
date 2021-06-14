# Python has many different options for working with data such as Pandas. To extract data from the internet, Python offers a library called  BeautifulSoup. Research how to use BeautifulSoup for Webscraping. Give some examples.


import requests
from bs4 import BeautifulSoup
import pandas as pd
page=requests.get("https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films").text
soup=BeautifulSoup(page,"lxml")
table=soup.find("table",{"class":"wikitable"})
data = table.findAll('tr')[2:]
oscar_winning_movies=[]
for i in data:
    movies=i.findAll("a")
    for x in movies:
        aString = str(x.get("title"))
        if "in film" in aString:
          continue
        oscar_winning_movies.append(x.get("title"))
dataframe=pd.DataFrame()
dataframe['oscar_winning_movies']= oscar_winning_movies
dataframe.to_csv("oscar_winning_movies.csv") # expected result CSV with list of films that have won oscar