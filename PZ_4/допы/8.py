# даны два целых числа A и B ( A<B). найти сумму всех целых чисел от A до B включительно (использовать оператор цикла)
a = input("Введите целое число А: ")
b = input("Введите целое число B: ")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите целое чило А: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите целое число B: ")
sum = 0
while a <= b:
    sum = sum + a
    a += 1
print("Сумма чисел:", sum)