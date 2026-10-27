import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class PageCart:

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса PageCart
        :param driver: WebDriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Получение списка товаров в корзине")
    def сart_contents(self) -> list[str]:
        """
        Возвращает список выбранных товаров
        :return: list[str] - список товаров
        """
        cart_contents = self.wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item_name")
        ))

        contents = [
            cart_contents[0].text,
            cart_contents[1].text,
            cart_contents[2].text
        ]
        return contents

    @allure.step("Нажатие на кнопку")
    def checkout(self) -> None:
        """
        Нажимает на кнопку Checkout
        """
        checkout_btn = self.wait.until(EC.presence_of_element_located(
            (By.ID, "checkout")
        ))
        checkout_btn.click()
