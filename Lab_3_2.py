print ('Лабораторная работа №3')
print ('Вариант 3')
print ('Выполнила студентка групы К19-1 Бодю К. О.')

print ('-------------------------------------------')

print ('Задание 2')

stor = float(input('Введите длинну стороны квадрата '))
             
def funct_area(stor):
   area = stor**2
   print ('Площадь квадрата равна: ', area)
   
funct_area(stor)

def funct_perimetr(stor):
   perimetr = stor*4
   print ('Периметр квадрата равен: ', perimetr)
   
funct_perimetr(stor)
