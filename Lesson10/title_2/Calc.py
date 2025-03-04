from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calc:
    """
    класс для работы с калькуляором на странице. время ожидания перед выводом результата указывается в поле delay
    """

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    @allure.step("выбор поля, очистка и заполнение временем ожидания - {wait}")
    def delay(self, wait: int):
        """
        выбор. очистка и заполнение поля ожидания (сек.)
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(wait)

    @allure.step("выбор и нажатие кнопки 7")
    def seven(self):
        """
        выбор и нажатие кнопки 7
        """
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()

    @allure.step("выбор и нажатие кнопки +")
    def add(self):
        """
        выбор и нажатие кнопки +
        """
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()

    @allure.step("выбор и нажатие кнопки 8")
    def eight(self):
        """
        выбор и нажатие кнопки 8
        """
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()

    @allure.step("выбор и нажатие кнопки =")
    def result(self):
        """
        выбор и нажатие кнопки =
        """
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("ожидание, до тех пор Ппока в итоге вычислений не появится результат 15 ")
    def waiter(self, wait_time):
        """
        ожидание до тех пор, пока в поле с итогом расчетов не появится результат 15"""
        waiter = WebDriverWait(self._driver, wait_time)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15")
            )

    @allure.step("возврат текста из параметров поля и конвертация текста в число")
    def final_res(self) -> int:
        """
        возвращает текст из поля с результатом вычислений и конвертирует его в число
        """
        final_res = int(self._driver.find_element(
            By.CSS_SELECTOR, "div.screen").text)
        return int(final_res)
