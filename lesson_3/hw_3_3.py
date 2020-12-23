# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def funSum(a, b, c):
    numbers = list(sorted([int(a), int(b), int(c)], reverse=True))
    return numbers[0] + numbers[1]


args = input("Введите три числа через пробел: ").split()
varSum = funSum(args[0], args[1], args[2])
print(f"Сумма двух наибольших чисел: {varSum}")
