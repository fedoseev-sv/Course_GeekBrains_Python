'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def delNum(arg1, arg2):
    try:
        variable = arg1 / arg2
    except ZeroDivisionError:
        variable = "Ошибка! Деление на 0 недопустимо"
    return variable


numberOne, numberTwo = int(input("Ввдите первое число: ")), int(input("Ввдите второе число: "))
print(f"Результат деления двух чисел: {delNum(numberOne, numberTwo)}")
