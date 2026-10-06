from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    wait = WebDriverWait(driver, 50)

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button_seven = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[text()='7']")
    ))
    button_seven.click()

    button_plus = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[text()='+']")
    ))
    button_plus.click()

    button_eight = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[text()='8']")
    ))
    button_eight.click()

    button_equals = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[@class='btn btn-outline-warning']")
    ))
    button_equals.click()

    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15"
    ))
    screen_result = driver.find_element(By.CLASS_NAME, "screen")
    assert screen_result.text == "15"

    driver.quit()
