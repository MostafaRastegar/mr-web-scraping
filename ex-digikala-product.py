import requests
import json
import pandas as pd
from urllib import request, response
from helpers import csvGenerator
import sys


def getDigikalaProductDetails(url, id):

    jsonData = requests.get(url + str(id) + '/').json()

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

    csvGenerator(dict, 'product-' + str(id) + '.csv', 'csv/digikala')


getDigikalaProductDetails('https://api.digikala.com/v1/product/', 7326528)

sys.modules[__name__] = getDigikalaProductDetails
