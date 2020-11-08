# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# Enter the list of string values and split them
str_list = [str(i) for i in input('Enter the str values using space: ').split()]
for ind, el in enumerate(str_list[:10]):  # Cycle for printing each element from list
    print(f'#{ind}: {el[:10]}')  # Print each element up to 10 symbols
