
import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re # manipulate regular expression

url="https://www.hubertiming.com/results/2018MLK"
html=urlopen(url)
soup = BeautifulSoup(html,)
title=soup.title
print(title)
print(title.text) # give only text
# find links
links=soup.findAll('a',href=True)
for link in links:
    print(link['href']) # its return only link in solid text
    # find data
data=[]
allrows=soup.find_all('tr')
#print(allrows)
#print(allrows[:10]) # slicing first 10 data
for row in allrows:
    row_list=soup.find_all('td')
    data_row=[]
    for cell in row_list:
        data_row.append(cell.text)
    data.append(data_row)
#print(data[0:2])



df=pd.DataFrame(data)
print(df.head(2))
print(df.tail(2))
header_list=[]
col_header=soup.find_all('th')
for col in col_header:
    header_list.append(col.text)
print(header_list)

#df.columns=header_list
# print(df.head())
print(df.info())

# *************** LEARN MORE ************
# THAT VIDEO IS SUCKS





