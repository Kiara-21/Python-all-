summa = 0
i = 0
num = int(input("введите количество чисел"))

while i < num:
    load = int(input("введите число"))
    summa = summa + load
    i = i + 1

srednee = summa/num

print("srednee = ", srednee)
