# ВАРИАНТ 25
# Найти сумму чисел ряда 1,2,3,4... от числа n до числа m. Суммирование оформить функцией с параметрами.
# Значения n и m  программа должна запрашивать.
def summa(n, m):
    s = 0
    while n <= m:
        s += n
        n += 1
    return s

n = input("Введите n: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите n: ")

m = input("Введите m: ")
while type(m) != int:
    try:
        m = int(m)
    except ValueError:
        print("Неправильно ввели!")
        m = input("Введите m: ")

if n <= m:
    print("Сумма чисел:", summa(n, m))
else:
    print("Ошибка! n должно быть меньше или равно m")