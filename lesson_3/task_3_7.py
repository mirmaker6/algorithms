# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

num = [[int(input(f'Введите {i + 1} элемент {j + 1} строки ')) for i in range(4)] for j in range(4)]
sum_ = 0

for i in range(4):
    for j in range(4):
        sum_ += num[i][j]
    num[i].append(sum_)
    sum_ = 0

for i in range(4):
    for j in range(5):
        print(num[i][j], end='\t')
    print()
