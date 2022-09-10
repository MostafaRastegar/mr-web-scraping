from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pickle
import time


def is_element_present(driver, how, what):
    try:
        driver.find_element(how, what)
    except NoSuchElementException as e:
        return False
    return True


def readCookies(driver, path):
    cookies = pickle.load(open(path, "rb"))
    print('==============cookies===============')
    print(cookies)
    print('=============================')
    for cookie in cookies:
        driver.add_cookie(cookie)


def findElement(driver, xpath):
    return driver.find_element(By.XPATH, xpath)


def findElements(driver, xpath):
    return driver.find_elements(By.XPATH, xpath)


def recursiveListLoop(elementList, n):
    if(n == 0):
        return []
    return [elementList[n - 1].text] + recursiveListLoop(elementList, n-1)


def release_list(drive, xpath):
    list_of_elements = findElements(drive, xpath)
    return recursiveListLoop(list_of_elements, len(list_of_elements))


def windowScrollTo(driver, n, screen_height):
    return driver.execute_script(
        "window.scrollTo(0, {screen_height}*{n});".format(screen_height=screen_height, n=n))


def bodyScrollHeight(driver):
    return driver.execute_script(
        "return document.body.scrollHeight;")


def getScreenHeight(driver):
    return driver.execute_script(
        "return window.screen.height;")


def recursiveScrollTo(driver, n, scroll_pause_time, screen_height):

    windowScrollTo(driver, n, screen_height)
    time.sleep(scroll_pause_time)
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * (n + 1) > bodyScrollHeight(driver):
        return False
    recursiveScrollTo(driver, n + 1, scroll_pause_time, screen_height)


def infiniteScrollPage(driver, n, scroll_pause_time):
    return recursiveScrollTo(driver, n, scroll_pause_time, getScreenHeight(driver))
