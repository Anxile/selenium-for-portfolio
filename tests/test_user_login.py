import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    yield _driver
    _driver.quit()


class TestUserLogin:
    def test_login_success(self, driver):
        name = "Yihe_mac"
        password = "123456"
        expected_path = "/posts"

        driver.get("https://www.bytecho.ca/")

        driver.find_element(By.ID,"login").click()
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user_name"))
        )
        username_input.send_keys(name)
        driver.find_element(By.ID, "user_password").send_keys(password)
        driver.find_element(By.NAME, "commit").click()

        WebDriverWait(driver, 10).until(
            EC.url_contains(expected_path)
        )

        assert driver.current_url.endswith(expected_path)

    def test_login_failure(self, driver):
        name = "Yihe_mac"
        password = "qqqqqqqq"
        expected_path = "/posts"

        driver.get("https://www.bytecho.ca/")

        driver.find_element(By.ID, "login").click()
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user_name"))
        )
        username_input.send_keys(name)
        driver.find_element(By.ID, "user_password").send_keys(password)
        driver.find_element(By.NAME, "commit").click()

        try:
            WebDriverWait(driver, 5).until(
                EC.url_contains(expected_path)
            )
            login_successful = True
        except TimeoutException:
            login_successful = False

        assert not login_successful
        assert not driver.current_url.endswith(expected_path)
