'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения
параметров a и b и выводить одно натуральное число — номер дня.
'''
print("ЗАДАНИЯ №6:\n")

startDistans = int(input("Введите дистанцию спорцмена в первый день тренировок: "))
finishDistans = int(input("Введите целевую дистанцию тренировок: "))

startDay = 1
while finishDistans > startDistans:
    startDistans = startDistans + startDistans * 0.1
    print("{}-й день = {:.2f} км".format(startDay, startDistans))

    startDay += 1

startDistansInt = int(startDistans // 1)
print(f"\nНа {startDay}-й день спорцмен пробежит не менее {startDistansInt} км")