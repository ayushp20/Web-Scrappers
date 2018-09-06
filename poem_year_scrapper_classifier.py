# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 00:54:20 2018

@author: Ayush Pandey
"""

## Imports.
import pandas as pd
from bs4 import BeautifulSoup
import request

all_poets = requests.get('http://www.famouspoetsandpoems.com/poets.html')
poets = BeautifulSoup(all_poets.text, 'lxml')



poet_years = []

for tag in poets.findAll('td'):
    try:
        if '(' in tag.get_text():
            poet_years.append(tag.get_text().strip())
    except:
        pass

poet_years2 = [x.strip() for x in poet_years]

poet_years2 = poet_years2[3:]
poet_years = poet_years2[::2]
poet_years