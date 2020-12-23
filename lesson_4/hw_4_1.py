# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

def calculatedSalary(hourWork, hourSalary, bonus):
    return (hourWork * hourSalary) + bonus

file_path, paramsOne, paramsTwo, paramsThree = argv
print("Заработная плата работника составляет:", calculatedSalary(int(argv[1]), int(argv[2]), int(argv[3])))
