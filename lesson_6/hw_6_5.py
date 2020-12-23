"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра."""

class Stationery:
    def __init__(self):
        self.title = "Что-то там"

    def draw(self):
        return f"{self.title}. Запуск отрисовки."

class Pen(Stationery):
    def __init__(self):
        self.title = "Карандаш"

    def draw(self):
        return f"{self.title}. Запуск отрисовки."

class Pencil(Stationery):
    def __init__(self):
        self.title = "Ручка"

    def draw(self):
        return f"{self.title}. Запуск отрисовки."

class Handle(Stationery):
    def __init__(self):
        self.title = "Другая ручка"

    def draw(self):
        return f"{self.title}. Запуск отрисовки."


thing_1 = Stationery()
print(thing_1.draw())

thing_2 = Pen()
print(thing_2.draw())

thing_3 = Pencil()
print(thing_3.draw())

thing_4 = Handle()
print(thing_4.draw())