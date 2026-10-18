# найти и вывести на экран S=1!+21+3!+4!+...+n!(n>1)
n = int(input("Введите n: "))
i = 1
f = 1
s = 0
while i <= n:
    f = f * i
    s = s + f
    i = i + 1
print("Сумма:", s)