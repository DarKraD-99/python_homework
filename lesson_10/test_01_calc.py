import pytest
import allure
from selenium import webdriver
from PageCalc import PageCalc


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет функцию сложения на калькуляторе")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_result_calc(driver):
    """
    Тест проверяет функционал калькулятора с опцией сложения
    :param driver: WebDriver - объект драйвера, переданный фикстурой
    :return: None
    """
    page_calc = PageCalc(driver)
    with allure.step("Открытие страницы калькулятора"):
        page_calc.open()

    with allure.step("Установка задержки в секундах"):
        page_calc.delay_input()

    with allure.step("Нажатие на кнопку '7'"):
        page_calc.btn_seven()

    with allure.step("Нажатие на кнопку '+'"):
        page_calc.btn_plus()

    with allure.step("Нажатие на кнопку '8'"):
        page_calc.btn_eight()

    with allure.step("Нажатие на кнопку '='"):
        page_calc.btn_equal()
        result = page_calc.screen_result()

    with allure.step("Проверка результата"):
        assert result == "15"
