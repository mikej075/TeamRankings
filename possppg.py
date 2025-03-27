import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP request to the webpage
url = "https://www.teamrankings.com/nba/stat/possessions-per-game" 
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table')

# Extract table data
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())
    data.append(row_data)

# Create a DataFrame
df = pd.DataFrame(data)
df.to_csv('POSSppg.csv', index=False)