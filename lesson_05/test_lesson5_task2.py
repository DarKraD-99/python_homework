from selenium import webdriver
from selenium.webdriver.common.by import By


def test_from_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    submission = driver.find_element(By.NAME, "custname")
    submission.send_keys("Дмитрий")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
