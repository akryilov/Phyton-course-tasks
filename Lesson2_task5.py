# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Enter the list of int values and split them:
str_list = [int(i) for i in input('Enter the int values list (from max to min) using space: ').split()]
# Enter the value for number:
value = int(input('Enter the number for adding: '))
value1 = value
i = 0
a = len(str_list) - 1
while i <= a:  # While for checking input list for adding the value
    try:
        if i == str_list.index(value):  # If the entered value are in the list
            x = str_list.count(value)
            str_list.insert(i + x, value)
            print(f'result: {str_list}')
            break
    except ValueError:  # If the entered value are not in the list then check 0 and the last index of th list
        if str_list[0] > value:  # Adding the entered value to the top of the list
            str_list.insert(len(str_list), value)
            print(f'result: {str_list}')
        else:  # Adding the entered value to the end of the list
            str_list.insert(0, value)
            print(f'result: {str_list}')
        break
    i += 1
