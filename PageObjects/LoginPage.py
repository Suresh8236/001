class LoginPage:
    textbox_usernmae_id = "usernameField"
    textbox_password_id = "passwordField"
    button_login_xpath = "//*[@id='loginForm']/div[3]/div[3]/div/button[1]"
    button_updateProfile_xpath = "//div[contains(text(),'UPDATE PROFILE')]"
    resume_id = "attachCV"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_usernmae_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickupdateProfile(self):
        self.driver.find_element_by_xpath(self.button_updateProfile_xpath).click()

    def UpdateResume(self,path):
        self.driver.find_element_by_id(self.resume_id).send_keys(path)

    def clickUpdate(self):
        self.driver.find_element_by_id(self.resume_id).click()


