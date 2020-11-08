print ('Лабораторная работа №7')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 1')

size = int(input('Введите количество чисел '))

print ('Введите элементы массива')

arr = [ int(input()) for i in range(size) ] 

for i in range(size): 
    print ( arr[i], end = " " )
print(' ')
print('********************************************')
print('Выполним подсчет сумм')

sum_plus = 0
count_plus = 0
for i in range(size):
    if arr[i] == 0:  
        print('Итерация №', i,': обнаружен элемент, равный нулю')
    else:
        if arr[i] > 0:
            sum_plus = sum_plus + arr[i]
            count_plus = count_plus + 1
print('Сумма положительных = ', sum_plus, ' количество' ,  count_plus )

sum_minus = 0
count_minus = 0
for i in range(size):
    if arr[i] < 0:
        sum_minus = sum_minus + arr[i]
        count_minus = count_minus + 1
print('Сумма отрицательных = ', sum_minus, ' количество' ,  count_minus )

