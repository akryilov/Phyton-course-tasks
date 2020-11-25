# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
#
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

# наследнки пальто и костюм. Реализовать абстрактный класс и проверить работу проперти.

from abc import ABC, abstractmethod


class Clother(ABC):
    def __init__(self, name, par):
        self._name = name
        self._par = par

    @abstractmethod
    def consamp_calc(self):
        pass

    def __add__(self, other):
        return self.consamp_calc() + other.consamp_calc()


class Coat(Clother):

    def consamp_calc(self):
        if self._name == 'Coat':
            self.par1 = (self._par / 6.5) + 0.5
        return self.par1


class Suit(Clother):

    def consamp_calc(self):
        if self._name == 'Suit':
            self.par2 = (self._par * 2) + 0.3
        return self.par2


coat_1 = Coat('Coat', 6.5)
suit_1 = Suit('Suit', 0.35)

print(coat_1.consamp_calc())
print(suit_1.consamp_calc())

print(coat_1 + suit_1)
