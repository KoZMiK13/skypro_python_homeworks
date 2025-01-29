import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tiltle_1.DataTypes import DataTypes
from tiltle_1.Submit import Submit

browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
browser = webdriver.Chrome()

# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html

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
submit = Submit(browser)

# Проверьте (assert), что поле Zip code подсвечено красным.

red = submit.zip_code().value_of_css_property("color")
green = submit.first_name().value_of_css_property("color")

assert submit.zip_code().value_of_css_property("color") == red

# # Проверьте (assert), что остальные поля подсвечены зеленым.

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

for element in elements:
    assert element.value_of_css_property("color") == green

browser.quit()
