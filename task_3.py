# 3. По введенным пользователем координатам двух точек вывести уравнение прямой,
# проходящей через эти точки.

x1 = float(input('Введите координату X первой точки '))
y1 = float(input('Введите координату Y первой точки '))
x2 = float(input('Введите координату X второй точки '))
y2 = float(input('Введите координату Y второй точки '))

k = (y2 - y1) / (x2 - x1)
b = (y1 - k * x1)

if b == 0:
    print(f'Уравнение прямой y = {k:.2f}x')
elif b > 0:
    print(f'Уравнение прямой y = {k:.2f}x + {b:.2f}')
else:
    print(f'Уравнение прямой y = {k:.2f}x - {abs(b):.2f}')


