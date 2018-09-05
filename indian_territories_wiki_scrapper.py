# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:12:19 2018

@author: Ayush Pandey
"""
from bs4 import BeautifulSoup
import requests
pd.set_option('max_colwidth', -1)
# Here, we're just importing both Beautiful Soup and the Requests library

page_link = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(page_link)
# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.
# print(page_content.prettify())

#all_links = page_content.find_all('a')
#for link in all_links:
#    print(link.get('href'))

page_content.table
right_table = page_content.find('table', class_="wikitable sortable plainrowheaders")
# print(right_table)

list_of_rows = []
for row in right_table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.find(text=True)
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

cell = []
for row in right_table.findAll('th'):
    cell.append(row.find(text=True))

# print(cell)  

#import pandas to convert list to data frame
import pandas as pd
df = pd.DataFrame(list_of_rows,columns=['Number','Admin_Capital', 'Legislative_capital', 'Judiciary_capital', 'Year_capital', 'Former_capital'])
df = df.drop(0)
cell_new = []
for i in range(7,43):
    cell_new.append(cell[i])
df['State/UT'] = cell_new

print(df)
list = df.iloc[5,:]
c1 = (list['Legislative_capital'])
print (c1)
list = df.iloc[2,:]
c2 = (list['Former_capital'])
print(c2)
list = df.iloc[27,:]
c3 = (list['Former_capital'])
print(c3)
list = df.iloc[30,:]
c4 = (list['Former_capital'])
print(c4)
df = df.replace([c1,c2,c3,c4], '--')
df.iloc[27,4] = '--'
cols=['Number','State/UT', 'Admin_Capital', 'Legislative_capital', 'Judiciary_capital', 'Year_capital', 'Former_capital']
df = df[cols]
df.to_csv('Indian States and Union Territories.csv', encoding='utf-8')
