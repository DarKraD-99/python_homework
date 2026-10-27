import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class PageCalc:

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса PageCalc
        :param driver: WebDriver - объект драйвера Selenium
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора
        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    @allure.step("Установка задержки в секундах")
    def delay_input(self) -> None:
        """
        Устанавливает задержку для выполнения операции
        :return: None
        """
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys("45")

    @allure.step("Нажатие на кнопку '7'")
    def btn_seven(self) -> None:
        """
        Нажимает на кнопку '7' на калькуляторе
        :return: None
        """
        btn_seven = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='7']")
        ))
        btn_seven.click()

    @allure.step("Нажатие на кнопку '+'")
    def btn_plus(self) -> None:
        """
        Нажимает на кнопку '+' на калькуляторе
        :return: None
        """
        btn_plus = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='+']")
        ))
        btn_plus.click()

    @allure.step("Нажатие на кнопку '8'")
    def btn_eight(self) -> None:
        """
        Нажимает на кнопку '8' на калькуляторе
        :return: None
        """
        btn_eight = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='8']")
        ))
        btn_eight.click()

    @allure.step("Нажатие на кнопку '='")
    def btn_equal(self) -> None:
        """
        Нажимает на кнопку '=' на калькуляторе
        :return: None
        """
        btn_equal = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='btn btn-outline-warning']")
        ))
        btn_equal.click()

    @allure.step("Получение результата на экране калькулятора")
    def screen_result(self) -> str:
        """
        Возвращает текущий результат с экрана калькулятора
        :return: str - текст результата на экране калькулятора
        """
        screen_result = self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"
            ))
        screen_result = self.driver.find_element(By.CLASS_NAME, "screen")
        return screen_result.text
