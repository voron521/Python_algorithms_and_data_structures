# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import timeit
import cProfile


# Для начала создадим объекты классов матриц чтобы оценивать не время создания матриц а время выполнения действий над матрицами(их объектами)


import random

SIZE_N = 5
SIZE_M = 4
MIN_ITEM = 0
MAX_ITEM = 100


class Matrix:

    def __init__(self, MIN_ITEM, MAX_ITEM, SIZE_N, SIZE_M):
        self.MIN_ITEM = MIN_ITEM
        self.MAX_ITEM = MAX_ITEM
        self.SIZE_N = SIZE_N
        self.SIZE_M = SIZE_M
        self.rezult_matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_M)] for _ in range(SIZE_N)]

    def __str__(self):
        return f"{self.rezult_matrix}"


matrix_1 = Matrix(MIN_ITEM, MAX_ITEM, SIZE_N, SIZE_M)
matrix_2 = Matrix(MIN_ITEM, MAX_ITEM, SIZE_N=50, SIZE_M=40)
matrix_3 = Matrix(MIN_ITEM, MAX_ITEM, SIZE_N=100, SIZE_M=80)
matrix_4 = Matrix(MIN_ITEM, MAX_ITEM, SIZE_N=200, SIZE_M=160)
matrix_5 = Matrix(MIN_ITEM, MAX_ITEM, SIZE_N=400, SIZE_M=320)
matrix_6 = Matrix(MIN_ITEM, MAX_ITEM, SIZE_N=800, SIZE_M=640)



# Вариант №1, который был сдан мной как дз

def version_1(matrix):
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

    return(f'максимальный элемент среди минимальных элементов столбцов: {min_2}')


print(timeit.timeit('version_1(matrix_1.rezult_matrix)', number=1000, globals=globals())) # 0.005647700000000144
print(timeit.timeit('version_1(matrix_2.rezult_matrix)', number=1000, globals=globals())) # 0.20349879999999998
print(timeit.timeit('version_1(matrix_3.rezult_matrix)', number=1000, globals=globals())) # 0.7294563999999999
print(timeit.timeit('version_1(matrix_4.rezult_matrix)', number=1000, globals=globals())) # 2.8563077999999997
print(timeit.timeit('version_1(matrix_5.rezult_matrix)', number=1000, globals=globals())) # 12.860992000000001
print(timeit.timeit('version_1(matrix_6.rezult_matrix)', number=1000, globals=globals())) # 58.028456600000005


cProfile.run('version_1(matrix_6.rezult_matrix)')

#     645 function calls in 0.057 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.057    0.057 <string>:1(<module>)
#     1    0.057    0.057    0.057    0.057 less_4_task_1.py:39(version_1)
#     1    0.000    0.000    0.057    0.057 {built-in method builtins.exec}
#   641    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Вариант №2, Ухудшим ситуацию, добавив второй массив и функцию append


def version_2(matrix):
    matrix_2 = [[] for _ in range(len(matrix[0]))]

    min_max = 0

    for i in range(0, len(matrix[0])):

        for j in range(0, len(matrix)):
            matrix_2[i].append(matrix[j][i])

    for i in matrix_2:
        if min(i) > min_max:
            min_max = min(i)

    return (min_max)

print(timeit.timeit('version_2(matrix_1.rezult_matrix)', number=1000, globals=globals())) # 0.016568499999999986
print(timeit.timeit('version_2(matrix_2.rezult_matrix)', number=1000, globals=globals())) # 0.4244191999999999
print(timeit.timeit('version_2(matrix_3.rezult_matrix)', number=1000, globals=globals())) # 1.5338538
print(timeit.timeit('version_2(matrix_4.rezult_matrix)', number=1000, globals=globals())) # 6.5810183
print(timeit.timeit('version_2(matrix_5.rezult_matrix)', number=1000, globals=globals())) # 28.6200215
print(timeit.timeit('version_2(matrix_6.rezult_matrix)', number=1000, globals=globals())) # 116.583259


