import os
import requests
import datetime
from dotenv import load_dotenv

# Gather dependencies
load_dotenv()
api_key = os.getenv("API_KEY")
yesterday = datetime.datetime.now() - datetime.timedelta(1)
date = yesterday.strftime("%Y-%m-%d")

# Set URL - Searching for "Royal Bank of Canada"
url = f"https://newsapi.org/v2/everything?q=Royal%20Bank%20of%20Canada&sortedBy=popularity&from={date}&apiKey={api_key}"

# Retrieve Info
request = requests.get(url)
content = request.json()

# Iterate Over Results
print(f"### NEWS ARTICLES FOR ROYAL BANK OF CANADA FROM {date}###\n")
for article in content['articles']:
    print('------')
    print(article['title'])
    print(article['description'])
    print()
