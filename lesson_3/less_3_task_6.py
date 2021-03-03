# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_num = array[0]
ind_max_num = 0
min_num = array[0]
ind_min_num = 0
sum_ = 0

for i in array:
    if i > max_num:
        max_num = i
        ind_max_num = array.index(i) # можно сделать было в цикле и enumerate и использовать его номер для ind_max_num
    elif i < min_num:
        min_num = i
        ind_min_num = array.index(i) # можно сделать было в цикле и enumerate и использовать его номер для ind_min_num

if ind_min_num > ind_max_num:
    first_ind, second_ind = ind_max_num, ind_min_num
else:
    first_ind, second_ind = ind_min_num, ind_max_num

print(f'Минимальное число: {min_num}, Максимальное число: {max_num}')

for i in range(first_ind + 1, second_ind):
    sum_ += array[i]
print(f'Сумма чисел между max и min: {sum_}')
