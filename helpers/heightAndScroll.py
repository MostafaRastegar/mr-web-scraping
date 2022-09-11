import pickle
import time


def readCookies(driver, path):
    cookies = pickle.load(open(path, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)


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
