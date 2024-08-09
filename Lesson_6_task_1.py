N = int(input("Введите количество чисел: "))

count_zeros = 0
for _ in range(N):
    number = int(input("Введите число: "))
    if number == 0:
        count_zeros += 1

print(count_zeros)