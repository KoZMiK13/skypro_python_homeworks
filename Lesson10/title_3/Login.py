from selenium.webdriver.common.by import By
import allure

class Login:
    """
    класс для работы с веб элеменами на странице для прохождения авторизации
    """
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация по логину {user_name} и паролю {password}")
    def autorization(self, user_name: str, password: str):
        """
        авторизация по логину и паролю
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").clear()
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").clear()
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
