import requests
import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-06\
&sortBy=publishedAt&apiKey=61aa060bbb4e4a6cbe56cc8ac2b599aa"
api_key = "61aa060bbb4e4a6cbe56cc8ac2b599aa"


# Make a request
request = requests.get(url)

# Get a dictionary from data
content = request.json()

# Access the article author
articles = content['articles']

# Create an message string with subject
message = """Subject: news digest\n
"""

# Populate the article title and description in the message
for article in articles:
    if article["title"]:
        message += article["title"] + "\n"
    else:
        message += "Missing title" + "\n"

    if article["description"]:
        message += article["description"] + 2*"\n"
    else:
        message += "Missing description" + 2*"\n"

message = message.encode('utf-8')
# Send email of news digest
send_email.send_email(message)

