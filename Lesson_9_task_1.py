N = int(input("Введите количество чисел(размер списка): "))

# Проверка корректности ввода кол-ва чисел
if N <= 1 or N > 100000:
    print("No-no-no: количество чисел должно быть в диапазоне не меньше 2 и до 100000.")
else:
    input_numbers = input("Введите числа списка: ")

    # Преобразование введенных чисел в список строк
    numbers_list = input_numbers.split()

    # Проверка корректности ввода чисел
    if len(numbers_list) != N:
        print("Количество введенных чисел не соответствует списку.")
    else:
        # Преобразование списка строк
        numbers_set = set()
        for num_str in numbers_list:
            num = int(num_str)
            if abs(num) > 2 * 10**9:
                print(f"Ошибка: число списка {num} превышает допустимый диапазон.")
            else:
                numbers_set.add(num)

        # Вывод количества различных чисел
        print("Количество различных(=уникальных) чисел в списке:", len(numbers_set))