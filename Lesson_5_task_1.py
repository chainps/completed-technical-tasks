number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
elif number > 0:
    if number % 2 == 0:
        print("положительное четное число")
    else:
        print("положительное нечетное число")
else:
    if number % 2 == 0:
        print("отрицательное четное число")
    else:
        print("отрицательное нечетное число")

if number % 2 != 0:
    print("число не является четным")