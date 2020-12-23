# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func_1(a, n):
    variable = 1
    for i in range(abs(n)):
        variable *= a
    if n >= 0:
        return variable
    else:
        return 1 / variable


def my_func_2(a, n):
    return a ** n

num_One = float(input("Введите действительное положительное число: "))
num_Two = int(input("Введите целое отрицательное число: "))
print(my_func_1(num_One, num_Two))
print(my_func_2(num_One, num_Two))
