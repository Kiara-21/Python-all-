print ('Дополнительные задания №1')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 1')

import math

S = float(input ('Введите S '))
R = float(input ('Введите R '))
K = float(input ('Введите K '))

a = math.sqrt(S)

_K = a - R 

if _K >= K:
    print ('Возможно')
else:
    print ('Невозможно')

