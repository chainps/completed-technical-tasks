A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A > B:
    print("Ошибка: A должно быть меньше или равно B.")
else:
    print(f"Четные числа в диапазоне от {A} до {B}:")
    for number in range(A, B + 1):
        if number % 2 == 0:
            print(number, end=' ')