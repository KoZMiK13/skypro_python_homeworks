from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(16)

# Перейдите на страницу http://uitestingplayground.com/ajax.
driver.get("http://uitestingplayground.com/ajax")

# Нажмите на синюю кнопку.
click_button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()

# Получите текст из зеленой плашки.
element = driver.find_element(By.CSS_SELECTOR, "#content")
text = element.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Выведите его в консоль
print(text)

driver.quit()
