# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial

def fact(num):
    i = 1
    while i <= num:
        res = factorial(i)
        i += 1
        yield res

n = int(input('Enter the n number: '))
quantity = 1
while quantity <= n:
    for el in fact(n):
        print(f'Factorial of {quantity} is: {el}')
        quantity +=1