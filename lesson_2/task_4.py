# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите n '))
s = 0
for i in range(n):
    s += (-1) ** i / 2 ** i
print(s)
