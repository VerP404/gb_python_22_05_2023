word = input()
word = word.upper()

points_eng = {
    1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2:['D', 'G'],
    3:['B', 'C', 'M', 'P'],
    4:['F', 'H', 'V', 'W', 'Y'],
    5:['K'],
    8:['J', 'X'],
    10:['Q', 'Z'],
}
points_rus = {
    1:['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
    2:['Д', 'К', 'Л', 'М', 'П', 'У'],
    3:['Б', 'Г', 'Ё', 'Ь', 'Я'],
    4:['Й', 'Ы'],
    5:['Ж', 'З', 'Х', 'Ц', 'Ч'],
    8:['Ш', 'Э', 'Ю'],
    10:['Ф', 'Щ', 'Ъ'],
}

point = 0
for letter in word:
    if letter in set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
        points = points_rus
    else:
        points = points_eng
    
for key, values in points.items():
    for letter in word:
        if letter in values:
            point = point + key
print(point)