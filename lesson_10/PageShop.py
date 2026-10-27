import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageShop:

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса PageShop
        :param driver: WebDriver - объект драйвера Selenium
        :return: None
        """
        self.driver = driver

    @allure.step("Добавление рюкзака в корзину")
    def backpack(self) -> None:
        """
        Нажимает на кнопку добавления в корзину рюкзака
        :return: None
        """
        backpack_buy = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        backpack_buy.click()

    @allure.step("Добавление футболки в корзину")
    def bolt_t(self) -> None:
        """
        Нажимает на кнопку добавления в корзину футболки
        :return: None
        """
        bolt_t_buy = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        bolt_t_buy.click()

    @allure.step("Добавление комбинезона в корзину")
    def onesie(self) -> None:
        """
        Нажимает на кнопку добавления в корзину комбинезона
        :return: None
        """
        onesie_buy = self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        onesie_buy.click()

    @allure.step("Переход в корзину")
    def cart(self) -> None:
        """
        Нажимает на корзину
        :return: None
        """
        cart_buy = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )
        cart_buy.click()
