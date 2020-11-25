# 3. Реализовать программу работы с органическими клетками состоящими из ячеек.

# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).

# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
# и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.

# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:  # Create class cell
    def __init__(self, num):  # initialization
        self.num = int(num)  # num attr initialization

    def __add__(self, other):  # creating add method
        return Cell(self.num + other.num)

    def __sub__(self, other):  # creating sub method
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            return f'Cell can not be < 0!'  # checking if cell < 0

    def __mul__(self, other):  # crating multiplication method
        return Cell(self.num * other.num)

    def __truediv__(self, other):  # creating truediv method
        return Cell(round(self.num // other.num))

    def __str__(self):  # crating multiplication method for returning 'self.num' as a result
        return f'{self.num}'

    def make_order(self, under_cell_num):  # creating make_order method
        self.under_cell_num = under_cell_num
        self.star_quantity = self.num
        self.index = under_cell_num
        self.print_res = ''
        for el in range(self.star_quantity):  # cycle 'for' for checking star_quantity and separation by lines
            while (self.star_quantity - self.under_cell_num) > 0:
                self.star_quantity -= self.under_cell_num
                self.print_res += f'{self.under_cell_num * "*"}\n'
                self.index += 1
            if (self.star_quantity - self.under_cell_num) == 0:
                self.print_res += f'{self.under_cell_num * "*"}\n'
                return self.print_res
            if (self.star_quantity - self.under_cell_num) < 0:
                self.print_res += f'{abs(self.star_quantity) * "*"}\n'
                return self.print_res


cell_1 = Cell(1)
cell_2 = Cell(3)
cell_3 = cell_1 + cell_2
print(type(cell_3))
print('sum of cell_1 and cell_2: {}'.format(cell_3))
print('cell separation below:\n{}' .format(cell_3.make_order(5)))

cell_4 = cell_2/cell_1
print('result of dividing: {}' .format(cell_4))

cell_5 = cell_1 - cell_2
print('result of substraction: {}' .format(cell_5))

cell_5_1 = cell_2 - cell_1
print('result of substraction: {}' .format(cell_5_1))

cell_6 = cell_2 * cell_1
print(cell_6)

cell_7 = cell_2 * cell_1
print(cell_7)

print(cell_6.make_order(2))