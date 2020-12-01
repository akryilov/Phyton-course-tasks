# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

sum_1 = 0  # Set the sum value

with open("Lesson5_task5.txt", "w+") as my_file:  # calculation the sum of elements:
    text_line = [int(i) for i in input('Enter numbers using space: ').split()]  # Entering the numbers in list and splitting them
    for i in text_line:
        my_file.write(str(i) + ' ')  # writing numbers in file with spaces
    my_file.seek(0)  # set to zero bite in file
    print(my_file.readlines())
    my_file.seek(0)
    for line in my_file:
        sum_1 = sum(int(el) for el in line.split())  # calculate the sum
print(f'Sum is: {sum_1}')
