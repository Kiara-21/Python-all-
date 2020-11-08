print ('Лабораторная работа №6')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 3')

import math

X = float(input('X = '))
Y = float(input('Y = '))

if (X<0) or (Y<0):
    print('Параметры не могут быть отрицательными или равными нулю. Конец программы.')        
else: 
    if X > Y:
        Z = math.sqrt(X*Y)
    else:
        Z = math.log1p(X+Y-1)
        
    print('Z = ', Z)
