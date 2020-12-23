"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

infoList = []
with open("hw_5_2_testlist.txt", "r") as f_obj:
    for line in f_obj.readlines():
        infoList.append(len(line.split()))

for item, el in enumerate(infoList):
    print(f"Строка №{item+1} содержит слов: {el}")