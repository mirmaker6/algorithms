# 7. По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника,составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

# Захотелось сделать через теорему косинусов
a = float(input('Введите длину первого отрезка  '))
b = float(input('Введите длину второго отрезка  '))
c = float(input('Введите длину третьего отрезка  '))

if (a != 0) and (b != 0) and (c != 0):  # Ловля ошибки деления на ноль
    cos = (b**2+c**2-a**2)/(2*b*c)
    if -1 < cos < 1:
        print('Треугольник возможен')
        if a == b == c:
            print('Треугольник равносторонний')
        elif (a == b) or (b == c) or (a == c):
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
    else:
        print('Треугольник невозможен')
else:
    print('Треугольник невозможен')
