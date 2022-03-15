import json
import requests
import time
import os
from requests.exceptions import HTTPError

from utils.notif import notify
from utils.time import current_time


notify("Kyber Trending", "Started running at " + current_time())


OLD_SYMBOLS = [
   'POLS', 'CVP', 'OGN', 'GRT', 'LDO', 'RVST', 'KNCL', 'KNC', 'PROS', 'BAT',
   'PMON', 'YOSHI', 'JASMY', 'MIR', 'ARV', 'GMEE', 'CVX', 'NBT', 'POWR', 'ADS',
   'IDEA', 'BEPRO', 'BETA', 'ATOM', 'MIST', 'BOND', 'FXS', 'ATA', 'BONE', 'FOR',
   'XYO', 'BSW', 'NOIA', '10SET', 'UNFI', 'VIDT', 'DEXE', 'ARPA', 'NEAR', 'AVAX',
   'FARM', 'EPS', 'POLY', 'BAND', 'LOOKS', 'MLN', 'STORJ', 'RAMP', 'IDEX', 'MCONTENT',
]

KYBER_TRENDING_URL = 'https://truesight.kyberswap.com/api/v1/trending-soon?timeframe=24h&page_number=0&page_size=50&search_token_name=&search_token_tag='
UA_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


while True:
    print("Current Time =", current_time())
    try:
        response = requests.get(KYBER_TRENDING_URL, headers=UA_HEADER)
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
    tokens = data['data']['tokens']
    symbols = [token['symbol'] for token in tokens]

    if symbols == OLD_SYMBOLS:
        print('Fetched => Same')
    else:
        print('Fetched => NEW:')
        new_symbols = []
        for symbol in symbols:
            if symbol not in OLD_SYMBOLS:
                print(symbol)
                new_symbols.append(symbol)
        symbols = OLD_SYMBOLS
        notify("Kyber Trending", "Found new coins: " + ' '.join([str(symbol) for symbol in new_symbols]))

    time.sleep(10 * 60)
