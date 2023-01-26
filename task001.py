"""Создайте список из случайных чисел. Найдите количество различных элементов в нем"""
import random
a = [random.randint(1,10) for _ in range(10)]
print(a)
new = set(a)
print(len(new))