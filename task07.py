#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = int(input('Введите координаты точки A: '))
B = int(input('Введите координаты точки B: '))
C = int(input('Введите координаты точки C: '))

AC = abs(A-C)
BC = abs(B-C)
sum_AC_BC = AC + BC

print(f"AC = {AC}\nBC = {BC}\nAC + BC = {sum_AC_BC}")