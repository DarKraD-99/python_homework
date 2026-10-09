import pytest
from selenium import webdriver
from PageCalc import PageCalc


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_result_calc(driver):
    page_calc = PageCalc(driver)
    page_calc.open()
    page_calc.delay_input()
    page_calc.btn_seven()
    page_calc.btn_plus()
    page_calc.btn_eight()
    page_calc.btn_equal()
    result = page_calc.screen_result()

    assert result == "15"
