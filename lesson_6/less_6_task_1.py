# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


# Windows 10 - x64
# Python 3.9.0


# За основу беру 7-ую задачу урока №3: В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import sys
import random
from collections import deque


def show(obj):
    get_size = sys.getsizeof(obj)
    print(f'{type(obj)=}, {get_size=}, {obj=}')
    obj_memory.append(get_size)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)

    return sum(obj_memory)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# Вариант задачи №1


def version_1(array):
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

    return min_num, min_num_2, locals()


print(f'список переменных программы версии №1: {version_1(array)[-1]}\n')

dict_variable_version_1 = version_1(array)[-1]

obj_memory = []
total_memory = 0

for val in dict_variable_version_1.values():
    total_memory += (show(val))
    obj_memory = []

print(f'\nВ общем на переменные программы версии №1 затрачено {total_memory} байт\n')


# список переменных программы версии №1: {'array': [12, 47, 58, 3, 52, 53, 6, 69, 82, 21], 'min_num': 3, 'min_num_ind': 3, 'i': 9, 'el': 21, 'min_num_2': 6}
#
# type(obj)=<class 'list'>, get_size=184, obj=[12, 47, 58, 3, 52, 53, 6, 69, 82, 21]
# type(obj)=<class 'int'>, get_size=28, obj=12
# type(obj)=<class 'int'>, get_size=28, obj=47
# type(obj)=<class 'int'>, get_size=28, obj=58
# type(obj)=<class 'int'>, get_size=28, obj=3
# type(obj)=<class 'int'>, get_size=28, obj=52
# type(obj)=<class 'int'>, get_size=28, obj=53
# type(obj)=<class 'int'>, get_size=28, obj=6
# type(obj)=<class 'int'>, get_size=28, obj=69
# type(obj)=<class 'int'>, get_size=28, obj=82
# type(obj)=<class 'int'>, get_size=28, obj=21
# type(obj)=<class 'int'>, get_size=28, obj=3
# type(obj)=<class 'int'>, get_size=28, obj=3
# type(obj)=<class 'int'>, get_size=28, obj=9
# type(obj)=<class 'int'>, get_size=28, obj=21
# type(obj)=<class 'int'>, get_size=28, obj=6
#
# В общем на переменные программы версии №1 затрачено 604 байт


# Вариант Задачи №2 поменяем тип лист на кортеж и добавим очередь

def version_2(array):
    min_num = array[0]
    min_nums = deque(maxlen=2)

    for i, el in enumerate(array):
        if el < min_num:
            min_nums.append(el)
            min_num_ind = i
    if min_num_ind == 0:
        try:
            min_num = array[1]
        except:
            return 'массив состоит из одного элемента, создайте массив из 3 или более элементов'

    for i, el in enumerate(array):
        if i != min_num_ind and el <= min_num:
            min_num = el
    min_nums.append(min_num)

    return min_nums, locals()


print(*version_2(tuple(array)))

print(f'список переменных программы версии №2: {version_2(array)[-1]}\n')

dict_variable_version_2 = version_2(array)[-1]

obj_memory = []
total_memory = 0

for val in dict_variable_version_2.values():
    total_memory += (show(val))
    obj_memory = []

print(f'\nВ общем на переменные программы версии №2 затрачено {total_memory} байт\n')

# список переменных программы версии №2: {'array': [93, 4, 97, 10, 68, 12, 15, 93, 97, 88], 'min_num': 4, 'min_num_ind': 1, 'i': 9, 'el': 88, 'min_num_2': 10}
#
# type(obj)=<class 'list'>, get_size=184, obj=[93, 4, 97, 10, 68, 12, 15, 93, 97, 88]
# type(obj)=<class 'int'>, get_size=28, obj=93
# type(obj)=<class 'int'>, get_size=28, obj=4
# type(obj)=<class 'int'>, get_size=28, obj=97
# type(obj)=<class 'int'>, get_size=28, obj=10
# type(obj)=<class 'int'>, get_size=28, obj=68
# type(obj)=<class 'int'>, get_size=28, obj=12
# type(obj)=<class 'int'>, get_size=28, obj=15
# type(obj)=<class 'int'>, get_size=28, obj=93
# type(obj)=<class 'int'>, get_size=28, obj=97
# type(obj)=<class 'int'>, get_size=28, obj=88
# type(obj)=<class 'int'>, get_size=28, obj=4
# type(obj)=<class 'collections.deque'>, get_size=624, obj=deque([88, 4], maxlen=2)
# type(obj)=<class 'int'>, get_size=28, obj=88
# type(obj)=<class 'int'>, get_size=28, obj=4
# type(obj)=<class 'int'>, get_size=28, obj=9
# type(obj)=<class 'int'>, get_size=28, obj=88
# type(obj)=<class 'int'>, get_size=28, obj=9
#
# В общем на переменные программы версии №2 затрачено 1256 байт


# Вариант Задачи №3 решим при помощи sort()

def version_3(array):
    array.sort()

    return array[0:1], locals()


print(*version_3(array))

print(f'список переменных программы версии №3: {version_3(array)[-1]}\n')

dict_variable_version_3 = version_3(array)[-1]

obj_memory = []
total_memory = 0

for val in dict_variable_version_3.values():
    total_memory += (show(val))
    obj_memory = []

print(f'\nВ общем на переменные программы версии №3 затрачено {total_memory} байт')

# список переменных программы версии №3: {'array': [8, 13, 24, 40, 47, 54, 67, 68, 80, 93]}
#
# type(obj)=<class 'list'>, get_size=184, obj=[8, 13, 24, 40, 47, 54, 67, 68, 80, 93]
# type(obj)=<class 'int'>, get_size=28, obj=8
# type(obj)=<class 'int'>, get_size=28, obj=13
# type(obj)=<class 'int'>, get_size=28, obj=24
# type(obj)=<class 'int'>, get_size=28, obj=40
# type(obj)=<class 'int'>, get_size=28, obj=47
# type(obj)=<class 'int'>, get_size=28, obj=54
# type(obj)=<class 'int'>, get_size=28, obj=67
# type(obj)=<class 'int'>, get_size=28, obj=68
# type(obj)=<class 'int'>, get_size=28, obj=80
# type(obj)=<class 'int'>, get_size=28, obj=93
#
# В общем на переменные программы версии №3 затрачено 464 байт




#Вывод: в точки зрения памяти решение №3 оптимально т.к используется минимальное количество переменных,
#если нужно было изначальный список оставить неизменым, сортировку можно было применить к его копии.
#Также коллекции используют значительно больше памяти чем список