from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = 'https://simple.wikipedia.org/wiki/List_of_Formula_One_World_Constructors%27_Champions'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[0]
headers = table.find_all('th')
column_names = [re.sub(r'\[.*?\]', '',header.text.strip()) for header in headers[:11]]

data_rows = table.find_all('tr')[1:67]
data = []
for rows in data_rows:
    cells = rows.find_all(['td', 'th'])
    row_data = [re.sub(r'\[.*?\]', '', cell.text.strip()) for cell in cells[:11]]
    data.append(row_data)


df= pd.DataFrame(data, columns=column_names)

print(df)

df.to_csv(r'C:\Users\user\Desktop\frm_scrapping\Constructor_Wins_By_Season.csv', index=False)
