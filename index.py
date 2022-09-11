from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
# from helpers import releaseList, infiniteScrollPage, getText, getAttributeValue
import pandas as pd

from helpers import hs, fg


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)

uri = "https://taaghche.com/filter?filter-category=183&filter-target=0&filter-bookType=0&filter-publisher=-106&order=7"


print('======== > loading url')
driver.get(uri)

print('========> start pagination')
hs.infiniteScrollPage(driver, 1, 0)

print(' ================> create dataFrame')
dict = {
    'title': fg.releaseList(driver, "//a[contains(@class,'book_bookTitle')]", fg.getText),
    'author': fg.releaseList(driver, "//a[contains(@class,'book_bookAuthor')]", fg.getText),
    'link': fg.releaseList(driver, "//a[contains(@class,'book_bookTitle')]", fg.getAttributeValue('href')),
}
print(' ================> fineshed')

df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv('taghche-scroll.csv')
