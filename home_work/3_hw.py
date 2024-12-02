# Задача 2. Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.
from itertools import count


def compare_numbers(num_1, num_2):
    if num_1>num_2:
        print(num_1)
    elif num_1 == num_2:
        print('Числа равны')
    else:
        print(num_2)

compare_numbers(5,55)


# Задача 3. Функция на вход получает два произвольных числа. Вывести в консоль “yes”,
# если они отличаются друг от друга на 135, иначе вывести на экран “No”


def number_difference_135(num_3, num_4):
    if abs(num_3 - num_4) == 135:
        print('Yes', abs(num_3 - num_4))
    else:
        print('No', abs(num_3 - num_4))

number_difference_135(-1,-136)


# Задача4. Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)


def time_of_year(month):
    if 1<=month<=12:
        if 1<=month<=2 or month == 12:
            print('Зима')
        elif month in range (3,5):
            print('Весна')
        elif month in range (6,8):
            print('Лето')
        elif month in range (9,11):
            print('Осень')
    else:
        print('Введите номер месяца (от 1 до 12)')


time_of_year(-9)

# Задача5. Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран “yes”, иначе “no”;

def three_numbers_greater_than_10(num_6,num_7,num_8):
    if num_6 > 10 and num_7 > 10 and num_8 > 10:
        print('yes')
    else:
        print('no')

three_numbers_greater_than_10(10,-22,-33)


# Задача6. Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.

def number_of_possitive_numbers(list_numbers:list):

    count: int = 0

    for elem in list_numbers:
        if elem > 0:
            count = count +1
    else:
        print (count)

number_of_possitive_numbers ([-1,-2,4,5,6])


# Задача7. Функция на вход получает 2 переменные.
# a. Кол-во лет (int)
# b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

def count_days(year:int, month:int):
    days:int = 0
    if year>=0 and month>=0:
        days = year * 12 * 29 + month * 29
        print('В данном периоде', days, 'дн.')
    else:
        print('Введите положительные целые числа')

count_days(1,-9)