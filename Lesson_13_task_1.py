import random

def create_matrix(size):
    """Создание матрицы заданного размера с случайными значениями."""
    return [[random.randint(-100, 100) for _ in range(size)] for _ in range(size)]

def sum_matrices(mat1, mat2):
    """Сложение двух матриц одинакового размера."""
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# Генерация двух матриц размером 10x10
matrix1 = create_matrix(10)
matrix2 = create_matrix(10)

# Сложение матриц
matrix3 = sum_matrices(matrix1, matrix2)

# Вывод матриц
print("Матрица 1:")
for row in matrix1:
    print(row)

print("\nМатрица 2:")
for row in matrix2:
    print(row)

print("\nСумма матриц:")
for row in matrix3:
    print(row)