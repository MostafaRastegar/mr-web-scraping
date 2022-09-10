from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
from helpers import releaseList, infiniteScrollPage, getText, getAttributeValue
import pandas as pd



chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

print('======== > loading url')
driver.get("https://taaghche.com/filter?filter-category=183&filter-target=0&filter-bookType=0&filter-publisher=-106&order=7")

print('========> start pagination')
infiniteScrollPage(driver, 1, 3)

print(' ================> create dataFrame')
dict = {
    'title': releaseList(driver, "//a[contains(@class,'book_bookTitle')]",getText),
    'author': releaseList(driver, "//a[contains(@class,'book_bookAuthor')]",getText),
    'link': releaseList(driver, "//a[contains(@class,'book_bookTitle')]",getAttributeValue('href')),
}
print(' ================> fineshed')

df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv('taghche-scroll.csv')
