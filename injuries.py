import requests
from bs4 import BeautifulSoup
import pandas as pd
# Send an HTTP request to the webpage
url = "https://sports.yahoo.com/nba/injuries/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACOOgZ1tKZz9F0kQx7fisQpGX38-A3i3NwPpGD1cyIlcBiPGJ7itBe7Sj-vea-kSn3JOQtw1mtnYcEGdhbqemHOxbNOd4uRDlmHF_czp_AYRAwfm18uC7VPSTVzDyIEJ8KM56xa7xqJySaTOU5HpRLywcdRCtwlYkuZkZ9U4NXat" 
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
df.to_csv('injuries.csv', index=False)