import os
from pageObjects.Loginpage import login
from utilities.readproperties import ReadConfig


class Test_acc_login():

    baseURL = ReadConfig.getApplicationURL()

    def testClick_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=login(self.driver)
        self.lp.set_user("standard_user")
        self.lp.set_password("secret_sauce")
        self.lp.set_login()
        self.msg=self.lp.get_msg()
        self.driver.close()
        if self.msg == "Swag Labs":
            assert True
        else:
            self.driver.get_screenshot_as_file(os.getcwd() + "//screenshots" + "testClick_login.png")
            self.driver.close()
            assert False

