# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
# 1_3_5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import cProfile


def arr_max_min_1(lst_len):

    num_lst = [random.randint(-1000, -800) for _ in range(lst_len)]
    max_min = 0

    for i in range(lst_len):
        if num_lst[i] < num_lst[max_min]:
            max_min = i

    for i in range(lst_len):
        if (num_lst[i] < 0) and num_lst[i] > num_lst[max_min]:
            max_min = i

    return num_lst[max_min]


# "task_1_2.arr_max_min_1(10)"
# 1000 loops, best of 3: 11.2 usec per loop
# "task_1_2.arr_max_min_1(100)"
# 1000 loops, best of 3: 102 usec per loop
# "task_1_2.arr_max_min_1(1000)"
# 1000 loops, best of 3: 1.11 msec per loop
# "task_1_2.arr_max_min_1(10000)"
# 1000 loops, best of 3: 10.6 msec per loop

# cProfile.run('arr_max_min_1(10000)')    10000    0.007    0.000    0.014    0.000 random.py:173(randrange)
#                                         10000    0.003    0.000    0.017    0.000 random.py:217(randint)
#                                         10000    0.005    0.000    0.007    0.000 random.py:223(_randbelow)
#                                         1        0.001    0.001    0.021    0.021 task_1_2.py:10(arr_max_min_1)
#                                         1        0.002    0.002    0.019    0.019 task_1_2.py:12(<listcomp>)

# cProfile.run('arr_max_min_1(1000000)')  1000000    0.540    0.000    1.171    0.000 random.py:173(randrange)
#                                         1000000    0.265    0.000    1.436    0.000 random.py:217(randint)
#                                         1000000    0.446    0.000    0.631    0.000 random.py:223(_randbelow)
#                                         1          0.137    0.137    1.782    1.782 task_1_2.py:10(arr_max_min_1)
#                                         1          0.210    0.210    1.646    1.646 task_1_2.py:12(<listcomp>)

def arr_max_min_2(lst_len):
    array = [random.randint(-1000, -800) for _ in range(lst_len)]
    SIZE = len(array)
    i = 0
    index = -1

    while i < SIZE:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        return array[index]


# "task_1_2.arr_max_min_2(10)"
# 1000 loops, best of 3: 11 usec per loop
# "task_1_2.arr_max_min_2(100)"
# 1000 loops, best of 3: 104 usec per loop
# "task_1_2.arr_max_min_2(1000)"
# 1000 loops, best of 3: 1.04 msec per loop
# "task_1_2.arr_max_min_2(10000)"
# 1000 loops, best of 3: 10.6 msec per loop

# cProfile.run('arr_max_min_2(1000000)')  1000000    0.539    0.000    1.155    0.000 random.py:173(randrange)
#                                         1000000    0.262    0.000    1.417    0.000 random.py:217(randint)
#                                         1000000    0.432    0.000    0.616    0.000 random.py:223(_randbelow)
#                                         1          0.137    0.137    1.752    1.752 task_1_2.py:47(arr_max_min_2)
#                                         1          0.198    0.198    1.615    1.615 task_1_2.py:48(<listcomp>)

def arr_max_min_3(lst_len):
    array = [random.randint(-1000, -800) for _ in range(lst_len)]
    num = float('-inf')
    index = -1

    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    if index != -1:
        return num

# "task_1_2.arr_max_min_3(10)"
# 1000 loops, best of 3: 10.4 usec per loop
# "task_1_2.arr_max_min_3(100)"
# 1000 loops, best of 3: 96.1 usec per loop
# "task_1_2.arr_max_min_3(1000)"
# 1000 loops, best of 3: 1.02 msec per loop
# "task_1_2.arr_max_min_3(10000)"
# 1000 loops, best of 3: 9.99 msec per loop

# Все бесполезно, так как основное время выполнения занимает генерация списка с рандомом
# Вывод, который я сделал для себя, что рандом очень медленный и его надо было вынести из функций и мерить без него
# Но отрицательный результат - тоже результат.
