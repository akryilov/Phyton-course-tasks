# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Solving thru list

month = int(input('Enter the number of month from 1 to 12: '))
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

if month > 12 or month < 1:
    print('Incorrect month value')

else:
    if month >= 12 and month <= 2:
        x = seasons[0]
        print(f'Season is: {x}')
    elif month >= 3 and month <= 5:
        x = seasons[1]
        print(f'Season is: {x}')
    elif month >= 6 and month <= 8:
        x = seasons[2]
        print(f'Season is: {x}')
    elif month >= 9 and month <= 11:
        x = seasons[3]
        print(f'Season is: {x}')

