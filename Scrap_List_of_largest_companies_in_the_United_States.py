#This is a project for my WebScrapping training which read one table data from a webpage, manipulate and reorginazie the data and insert the data into a CSV file on my google drive

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
table = soup.find('table',class_ = 'wikitable sortable')
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]
df = pd.DataFrame(columns = world_table_titles)
column_data = table.find_all('tr')
for row in column_data[1:]:
  row_data = row.find_all('td')
  Individual_row_data = [data.text.strip() for data in row_data]
  length = len(df)
  df.loc[length] = Individual_row_data

####import google.colab run one time
#from google.colab import drive
#drive.mount('/content/drive')

df.to_csv('/content/drive/My Drive/Py/LargeCompanies.csv' , index=False)