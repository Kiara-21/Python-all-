print ('Лабораторная работа №6')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 4')

import math

A = float(input('Введите  А '))

if A <= 0:
    f = 0
else:
    if (A > 0) and (A <= 1):
        f = (A**2) - A
    else:
        f = (A**2 - math.sin(math.pi*(A**2)))

print ('f(A) = ', f)
