# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита
# они стоят и сколько между ними находится букв.

f = ord('a')-1  # Порядковый номер первой буквы алфавита в Юникоде
a = input('Введите первую букву ')
print(f'Порядковый номер первой буквы = {ord(a)- f}\n')
b = input('Введите вторую букву ')
print(f'Порядковый номер первой буквы = {ord(b)- f}\n')
print(f'Количество букв между ними = {ord(b)-ord(a)-1}')
