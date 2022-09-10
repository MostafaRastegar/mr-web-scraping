from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from helpers import release_list, infiniteScrollPage
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://taaghche.com/filter?filter-category=183&filter-target=0&filter-bookType=0&filter-publisher=-106&order=7")


infiniteScrollPage(driver, 1, 5)
time.sleep(3)


dict = {
    'title': release_list(driver, "//a[contains(@class,'book_bookTitle')]"),
}
print(' ================> fineshed')
df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv('taghche-scroll.csv')
