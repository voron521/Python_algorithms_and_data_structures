# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_N = 5
SIZE_M = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]

print(*matrix, sep='\n')

triger = 0

for i in range(0, len(matrix[0])):
    min_ = matrix[0][i]
    for j in range(0, len(matrix)):
        if matrix[j][i] < min_:
            min_ = matrix[j][i]
    if triger == 0:
        min_2 = min_
        triger = 1
    if min_2 < min_:
        min_2 = min_

print(f'максимальный элемент среди минимальных элементов столбцов: {min_2}')
