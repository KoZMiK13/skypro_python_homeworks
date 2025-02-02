import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from title_2.Calc import Calc

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
calc = Calc(driver)

# В поле ввода по локатору #delay введите значение 45.
calc.delay(45)

# Нажмите на кнопки:
# 7
# +
# 8
# =
calc.seven()
calc.add()
calc.eight()
calc.result()

calc.waiter(46)

final_res = calc.final_res()

print("7+8 =", final_res)

# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.


def test_res():
    assert final_res == 7+8


driver.quit()
