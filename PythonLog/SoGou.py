#encoding=utf-8
from selenium import webdriver
import unittest
from Log import *

class TestSoGouSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="c:\\geckodriver")

    def testSoGouSearch(self):
        logging.info(u"==============sousuo=============")
        url="http://www.sogou.com"
        self.driver.get(url)
        logging.info(u"message1")
        self.driver.find_element_by_id("query").send_keys(u"guangrong")
        logging.info(u"message2")
        self.driver.find_element_by_id("stb").click()
        logging.info(u"message3")
        logging.info(u"===============finish============")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()