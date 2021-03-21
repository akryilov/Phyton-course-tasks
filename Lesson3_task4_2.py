# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# solving thru cycle #

def inv(x, y):
    i = 0
    r = 1
    while i <= abs(y)-1:
        r = r * (1 / x)
        i += 1
    return r


print(f'Enter the positive value a=: ')
a = int(input())
if a < 0:
    print('a < 0!')
else:
    print(f'Enter the negative value b=:')
    b = int(input())
    if b > 0:
        print('b > 0!')
    else:
        result = inv(a, b)
        print(float(result))
