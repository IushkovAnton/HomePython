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

f = open('index.html', 'w+', encoding='utf-8')
f.write(template)

with open('index.html', 'r') as file:
    data = file.read().replace('\n', '')


# Индекс Знака вопроса
def template_index():
        return data.find('?')

print(template_index())


# print(template_index())
# i = 0
# def value_i():
#         match i:
#                 case 0:
#                         return 'title'
#                 case 1:
#                         return 'charset'
#                 case 2:
#                         return 'alert'
#                 case 3:
#                         return 'p'
#
#
# print(value_i())
#
# for i in range(len(template)):
#         # if '?' in template[template_index():(template_index() + 10)]:
#         #         template = template.replace('?', page[value_i()], 1)
#                 f = open('index.html', 'w', encoding='utf-8')
#                 f.write(template)

#
#
