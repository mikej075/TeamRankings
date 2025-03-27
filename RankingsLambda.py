import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import boto3
from io import StringIO
import os
from datetime import datetime

# Initialize S3 client
s3 = boto3.client('s3')

# URL to scrape data
URL = "https://www.teamrankings.com/nba/stat/points-per-game"

# Environment Variables
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

def lambda_handler(event, context):
    try:
        if not S3_BUCKET_NAME:
            raise ValueError("Missing environment variable: S3_BUCKET_NAME")

        # Send HTTP request
        response = requests.get(URL)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')

        if not table:
            raise ValueError("Error: Could not find the table on the webpage")

        # Extract headers
        headers = [header.text.strip() for header in table.find_all('th')]

        # Extract table data
        data = []
        for row in table.find_all('tr')[1:]:  # Skip header row
            row_data = [cell.text.strip() for cell in row.find_all('td')]
            if row_data:
                data.append(row_data)

        # Create DataFrame
        df = pd.DataFrame(data, columns=headers)

        # Check if DataFrame is empty
        if df.empty:
            raise ValueError("DataFrame is empty. No data to upload.")

        # Convert DataFrame to CSV in memory
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # Retrieve CSV data
        csv_data = csv_buffer.getvalue()

        # Check if csv_data is a string or bytes-like object
        if not isinstance(csv_data, (str, bytes)):
            raise TypeError(f"CSV data is not a string or bytes-like object: {type(csv_data)}")

        # Generate unique CSV filename
        csv_filename = f"pointppg_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.csv"

        # Upload CSV to S3
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=csv_filename,
            Body=csv_data
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"Data successfully uploaded to S3 as '{csv_filename}'")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
