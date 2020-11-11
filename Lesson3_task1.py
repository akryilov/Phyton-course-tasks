# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_f(x, y):  # Function 'divide' definition
    if y == 0:
        res = 'Dividing by zero!'
        return res
    else:
        res = x / y
        return res


x = [int(i) for i in input('Enter 2 numbers using space: ').split()]
i = 0
a = x[i]
b = x[i + 1]
result = my_f(a, b)
print(result)