# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
# 1_2_4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile


def ser_sum(n):
    sum_ = 0
    for i in range(n):
        sum_ += (-1) ** i / 2 ** i
    return sum_

# "task_1.ser_sum(3)"
# 1000 loops, best of 3: 1.16 usec per loop
# "task_1.ser_sum(30)"
# 1000 loops, best of 3: 13 usec per loop
# "task_1.ser_sum(300)"
# 1000 loops, best of 3: 220 usec per loop
# "task_1.ser_sum(3000)"
# 1000 loops, best of 3: 4.58 msec per loop

# Алгоритм имеет линейную сложность
# Сложность ~ O(1.6*N)

# cProfile.run('ser_sum(30000)')1    0.916    0.916    0.916    0.916 task_1.py:10(ser_sum)
# cProfile.run('ser_sum(300000)') 1  116.356  116.356  116.356  116.356 task_1.py:10(ser_sum)


def ser_sum_var(n):
    item = 1
    summ = 0
    for _ in range(n):
        summ += item
        item /= -2
    return summ

# "task_1.ser_sum_var(3)"
# 1000 loops, best of 3: 0.437 usec per loop
# "task_1.ser_sum_var(30)"
# 1000 loops, best of 3: 1.82 usec per loop
#  "task_1.ser_sum_var(300)"
# 1000 loops, best of 3: 14.8 usec per loop
# "task_1.ser_sum_var(3000)"
# 1000 loops, best of 3: 164 usec per loop
#
# Сложность ~ O(0.05*N)

# cProfile.run('ser_sum_var(30000)')1    0.002    0.002    0.002    0.002 task_1.py:29(ser_sum_var)
# cProfile.run('ser_sum_var(300000)') 1    0.017    0.017    0.017    0.017 task_1.py:29(ser_sum_var)
# cProfile.run('ser_sum_var(3000000)')1    0.177    0.177    0.177    0.177 task_1.py:29(ser_sum_var)


def ser_sum_const(n):
    summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return summa_2

# "task_1.ser_sum_const(3)"
# 1000 loops, best of 3: 0.256 usec per loop
# "task_1.ser_sum_const(30)"
# 1000 loops, best of 3: 0.253 usec per loop
# "task_1.ser_sum_const(300)"
# 1000 loops, best of 3: 0.255 usec per loop
# "task_1.ser_sum_const(3000)"
# 1000 loops, best of 3: 0.276 usec per loop
#
# Константная сложность

# cProfile.run('ser_sum_const()') не имеет смысла ввиду константной сложности

# Алгоритм с перемнной оказался быстрее моего
