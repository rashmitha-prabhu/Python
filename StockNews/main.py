import requests
import os
from twilio.rest import Client

# STOCK = "HDB"
# COMPANY_NAME = "HDFC Bank"

STOCK = "BEN"
COMPANY_NAME = "Franklin Resources"

api_key = os.environ['STOCK_API']
stock_prices = "https://www.alphavantage.co/query"
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': api_key
}

data = requests.get(stock_prices, params=stock_params)
data.raise_for_status()

stock_data = data.json()['Time Series (Daily)']
req_data = dict(list(stock_data.items())[:2])
days = list(stock_data.keys())[:2]

yesterday = float(req_data[days[0]]['4. close'])
day_before = float(req_data[days[1]]['4. close'])

change = ((yesterday-day_before)/yesterday)*100
print(change)

if abs(change) >= 0:

    news_api = "http://newsapi.org/v2/everything"
    news_api_key = os.environ['NEWS_API']
    news_param = {
        'qInTitle': COMPANY_NAME,
        'language': 'en',
        'apikey': news_api_key,
        'sortBy': 'publishedAt'
    }

    news = requests.get(news_api, params=news_param)
    news.raise_for_status()
    articles = news.json()['articles'][:3]

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    for i in range(len(articles)):
        message = client.messages \
                    .create(
                        body=f"""
                        {STOCK} : {round(change, 2)}%\n\n
                        Headline: {articles[i]['title']}\n\n
                        Brief: {articles[i]['description']}\n\n
                        Link: {articles[i]['url']}
                        """,
                        from_='+18183515076',
                        to='+917829621594'
                    )
