# В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:


    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def Start(self):
        return print('Автомобиль заведен')

    def Turned_off(self):
        return print('Автомобиль заглушен')

    def Year_of_manufacture(self):
        return f'Год выпуска {self.year}'

    def Car_type(self):
        return f'Машина {self.type}'

    def Car_color(self):
        return f'Цвет машины {self.color}'

newcar = Car ('white', 'BMW', 2024)

newcar.Start()
newcar.Turned_off()
print(newcar.Year_of_manufacture())
print(newcar.Car_type())
print(newcar.Car_color())
