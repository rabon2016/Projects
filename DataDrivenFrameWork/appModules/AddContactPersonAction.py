#encoding=utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import  AddressBookPage
import traceback
import time

class AddContactPerson(object):
    def __init__(self):
        print("add contact person")


    @staticmethod
    def add(driver, contactName, contactEmail, isStar, contactPhone, contactComment):
        try:
            hp=HomePage(driver)
            hp.addressLink().click()
            time.sleep(3)
            apd=AddressBookPage(driver)
            apd.createContactPersonButton().click()
            if contactName:
                apd.contactPersonName().send_keys(contactName)
            apd.contactPersonEmail().send_keys(contactEmail)
            if isStar == u"是":
                apd.starContacts().click()
            if contactPhone:
                apd.contactPersonMobile().send_keys(contactPhone)
            if contactComment:
                apd.contactPersonComment().send_keys(contactComment)
            apd.saveContacePerson().click()
        except Exception as e:
            print(traceback.print_exc())
            raise e

if __name__ == '__main__':

    from appModules.LoginAction import LoginAction
    from selenium import  webdriver
    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    driver.get("http://mail.163.com")
    time.sleep(5)
    LoginAction.login(driver, "13530480151", "k511983973")
    time.sleep(5)
    AddContactPerson.add(driver, u"张三", "sz@qq.com", u"是", "", "")
    time.sleep(5)
    assert u"张三" in driver.page_source
    driver.quit()
