from selenium.webdriver.common.by import By
import allure


class Overview:
    """
    класс для работы с вэб-элементами на странице с заказом
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")

    @allure.step("Возврат общей суммы заказа (Total)")
    def total(self) -> str:
        """
        возвращает общую суииу заказа
        """
        totals = list((self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text).split(" ")
            )
        total = totals[1]
        return total
