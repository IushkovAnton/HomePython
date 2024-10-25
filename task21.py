#todo: Задан словарь, его значения необходимо внести по
# соответствующим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""


with open('index.html', encoding='utf-8') as file:
    contents = file.readlines()
    for j in range(1, len(contents)):
        str1 = contents[j]
        if '?' in str1:
            for i in page:
                if i in str1:
                    value = page[i]
                    template = template.replace('?', value, 1)

f = open('index.html', 'w', encoding='utf-8')
f.write(template)

