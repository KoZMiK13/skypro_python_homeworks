from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calc:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self, wait):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(wait)


    def seven(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()

    def add(self):
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
    

    def eight(self):
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        
    def result(self):
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def waiter(self, wait_time):
        waiter = WebDriverWait(self._driver, wait_time)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
            )
    
    def final_res(self):
        final_res = int(self._driver.find_element(By.CSS_SELECTOR, "div.screen").text)
        return int(final_res)
