import requests
import datetime
import time
from bs4 import BeautifulSoup
import json

def get_prices(symbol):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    info_list = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')
    info_list = [i.text for i in info_list]
    stock = {
        'symbol': symbol,
        'price': info_list[0],
        'change': info_list[1],
        'percent': info_list[2][1:len(info_list[2]) - 2]
    }
    return stock

stop_time = datetime.datetime.now() + datetime.timedelta(minutes=1)  

stock_data = []

while datetime.datetime.now() < stop_time:

    stock_data.append(get_prices('AAPL'))
    
    print("Got data")

    with open('stockdata.json', 'w') as f:
        json.dump(stock_data, f)


    time.sleep(2) 
