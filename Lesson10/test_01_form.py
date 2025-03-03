import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tiltle_1.DataTypes import DataTypes
from tiltle_1.Submit import Submit

@allure.epic("Главная страница")
@allure.severity("minor")
@allure.story("проверка цветов выдеоения полей при заполнении")
@allure.feature("Fill")
@allure.title("Подсветка полей на странице в зависимости от корректного/некорректного заполнения")
@allure.description("заполнение формы обратной связи")
@allure.suite("Тест цветов")
def test_colors():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser = webdriver.Chrome()

# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    with allure.step("Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html"):
        datatypes = DataTypes(browser)

# Заполните форму значениями:
# First name - Иван
# Last name - Петров
# Address - Ленина, 55-3
# Email - test@skypro.com
# Phone number - +7985899998787
# Zip code - *оставить пустым
# City - Москва
# Country - Россия
# Job position - QA
# Company - SkyPro
    with allure.step("Заполнить поля значениями:"):
        datatypes.first_name("Иван")
        datatypes.last_name("Петров")
        datatypes.address("Ленина, 55-3")
        datatypes.email("test@skypro.com")
        datatypes.phone_number("+7985899998787")
        datatypes.zip_code("")
        datatypes.city("Москва")
        datatypes.country("Россия")
        datatypes.job_position("QA")
        datatypes.company("SkyPro")

# Нажмите кнопку Submit.
    with allure.step("Нажать кнопку Submit"):
        submit = Submit(browser)

# Проверьте (assert), что поле Zip code подсвечено красным.
    with allure.step("Проверить что поле Zip code подсвечено красным"):
        with allure.step("выбор элемента подсвеченного красным для установки параметров красного цвета"):
            red = submit.zip_code()
        
        with allure.step("подтвердить что подсветка поля соответствует параметрам цвета поля подсвеченного красным цветом "):
            assert submit.zip_code() == red

# # Проверьте (assert), что остальные поля подсвечены зеленым.
    with allure.step("Проверить что остальные поля подсвечены зеленым"):
        with allure.step("выбор элемента подсвеченного зеленым для установки параметров зеленого цвета"):
            green = submit.first_name()
        
        with allure.step("формирование списка ос оставшимися параметрами элементов"):
            elements = [
                submit.first_name(),
                submit.last_name(),
                submit.address(),
                submit.email(),
                submit.phone_number(),
                submit.city(),
                submit.country(),
                submit.job_position(),
                submit.company()
            ]

        with allure.step("подтвердить что  подсветка каждого элемента списка соответствует параметрам цвета поля подсвеченным зеленым цветом "):
            for element in elements:
                assert element == green
    
    
    browser.quit()
