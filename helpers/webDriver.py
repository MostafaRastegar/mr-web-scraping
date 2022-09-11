import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def webDriver(options):
    chrome_options = Options()
    for option in options:
        chrome_options.add_argument(option)

    return webdriver.Chrome(
        ChromeDriverManager().install(), options=chrome_options)


sys.modules[__name__] = webDriver
