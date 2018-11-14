# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во
# второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# Python 3.6.6
# OS - 64bit

import random
from count_size import count_size


LST_LEN = 10
num_lst = [random.randint(0, 11) for _ in range(LST_LEN)]
even_num = []
for i in range(LST_LEN):
    if num_lst[i] % 2 == 0:
        even_num.append(i + 1)
print(f'Базовый массив\n{num_lst}')
print(f'Массив идексов четных чисел\n{even_num}')

sum_ = 0
var_lst = (LST_LEN, num_lst, even_num, i)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 792 байт памяти
# Два списка, две переменные типа инт
