# Ввод размера массива
N = int(input("Укажите количество элементов(чисел) в массиве: "))

# Заполнение и сохранение массива
numbers = []
print("Укажите числа по одному на строке:")
for _ in range(N):
    number = int(input())
    numbers.append(number)

# Переворачивание массива
reversed_numbers = numbers[::-1]

# Вывод исходного и перевернутого массива
print("Исходный массив чисел:")
print(f"[{', '.join(map(str, numbers))}]")

print("Перевернутый массив чисел:")
print(f"[{', '.join(map(str, reversed_numbers))}]")