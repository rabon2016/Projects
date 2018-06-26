#encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import  ParseConfigFile

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemsSection("163mail_login")

    def switchToFrame(self):
        try:
            locatorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
            self.driver.switch_to.frame(locatorExpression)
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def userNameObj(self):
        try:
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            #获取登录页面的密码输入框页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            #获取登录页面的登录按钮页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    #测试代码
    from selenium import webdriver
    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    driver.get("http://mail.163.com")
    import time
    time.sleep(5)
    login = LoginPage(driver)
    driver.switch_to.frame("x-URS-iframe")
    login.userNameObj().send_keys("13530480151")
    login.passwordObj().send_keys("k511983973")
    login.loginButton().click()
    time.sleep(10)
    login.switchToDefaultFrame()
    driver.quit()


