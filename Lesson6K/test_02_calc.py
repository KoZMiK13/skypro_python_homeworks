import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 16)

# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# В поле ввода по локатору #delay введите значение 45.
driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(15)

# Нажмите на кнопки:
# 7
# +
# 8
# =
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

final_res = int(driver.find_element(By.CSS_SELECTOR, "div.screen").text)

print("7+8 =", final_res)

# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
assert final_res == 7+8

driver.quit()
