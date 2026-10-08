from selenium.webdriver.common.by import By


class PageShop:

    def __init__(self, driver):
        self.driver = driver

    def backpack(self):
        backpack_buy = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        backpack_buy.click()

    def bolt_t(self):
        bolt_t_buy = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        bolt_t_buy.click()

    def onesie(self):
        onesie_buy = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        onesie_buy.click()

    def cart(self):
        cart_buy = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        cart_buy.click()
