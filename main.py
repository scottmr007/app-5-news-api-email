import requests
from send_email import send_email

topic = 'tesla'
api_key = "api_key"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2024-02-04&" \
    "sortBy=publishedAt&" \
    "apiKey=api_key&" \
    "language=en"

r = requests.get(url)
content = r.json()

body = ""
for article in content["articles"][0:20]:
    body = "Subject: Today's news" + "\n" + body + article['title'] + "\n" + article['description'] + "\n" + 2*"\n"
    
body = body.encode()('utf-8')
send_email(message=body)
    
    