# задача №1:Напишите программу, которая заполняет массив первыми N натуральными числами и
# выводит его.
import random

# Hello Stas!!! 
def f():
    n = int(input())
    if 0 < n <= 100:
        for i in range(1,n+1):
            print(i, end=' ')
    else:
        print('введённое число выходит за рамки')

#задача №2:Напишите программу, которая заполняет массив из N элементов степенями числа 2,
#начиная с 2-ух в 1-ой степени до 2-ух в N-ной степени, в обратном порядке.

def k():
    m = int(input())
    if 0 < m <= 30:
        for i in range(m,0, -1):
            print(2**i, end=' ')
    else:
        print('введённое число выходит за рамки')

#задача №3 :Напишите программу, которая заполняет массив из N элементов случайными целыми
#числами в диапазоне [A , B] и определяет количество элементов этого массива, у которых
#вторая цифра в десятичной записи (число десятков) – чётная.

def g():
    n ,a ,b ,col, count = [], int(input()), int(input()), int(input()), 0
    for i in range(col):
        m = random.randint(a, b)
        l = (m // 10) % 10
        if l % 2 == 0:
            count += 1

        n.append(m)
    print(*n)
    print(count)

f()
print()
k()
print()
g()