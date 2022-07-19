import requests


def get_bit_course():
    btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return btc.json()['bpi']


# bit = get_bit_course('USD')
# print(bit)

def get_euro_usd_course():
    eurusd = requests.get('https://currate.ru/api/?get=rates&pairs=EURRUB,USDRUB&key=2a589443e712033d60669015d7f88f76')
    return eurusd.json()['data']

# EUR = get_euro_usd_course()
# print(EUR)