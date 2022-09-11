from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def findElement(driver, xpath):
    return driver.find_element(By.XPATH, xpath)


def findElements(driver, xpath):
    return driver.find_elements(By.XPATH, xpath)


def getText(element):
    return element.text


def getAttributeValue(attr):
    def getAttribute(element):
        return element.get_attribute(attr)
    return getAttribute


def isElementPresent(driver, how, what):
    try:
        driver.find_element(how, what)
    except NoSuchElementException as e:
        return False
    return True


def recursiveListLoop(elementList, n, getter):
    if(n == 0):
        return []
    return [getter(elementList[n - 1])] + recursiveListLoop(elementList, n-1, getter)


def releaseList(drive, xpath, getter):
    list_of_elements = findElements(drive, xpath)
    return recursiveListLoop(list_of_elements, len(list_of_elements), getter)


def printer(x):
    print('=============> ', x)
