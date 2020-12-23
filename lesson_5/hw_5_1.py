"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

my_list = []
while True:
    var_insert = input("Введите данные для записи в файл (для окончания записи введите пустую строку): ")
    if var_insert != "":
        my_list.append(var_insert+'\n')
    else:
        with open("worklist.txt", "w") as worklist:
            worklist.writelines(my_list)
            break

with open("worklist.txt", "r") as worklist:
    print("#" * 40 + '\n')
    print("В файл 'worklist.txt' записано: ")
    for el in worklist.readlines():
        print(el[:-1])