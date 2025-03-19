import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from title_2.Calc import Calc


@allure.epic("Калькулятор")
@allure.severity("minor")
@allure.story("тестирование работы калькулятора")
@allure.title("Проверка результата вычислений с ожиданием в соответствии с заданными параметрами")
@allure.description("вычисления калькулятора с ожиданием")
@allure.suite("Тест калькулятора")
def test_res():
    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager().install()
            )
        )

    # Откройте страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    with allure.step("Открыть страницу https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"):
        calc = Calc(driver)

    # В поле ввода по локатору #delay введите значение 45.
    calc.delay(5)

    # Нажмите на кнопки:
    # 7
    # +
    # 8
    # =
    calc.seven()
    calc.add()
    calc.eight()
    calc.result()

    calc.waiter(6)

    final_res = calc.final_res()

    print("7+8 =", final_res)

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.

    with allure.step("Подтвердить, что полученный результат равен 7+8"):
        assert final_res == 7+8

    driver.quit()
