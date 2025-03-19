from selenium.webdriver.common.by import By
import allure


class Information:
    """
    класс для работы с вэб элементами на странице с Информацией о покупателе"""
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://www.saucedemo.com/checkout-step-one.html")

    @allure.step("Заполненние и отправка формы обратной связи {f_name}, {l_name}, {zip}")
    def fill_info(self, f_name: str, l_name: str, zip: str):
        """
        заполнение полей first-name, last-name, postal-code и отправка введенной информации
        """
        with allure.step("очистка и заполнение поля first-name {f_name}"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#first-name").clear()
            self.driver.find_element(
                By.CSS_SELECTOR, "#first-name").send_keys(f_name)

        with allure.step("очистка и заполнение поля last-name {l_name}"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#last-name").clear()
            self.driver.find_element(
                By.CSS_SELECTOR, "#last-name").send_keys(l_name)

        with allure.step("очистка и заполнение поля postal-code {zip}"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#postal-code").clear()
            self.driver.find_element(
                By.CSS_SELECTOR, "#postal-code").send_keys(zip)

        with allure.step("Нажать кнопку continue"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#continue").click()
