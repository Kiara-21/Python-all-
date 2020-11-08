print ('Лабораторная работа №7')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 2')

size = int(input('Введите количество чисел '))

print ('Введите элементы массива')

arr = [ int(input()) for i in range(size) ] 

for i in range(size): 
    print ( arr[i], end = " " )
print(' ')
print('********************************************')
_sum = 0

for i in range(size):
    _sum = _sum + arr[i]

ser = _sum/size
round(ser, 2)
print('Среднее арифметическое равно ', ser)

