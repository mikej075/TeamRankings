import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send HTTP request to the webpage
url = "https://www.teamrankings.com/nba/stat/points-per-game"
response = requests.get(url)
response.raise_for_status()  # Ensures request success

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table')

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table data
data = []
for row in table.find_all('tr')[1:]:  # Skip header row
    row_data = [cell.text.strip() for cell in row.find_all('td')]
    if row_data:  # Avoid empty rows
        data.append(row_data)

# Create DataFrame with headers
df = pd.DataFrame(data, columns=headers)

# Save DataFrame to CSV
df.to_csv('pointppg.csv', index=False)

print("Data successfully scraped and saved to 'pointppg.csv'")