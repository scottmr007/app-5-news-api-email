import requests

api_key = "2ffa5acd3bef4b2c864f5675ac619377"
url = "https://newsapi.org/v2/everything?q=aaple&from=2024-01-24&" \
        "sortBy=publishedAt&apiKey=2ffa5acd3bef4b2c864f5675ac619377"

r = requests.get(url)
content = r.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])
    
    