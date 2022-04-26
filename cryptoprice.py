import requests
import pandas as pd
import json, requests
from datetime import datetime

# get today openign price of the coin
api_key = 'MRzAy2PbkeE5IkK7Ad1mHPTAUPQS7MvP'
def get_crypto_price(symbol,api_key):
    symbol=(symbol.upper())
    #get todat date
    today =datetime.today().strftime('%Y-%m-%d')
    api_url=f'https://api.polygon.io/v1/open-close/crypto/'
    response2 = requests.get(api_url + symbol + f'/USD/' + today +f'?adjusted=true&apiKey='+api_key)
    if response2.status_code == 200:
        response_json2 = json.loads(response2.content)
        price=response_json2['open']
        print("Today "+symbol+" opening price: {} USD".format(price))
    else:
        print("Sorry, I could not resolve price of"+ symbol)

