# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.
#
# Задача.
# Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print(len(alphabet))
list_letter = []

def shifr():
    j = 0
    while j != 6: # где 6 это сколько в тексте строк+1
        with open('message.txt', encoding='utf-8') as file:
            contents = file.readlines()
            str1 = contents[j]
            for i in range(len(str1)):
                str1 = str1.lower()
                if str1[i] in alphabet:
                    letter = alphabet[alphabet.find(str1[i])-(j+1)]
                else:
                    letter = str1[i]
                list_letter.append(letter)
            contents[j] = list_letter
            j +=1
    me_text = "".join(list_letter)
    return me_text

print(shifr())

