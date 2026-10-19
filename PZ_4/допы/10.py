# вывести первые N (N>3) чисел Фибоначчи и посчитать количество четных чисел
n = input("Введите N ( N>=3): ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите N ( N>=3): ")

a = 0
b = 1
i = 0
k = 0
while i < n:
    print(a)

    if a % 2 == 0:
        k += 1
    c = a + b
    a = b
    b = c
    i += 1
print("Количество четных чисел:", k)
