from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))


driver = webdriver.Chrome()


# Перейдите на сайт http://uitestingplayground.com/textinput.
driver.get("http://uitestingplayground.com/textinput")

# Укажите в поле ввода текст SkyPro.
find_element = driver.find_element(By.CSS_SELECTOR, "input#newButtonName")
find_element.send_keys("SkyPro")

# Нажмите на синюю кнопку.
new_element = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
click_new_element = new_element.click()

# Получите текст кнопки и выведите в консоль ("SkyPro").
text = new_element.text
print(text)

driver.quit()
