# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print('Введите две разные строчные английские буквы')
a = input('Первая буква ')
b = input('Вторая буква ')

a_pos = ord(a) - 96
b_pos = ord(b) - 96
print(f'Первая буква находится на {a_pos} месте')
print(f'Вторая буква находится на {b_pos} месте')

if a_pos > b_pos:
    col = a_pos - b_pos - 1
else:
    col = b_pos - a_pos - 1

print(f'Расстояние между буквами {col}')
