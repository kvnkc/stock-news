import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api = '9271981438a44098b6dc0b5842d80876'

news_parameters = {
    'q': 'Apple',
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
news_data = news_response.json()

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
stock_time_series = stock_data['Time Series (Daily)']

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
previous_day_closing_stock_price = float(
    stock_time_series['2022-11-01']['4. close'])
print(previous_day_closing_stock_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_closing_stock_price = float(
    stock_time_series['2022-10-31']['4. close'])
print(day_before_yesterday_closing_stock_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(
    previous_day_closing_stock_price - day_before_yesterday_closing_stock_price)
print(positive_difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = positive_difference / \
    ((previous_day_closing_stock_price + day_before_yesterday_closing_stock_price)/2) * 100

# If percentage is greater than 5 then print("Get News").
if percentage > 5:
    print('Get News')

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
