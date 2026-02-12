from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def Login(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("secret_sauce")
