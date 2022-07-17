import requests



def get_bit_course(currency):
    btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    a = btc.json()
    return btc.json()['bpi'][currency]['rate']



bit = get_bit_course('USD')
print(bit)


