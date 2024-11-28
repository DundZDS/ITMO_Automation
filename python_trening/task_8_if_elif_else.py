# Программа проверяет число, являееся оно положительными
# или отрицательным и выводит соответствующие сообщение


# num = 0
#
#
# if num >= 0:
#     print('Число больше или равно 0')
# else:
#     print('Число отрицательное')
#
#
# # str_2 содержит в себе str_1?
#
#
# str_1 = 'test'
# str_2 = 'test1'
#
# def task_yes_or_no (str_1, str_2):
#     if str_1 in str_2:
#         print('yes')
#     else:
#         print('no')
#
# task_yes_or_no(str_1 = 'tast', str_2 = 'test1')
#
#
# num_float = -3.4
#
#
# if num_float > 0:
#     print('Положительное число')
# elif num_float == 0:
#     print('Ноль')
# else:
#     print('Число отрицательное')


# num = 1
#
# permit_print = True
#
#
# if num > 0 and permit_print:
#     print('num - положительное число')
# elif not permit_print:
#     print('Печать запрещена')

#
# def cours(year):
#     if 1<=year<=4:
#         print('Бакалавр')
#     elif 5<=year<=6:
#         print('Магистр')
#     elif 7<=year<=9:
#         print('Аспирант')
#     else:
#         print('Введите корректный год обучения')
#
# cours(7)
#
# def student_rank(year_of_study):
#     if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study ==4:
#         print('Вы - бакалавр')
#     elif year_of_study in range(5-7):
#         print('Вы - магистр')
#     elif 7<= year_of_study <=9:
#         print('Вы - аспирант')
#     else:
#         print('Введите корректный год обучения')
#
#
# student_rank(0)


def num_x (num):
    if num>100 or num<-100:
        print('-')
    else:
        print('+')


num_x(111)