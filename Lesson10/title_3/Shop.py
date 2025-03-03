from selenium.webdriver.common.by import By
import allure

class Shop:
    """класс для работы с вэб-элементами на странице магазина
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/inventory.html")

    @allure.step("добавление в корзину товаров Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie")
    def add_to_cart(self):
        """
        добавление в корзину товаров Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
