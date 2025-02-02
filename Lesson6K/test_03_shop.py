import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 16)

# Откройте сайт магазина: https://www.saucedemo.com/.
driver.get("https://www.saucedemo.com/")

# Авторизуйтесь как пользователь standard_user.
driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

driver.find_element(By.CSS_SELECTOR, "#password").clear()
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

driver.find_element(By.CSS_SELECTOR, "#login-button").click()

# Добавьте в корзину товары:
# Sauce Labs Backpack.
# Sauce Labs Bolt T-Shirt.
# Sauce Labs Onesie.
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

# Перейдите в корзину.
driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()

# Нажмите Checkout.
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

# Заполните форму своими данными:
# имя,
# фамилия,
# почтовый индекс.
driver.find_element(By.CSS_SELECTOR, "#first-name").clear()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Constantine")

driver.find_element(By.CSS_SELECTOR, "#last-name").clear()
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Belyakov")

driver.find_element(By.CSS_SELECTOR, "#postal-code").clear()
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(199406)

# Нажмите кнопку Continue.
driver.find_element(By.CSS_SELECTOR, "#continue").click()

# Прочитайте со страницы итоговую стоимость (Total).
total = list((driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text).split(" "))

# Закройте браузер.
driver.close()

# Проверьте, что итоговая сумма равна $58.29.
assert total[1] == "$58.29"

driver.quit()