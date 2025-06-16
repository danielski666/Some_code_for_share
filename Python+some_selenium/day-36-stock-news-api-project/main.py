STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY="ZC6KV199E74BH1VX"
NEWS_API_KEY = "6624afc8b35f4db393267975b0c1aeb3"
import requests
from datetime import datetime

current_date = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"
yesterday_date = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day-1}"



STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": STOCK_API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_params = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "pageSize": 3,
    "apiKey": NEWS_API_KEY,
}
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

stock_request = requests.get(STOCK_ENDPOINT, params=stock_params)
data = stock_request.json()["Time Series (Daily)"]
list_data = [value for (key, value) in data.items()]
yesterday_data = list_data[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = list_data[1]
day_before_yesterday_close_price = day_before_yesterday["4. close"]

closing_diff = abs(float(day_before_yesterday_close_price)-float(yesterday_closing_price))

percentage_diff = (closing_diff / float(yesterday_closing_price)) * 100
if percentage_diff > 3.:
    news_request = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_request.json()["articles"]
    news_data_list = [f"Title: {news['title']}. \nBrief desc.: {news['description']}. \n{news['url']}" for news in news_data]
    print(news_data_list)
    print(news_data)

# Not possible to send mail and\or sms due to lack of the accounts ;P

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

