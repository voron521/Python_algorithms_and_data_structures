# Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint

size = randint(4, 6)
array = [randint(0, 10) for i in range(2 * size + 1)]

for i, el in enumerate(array):
    count_less = 0
    count_more = 0
    equally = 0
    for j, el_2 in enumerate(array):
        if i != j:
            if el_2 > el:
                count_more += 1
            elif el_2 < el:
                count_less += 1
            else:
                equally += 1

    if count_more == count_less or count_more + equally == count_less or count_less + equally == count_more:
        print(f'массив:{array}\nмедина ={el}')
        break
