# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min_num = array[0]
min_num_ind = 0

for i in array:
    if i < min_num:
        min_num = i
        min_num_ind = array.index(i)

for i, el in enumerate(array):
    if i != min_num_ind:
        min_num_2 = el
        break

for i, el in enumerate(array):
    if el <= min_num_2 and min_num_ind != i:
        min_num_2 = el

print(f'два минимальных числа: {min_num}, {min_num_2}')
