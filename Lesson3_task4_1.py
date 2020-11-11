# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).

# solving thru ** #

def my_func(x, y):
    res = x ** y
    return res

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
        result = my_func(a, b)
        print(float(result))


