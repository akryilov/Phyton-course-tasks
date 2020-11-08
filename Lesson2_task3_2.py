# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Solving thru dict

# Enter the month number:
month = int(input('Enter the month from 1 to 12: '))
# Dictionary with name of months and months numbers:
seasons = {"Winter": (12, 1, 2), "Spring": (3, 4, 5), "Summer": (6, 7, 8), "Autumn": (9, 10, 11)}

mth_list = list((seasons.keys()))  # Get the list of months
i1 = len(mth_list) - 1  # The lenght of the list of months
a1 = 0
a2 = 0
while a1 <= i1:  # Getting and checking if the month number = the numbers in seasons dictionary
    h = list(seasons.get(mth_list[a1]))  # Get the months numbers for each season
    while a2 <= 2:  # Getting months numbers from dictionary for each a2 value
        n = h[a2]
        a2 += 1
        if month == n:  # Checking if month number = month numbers from dictionary?
            print(f'Season is: {mth_list[a1]}')
            break
    a1 += 1  # Increase the a1 value
    a2 = 0  # Set = a2 = 0
