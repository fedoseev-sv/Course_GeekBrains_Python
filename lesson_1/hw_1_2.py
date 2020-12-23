'''
№2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
print("ЗАДАНИЯ №2:\n")

seconds = int(input("Введите колическо секунд: "))


variable_hour = seconds // 3600
variable_minutes = (seconds - variable_hour * 3600) // 60
variable_seconds = (seconds - variable_hour * 3600) % 60

print("Указанное время: %02d:%02d:%02d" % (variable_hour, variable_minutes, variable_seconds))