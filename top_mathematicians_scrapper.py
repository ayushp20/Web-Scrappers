# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:56:54 2018

@author: Ayush Pandey
"""

from bs4 import BeautifulSoup
import requests

link = "http://www.fabpedigree.com/james/mathmen.htm"
response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.prettify())

#for i, li in enumerate(soup.find_all('li')):
#    print(i, li.text)
names = set()
for i, li in enumerate(soup.find_all('li')):
    for name in li.text.split('\n'):
        names.add(name.strip())

name_ = list(names)
name_.remove('')
name_list = []
for name in name_:
#    print(type(name))
    name = name.replace("  ", "_")
    name = name.replace(". ","_")
    name = name.replace("-","_")
    name = name.replace(" ","_")
#    print(name)
    name_list.append(name)

name_list

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_hits_on_name(name):
    """
    Accepts a `name` of a mathematician and returns the number
    of hits that mathematician's Wikipedia page received in the 
    last 60 days, as an `int`
    """
    # url_root is a template string that is used to build a URL.
    url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
    response = requests.get(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response.content, 'html.parser')

        hit_link = [a for a in html.find_all('a') if a['href'].find('latest-60') > -1]

        if len(hit_link) > 0:
            # Strip commas
            link_text = hit_link[0].text.replace(',', '')
            try:
                # Convert to integer
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))

    log_error('No pageviews found for {}'.format(name))
    return None

results = []

print('Getting stats for each name....')

for name in name_list:
    try:
        hits = get_hits_on_name(name)
        if hits is None:
            hits = -1
        results.append((hits, name))
    except:
        results.append((-1, name))
        log_error('error encountered while processing '
                  '{}, skipping'.format(name))

print('... done.\n')

results.sort()
results.reverse()
print(results)

if len(results) > 5:
    top_marks = results[:5]
else:
    top_marks = results
    
print('\nThe most popular mathematicians are:\n')
for (mark, mathematician) in top_marks:
    print('{} with {} pageviews'.format(mathematician, mark))

no_results = len([res for res in results if res[0] == -1])
print('\nBut we did not find results for '
      '{} mathematicians on the list'.format(no_results//2))
    
