# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

import random

SIZE_N = 5
SIZE_M = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]
# если нужен ручной ввод:
# matrix = [[int(input('введите число матрицы')) for _ in range(SIZE_M)] #for _ in range(SIZE_N)]

print(*matrix, sep='\n')

for i in matrix:
    sum_ = 0
    for j in i:
        sum_ += j
    i.append(sum_)

print('\n', *matrix, sep='\n')
