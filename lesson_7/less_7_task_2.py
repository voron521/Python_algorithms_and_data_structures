# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint

array = [randint(0, 49) for _ in range(10)]


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    first = merge_sort(arr[:len(arr) // 2])
    second = merge_sort(arr[len(arr) // 2:])

    ind_first = 0
    ind_second = 0
    prom_rezult = []
    while ind_first < len(first) and ind_second < len(second):

        if first[ind_first] <= second[ind_second]:
            prom_rezult.append(first[ind_first])
            ind_first += 1

        else:
            prom_rezult.append(second[ind_second])
            ind_second += 1

    prom_rezult.extend(first[ind_first:])
    prom_rezult.extend(second[ind_second:])

    return (prom_rezult)


print(f'Исходные массив:\n{array}\nОтсортированный массив:\n{merge_sort(array)}')
