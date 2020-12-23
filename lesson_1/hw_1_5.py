'''
№5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''
print("ЗАДАНИЯ №5:\n")

companyRevenue = int(input("Укажите выручку фирмы: "))
companyCosts = int(input("Укажите издержки компании: "))

if companyRevenue > companyCosts :
    companyProfit = companyRevenue - companyCosts
    companyProfitability = companyProfit / companyRevenue
    print(f"Поздравляю, компания отработала с прибылью {companyProfit}. "
          f"Рентабельность выручки составляет {companyProfitability}%")
    employeers = int(input("Для расчета прибыли на одного сотрудника уражите количество работников: "))
    employeersRevenue = companyRevenue / employeers
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет: {employeersRevenue}")
elif companyRevenue == companyCosts :
    print("Вы ничего не заработали, но и ничего не потеряли")
else:
    companyLost = companyCosts - companyRevenue
    print(f"Вы потеряли: {companyLost}, работайте лучше")

