# def f(s:str = ''):
#     return len(s)
# print('length string =', f('vsve4vw34fvv4'))
#
#
# def max_list(list_1:list, list_2: list) -> int:
#     return max(len(list_1),len(list_2))
# print(max_list(('a', 'v', 'f', 'f','a' ),('a', 'f')))


def append_list(my_list: list):
    my_list.append('jhh')
    return my_list
print(append_list(['h']))

def sum_list(list3: list) ->int:
    result = 0
    for elem in list3:
        result = result +elem
    return result
print(sum_list([2, 3, 4, 5]))

