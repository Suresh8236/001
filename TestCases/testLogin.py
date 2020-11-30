from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from TestCases.confest import setup
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import logGen
from selenium.webdriver.common.keys import Keys
import time

class Test_001_Login:
    URL = ReadConfig.getApplicationurl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ReadConfig.getPath()

    logger = logGen.loggen()

   # def test_HomaPageTitle(self,setup):
    #    self.logger.info("****************   Test_001_Login   *********************")
    #    self.logger.info("****************   test_HomePageTitle   *********************")
     #   self.driver = setup
     #   self.driver.get(self.URL)
     #   act_title = self.driver.title
     #   self.driver.close()
    #    if act_title == "Jobseeker's Login: Search the Best Jobs available in India & Abroad - Naukri.com":
      #      assert True
    #        self.logger.info("****************   test_HomePageTitle is passed   *********************")
      #  else:
    #        self.logger.info("****************   test_HomePageTitle is failed  *********************")
    #        assert False

    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("****************   test_Login   *********************")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.lp.clickupdateProfile()
        time.sleep(5)
        self.lp.UpdateResume(self.path)
        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(5)
        self.driver.save_screenshot("C:\\Users\\Suresh\\PycharmProjects\\001\\Screenshots\\ResumeUpdated.png")
        self.driver.close()










