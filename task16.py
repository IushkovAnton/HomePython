# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
dlin = len(users)

sort = int(input('''Введите тип сортировки:
1. По возрасту
2. По первой букве
3. По группе
=>'''))
match sort:
    case 1:
        age = int(input('Введите возраст: '))
        for i in range(dlin):
            slovar = users[i]
            if slovar['age'] > age:
                print(users[i])
            else:
                print('Слишком большой возраст')
    case 2:
        letter_login = input('Введите первую букву логина: ').upper()
        for i in range(dlin):
            slovar = users[i]
            if slovar['login'][0] == letter_login:
                print(users[i])
    case 3:
        group = input('Введите наименование группы: ')
        for i in range(dlin):
            slovar = users[i]
            if slovar['group'] == group:
                print(users[i])
    case _:
        print('Введите цифру от 1 до 3: ')













# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16
#
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"




