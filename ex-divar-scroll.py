from helpers import hs, fg, csvGenerator, webDriver

driver = webDriver(['--headless'])
uri = "https://divar.ir/s/tehran/buy-apartment?price=1500000000-1750000000&size=55-75&rooms=2&floor=-3&has-photo=true"


print('========> loading url')
driver.get(uri)


def scrollCallback(n):
    print(' ========> create dataFrame')
    dict = {
        'title': fg.releaseList(driver, "//h2[contains(@class,'kt-post-card__title')]", fg.getText),
        'price': fg.releaseList(driver, "//div[contains(@class,'kt-post-card__description')]", fg.getText),
        'enterprise': (str(fg.releaseList(driver, "//span[contains(@class,'kt-post-card__bottom-description')]", fg.getText)).split(' در '))[1],
        'link': fg.releaseList(driver, "//div[@class='virtual-infinite-scroll__viewport']//a", fg.getAttributeValue('href')),
    }
    print(' ========> fineshed')
    csvGenerator(dict, 'ex-divar-scroll-' + str(n) + '.csv', 'csv/divar')


print('========> start pagination')
hs.infiniteScrollPage(driver, 1, 3, scrollCallback)
