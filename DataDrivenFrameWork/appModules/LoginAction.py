#encoding=utf-8
from pageObjects.LoginPage import LoginPage

class LoginAction(object):
    def __init__(self):
        print("login...")

    @staticmethod
    def login(driver, username, password):
        try:
            login = LoginPage(driver)
            login.switchToFrame()
            login.userNameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginButton().click()
            login.switchToDefaultFrame()
        except Exception as e:
            raise e
