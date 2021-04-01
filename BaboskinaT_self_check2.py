"""
Бабошкина Татьяна Владимировна
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
s = 'Бабошкина Татьяна Владимировна'
i = 2

""" +++ ВЛОЖЕННЫЕ СПИСКИ +++ """

""" Задание №1
Создайте пустой список 'fio'
---------------начало блока редактирования----------------"""

fio = []

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == []))

""" Задание №2
Используя цикл for добавьте в 'fio' список букв вашей фамилии, список букв вашего имени и список букв вашего отчества
---------------начало блока редактирования----------------"""

a = s.split(' ')
for letter in a:
    fio.append(list(letter))

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(fio == [['Б', 'а', 'б', 'о', 'ш', 'к', 'и', 'н', 'а'], ['Т', 'а', 'т', 'ь', 'я', 'н', 'а'], ['В', 'л', 'а', 'д', 'и', 'м', 'и', 'р', 'о', 'в', 'н', 'а']]))

""" Задание №3
Используя цикл while переверните каждый элемент в 'fio' задом наперёд
---------------начало блока редактирования----------------"""

b = 0
while b < len(fio):
    fio[b] = list(reversed(fio[b]))
    b += 1

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(fio == [['а', 'н', 'и', 'к', 'ш', 'о', 'б', 'а', 'Б'], ['а', 'н', 'я', 'ь', 'т', 'а', 'Т'], ['а', 'н', 'в', 'о', 'р', 'и', 'м', 'и', 'д', 'а', 'л', 'В']]))

""" Задание №4
Получите из переменной fio 3-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][-3]

"""------------ конец блока редактирования----------------"""
print('№4 ' + str(char == 'т'))

""" Задание №5
Получите из переменной fio 3-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][-3]

"""------------ конец блока редактирования----------------"""
print('№5 ' + str(char == 'т'))

""" Задание №6
Создайте список fio_len и запишите в него длины вашей фамилии, имени и отчества, получив их из fio
---------------начало блока редактирования----------------"""

fio_len = [len(fio[0]), len(fio[1]), len(fio[2])]

"""------------ конец блока редактирования----------------"""
print('№6 ' + str(fio_len == [9, 7, 12]))

""" Задание №7
Используя стандартную функцию min получите длину самого короткого слова из ваших ФИО
---------------начало блока редактирования----------------"""

min_len = min(len(fio[0]), len(fio[1]), len(fio[2]))

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(min_len == 7))

""" Задание №8
Используя цикл в цикле получите строку, в которой будет:
последняя буква вашей фамилии, затем имени, затем отчества,
затем предпоследния буква вашей фамилии, имени, отчества,
затем предпредпоследния буква вашей фамилии, имени, отчества,
и так до того момента, пока не закончатся символы в самом коротком слове из вашей ФИО
---------------начало блока редактирования----------------"""

i = 0
chars = str()

while i < min_len:
    for l in range(len(fio)):
        chars += fio[l][i]
    i += 1

"""------------ конец блока редактирования----------------"""
print('№8 ' + str(chars == 'аааннниявкьоштроаибТм'))


""" +++ СЛОВАРИ +++ """

""" Задание №9
Создайте словарь с ключами 'фамилия' 'имя' 'отчество' и соответствующими значениями ФИО задом наперёд
---------------начало блока редактирования----------------"""

reversed_fio_dict = {
    'фамилия': fio[0],
    'имя': fio[1],
    'отчество': fio[2],
}


"""------------ конец блока редактирования----------------"""
print('№9 ' + str(reversed_fio_dict == {'фамилия': ['а', 'н', 'и', 'к', 'ш', 'о', 'б', 'а', 'Б'], 'имя': ['а', 'н', 'я', 'ь', 'т', 'а', 'Т'], 'отчество': ['а', 'н', 'в', 'о', 'р', 'и', 'м', 'и', 'д', 'а', 'л', 'В']}))

""" Задание №10
Получите список ключей словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_keys = list(reversed_fio_dict.keys())

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(reversed_fio_dict_keys == ['фамилия', 'имя', 'отчество']))

