# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

new_list = []  # Create new (clear) list
i = 0
print('Enter the value (tap "end list" for the end): ')
while True:
    list1 = input(f'Element #{i}:')
    if list1 == 'end list':
        break
    i += 1
    new_list.append(list1)
print(f'Entered list: {new_list}')
a = 0

#
if i % 2 == 0:
    while a <= i - 1:
        tmp = new_list[a]
        new_list[a] = new_list[a + 1]
        new_list[a + 1] = tmp
        a += 2
else:
    while a <= i - 2:
        tmp = new_list[a]
        # print(tmp)
        new_list[a] = new_list[a + 1]
        new_list[a + 1] = tmp
        a += 2
print(f'New list is: {new_list}')
