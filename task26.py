# #todo Задача 1. Чтение матрицы, load_matrix(filename)
# # Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)
#
matrix = '''11 12 13 14 15 16
21 22 23 24 25 26
31 32 33 34 35 36
'''
#
#
# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.
#
# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
    with open(filename, encoding='utf-8') as file:
        contents = file.readlines()
        if len(contents[0]) == len(contents[1]) == len(contents[2]):
            me_text = "".join(contents)
            return me_text
        else:
            return False

print(load_matrix('file_matrix.txt'))
