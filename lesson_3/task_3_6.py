# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

LST_LEN = 20

num_lst = [random.randint(0, 100) for _ in range(LST_LEN)]
min_ = max_ = sum_ = 0

for i in range(LST_LEN):
    if num_lst[i] <= num_lst[min_]:
        min_ = i
    if num_lst[i] >= num_lst[max_]:
        max_ = i

if min_ > max_:
    min_, max_ = max_, min_

for i in range(min_+1, max_):
    sum_ += num_lst[i]

print(f'Исходный массив\n{num_lst}\n\n'
      f'Сумма элементов между минимальным и максимальным значениями равна {sum_}'
      )
