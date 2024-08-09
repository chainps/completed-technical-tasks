def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def create_factorial_list(n):
    factorial_n = factorial(n)
    return [factorial(i) for i in range(factorial_n, 0, -1)]

n = int(input("Число: "))
factorial_n = factorial(n)
factorial_list = create_factorial_list(n)

print(f"Факториал [{n}]: {factorial_n}")
print(f"Список факториалов [{factorial_n}]: {factorial_list}")