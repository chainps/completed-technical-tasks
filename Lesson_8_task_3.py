# Вводим данных
m = int(input("Введите максимальную грузоподъемность лодки: "))
n = int(input("Введите количество рыбаков: "))
fishers = []
for i in range(n):
    fishers.append(int(input(f"Введите вес рыбака {i + 1}: ")))

# Сортируем список рыбаков по весу
fishers.sort()

# Указатели на самого легкого и самого тяжелого рыбаков
left, right = 0, n - 1

# Считаем лодки
boats = 0

while left <= right:
    if fishers[left] + fishers[right] <= m:
        left += 1
    right -= 1
    boats += 1

# Вывод количества лодок
print("Требуемое(минимальное) количество лодок:", boats)