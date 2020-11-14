# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count

init_value = int(input('Enter the initial int value: '))
stop_value = int(input('Enter the stop int value: '))

while init_value >= stop_value:
    print('initial >= stop!')
    break
else:
    for el in count(init_value):
        if el > stop_value:
            print('the stop value achieved')
            break
        else:
            print(el)


# Solving 6.2

# from itertools import cycle
#
# #
# init_value = [str(i) for i in input('Enter numbers using space: ').split()]
# stop_value = int(input('Enter the # of counts: '))
#
# i = 1
# for el in cycle(init_value):
#     if i > stop_value * len(init_value):
#         print('the # of counts achieved')
#         break
#     print(f'{el}')
#     i += 1
