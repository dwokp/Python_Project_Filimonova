num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = num1 + num2
if result % 5 == 0:
    print(result + 1)
else:
    print(result - 2)