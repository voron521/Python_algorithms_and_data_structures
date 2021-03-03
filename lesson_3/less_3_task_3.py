# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_num = array[0]
ind_max_num = 0
min_num = array[0]
ind_min_num = 0

for i in array:
    if i > max_num:
        max_num = i
        ind_max_num = array.index(i)
    elif i < min_num:
        min_num = i
        ind_min_num = array.index(i)

print(f'Массив до выполнения задачи:\n{array}')

array[ind_max_num], array[ind_min_num] = array[ind_min_num], array[ind_max_num]

print(f'Массив после выполнения задачи:\n{array}')
