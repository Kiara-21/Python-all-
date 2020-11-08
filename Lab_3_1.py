print ('Лабораторная работа №3')
print ('Вариант 3')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 1')

import math

grad = float(input('Введите величину в градусах: '))

def funct_converte(grad):
   radia = (grad*(math.pi/180))
   print ('Величина угла в радианах: ', radia)
   
funct_converte(grad)


