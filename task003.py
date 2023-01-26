"""Старший и младший. Пользователь вводит число N. Затем он вводит личные данные 
(имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей 
с ключами name и age. Найдите самого младшего из друзей и выведите его имя."""

friends = []
kol = int(input("Введите количество друзей: "))
for _ in range(kol):
    name = input("Введите имя друга: ")
    age = int(input("Введите его возраст: "))
    friends.append({'name':name, 'age':age})
# print(friends)
min_age = friends[0]['age']
for new_friends in friends:
    if new_friends['age'] < min_age:
        min_age = new_friends['age']
for new_friends in friends:
    if new_friends['age'] == min_age:
        print(new_friends['name'])
        break

