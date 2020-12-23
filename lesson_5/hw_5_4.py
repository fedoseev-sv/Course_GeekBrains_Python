"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

f_in_obj = open("hw_5_4_in", "r", encoding='utf-8')
f_out_obj = open("hw_5_4_out", "a", encoding='utf-8')
list = []

for el in f_in_obj.readlines():
    if el[-1] == "\n":
        el = el[0:-1]
    list = el.split()
    if list[0] == "One":
        list[0] = "Один"
    elif list[0] == "Two":
        list[0] = "Два"
    elif list[0] == "Three":
        list[0] = "Три"
    elif list[0] == "Four":
        list[0] = "Четыри"
    print(list)
    slist = " ".join(list)
    f_out_obj.writelines(slist)

f_in_obj.close()
f_out_obj.close()
