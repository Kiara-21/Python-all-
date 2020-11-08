print ('Лабораторная работа №5')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 2')

import math

x = float(input('Введите x '))
c = float(input('Введите c '))

g = pow( (math.sin(math.radians(x)) + c) , (1/3) ) / (c*math.exp(x))

print ('g = ', g)

print ('Использование пользовательской функции:')

x = float(input('Введите x '))
c = float(input('Введите c '))

def function(x, c):
    a = math.radians(x)
    b = pow((math.sin(a)+c), (1/3))
    m = c*math.exp(x)
    g = b/m
    print ('g = ', g)

function(x, c)
