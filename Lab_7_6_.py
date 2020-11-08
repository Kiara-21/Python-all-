import math
num = int(input("введите число "))

summa = 0

if num < 0:
    num = math.fabs(num)
    
while num > 0:
    cufra = num % 10
    if cufra % 2 != 0:
        summa = summa + cufra**2
    num = num // 10

print("сумма:", summa)
