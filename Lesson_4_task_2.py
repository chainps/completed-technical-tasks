number = float(input('5-значное число: '))

number_str = str(int(number))
d1 = float(number_str[0])
d2 = float(number_str[1])
d3 = float(number_str[2])
d4 = float(number_str[3])
d5 = float(number_str[4])

e0 = d4 ** d5
e1 = e0 * d3
e2 = d1 - d2

if e2 == 0:
    print("Ошибка: деление на ноль")
else:
    e3 = e1 / e2
    print(f'Результат: {e3}')