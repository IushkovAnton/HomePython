
def shifr(namefile, text):
    j = 0
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    list_letter = []
    with open(namefile, 'w', encoding='utf-8') as f:
        f.write(text)
    with open(namefile, 'r+', encoding='utf-8') as f:
        contents = f.readlines()
    while j != len(contents):
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

