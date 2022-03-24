import json
import requests
import time
import os
from requests.exceptions import HTTPError

from utils.notif import notify
from utils.time import current_time, timestamp_to_str


notify("pFTM price watch", "Started running at " + current_time())


COINGECKO_PRICE_URL = 'https://api.coingecko.com/api/v3/simple/price/?ids=pftm,fantom&vs_currencies=USD'
UA_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


while True:
    print("Current Time =", current_time())
    try:
        response = requests.get(COINGECKO_PRICE_URL, headers=UA_HEADER)
    except HTTPError as e:
        print('========== FAILED TO FETCH')
        print(e.response.text)


    if response.status_code != 200:
        print('========== FAILED TO FETCH')
        print(response)
        print(response.status_code)
        print('========== HEADERS')
        print(response.headers)
        print('========== CONTENT')
        print(response.content)
        break

    data = json.loads(response.content)
    pftm_price = data['pftm']['usd']
    ftm_price = data['fantom']['usd']

    rate = pftm_price / ftm_price
    print('rate =', rate)

    if rate < 0.97:
        notify("pFTM rate", "{} / {} = {}".format(pftm_price, ftm_price, rate))

    time.sleep(10 * 60)
