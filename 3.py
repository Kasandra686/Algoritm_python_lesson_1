# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

print('Введите координаты первой точки: ')
x1 = int(input())
y1 = int(input())
print('Введите координаты второй точки: ')
x2 = int(input())
y2 = int(input())
if x1 != x2:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Линейное уравнение прямой y={k:.2f}x + {b:.2f}')
else:
    print(f'Линейное уравнение прямой x={x1}')
