from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 40)

# Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

# Дождитесь загрузки всех картинок.
waiter.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "#text"), "Done!"))

# Получите значение атрибута src у 3-й картинки.
src = driver.find_element(By.CSS_SELECTOR, "img#award")

# Выведите значение в консоль.
print(src.get_attribute("src"))

driver.quit()
