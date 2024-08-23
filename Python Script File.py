# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RqhFPbozmXhZGgxr2sr-tyQIXriFPlKR
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

print(soup)

table = soup.find('table', class_ = 'wikitable sortable')

print(table)

titles = table.find_all('th')

print(titles)

table_titles = [title.text.strip() for title in titles]

print(table_titles)

df = pd.DataFrame(columns = table_titles)

df

column_data = table.find_all('tr')

print(column_data)

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  length = len(df)
  df.loc[length] = individual_row_data

df

df.to_csv('Companies.csv', index=False)

from google.colab import files
files.download('Companies.csv')