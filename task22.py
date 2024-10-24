#todo:  Задан файл dump.txt.
# Необходимо для заданного файла подсчитать статистику
# количества гласных букв в тексте.


#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................


f = open('dump.txt', 'r', encoding='utf-8')
text = f.read()
letter_a = text.count('а')
letter_e = text.count('е')
letter_io = text.count('ё')
letter_i = text.count('и')
letter_o = text.count('о')
letter_y = text.count('у')
letter_i = text.count('ы')
letter_ye = text.count('э')
letter_u = text.count('ю')
letter_ya = text.count('я')

print(f'''Количество букв a - {letter_a}
Количество букв е - {letter_e}
Количество букв ё - {letter_io}
Количество букв и - {letter_i}
Количество букв о - {letter_o}
Количество букв у - {letter_y}
Количество букв ы - {letter_i}
Количество букв э - {letter_ye}
Количество букв ю - {letter_u}
Количество букв я - {letter_ya}
''')