# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

LST_LEN = 10

num_lst = [random.randint(-100, 100) for _ in range(LST_LEN)]
max_min = min_ = 0

for i in range(LST_LEN):
    if num_lst[i] < num_lst[max_min]:
        max_min = i


for i in range(LST_LEN):
    if (num_lst[i] < 0) and num_lst[i] > num_lst[max_min]:
        max_min = i


print(f'Максимальный минимальный элемент в массиве\n{num_lst}\n'
      f'имеет значение {num_lst[max_min]} и позицию {max_min+1}')