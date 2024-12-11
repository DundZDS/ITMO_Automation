# создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:


    def __init__(self, width, height):
        self.width = width
        self.height = height

    def Area(self):
        if self.width >0 and self.height >0:
            Area = self.width * self.height
            print('Area = ',Area)
        else:
            print('Введите корректные параметры ширины и высоты')

    def Perimetr(self):
        if self.width > 0 and self.height > 0:
            Perimetr = 2*(self.width + self.height)
            print('Perimetr = ', Perimetr)
        else:
            print('Введите корректные параметры ширины и высоты')

rectangle1 = Rectangle(5,2)
rectangle1.Area()
rectangle1.Perimetr()

print('\n')

rectangle2 = Rectangle(10, 4)
rectangle2.Area()
rectangle2.Perimetr()

print('\n')

rectangle3 = Rectangle(3, 7)
rectangle3.Area()
rectangle3.Perimetr()

print('\n')

# Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с
# ними нужно производить соответствующие действия и печатать ответ.


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Addition(self):
        addition = self.a +self.b
        print('Сумма чисел равно ', addition)

    def Multiplication(self):
        multiplication = self.a * self.b
        print('Произведение чисел равно',multiplication)

    def Division(self):
        if self.b != 0:
            division = self.a/self.b
            print('Частные от деления чисел равно ', division)
        else:
            print('Значение b не должно быть 0')

    def Subtraction(self):
        subtraction = self.a - self.b
        print('Разность чисел равна ', subtraction)

math = Math(10,0)

math.Addition()
math.Multiplication()
math.Subtraction()
math.Division()


# откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки


class Tools:


    type: str = 'Button'


    def __init__(self, text, loc = None):
        self.text = text
        self.loc = loc


    def click(self):
        return 'Клик по кнопке - {}'.format(self.text)

Text_Box = Tools('Text Box', type)
print(Text_Box.text, Text_Box.click())
Check_Box = Tools('Check Box')
print(Check_Box.text, Check_Box.click())
Radio_button = Tools('Radio Button')
print(Radio_button.text, Radio_button.click())
Web_Tables = Tools('Web Tables')
print(Web_Tables.text , Web_Tables.click())
Buttons = Tools('Buttons')
print(Buttons.text , Buttons.click())
Links = Tools('Links')
print(Links.text , Links.click())
Broken_links_Images = Tools('Broken links - Images')
print(Broken_links_Images.text, Broken_links_Images.click())
Upload_and_Download = Tools('Upload and Download')
print(Upload_and_Download.text, Upload_and_Download.click())
Dynamic_Properties = Tools('Dynamic Properties')
print(Dynamic_Properties.text, Dynamic_Properties.click())



