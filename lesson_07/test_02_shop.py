import pytest
from selenium import webdriver
from PageAuth import PageAuth
from PageShop import PageShop
from PageCart import PageCart
from PageCheckout import PageCheckout


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):
    page_auth = PageAuth(driver)
    page_auth.open()
    page_auth.input_login()
    page_auth.input_password()
    page_auth.login_button()

    page_shop = PageShop(driver)
    page_shop.backpack()
    page_shop.bolt_t()
    page_shop.onesie()
    page_shop.cart()

    page_cart = PageCart(driver)
    page_cart.checkout()

    page_checkout = PageCheckout(driver)
    page_checkout.input_forms()
    page_checkout.continue_btn()
    total = page_checkout.total_price()
    assert total == "Total: $58.29"
