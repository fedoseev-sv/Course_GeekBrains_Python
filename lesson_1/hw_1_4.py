'''
№4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
print("ЗАДАНИЯ №4:\n")

variableOne = int(input("Введите целое положительное число: "))
variableTwo = variableOne % 10
variableOne = variableOne // 10
while variableOne > 0:
    if variableOne % 10 > variableTwo:
        variableTwo = variableOne % 10
    variableOne = variableOne // 10

print("Наибольшаа цифра в веденном числе: ", variableTwo)