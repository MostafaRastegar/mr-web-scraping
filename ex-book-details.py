from helpers import hs, fg
import helpers.csvGenerator as csvGenerator
import helpers.webDriver as webDriver


# uri = input("Enter path uri: ")
uri = "https://taaghche.com/book/30242/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84"

driver = webDriver(['--headless'])
print('========> loading url')
driver.get(uri)


print('========> fetching data')


def getChildFirstSpanText(nth):
    return fg.findElement(
        driver,
        "//div[contains(@class,'moreInfo_moreInfoItems')]/div[contains(@class,'moreInfo_moreInfoItem')][" + str(nth) + "]/span[2]"
    )


dict = {
    'name': fg.getText(fg.findElement(driver, "//h1")),
    'price': fg.getText(fg.findElement(driver, "//div[contains(@class, 'price_price__')]/span[1]")),
    'pageTotals': fg.getText(getChildFirstSpanText(1)),
    'paperPrice': fg.getText(getChildFirstSpanText(2)),
    'type': fg.getText(getChildFirstSpanText(3)),
    'published': fg.getText(getChildFirstSpanText(4)),
    'isbn': fg.getText(getChildFirstSpanText(5))
}


print('========> fineshed')
csvGenerator(dict, 'ex-book-details.csv', 'csv', ['book'])
