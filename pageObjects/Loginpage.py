import os.path

from selenium.webdriver.common.by import By


class login():
    txt_usrname_xpath = "//input[@id='user-name']"
    txt_password_xpath= "//input[@id='password']"
    but_login_xpath = "//input[@id='login-button']"
    txt_confirm_xpath= "//div[@class='app_logo']"

    def __init__(self,driver):
        self.driver = driver

    def set_user(self,uname):
        self.driver.find_element(By.XPATH,self.txt_usrname_xpath).send_keys(uname)

    def set_password(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def set_login(self):
        self.driver.find_element(By.XPATH,self.but_login_xpath).click()

    def get_msg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_confirm_xpath).text
        except:
            None