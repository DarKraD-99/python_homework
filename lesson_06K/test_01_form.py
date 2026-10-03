from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_input():
    driver = webdriver.Edge()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    forms_input = driver.find_elements(By.CLASS_NAME, "form-control")
    assert len(forms_input) == 10

    forms = [
        "Иван",
        "Петров",
        "Ленина, 55-3",
        "",
        "Москва",
        "Россия",
        "test@skypro.com",
        "+7985899998787",
        "QA",
        "SkyPro"
    ]

    for i in range(10):
        forms_input[i].send_keys(forms[i])

    button_submit = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "btn")
    ))
    button_submit.click()

    alert_input = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")
    ))
    assert "alert-danger" in alert_input.get_attribute("class")

    success_input = wait.until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "alert-success")
    ))
    assert len(success_input) == 9

    driver.quit()
