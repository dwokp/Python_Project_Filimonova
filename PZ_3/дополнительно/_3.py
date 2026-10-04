num = int(input("Введите двухзначное число: "))
num1 = num // 10
num2 = num % 10
result = num1 + num2
if result % 2 == 0:
    print(num + 2)
else:
    print(num - 2)