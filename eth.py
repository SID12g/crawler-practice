import requests
import json

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/krw/eth?interval=1h')
dict = json.loads(data.content)
print(dict['body']['candles'][0]['close'])

