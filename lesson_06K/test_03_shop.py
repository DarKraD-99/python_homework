from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    input_login = driver.find_element(By.ID, "user-name")
    input_login.send_keys("standard_user")

    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("secret_sauce")

    login_btn = wait.until(EC.presence_of_element_located(
        (By.ID, "login-button")
    ))
    login_btn.click()

    backback_buy = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    )
    backback_buy.click()

    bolt_t_buy = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    bolt_t_buy.click()

    onesie_buy = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie"
    )
    onesie_buy.click()

    cart_buy = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_buy.click()

    checkout_btn = wait.until(EC.presence_of_element_located(
        (By.ID, "checkout")
    ))
    checkout_btn.click()

    input_forms = driver.find_elements(By.CLASS_NAME, "form_input")
    assert len(input_forms) == 3

    forms = [
        "Дмитрий",
        "Пашкин",
        "650000"
    ]

    for i in range(3):
        input_forms[i].send_keys(forms[i])

    continue_btn = wait.until(EC.presence_of_element_located(
        (By.ID, "continue")
    ))
    continue_btn.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "summary_total_label"), "Total: $58.29"
    ))
    price_total = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total = price_total.text

    driver.quit()

    assert total == "Total: $58.29"
