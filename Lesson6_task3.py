# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
#
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income*0.7, 'bonus': income*0.3}  # set dictionary where wage = 70%, bonus = 30%

class Position(Worker):

    def get_full_name(self):
        print(f'Full Name: {self.name + " " + self.surname}')

    def get_total_income(self):
        print(f'Total income: {sum(self._income.values())}')

    def get_bonus(self):
            print(f'Bonus: {self._income.setdefault("bonus")}')


ex_1 = Position('Ivan','Petrov','CEO', 20000)
ex_1.get_full_name()
ex_1.get_bonus()
ex_1.get_total_income()