import allure
from selenium.webdriver.common.by import By

@allure.epic("Главная страница")
@allure.severity("minor")
class DataTypes:
    """
    класс для работы с элементами на главной станице
    """

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение поля first name {data}")
    def first_name(self, data: str):
        """
        выбор заполнение поля first-name            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='first-name']").send_keys(data)

    @allure.step("Заполнение поля last name {data}")
    def last_name(self, data: str):
        """
        выбор и заполнение поля last-name            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='last-name']").send_keys(data)

    @allure.step("Заполнение поля address {data}")
    def address(self, data: str):
        """
        выбор и заполнение поля adress            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='address']").send_keys(data)

    @allure.step("Заполнение поля e-mail {data}")
    def email(self, data: str):
        """
        выбор и заполнение поля e-mail            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='e-mail']").send_keys(data)

    @allure.step("Заполнение поля phone number {data}")
    def phone_number(self, data: str):
        """
        выбор и заполнение поля phone            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='phone']").send_keys(data)

    @allure.step("Заполнение поля zip code {data}")
    def zip_code(self, data: str):
        """
        выбор и заполнение поля zip-code            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='zip-code']").send_keys(data)

    @allure.step("Заполнение поля first city {data}")
    def city(self, data: str):
        """
        выбор и заполнение поля city            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='city']").send_keys(data)

    @allure.step("Заполнение поля country {data}")
    def country(self, data: str):
        """
        выбор и заполнение поля country            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='country']").send_keys(data)

    @allure.step("Заполнение поля job position {data}")
    def job_position(self, data: str):
        """
        выбор и заполнение поля job-position            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='job-position']").send_keys(data)

    @allure.step("Заполнение поля company {data}")
    def company(self, data: str):
        """
        выбор и заполнение поля company            
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "[name='company']").send_keys(data)

    @allure.step("Нажать на кнопку Submit")
    def submit(self):
        """
        выбор кнопки submit и клик            
        """
        submit_button = self._driver.find_element(
                By.CSS_SELECTOR, "button.btn"
                )
        submit_button.click()
