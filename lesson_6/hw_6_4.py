"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

class Car:
    def __init__(self, speed, name):
        self.speed = int(speed)
        self.color = "black"
        self.name = name
        self.is_police = False

    def go(self):
        if self.is_police:
            return f"Хей {self.name}, тащи свою задницу в свою {self.color} машину. " \
                   f"Вперед комрад со скоростью {self.speed} в час"
        return f"Машина поехала. Ваша скорость {self.speed}"

    def stop(self):
        return f"Стопе!"

    def turn(self, direction):
        if direction == "left":
            return f"Поворачиваем налево"
        elif direction == "right":
            return f"Поворачиваем направо"
        else:
            return f"Едим дальше"

    def show_speed(self):
        return f"Ваша скорость {self.speed}"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Ваша скорость {self.speed}. Снизьте скорость до 60"
        else:
            return f"Ваша скорость {self.speed}. Все хорошо, наслаждайтесь городом!"

class SportCar(Car):
    def __init__(self, speed, name):
        self.speed = int(speed)
        self.color = "yellow"
        self.name = name
        self.is_police = True

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Ваша скорость {self.speed}. Снизьте скорость до 60"
        else:
            return f"Ваша скорость {self.speed}. Все хорошо, наслаждайтесь работой!"

class PoliceCar(Car):
    def __init__(self, speed, name):
        self.speed = int(speed)
        self.color = "black"
        self.name = name
        self.is_police = True


my_car_1 = Car(60, "Алексей")
print("#"*20 + "\n" + "Просто машина" + "\n" + "#"*20)
print(my_car_1.go())
print(my_car_1.turn("left"))
print(my_car_1.turn("right"))
print(my_car_1.turn("go"))
print(my_car_1.stop())
print(my_car_1.show_speed())

my_car_2 = TownCar(60, "Алексей")
print("#"*20 + "\n" + "Просто машина" + "\n" + "#"*20)
print(my_car_2.go())
print(my_car_2.turn("left"))
print(my_car_2.turn("right"))
print(my_car_2.turn("go"))
print(my_car_2.stop())
print(my_car_2.show_speed())

my_car_3 = SportCar(300, "Алексей")
print("#"*20 + "\n" + "Просто машина" + "\n" + "#"*20)
print(my_car_3.go())
print(my_car_3.turn("left"))
print(my_car_3.turn("right"))
print(my_car_3.turn("go"))
print(my_car_3.stop())
print(my_car_3.show_speed())

my_car_4 = WorkCar(60, "Алексей")
print("#"*20 + "\n" + "Просто машина" + "\n" + "#"*20)
print(my_car_4.go())
print(my_car_4.turn("left"))
print(my_car_4.turn("right"))
print(my_car_4.turn("go"))
print(my_car_4.stop())
print(my_car_4.show_speed())

my_car_5 = PoliceCar(60, "Алексей")
print("#"*20 + "\n" + "Просто машина" + "\n" + "#"*20)
print(my_car_5.go())
print(my_car_5.turn("left"))
print(my_car_5.turn("right"))
print(my_car_5.turn("go"))
print(my_car_5.stop())
print(my_car_5.show_speed())