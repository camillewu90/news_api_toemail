import requests


url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-06\
&sortBy=publishedAt&apiKey=61aa060bbb4e4a6cbe56cc8ac2b599aa"
api_key = "61aa060bbb4e4a6cbe56cc8ac2b599aa"

# Make a request
request = requests.get(url)

# Get a dictionary from data
content = request.json()

# Access the article author
articles = content['articles']
for article in articles:
    print(article["author"])

