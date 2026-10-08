from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCalc:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def delay_input(self):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys("45")

    def btn_seven(self):
        btn_seven = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='7']")
        ))
        btn_seven.click()

    def btn_plus(self):
        btn_plus = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='+']")
        ))
        btn_plus.click()

    def btn_eight(self):
        btn_eight = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='8']")
        ))
        btn_eight.click()

    def btn_equal(self):
        btn_equal = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='btn btn-outline-warning']")
        ))
        btn_equal.click()

    def screen_result(self):
        screen_result = self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"
            ))
        screen_result = self.driver.find_element(By.CLASS_NAME, "screen")
        return screen_result.text
