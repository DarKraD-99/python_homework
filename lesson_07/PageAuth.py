from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageAuth:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def input_login(self):
        input_login = self.driver.find_element(By.ID, "user-name")
        input_login.send_keys("standard_user")

    def input_password(self):
        input_password = self.driver.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")

    def login_button(self):
        login_btn = self.wait.until(EC.presence_of_element_located(
            (By.ID, "login-button")
        ))
        login_btn.click()
