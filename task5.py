#todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))

print(f"""Сумма: {num1 + num2}
Разность: {num1 - num2}
Частное: {num1 / num2}
Произведение: {num1 * num2}
Целочисленное деление: {num1 // num2}
Деление с остатком: {num1 % num2}
Возведение в степень: {num1 ** num2}""")