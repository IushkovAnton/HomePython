# #todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!



num = input().split()
num = list(num)
book = []

for i in range(len(num)):
    if num[i] == ',' or num[i] == '!':
        letter = num[i]
    else:
        letter = chr(ord('`')+int(num[i]))
    book.append(letter)
me_text = "".join(book)
print(me_text)