""" Задание №11
Получите список значений словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_values = list(reversed_fio_dict.values())

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(reversed_fio_dict_values == [['а', 'н', 'и', 'к', 'ш', 'о', 'б', 'а', 'Б'], ['а', 'н', 'я', 'ь', 'т', 'а', 'Т'], ['а', 'н', 'в', 'о', 'р', 'и', 'м', 'и', 'д', 'а', 'л', 'В']]))

""" Задание №12
Получите список картежей, содержащий пары ключ и значение словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_items = list(reversed_fio_dict.items())

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(reversed_fio_dict_items == [('фамилия', ['а', 'н', 'и', 'к', 'ш', 'о', 'б', 'а', 'Б']), ('имя', ['а', 'н', 'я', 'ь', 'т', 'а', 'Т']), ('отчество', ['а', 'н', 'в', 'о', 'р', 'и', 'м', 'и', 'д', 'а', 'л', 'В'])]))

""" Задание №13
Получите значение словаря reversed_fio_dict по ключу фамилия
---------------начало блока редактирования----------------"""

res = reversed_fio_dict['фамилия']

"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['а', 'н', 'и', 'к', 'ш', 'о', 'б', 'а', 'Б']))

""" Задание №14
Создайте пустой словарь chars
---------------начало блока редактирования----------------"""

chars = {}

"""------------ конец блока редактирования----------------"""
print('№14 ' + str(chars == {}))

""" Задание №15
Преобразуйте строку с вашей ФИО так, чтобы в ней были только маленькие буквы и отсутствовали пробелы
---------------начало блока редактирования----------------"""

s = s.lower().replace(' ', '')

"""------------ конец блока редактирования----------------"""
print('№15 ' + str(s == 'бабошкинататьянавладимировна'))

""" Задание №16
Пройдите в цикле по всем буквам своих ФИО 's' и сосчитайте количество повторений каждой буквы.
Получите список 'res' из пар (кортежей):
( <буква вашей ФИО>, <количество её появления в вашей ФИО> )
---------------начало блока редактирования----------------"""

res = {}

for i in s:
    res[i] = s.count(i)
res = list(res.items())


"""------------ конец блока редактирования----------------"""
print('№16 ' + str(res == [('б', 2), ('а', 6), ('о', 2), ('ш', 1), ('к', 1), ('и', 3), ('н', 3), ('т', 2), ('ь', 1), ('я', 1), ('в', 2), ('л', 1), ('д', 1), ('м', 1), ('р', 1)]))


""" +++ ФУНКЦИИ +++ """

""" Задание №17
Напишите функцию tat_anaCharToIndex которая:
- получает на вход букву русского алфавита,
- возвращает её номер в алфавите (от 1 до 33).
Например вызов tat_anaCharToIndex('А') должен возвращать 1
---------------начало блока редактирования----------------"""

char_new = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def tat_anaCharToIndex(let):
    letter = let.lower()
    return char_new.find(letter) + 1

"""------------ конец блока редактирования----------------"""
print('№17 ' + str(tat_anaCharToIndex("Э") == 31))

""" Задание №18
При помощи функции tat_anaCharToIndex измените fio так, чтобы вместо букв, в нём были их номера в алфавите
---------------начало блока редактирования----------------"""

for i in range(len(fio)):
    k = 0
    s = []
    while k < len(fio[i]):
        s.append(tat_anaCharToIndex(fio[i][k]))
        k += 1
    fio[i] = s

"""------------ конец блока редактирования----------------"""
print('№18 ' + str(fio == [[1, 15, 10, 12, 26, 16, 2, 1, 2], [1, 15, 33, 30, 20, 1, 20], [1, 15, 3, 16, 18, 10, 14, 10, 5, 1, 13, 3]]))


""" +++ КОНЕЦ =) +++ """
