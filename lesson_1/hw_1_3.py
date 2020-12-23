'''
№3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
print("ЗАДАНИЯ №3:\n")

variable_number_n = input("Введите число: ") # Запрос ввода числа. Проверка корректности ввода не осуществляется. Возможно аварийное завершение.
variable_number_nn = variable_number_n*2
variable_number_nnn = variable_number_n*3
variable_number_n_summer = int(variable_number_n) + int(variable_number_nn) + int(variable_number_nnn)

print(f'Вычисленное выражение: {variable_number_n} + {variable_number_nn} + {variable_number_nnn} = {variable_number_n_summer}')