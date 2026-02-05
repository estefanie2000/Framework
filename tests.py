from framework import get_driver, BASE_URL
from pages import LoginPage
import time


def test_login():
    driver = get_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    time.sleep(5)  # para ver el navegador abierto
    driver.quit()


if __name__ == "__main__":
    test_login()
