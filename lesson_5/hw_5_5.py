"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
def input_data():
    try:
        with open('hw_5_5_file', 'w', encoding='utf-8') as f_obj:
            line = input('Введите цифры через пробел \n')
            f_obj.writelines(line)
    except IOError:
        print('Ошибка в файле')

def read_and_sum_in_file():
    list = []
    try:
        with open('hw_5_5_file', 'r', encoding='utf-8') as f_obj:
            for el in f_obj.read().split():
                list.append(int(el))
            return sum(list)
    except ValueError as err:
        return err

input_data()
print(read_and_sum_in_file())