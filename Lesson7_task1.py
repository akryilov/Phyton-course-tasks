# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
#
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5
# 8 3
# 8 3
# 7 1
#
# Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.index = 0
        self.print_res = ''
        for self.el in self.matrix:
            if self.index <= len(self.matrix):
                self.print_res += f'{self.el}\n'
                self.index += 1
        return self.print_res

    def __add__(self, other):
        self.result = self.matrix
        for i in range(len(self.matrix)):  # cycle matrix lines
            for j in range(len(self.matrix[0])):  # cycle matrix rows
                if len(self.matrix) == len(other.matrix):  # checking for matrices dimensions:
                    self.result[i][j] = self.matrix[i][j] + other.matrix[i][j]  # if true -> sum
                else:
                    return f'check dimensions of matrices!'  # if false: print error
        return Matrix(self.result)


matrix_1 = Matrix([[31, 23], [37, 43], [51, 86], [20, 10]])
print(matrix_1)

matrix_2 = Matrix([[31, 23], [37, 43], [51, 86]])
print(matrix_2)

matrix_3 = Matrix([[31, 23], [37, 43], [51, 86]])
print(matrix_3)

print(matrix_1 + matrix_2)
print(matrix_2 + matrix_3)
