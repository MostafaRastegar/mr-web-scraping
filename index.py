from helpers import hs, fg, csvGenerator, webDriver

driver = webDriver(['--headless'])
uri = "https://taaghche.com/filter?filter-category=183&filter-target=0&filter-bookType=0&filter-publisher=-106&order=7"


print('========> loading url')
driver.get(uri)

print('========> start pagination')
hs.infiniteScrollPage(driver, 1, 3)

print(' ========> create dataFrame')
dict = {
    'title': fg.releaseList(driver, "//a[contains(@class,'book_bookTitle')]", fg.getText),
    'author': fg.releaseList(driver, "//a[contains(@class,'book_bookAuthor')]", fg.getText),
    'link': fg.releaseList(driver, "//a[contains(@class,'book_bookTitle')]", fg.getAttributeValue('href')),
}

print(' ========> fineshed')
csvGenerator(dict, 'taghche-scroll.csv')
