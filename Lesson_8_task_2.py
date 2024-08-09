# Ввод размера массива
N = int(input("Укажите количество элементов(чисел)в массиве:" ))
# Ввод массива чисел
print("Заполните массив: ")
arr = list(map(int, input().split()))

# Изменение массива
result = [0] * N
result[0] = arr[-1]

for i in range(1, N):
    result[i] = arr[i - 1]

# Вывод измененного массива
print(*result)