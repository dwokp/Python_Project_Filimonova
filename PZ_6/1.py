# ВАРИАНТ 25
#Дан целочисленный список размера N. Проверить, чередуются ли в нем четные и нечетные числа. Если чередуются,
# то вывести 0, если нет, то вывести порядковый номер первого элемента, нарушающего закономерность.
import random

n = int(input("Введите размер списка: "))
numbers = []

for i in range(n):
    num = random.randint(1, 100)
    numbers.append(num)
print(numbers)

i = 0
rez = 0

while i < n:
    if numbers[i] % 2 == 0 and numbers[i - 1]:
        rez = i + 1
        break
    i += 1
print(rez)