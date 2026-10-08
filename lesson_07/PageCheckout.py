from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCheckout:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def input_forms(self):
        input_forms = self.driver.find_elements(By.CLASS_NAME, "form_input")
        forms = [
            "Дмитрий",
            "Пашкин",
            "650000"
            ]
        for i in range(3):
            input_forms[i].send_keys(forms[i])

    def continue_btn(self):
        continue_btn = self.wait.until(EC.presence_of_element_located(
            (By.ID, "continue")
        ))
        continue_btn.click()

    def total_price(self):
        self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        ))
        price_total = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return price_total.text
