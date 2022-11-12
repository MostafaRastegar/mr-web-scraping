import requests
import json
import pandas as pd
from urllib import request, response
from helpers import csvGenerator
import time
import random

uri = "https://api.digikala.com/v1/categories/mobile-phone/search/?has_selling_stock=1&page="
jsonData = requests.get(uri + '1').json()


print('========> loading url')
pager = jsonData['data']['pager']


def getProductsId(url, totalPages):
    productsIdList = []
    for pageNumber in range(totalPages):
        print('====' + str(pageNumber))
        time.sleep(2 + random.random())
        jsonData = requests.get(url + str(pageNumber + 1)).json()
        products = jsonData['data']['products']
        for product in products:
            productsIdList.append(product['id'])
    csvGenerator(productsIdList, 'ex-digikala-product-list.csv', 'csv')
    return productsIdList


getProductsId(uri, pager['total_pages'])

# csvGenerator([1, 2, 3], 'ex-digikala-product-list.csv')
