# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.
#
text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.\n"


alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_letter = []
h = 0

while h < 26:

    for i in range(len(text)):
        if text[i] in alphabet:
            letter = alphabet[alphabet.find(text[i])-h]
            list_letter.append(letter)
        else:
            list_letter.append(text[i])
    h +=1

me_text = "".join(list_letter)
print(me_text)