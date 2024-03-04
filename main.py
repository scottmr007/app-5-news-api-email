import requests
from send_email import send_email

api_key = "api_key"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-04&sortBy=publishedAt&            apiKey=api_key"

r = requests.get(url)
content = r.json()

body = ""
for article in content["articles"]:
    body = body + article['title'] + "\n" + article['description'] + 2*"\n"
    
body = body.encode()('utf-8')
send_email(message=body)
    
    