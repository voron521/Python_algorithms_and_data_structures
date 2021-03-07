# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import timeit
import cProfile


def with_resheto(n):
    start = 3
    stop = n * 4
    count = 1
    rezult = [i for i in range(start, stop) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:
        for i in range(len(rezult)):
            if rezult[i] != 0:
                count += 1
                if count == n:
                    return rezult[i]
                j = i + rezult[i]
                while j < len(rezult):
                    rezult[j] = 0
                    j += rezult[i]

        prime.extend([i for i in rezult if i != 0])
        start, stop = stop, stop + 2 * n
        rezult = [i for i in range(start, stop) if i % 2 != 0]

        for i in range(len(rezult)):
            for num in prime:
                if rezult[i] % num == 0:
                    rezult[i] = 0
                    break

print(with_resheto(5))


print(timeit.timeit('with_resheto(5)', number=1000, globals=globals())) # 0.005030899999999998
print(timeit.timeit('with_resheto(10)', number=1000, globals=globals())) # 0.009702500000000003
print(timeit.timeit('with_resheto(20)', number=1000, globals=globals())) # 0.018044400000000002
print(timeit.timeit('with_resheto(40)', number=1000, globals=globals())) # 0.1108258
print(timeit.timeit('with_resheto(80)', number=1000, globals=globals())) # 0.2856384
print(timeit.timeit('with_resheto(160)', number=1000, globals=globals())) # 0.7840748000000002
print(timeit.timeit('with_resheto(320)', number=1000, globals=globals())) # 4.9027692


cProfile.run('with_resheto(320)')

#      1262 function calls in 0.005 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#     1    0.005    0.005    0.005    0.005 less_4_task_2.py:15(with_resheto)
#     1    0.000    0.000    0.000    0.000 less_4_task_2.py:19(<listcomp>)
#     2    0.000    0.000    0.000    0.000 less_4_task_2.py:36(<listcomp>)
#     2    0.000    0.000    0.000    0.000 less_4_task_2.py:38(<listcomp>)
#     1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#  1251    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


def without_eratosthenes(n):

    numb_list = [2]
    number = 3
    while len(numb_list) < n:
        triger = True
        for i in numb_list:
            if number % i == 0:
                triger = False
                break
        if triger:
            numb_list.append(number)
        number += 1
    return numb_list[-1]


print (without_eratosthenes(5))

print(timeit.timeit('without_eratosthenes(5)', number=1000, globals=globals())) # 0.004569900000000002
print(timeit.timeit('without_eratosthenes(10)', number=1000, globals=globals())) # 0.010803799999999988
print(timeit.timeit('without_eratosthenes(20)', number=1000, globals=globals())) # 0.03507400000000002
print(timeit.timeit('without_eratosthenes(40)', number=1000, globals=globals())) # 0.1031366
print(timeit.timeit('without_eratosthenes(80)', number=1000, globals=globals())) # 0.41804869999999994
print(timeit.timeit('without_eratosthenes(160)', number=1000, globals=globals())) # 1.2885442
print(timeit.timeit('without_eratosthenes(320)', number=1000, globals=globals())) # 4.6320005


cProfile.run('without_eratosthenes(320)')

#      2451 function calls in 0.006 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#     1    0.005    0.005    0.006    0.006 less_4_task_2.py:63(without_eratosthenes)
#     1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#  2128    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   319    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Вывод: Скорость выполнения почти одинакова