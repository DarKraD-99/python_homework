import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class PageAuth:

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса PageAuth
        :param driver: WebDriver - объект драйвера Selenium
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы с авторизацией")
    def open(self) -> None:
        """
        Открывает страницу авторизации
        :return: None
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод логина для авторизации")
    def input_login(self) -> None:
        """
        Вводит логин для авторизации
        :return: None
        """
        input_login = self.driver.find_element(By.ID, "user-name")
        input_login.send_keys("standard_user")

    @allure.step("Ввод пароля для авторизации")
    def input_password(self) -> None:
        """
        Вводит пароль для авторизации
        :return: None
        """
        input_password = self.driver.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")

    @allure.step("Нажатие на кнопку авторизации")
    def login_button(self) -> None:
        """
        Нажимает на кнопку авторизации
        :return: None
        """
        login_btn = self.wait.until(EC.presence_of_element_located(
            (By.ID, "login-button")
        ))
        login_btn.click()
