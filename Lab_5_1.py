print ('Лабораторная работа №5')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 1')


print('2.1.1')

x = float(input('Введите х '))
y = float(input('Введите y '))

a = x
x = y
y = a


print ('x = ', x)
print ('y = ', y)


print('2.1.2')

x = float(input('Введите х '))
y = float(input('Введите y '))

def function (x, y):
    m = x
    x = y
    y = m
    print ('x = ', x)
    print ('y = ', y)

function (x, y)

print('2.2')

x = float(input('Введите х '))
y = float(input('Введите y '))

x, y = y, x

print ('x = ', x)
print ('y = ', y)
