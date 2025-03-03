from selenium.webdriver.common.by import By
import allure

class Cart:
    """
    класс для работы с вэб-элементами корзины
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Нажать кнопку Checkout")
    def checkout(self):
        """
        выбор и нажатие кнопки checkout
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
