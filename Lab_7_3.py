print ('Лабораторная работа №7')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 3')

size = int(input('Введите количество чисел '))

print ('Введите элементы массива')

arr = [ int(input()) for i in range(size) ] 

for i in range(size): 
    print ( arr[i], end = " " )
print(' ')
print('********************************************')
sum_par_plus = 0
sum_par_minus = 0
sum_nepar_plus = 0
sum_nepar_minus = 0

plus_count = 0
minus_count = 0
zero_count = 0

for i in range(size):
    if arr[i] > 0:
        plus_count = plus_count+1
        if arr[i] % 2 == 0:
            sum_par_plus = sum_par_plus + arr[i]
        else:
            sum_nepar_plus = sum_nepar_plus + arr[i]
    else:
        if arr[i] < 0:
            minus_count = minus_count + 1
            if arr[i] % 2 ==0:
                sum_par_minus = sum_par_minus + arr[i]
            else:
                sum_nepar_minus = sum_nepar_minus + arr[i]
        else:
            if arr[i] == 0:
                zero_count = zero_count + 1

print('Сумма положительных парных ', sum_par_plus)
print('Сумма отрицательных парных ', sum_par_minus)
print('Сумма положительных непарных ', sum_nepar_plus)
print('Сумма отрицательных непарных ', sum_nepar_minus)

print('Количество положительных чисел ', plus_count)
print('Количество отрицательных чисел ', minus_count)
print('Количество нулей ', zero_count)
