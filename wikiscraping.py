import requests,datetime
import pandas as pd
import os 
import glob 

from bs4 import BeautifulSoup


url = "http://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")
table = bsObj.find("table", class_ = "sortable")
tables = bsObj.find_all("table")

df_pandas = pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)", attrs = {"class" : "wikitable"}, flavor = "bs4" , thousands = ".")
for df in df_pandas:
    df.to_csv(r'C:\Users\nachu\OneDrive\Documents\GitHub\data-engineering-project\GDP.csv')


##curr_dir = os.path.dirname(os.path.realpath(__wikiscraping.py__))
print(curr_dir)
##print(table)
