X = int(input("Минимальная сумма инвестиций: "))
A = int(input("Сумма, которую может инвестировать Майкл: "))
B = int(input("Сумма, которую может инвестировать Иван: "))

if A >= X and B >= X:
    result = 2
elif A >= X:
    result = "Mike"
elif B >= X:
    result = "Ivan"
elif A + B >= X:
    result = 1
else:
    result = 0

print(result)