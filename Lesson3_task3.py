# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def user(xx, yy, zz):
    list_1 = [xx, yy, zz]
    a = sorted(list_1)
    res = a[1] + a[2]
    return res


x_1 = [int(i) for i in input('Enter 3 numbers using space: ').split()]
x = x_1[0]
y = x_1[1]
z = x_1[2]
result = user(x, y, z)
print(f'Result is: {result}')
