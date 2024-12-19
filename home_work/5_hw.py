from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get ("https://www.saucedemo.com/")

# поиск элемента
username_field = driver.find_element(By.CSS_SELECTOR,' #user-name ')
password_field = driver.find_element(By.CSS_SELECTOR, ' #password ')
button_submit = driver.find_element(By.CSS_SELECTOR, ' #login-button ')

if (username_field or password_field or button_submit) is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

