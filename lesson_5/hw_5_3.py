"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

f_list = {}

with open("hw_5_3_txt", "r") as f_obj:
    for el in f_obj.readlines():
        family, salary = el.split("|")
        if salary[-1] == "\n":
            salary = salary[0:-1]
        f_list.setdefault(family, salary)


salary_list = []
family_luser_list = []

for key, val in f_list.items():
    salary_list.append(int(val))
    if int(val) < 20000:
        family_luser_list.append(key)

sr_salary = sum(salary_list) / len(salary_list)

print(f"Средняя зарплата: {sr_salary}")
print(f"Меньше 20 000 руб получают: {family_luser_list}")