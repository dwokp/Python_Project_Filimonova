try:
    N = int(input("Введите количество секунд: "))
    full_hour = N // 3600
    print(f"Полных часов прошло: {full_hour} ")
except ValueError:
    print("Ошибка, нужно ввести целое число")
