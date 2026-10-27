import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckout:

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса PageCheckout
        :param driver: WebDriver - объект драйвера Selenium
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение формы личными данными")
    def input_forms(self) -> None:
        """
        Заполняет форму личными данными
        :return: None
        """
        input_forms = self.driver.find_elements(By.CLASS_NAME, "form_input")
        forms = [
            "Дмитрий",
            "Пашкин",
            "650000"
            ]
        for i in range(3):
            input_forms[i].send_keys(forms[i])

    @allure.step("Нажатие на кнопку 'Continue'")
    def continue_btn(self) -> None:
        """
        Нажимает на кнопку 'continue'
        :return: None
        """
        continue_btn = self.wait.until(EC.presence_of_element_located(
            (By.ID, "continue")
        ))
        continue_btn.click()

    @allure.step("Получение итоговой стоимости товаров в корзине")
    def total_price(self) -> str:
        """
        Возвращает итоговую стоимость всех товаров в корзине
        :return: str - текст итоговой стоимости
        """
        self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        ))
        price_total = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        return price_total.text
