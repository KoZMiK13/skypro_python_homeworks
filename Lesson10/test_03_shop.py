import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from title_3.Login import Login
from title_3.Shop import Shop
from title_3.Cart import Cart
from title_3.Information import Information
from title_3.Overview import Overview


@allure.epic("Интернет магазин")
@allure.severity("minor")
@allure.story("Тестирование корзины")
@allure.title("Проверка расчета общей суммы товаров в корзине")
@allure.description("оформление заказа")
@allure.suite("Тест корзины")
def test_total():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    # Откройте сайт магазина: https://www.saucedemo.com/.
    with allure.step("Открыть сайт магазина: https://www.saucedemo.com/"):
        login = Login(driver)

    # Авторизуйтесь как пользователь standard_user.

    login.autorization('standard_user', 'secret_sauce')

    # Добавьте в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T-Shirt.
    # Sauce Labs Onesie.
    shop = Shop(driver)
    shop.add_to_cart()

    # Перейдите в корзину.
    with allure.step("Перейти в корзину"):
        cart = Cart(driver)

    # Нажмите Checkout.
    with allure.step("Нажать CHeckout"):
        information = Information(driver)

    # Заполните форму своими данными:
    # имя,
    # фамилия,
    # почтовый индекс.
    information.fill_info("Constantine", "Belyakov", 199406)

    # Нажмите кнопку Continue.
    with allure.step("Нажать Continue"):
        overview = Overview(driver)

    # Прочитайте со страницы итоговую стоимость (Total).
    total = overview.total()

    # Закройте браузер.
    with allure.step("Закрыть браузер"):
        driver.close()

    # Проверьте, что итоговая сумма равна $58.29.
    with allure.step("Проверить, что итоговая сумма равна $58.29."):
        assert total == "$58.29"

    driver.quit()
