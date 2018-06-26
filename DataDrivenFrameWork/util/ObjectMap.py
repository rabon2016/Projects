__author__ = 'dell'

from selenium.webdriver.support.ui import WebDriverWait

#获取单个页面元素对象
def getElement(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locateType, value=locatorExpression))
        return element
    except Exception as e:
        raise e

def getElements(driver, locateType, locaterExpression):
    try:
        elements = WebDriverWait(driver, 30).until(lambda x:x.find_elements(by=locateType, value=locaterExpression))
        return elements
    except Exception as e:
        raise e

if __name__ == '__main__':
    from selenium import webdriver
    #进行单元测试
    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    driver.get("http://www.baidu.com")
    driver.quit()