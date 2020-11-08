print ('Лабораторная работа №7')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 6')

import math

number = input('Введите число ')

if number[0] == "-":
    number = number[1:]

arr = [int(x) for x in str(number)]

for k in arr: 
    print ( arr[k-1], end = " " )
print(' ')
print('********************************************')
_sum = 0
for k in arr:
    if arr[k-1] % 2 != 0:
        _sum = _sum + arr[k-1]**2
print ('Сумма равна ', _sum)
