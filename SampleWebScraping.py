from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all('table')[1]
headers = table.find_all('th')
column_names = [header.text.strip() for header in headers]

data_rows = table.find_all('tr')[1:]  # Skip header row
data = []
for row in data_rows:
    cells = row.find_all(['td', 'th'])
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

df = pd.DataFrame(data, columns=column_names)
print(df)
