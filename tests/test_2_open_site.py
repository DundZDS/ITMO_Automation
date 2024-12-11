from selenium import webdriver


driver = webdriver.Firefox()
driver.get ("https://demoqa.com/")


# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR,'header > a > img')
if icon is None:
    print('Элемент не найден')




