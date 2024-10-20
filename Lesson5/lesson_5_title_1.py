from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver = webdriver.Chrome()

#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element

for x in range(5):
    click_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()

sleep(5)

# Соберите со страницы список кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

sleep(5)

# Выведите на экран размер списка.
print(len(delete_buttons))
