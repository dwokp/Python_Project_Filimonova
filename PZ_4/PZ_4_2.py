#ВАРИАНТ 25
# Дано целое число N(>0). Если оно является степенью числа 3, то вывести  TRUE, если не является - вывести FALSE
# запрашиваем число n
n = input("Введите целое число N: ")
while type(n) != int:
    try:
        n = int(n)
    # ошибка
    except ValueError:
        print("Неправильно ввели!")
        n =  input("Введите целое число N: ")
# проверка н
while n % 3 == 0:
    n //= 3
#условие для true/ false
if n == 1:
    print("TRUE")
else:
    print("FALSE")
