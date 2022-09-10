from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.instagram.com")
cookies = pickle.load(open("instag_cookies.pkl", "rb"))
print('==============cookies===============')
print(cookies)
print('=============================')
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://www.instagram.com")
