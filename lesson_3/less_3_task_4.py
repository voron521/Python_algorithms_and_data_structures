# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_count = 0
max_ind = 0

for i in array:
    count = 0
    for j in array:
        if i == j:
            count += 1
    if max_count < count:
        max_count = count
        max_ind = array.index(i)

print(f'чаще всего встречается число: {array[max_ind]}')
