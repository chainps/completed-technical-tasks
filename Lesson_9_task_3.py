# Ввод последовательности чисел
numbers = input("Введите последовательно числа через пробел: ").split()

# Создание множества для хранения уникальных чисел
seen_numbers = set()

# Выполнение проверки каждого числа в последовательностии
for number in numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)