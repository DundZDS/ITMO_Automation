# папка python_trening
# Создайте файл task_9_checks.py
# a. создайте класс Checks, принимающий 1 аргумент при инициализации (loc)
# b. создайте для него метод check_text, метод возвращает self.loc
# в файле task_9_oop_1.py
# c. наследуйте все классы от класса Checks
# i. чтобы использовать класс из другого файла его нужно импортировать
# from название файла(без расширения) import название класса
# d. переделайте все 4 класса в файле task_9_oop_1.py так чтоб в объектах можно было использовать методы родительского класса
# e. распечатайте в консоль результаты метода .check_text() вызванного от каждого объекта классов файла task_9_oop_1.py

from task_9_oop_1 import Input, Button, Title, Link, Page
from python_trening.task_9_oop_1 import Search, home_title, home_link, home_button

print(Search.check_text())
print(home_button.check_text())
print(home_title.check_text())
print(home_link.check_text())

