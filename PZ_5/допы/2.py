# рассчитать и вывести периметр и площадь прямоугольника. расчеты оформить в функции
def perimetr(x, y):
    return x*2 + y*2

def ploshad(x, y):
    return x * y

x = int(input("Введите число: "))
y = int(input("Введите число: "))
print("Периметр: ", perimetr(x, y), "Площадь: ", ploshad(x, y) )

