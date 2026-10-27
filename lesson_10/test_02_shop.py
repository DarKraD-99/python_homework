import pytest
import allure
from selenium import webdriver
from PageAuth import PageAuth
from PageShop import PageShop
from PageCart import PageCart
from PageCheckout import PageCheckout


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.title("Тестирование магазина")
@allure.description(
    "Тест проверяет авторизацию, добавление товаров в корзину, "
    "заполнение формы данными, сумму товаров в корзине"
)
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет авторизацию, добавление товаров в корзину,
    заполнение формы личными данными и сумму всех добавленных в корзину товаров
    """
    page_auth = PageAuth(driver)

    with allure.step("Открытие страницы авторизации"):
        page_auth.open()

    with allure.step("Ввод логина"):
        page_auth.input_login()

    with allure.step("Ввод пароля"):
        page_auth.input_password()

    with allure.step("Нажатие на кнопку авторизации"):
        page_auth.login_button()

    page_shop = PageShop(driver)

    with allure.step("Добавление в корзину рюкзака"):
        page_shop.backpack()

    with allure.step("Добавление в корзину футболки"):
        page_shop.bolt_t()

    with allure.step("Добавление в корзину комбинезона"):
        page_shop.onesie()

    with allure.step("Переход в корзину"):
        page_shop.cart()

    page_cart = PageCart(driver)

    with allure.step("Нажатие на кнопку для ввода личных данных"):
        page_cart.checkout()

    page_checkout = PageCheckout(driver)

    with allure.step("Ввод личных данных"):
        page_checkout.input_forms()

    with allure.step("Нажатие на кнопку с проверкой цены"):
        page_checkout.continue_btn()
        total = page_checkout.total_price()

    with allure.step("Проверка стоимости товаров добавленных в корзину"):
        assert total == "Total: $58.29"
