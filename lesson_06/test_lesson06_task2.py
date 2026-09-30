from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NmVkYmFiMjAtZjQ1OS00ZWU5LTk3OWYtOGMwZjUzMTU2YTNl",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/stud01")
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//b[text()='@stud01']")
    ))
    url_user1 = driver.current_url

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "OWE1YzQ0MTctYjUwZi00NWI4LTg4ZGQtMDIzMDcwZjJlZDUy",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/stud02")
    wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//b[text()='@stud02']")
    ))
    url_user2 = driver.current_url

    assert url_user1 != url_user2, (
        f"URL совпадают: user1={url_user1}, user2={url_user2}"
    )

    driver.quit()
