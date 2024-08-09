X = int(input("Введите натуральное число: "))

count_divisors = 0
divisors = []

for i in range(1, X + 1):
    if X % i == 0:
        count_divisors += 1
        divisors += [i]  # Добавляем делитель в список

# Формируем строку с делителями
divisors_str = ", ".join(map(str, divisors))

print(f"Количество натуральных делителей числа {X} равно: {count_divisors}\nНатуральные делители числа {X}: {divisors_str}")