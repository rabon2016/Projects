#encoding = utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.LoginAction import LoginAction
from appModules.AddContactPersonAction import AddContactPerson
import traceback
from time import sleep


excelObj = ParseExcel()
excelObj.loadWorkBook(dataFilePath)

def LaunchBrowser():
    # chrome_options = Options()
    # chrome_options.add_argument("--disable-extension")
    # chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # chrome_options.add_argument('--start-maximized')
    # driver = webdriver.Firefox(executable_path="c:\\geckodriver", chrome_options = chrome_options)
    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    driver.get("http://mail.163.com")
    sleep(3)
    return driver

def test163MailAddContacts():
    try:
        userSheet = excelObj.getSheetByName(u"163账号")
        isExecuteUser = excelObj.getColumn(userSheet, account_isExecute)
        dataBookColumn = excelObj.getColumn(userSheet, account_dataBook)
        print(u"测试为163邮箱添加联系人执行开始......")
        for idx, i in enumerate(isExecuteUser[1:]):
            if i.value == "y":
                userRow = excelObj.getRow(userSheet, idx+2)
                username = userRow[account_username-1].value
                password = str(userRow[account_password-1].value)
                print(username, password)

                driver = LaunchBrowser()

                LoginAction.login(driver, username, password)
                sleep(3)
                dataBookName = dataBookColumn[idx+1].value
                dataSheet = excelObj.getSheetByName(dataBookName)
                isExecuteData = excelObj.getColumn(dataSheet, contacts_isExecute)
                contactNum = 0
                isExecuteNum =0
                for id, data in enumerate(isExecuteData[1:]):
                    if data.value == "y":
                        isExecuteNum += 1
                        rowContent = excelObj.getRow(dataSheet, id+2)
                        contactPersonName = rowContent[contacts_contactPersonName-1].value
                        contactPersonEmail = rowContent[contacts_contactPersonEmail-1].value
                        isStar = rowContent[contacts_isStar-1].value
                        contactPersonPhone = rowContent[contacts_contactPersonMobile-1].value
                        contactPersonComment = rowContent[contacts_contactPersonComment-1].value
                        assertKeyWord = rowContent[contacts_assertKeyWords-1].value
                        print(contactPersonName)

                        AddContactPerson.add(driver, contactPersonName, contactPersonEmail, isStar, contactPersonPhone, contactPersonComment)
                        sleep(1)

                        excelObj.writeCellCurrentTime(dataSheet, rowNo = id + 2, colsNo = contacts_runTime)
                        try:
                            assert assertKeyWord in driver.page_source
                        except AssertionError as e:
                            excelObj.writeCell(dataSheet, "faild", rowNo= id + 2, colsNo= contacts_testResult, style = "green")
                            contactNum += 1
                        else:
                            excelObj.writeCell(dataSheet, "pass", rowNo= id + 2, colsNo= contacts_testResult, style= "green")
                            contactNum += 1
                print("Todo1")

                if contactNum == isExecuteNum:
                    excelObj.writeCell(userSheet, "pass", rowNo= idx+2, colsNo= account_testResult, style="green")
                    print("Todo2")
                else:
                    excelObj.writeCell(userSheet, "faild", rowNo= idx+2, colsNo= account_testResult, style="red")
            else:
                print("Todo3")
            driver.quit()



    except Exception as e:
        print(u"数据驱动框架主程序发生异常，异常信息为:")
        print(traceback.print_exc())

if __name__ == '__main__':
    test163MailAddContacts()
