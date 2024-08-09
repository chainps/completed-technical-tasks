# Ввод первого списка чисел
first_list = set()
N1 = int(input("Введите количество чисел в первом списке: "))
print("Введите числа первого списка:")
for _ in range(N1):
    number = int(input())
    first_list.add(number)

# Ввод второго списка чисел
second_list = set()
N2 = int(input("Введите количество чисел во втором списке: "))
print("Введите числа второго списка:")
for _ in range(N2):
    number = int(input())
    second_list.add(number)

# Находим пересечение общих чисел в двух списках
common_numbers = first_list & second_list

# Вывод количества чисел, содержащихся одновременно в обоих списках
print("Количество чисел, содержащихся одновременно в обоих списках:", len(common_numbers))