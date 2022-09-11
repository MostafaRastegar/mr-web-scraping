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
    ChromeDriverManager().install())

uri = "https://taaghche.com/book/30242/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84"


print('======== > loading url')
driver.get(uri)


# print(' ================> create dataFrame')

def getFirstSpan():
    return fg.findElements(driver, "//a[contains(@class,'book_bookTitle')][0]/span[1]")

print(fg.getText(getFirstSpan()))

    
# dict = {
#     'pageTotals': fg.getText(fg.findElements(driver, "//a[contains(@class,'book_bookTitle')]")[0])
#     'pageTotals': fg.getElements(driver, "//a[contains(@class,'book_bookTitle')]", fg.getText),

# }
# print(' ================> fineshed')

# df = pd.DataFrame(dict)
# # saving the dataframe
# df.to_csv('ex-book-details.csv')
