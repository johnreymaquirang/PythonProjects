import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://simple.wikipedia.org/wiki/List_of_Formula_One_World_Constructors%27_Champions'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table')[1]
headers = table.find_all('th')
column_names = [header.text.strip() for header in headers]

data_rows = table.find_all('tr')[1:]
data = []

for rows in data_rows:
    cells = rows.find_all(['td', 'th'])
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

df = pd.DataFrame(data, columns = column_names)

print(df)
