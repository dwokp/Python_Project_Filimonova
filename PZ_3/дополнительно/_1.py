num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
total = num1 * num2
if total < 0:
    res = total * 8
    print(res)
else:
    res2 = total * 1.5
    print(res2)