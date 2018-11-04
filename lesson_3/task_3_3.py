# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

LST_LEN = 10

num_lst = [random.randint(0, 100) for _ in range(LST_LEN)]
min_ = max_ = 0

for i in range(LST_LEN):
    if num_lst[i] < num_lst[min_]:
        min_ = i
    if num_lst[i] > num_lst[max_]:
        max_ = i

print(f'Исходный массив\n{num_lst}\n')

num_lst[min_], num_lst[max_] = num_lst[max_], num_lst[min_]

print(f'Измененный массив\n{num_lst}')

