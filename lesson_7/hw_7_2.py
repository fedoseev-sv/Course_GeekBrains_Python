"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

class Clothes():
    fabric_all = 0

    def __init__(self):
        self.name = ""
        self.var_V = 0
        self.var_H = 0

    @property
    def get_name(self):
        return self.name


class Coat(Clothes):
    def __init__(self, V, H):
        super().__init__()
        self.name = "Пальто"
        self.var_V = V
        self.var_H = H

    def fabric_consumption(self):
        temp = self.var_V / 6.5 + 0.5
        Clothes.fabric_all += temp
        return temp


class Suit(Clothes):
    def __init__(self, V, H):
        super().__init__()
        self.name = "Костюм"
        self.var_V = V
        self.var_H = H

    def fabric_consumption(self):
        temp = 2 * self.var_H + 0.3
        Clothes.fabric_all += temp
        return temp


object_1 = Coat(0.3, 2)
object_2 = Suit(0.8, 1.8)
print(f"Расход ткани на {object_1.get_name} составило {object_1.fabric_consumption():.2f} \n"
      f"Расход ткани на {object_2.get_name} составило {object_2.fabric_consumption():.2f} \n"
      f"Общий расход ткани составил {Clothes.fabric_all:.2f}")