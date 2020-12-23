# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

firstList, secondList = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55], []
print(firstList)
# первый вариант решения
for i in range(len(firstList)):
    if firstList[i]>firstList[i-1] and i!=0:
        secondList.append(firstList[i])

print(secondList)

# второй вариант решения. Всю голову сломал и интернет перерыл. Вот теперь я точно все знаю про генераторы списков)
generatList = [el for item, el in enumerate(firstList) if item != 0 and el > firstList[item-1]]
print(generatList)