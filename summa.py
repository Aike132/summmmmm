import math
from random import randint
spisok = []
sum1 = 0
sum2 = 0
print("хотите ввести числа вручную(1) или сгенерировать рандомно(0)?")
otvet = int(input())
if otvet > 0:
    for i in range(15):
        print("введите число")
        a = int(input())
        spisok.append(a)
else:
    for i in range(15):
        a = randint(-100, 100)
        while a == 0:
            a = randint(-100, 100)
        print(a)
        spisok.append(a)
for i in range(15):
    if spisok[i] > 0:
        sum1 = sum1 + spisok[i]
    else:
        sum2 = sum2 + spisok[i]
print(sum1)
print(sum2)