# #todo: Требуется создать csv-файл «algoritm.csv» со
# следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# 1 % "C4.5"
# 2 % "k - means"
# и т.д.


import csv
csv_file = 'algoritm.csv'
algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
              "EM", "PageRank", "AdaBoost", "kNN",
              "Наивный байесовский классификатор", "CART"]

with open(csv_file, 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'text'])
    for i in range(0, len(algoritm)):
        x = algoritm[i]
        y = i + 1
        writer.writerow([f'{y} % {x}'])
