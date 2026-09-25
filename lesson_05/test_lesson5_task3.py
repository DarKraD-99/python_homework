from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    multiple_elements = driver.find_elements(By.TAG_NAME, "a")
    assert len(multiple_elements) == 9

    for element in multiple_elements:
        assert element.is_displayed()

    assert "1" in multiple_elements[0].text

    driver.quit()
