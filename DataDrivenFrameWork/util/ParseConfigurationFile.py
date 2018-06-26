#encoding=utf-8
from configparser import ConfigParser
from config.VarConfig import pageElementLocatorPath

class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        value = self.cf.get(sectionName, optionName)
        return value

if __name__ == '__main__':
    pc = ParseConfigFile()
    print(pc.getItemsSection("163mail_login"))
    print(pc.getOptionValue("163mail_login", "loginPage.frame"))