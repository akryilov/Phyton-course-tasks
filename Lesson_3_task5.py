# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

def my_func(x):
    global sum_1
    for k in [x]:  # Sum each element in the list of words
        if 'q' in x:  # 'q' criteria checking
            y = x[0:(x.index('q'))]
            for n, elem in enumerate(y):
                y[n] = int(elem)  # convert data into int type
                sum_1 += y[n]  # sum all elements before 'q'
            print(sum_1)
            return 0
        else:  # if 'q' is not in the list:
            y = x
            for j, elem in enumerate(y):
                y[j] = int(elem)
                sum_1 += y[j]
            print(sum_1)


sum_1 = 0
i = 0
while True:  # Cycle for continuous entering the words
    x = [i for i in input('Enter numbers using space (q - exit): ').split()]  # enter the words
    if my_func(x) == 0:
        break
