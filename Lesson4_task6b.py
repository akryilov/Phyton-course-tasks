# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Solving 6.b

from itertools import cycle


init_value = [str(i) for i in input('Enter numbers using space: ').split()]
stop_value = int(input('Enter the # of counts: '))

i = 1
for el in cycle(init_value):
    if i > stop_value * len(init_value):
        print(f'the #{stop_value} of counts achieved')
        break
    print(f'{el}')
    i += 1