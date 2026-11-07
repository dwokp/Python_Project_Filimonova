# даны три целых числа. определить у какого числа больше сумма. вывод результата предусмотреть в основной программе.
# расчет суммы цифр оформить в функции.
def sum_n(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
sum_a = sum_n(a)
sum_b = sum_n(b)
sum_c = sum_n(c)
if sum_a > sum_b and sum_a > sum_c:
    print("наибольшая сумма у числа:", a, "сумма цифр:", sum_a)
elif sum_b > sum_a and sum_b > sum_c:
    print("наибольшая сумма у числа:", b, "сумма цифр:", sum_b)
elif sum_c > sum_a and sum_c > sum_b:
    print("наибольшая сумма у числа:", c, "сумма цифр:", sum_c)