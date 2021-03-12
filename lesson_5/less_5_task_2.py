# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from collections import defaultdict

numb_1 = deque(input('Введите 16-ти ричное число a: '))
numb_2 = deque(input('Введите 16-ти ричное число b: '))

simbol_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

simbol_dict_reverse = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',
                       12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def summ_number(num_1, num_2):
    a = num_1.copy()
    b = num_2.copy()
    a.reverse()
    b.reverse()
    sum_rezult = deque()
    inter_res = 0  # 0 или 1 перенос единицы на следущее сложение
    if len(b) > len(a):
        a, b = b, a

    while a:
        sum_1 = simbol_dict[a.popleft()]
        try:
            sum_2 = simbol_dict[b.popleft()]
        except:
            sum_2 = 0
        sum_ = sum_1 + sum_2 + inter_res

        if sum_ > 15:
            sum_ -= 16
            inter_res = 1
        else:
            inter_res = 0
        sum_rezult.appendleft(simbol_dict_reverse[sum_])

    if inter_res != 0:
        sum_rezult.appendleft(inter_res)

    return sum_rezult


def multip(num_1, num_2):
    a = num_1.copy()
    b = num_2.copy()
    a.reverse()
    b.reverse()
    if len(b) > len(a):
        a, b = b, a

    com_rezult = deque()
    inter_res = 0  # 0 или 1 перенос единицы на следущее сложение

    while b:

        compos_1 = simbol_dict[b.popleft()]
        for i in a:
            compos_2 = simbol_dict[i]
            compos = compos_1 * compos_2 + inter_res
            if compos > 15:
                inter_res = compos // 16
                compos = compos % 16
            else:
                inter_res = 0
            com_rezult.appendleft(simbol_dict_reverse[compos])

        if inter_res != 0:
            if inter_res <= 9:
                com_rezult.appendleft(f'{inter_res}')
            else:
                com_rezult.appendleft(simbol_dict_reverse[inter_res])

            inter_res = 0
        com_rezult.appendleft('*')

    summ_ = defaultdict(list)

    j = 0

    com_rezult.reverse()

    for i in com_rezult:
        if i == '*':
            j += 1
        else:
            summ_[j].append(i)

    for i in summ_:
        summ_[i].reverse()
        summ_[i].extend(['0'] * i)

    term_1 = deque('0')
    term_2 = deque()

    for i in summ_:
        term_2.extend(summ_[i])
        term_1 = (summ_number(term_1, term_2))
        term_2.clear()

    return term_1


print('a + b = ', *summ_number(numb_1, numb_2))
print('a * b = ', *multip(numb_1, numb_2))
