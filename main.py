import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api = '9271981438a44098b6dc0b5842d80876'

news_parameters = {
    'q': COMPANY_NAME,
    'from': 2022-11-2,
    'sortBy': 'popularity',
    'apiKey': news_api
}

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': 'VIZRCW2WW0UB437T'
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()['articles']

# When stock price increase/decreases by 5% between yesterday and the day before yesterday.
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']

# Yesterday's closing stock price.
previous_day_closing_stock_price = float(
    stock_data['2022-11-01']['4. close'])

# The day before yesterday's closing stock price
day_before_yesterday_closing_stock_price = float(
    stock_data['2022-10-31']['4. close'])

# The positive difference between 1 and 2.
positive_difference = abs(
    previous_day_closing_stock_price - day_before_yesterday_closing_stock_price)

# The percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = positive_difference / (previous_day_closing_stock_price) * 100

# If percentage is greater than 5 then prints first 3 articles from newsapi
if percentage > 5:
    articles = news_data[0:3]
    print(articles)
