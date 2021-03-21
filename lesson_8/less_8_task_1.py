# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

string = 'sova'
sum_string = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        print(string[i:j])
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_string.add(hash_str)

print(f'в строке {string} {len(sum_string) - 1} подстрок')