cProfile.run('version_2(matrix_6.rezult_matrix)')

#      513287 function calls in 0.235 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.001    0.001    0.235    0.235 <string>:1(<module>)
#     1    0.153    0.153    0.234    0.234 less_4_task_1.py:85(version_2)
#     1    0.000    0.000    0.000    0.000 less_4_task_1.py:87(<listcomp>)
#     1    0.000    0.000    0.235    0.235 {built-in method builtins.exec}
#   642    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   640    0.011    0.000    0.011    0.000 {built-in method builtins.min}
# 512000    0.070    0.000    0.070    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант №3, Используем библиотеку numpy

import numpy as np


def version_3(matrix):
    min_max = 0

    matrix = np.rot90(matrix)
    for i in matrix:
        if min(i) > min_max:
            min_max = min(i)

    return (min_max)

print(timeit.timeit('version_3(matrix_1.rezult_matrix)', number=1000, globals=globals())) # 0.057119699999999884
print(timeit.timeit('version_3(matrix_2.rezult_matrix)', number=1000, globals=globals())) # 0.5882501
print(timeit.timeit('version_3(matrix_3.rezult_matrix)', number=1000, globals=globals())) # 1.9952434999999995
print(timeit.timeit('version_3(matrix_4.rezult_matrix)', number=1000, globals=globals())) # 7.8221102
print(timeit.timeit('version_3(matrix_5.rezult_matrix)', number=1000, globals=globals())) # 31.1333939
print(timeit.timeit('version_3(matrix_6.rezult_matrix)', number=1000, globals=globals())) # 114.84975379999999


cProfile.run('version_3(matrix_6.rezult_matrix)')

#          672 function calls (670 primitive calls) in 0.114 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(flip)
#     1    0.000    0.000    0.066    0.066 <__array_function__ internals>:2(rot90)
#     1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(transpose)
#     1    0.000    0.000    0.114    0.114 <string>:1(<module>)
#     1    0.000    0.000    0.066    0.066 _asarray.py:110(asanyarray)
#     1    0.000    0.000    0.000    0.000 fromnumeric.py:52(_wrapfunc)
#     1    0.000    0.000    0.000    0.000 fromnumeric.py:598(_transpose_dispatcher)
#     1    0.000    0.000    0.000    0.000 fromnumeric.py:602(transpose)
#     1    0.000    0.000    0.000    0.000 function_base.py:146(_flip_dispatcher)
#     1    0.000    0.000    0.000    0.000 function_base.py:150(flip)
#     1    0.000    0.000    0.000    0.000 function_base.py:55(_rot90_dispatcher)
#     1    0.000    0.000    0.066    0.066 function_base.py:59(rot90)
#     2    0.000    0.000    0.000    0.000 index_tricks.py:748(__getitem__)
#     1    0.001    0.001    0.113    0.113 less_4_task_1.py:131(version_3)
#     1    0.000    0.000    0.000    0.000 numeric.py:1341(normalize_axis_tuple)
#     1    0.000    0.000    0.000    0.000 numeric.py:1391(<listcomp>)
#     1    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#     1    0.000    0.000    0.114    0.114 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
#     3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   640    0.046    0.000    0.046    0.000 {built-in method builtins.min}
#     1    0.000    0.000    0.000    0.000 {built-in method numpy.arange}
#     1    0.066    0.066    0.066    0.066 {built-in method numpy.array}
#   3/1    0.000    0.000    0.066    0.066 {built-in method numpy.core._multiarray_umath.implement_array_function}
#     1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.normalize_axis_index}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'transpose' of 'numpy.ndarray' objects}





# Итоговый вывод:

# Проверка проводилась для матриц:
# 5х4
# 50х40
# 100х80
# 200х160
# 400х320
# 800х640

# Самый быстрый вариант решения №1 т.к не создаются лишние массивы, нет лишних функций,
# таких как append и не используються библиотеки(по крайнеме мере в данном случае Numpy не дает скорости)