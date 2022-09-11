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

uri = "https://taaghche.com/book/30242/%D9%86%D8%A7%D8%B1%DA%AF%DB%8C%D9%84"


print('======== > loading url')
driver.get(uri)


# print(' ================> create dataFrame')

def getChildFirstSpanText(nth):
    return fg.findElement(
        driver,
        "//div[contains(@class,'moreInfo_moreInfoItems')]/div[contains(@class,'moreInfo_moreInfoItem')][" + str(nth) + "]/span[2]"
    )


print(getChildFirstSpanText(1))

dict = {
    'pageTotals': fg.getText(getChildFirstSpanText(1)),
    'price': fg.getText(getChildFirstSpanText(2)),
    'type': fg.getText(getChildFirstSpanText(3)),
    'published': fg.getText(getChildFirstSpanText(4)),
    'isbn': fg.getText(getChildFirstSpanText(5))
}
# print(' ================> fineshed')

df = pd.DataFrame(dict, index=[0])
# saving the dataframe
df.to_csv('ex-book-details.csv')
