# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user(name, surname, year, city, email, phone):
    result = [name, surname, year, city, email, phone]
    my_string = ' '.join(result)  # Join all attributes into one str
    print(f'User summary info: {my_string}')
    return


i = 0
v = ['', '', '', '', '', '']
attr = ['name', 'surname', 'year', 'city', 'email', 'phone']
while i <= len(attr)-1:
    print(f'Enter the {attr[i]} for user #: ')
    v[i] = input()
    # print(v)
    i += 1

user(name=v[0], surname=v[1], year=v[2], city=v[3], email=v[4], phone=v[5])
