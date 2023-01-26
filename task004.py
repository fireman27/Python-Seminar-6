"""Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) 
своих N друзей. Создайте список friends и добавьте в него N словарей 
с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.
# Ввод:
>> 3 # Количество друзей
>> Иван
>> 12
>> Иннокентий
>> 20
>> Леша
>> 10
# Вывод:
>> 14
>> Иннокентий"""

friends = []
kol = int(input("Введите количество друзей: "))
for _ in range(kol):
    name = input("Введите имя друга: ")
    age = int(input("Введите его возраст: "))
    friends.append({'name':name, 'age':age})
# print(friends)
summa = 0
max_name = friends[0]['name']
for i in friends:
    summa += i['age']
    if len(i['name']) > len(max_name):
        max_name = i['name']
print(f'Средний возраст друзей: ', summa // kol)
print('Самое длинное имя - ', max_name)
