from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)

    start_button = driver.find_element(
        By.CSS_SELECTOR, "#start button"
    )
    start_button.click()

    start_text = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//h4[text()='Hello World!']")
    ))

    driver.save_screenshot("screen_page.png")

    assert start_text.text == "Hello World!", "Текст не совпадает"

    driver.quit()
