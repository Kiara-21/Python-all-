summa_minus = 0
summa_plus = 0
i = 0
num = int(input("введите количество чисел"))

while i < num:
    load = int(input("введите число"))
    if load < 0:
        summa_minus = summa_minus + load
    else:
        if load > 0:
            summa_plus = summa_plus + load
        else:
            print("обнаружен ноль")
    i = i + 1

print("summa_minus = ", summa_minus)
print("summa_plus = ", summa_plus)
