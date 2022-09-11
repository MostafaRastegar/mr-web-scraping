import requests
import json
import pandas as pd
from urllib import request, response
from helpers import csvGenerator

uri = "https://api.digikala.com/v1/product/7845430/"
# https://api.digikala.com/v1/categories/mobile-phone/search/?has_selling_stock=1&page=1
jsonData = requests.get(uri).json()


print('========> loading url')

product = jsonData['data']['product']
variants = product['variants']


def variantNameAndPrice(item):
    return {
        'name': item['warranty']['title_fa'],
        'price': item['price']['selling_price'],
    }


variantList = list(map(variantNameAndPrice, product['variants']))

dict = {
    "brand": product['brand']['title_fa'],
    "id": product['id'],
    "deviceNameFa": product['title_fa'],
    "deviceNameEn": product['title_en'],
    "variants": variantList,
}

print(dict)
csvGenerator(dict, 'test.csv')
