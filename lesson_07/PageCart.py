from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCart:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def сart_contents(self):
        cart_contents = self.wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item_name")
        ))

        contents = [
            cart_contents[0].text,
            cart_contents[1].text,
            cart_contents[2].text
        ]
        return contents

    def checkout(self):
        checkout_btn = self.wait.until(EC.presence_of_element_located(
            (By.ID, "checkout")
        ))
        checkout_btn.click()
