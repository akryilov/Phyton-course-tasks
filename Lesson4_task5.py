# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(prev_el, el):
    # prev_el - previous element
    # el - current element
    return prev_el * el


my_list = [int(el) for el in range(100, 1001) if el % 2 == 0]
print(f"Incoming numbers: {my_list}")
print(f'Result is: {reduce(my_func, my_list)}')
