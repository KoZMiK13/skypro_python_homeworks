from selenium.webdriver.common.by import By
import allure


class Submit:
    """
    класс для работы с элементами после нажатия кнопки Submit на главной странице
    """

    def __init__(self, browser):
        self.driver = browser
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "button.btn")
        submit_button.click()

    @allure.step("выбор элемента first name для возврата параметров цвета")
    def first_name(self):
        """
        возвращает параметры поля first-name
        """
        first_name = self.driver.find_element(
            By.CSS_SELECTOR, "#first-name")
        return first_name.value_of_css_property("color")

    @allure.step("выбор элемента last name для возврата параметров цвета")
    def last_name(self):
        """
        возвращает параметры поля last-name
        """
        last_name = self.driver.find_element(
            By.CSS_SELECTOR, "#last-name")
        return last_name.value_of_css_property("color")

    @allure.step("выбор элемента adress для возврата параметров цвета")
    def address(self):
        """
        возвращает параметры поля adress
        """
        address = self.driver.find_element(
            By.CSS_SELECTOR, "#address")
        return address.value_of_css_property("color")

    @allure.step("выбор элемента e-mail для возврата параметров цвета")
    def email(self):
        """
        возвращает параметры поля email
        """
        email = self.driver.find_element(
            By.CSS_SELECTOR, "#e-mail")
        return email.value_of_css_property("color")

    @allure.step("выбор элемента phone-number для возврата параметров цвета")
    def phone_number(self):
        """
        возвращает параметры поля phone-number
        """
        phone_number = self.driver.find_element(
            By.CSS_SELECTOR, "#phone")
        return phone_number.value_of_css_property("color")

    @allure.step("выбор элемента zip-code для возврата параметров цвета")
    def zip_code(self):
        """
        возвращает параметры поля zip-code
        """
        zip_code = self.driver.find_element(
            By.CSS_SELECTOR, "#zip-code")
        return zip_code.value_of_css_property("color")

    @allure.step("выбор элемента city для возврата параметров цвета")
    def city(self):
        """
        возвращает параметры поля city
        """
        city = self.driver.find_element(
            By.CSS_SELECTOR, "#city")
        return city.value_of_css_property("color")

    @allure.step("выбор элемента country для возврата параметров цвета")
    def country(self):
        """
        возвращает параметры поля counry
        """
        country = self.driver.find_element(
            By.CSS_SELECTOR, "#country")
        return country.value_of_css_property("color")

    @allure.step("выбор элемента job-position для возврата параметров цвета")
    def job_position(self):
        """
        возвращает параметры поля job-position
        """
        job_position = self.driver.find_element(
            By.CSS_SELECTOR, "#job-position")
        return job_position.value_of_css_property("color")

    @allure.step("выбор элемента company для возврата параметров цвета")
    def company(self):
        """
        возвращает параметры поля company
        """
        company = self.driver.find_element(
            By.CSS_SELECTOR, "#company")
        return company.value_of_css_property("color")
