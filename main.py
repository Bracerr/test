import re

# s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
# result = re.match('DC ', s) #В начале строки
# print(result)

# result = re.search('DC', s) По всей строке первое вхождение
# print(result[0])

# result = re.findall('AC', s) Создает список со всеми схождениями
# print(result)

# result = re.split('/', s) Создает список и разбивает по символу
# print(result)

# result = re.sub('A', 'D', s) Заменяет A на D
# print(result)

# result = re.fullmatch('A', s) Сравнивает строчки
# print(result)

s = '87+648642   ---- gjkagkg22255 HFNKThhfhff'
# result = re.search(r'g.k', s) пропуск элементов
# print(result)

# result = re.search(r'\d', s) цифры

# result = re.search(r'\D', s) всё кроме цифр

# result = re.search(r'\s', s) \t \n e.t.c

# result = re.search(r'\S', s) любой не пробельный

# result = re.search(r'\b87', s) начало слова

# result = re.search(r'\d*', s) ноль или более вхождений

# result = re.search(r'[gABCD]', s) ищет совпадение с таким шаблоном

# result = re.search(r'[^gABCD]', s) ищет несовпадение с таким шаблоном

# result = re.search(r'\d{3}', s) колл- во повторений

# result = re.search(r'\w+', s) начало слова

# result = re.search(r'\d{3,}', s) колл- во повторений не менее 3
print(result)
