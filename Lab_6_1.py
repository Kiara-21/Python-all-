print ('Лабораторная работа №6')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 1')

import math

print ('Первый способ')

radius = float(input('Введите радиус конуса '))
height = float(input('Введите высоту конуса '))

if(radius <= 0)or(height <= 0):
    print('Параметры не могут быть отрицательными или равными нулю. Конец программы.')
else:
    s_osn = math.pi*(radius**2)
    l = math.sqrt(((radius/2)**2) + (height**2))
    s_b_p = math.pi*radius*l
    s_p_p = s_osn + s_b_p
    print('Площадь развертки = ', s_p_p)
    v = (1/3)*s_osn*height
    print('Объем конуса = ', v)

print ('Второй способ')

radius = float(input('Введите радиус конуса '))
height = float(input('Введите высоту конуса '))

def function_conus (radius, height):
    if(radius <= 0)or(height <= 0):
        print('Параметры не могут быть отрицательными или равными нулю. Конец программы.')
    else:
        s_osn = math.pi*(radius**2)
        l = math.sqrt(((radius/2)**2) + (height**2))
        s_b_p = math.pi*radius*l
        s_p_p = s_osn + s_b_p
        print('Площадь развертки = ', s_p_p)
        v = (1/3)*s_osn*height
        print('Объем конуса = ', v)

function_conus(radius, height)
