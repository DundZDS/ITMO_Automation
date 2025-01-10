from selenium import webdriver

from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get ("https://demoqa.com/")


# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR,'header > a > img')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


# > body > > div >header > a >img src='/images/toolsqa.jpg'
#
# footer span
#
#
# [class = "card mt-4 top-card"]