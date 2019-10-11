# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# \Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile

def sieve_of_erat(n):

    ADD = 10
    sieve = [i for i in range(ADD)]
    sieve[1] = 0
    res = []

    while len(res) < n:

        for i in range(2, len(sieve)):

            if sieve[i] != 0:

                j = i + i

                while j < len(sieve):
                    sieve[j] = 0
                    j += i

        res = [i for i in sieve if i != 0]
        add_arr = [i for i in range(ADD, 2*ADD)]
        ADD *= 2
        sieve = sieve + add_arr

    return res[n-1]

# "task_2.sieve_of_erat(100)"
# 100 loops, best of 3: 361 usec per loop
# "task_2.sieve_of_erat(1000)"
# 100 loops, best of 3: 6.65 msec per loop
# "task_2.sieve_of_erat(10000)"
# 100 loops, best of 3: 128 msec per loop
# "task_2.sieve_of_erat(100000)"
# 100 loops, best of 3: 1.23 sec per loop
#
# cProfile.run('sieve_of_erat(10000)')    15    0.008    0.001    0.008    0.001 task_2.py:26(<listcomp>)
#                                         15    0.012    0.001    0.012    0.001 task_2.py:27(<listcomp>)
#                                         1    0.160    0.160    0.224    0.224 task_2.py:7(sieve_of_erat)
#                                         1    0.000    0.000    0.227    0.227 {built-in method builtins.exec}
#                                    865383    0.044    0.000    0.044    0.000 {built-in method builtins.len}
# # Как я понимаю очень много времени занимает создание нового массива и добовление его к существующему


def prime_numb(n):

    prime_array = [2]
    current_number = 2

    while len(prime_array) < n:

        counter = 0

        for i in prime_array:
            if current_number % i == 0:
                counter += 1

        if counter == 0:
            prime_array.append(current_number)

        current_number += 1

    return prime_array[n-1]


# "task_2.prime_numb(100)"
# 100 loops, best of 3: 1.17 msec per loop
# "task_2.prime_numb(1000)"
#  "task_2.prime_numb(6000)"
# 1 loops, best of 3: 8.54 sec per loop
# 100 loops, best of 3: 185 msec per loop
#  "task_2.prime_numb(10000)"
# 1 loops, best of 3: 25.2 sec per loop
# "task_2.prime_numb(100000)"
# Не дождался
#
# cProfile.run('prime_numb(10000)')#   1    0.000    0.000    0.234    0.234 <string>:1(<module>)
#                                     1    0.233    0.233    0.234    0.234 task_2.py:50(prime_numb)
#                                     1    0.000    0.000    0.234    0.234 {built-in method builtins.exec}
#                                  7919    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#                                   999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#                               1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Как я понимаю основная проблема со скоростью во вложенности
# Построил график зависимости, сложность О(3Е-4 n**2)
# Решение с решетом значительно быстрее


def test_prime(func1, func2):

    delta = 0

    for i in range(1, 100):
        delta += abs(func1(i)-func2(i))

    if delta == 0:
        print('TEST OK')
    else:
        print('NOT OK')

# Тестируем правильность функций
# test_prime(sieve_of_erat, prime_numb)   #TEST OK
