import requests


def get_bit_course():
    btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return btc.json()['bpi']

# bit = get_bit_course('USD')
# print(bit)
