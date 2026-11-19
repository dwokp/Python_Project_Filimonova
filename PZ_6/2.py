#ВАРИАНТ 25
# Даны два списка A и B одинакового размера N. Сформировать новый список C того же размера, каждый элемент
# которого равен максимальному из элементов списков A и B.

import random
n = int(input("Введите размер списка: "))
a = []
b = []

for i in range(n):
    num = random.randint(1, 100)
    a.append(num)
for i in range(n):
    nu = random.randint(1, 100)
    b.append(nu)

c = []
for i in range(n):
    if a[i] > b[i]:
        c.append(a[i])
    else:
        c.append(b[i])

print(f"Список А: {a}, Список B: {b}, Список C: {c}")