# 🏀 NBA Points Per Game Data Scraper and S3 Uploader ☁️

This Python script is designed to scrape NBA points per game data from the TeamRankings website, process the data, and upload it to an Amazon S3 bucket as a CSV file. The script leverages several libraries, including requests for HTTP requests, BeautifulSoup for HTML parsing, pandas for data handling, and boto3 for AWS interactions.

🔑 Key Features:

Scrapes NBA points per game data from the URL: TeamRankings NBA Stats 🏀

Extracts the relevant table data and converts it into a pandas DataFrame 📊

Generates a unique CSV filename using the current timestamp ⏱️

Uploads the CSV data to an S3 bucket (specified via environment variables) ☁️

Handles errors and logs them for easier troubleshooting ⚠️

📋 Prerequisites:

Python 3.x 🐍

Required Python libraries: requests, beautifulsoup4, pandas, boto3 📦

AWS credentials with permission to write to the specified S3 bucket 🔑

🌍 Environment Variables:

S3_BUCKET_NAME: The name of the S3 bucket where the CSV data will be uploaded 🗄️