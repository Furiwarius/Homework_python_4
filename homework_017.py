# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from random import randrange

def simple_multiplier(value):
    mult_list = []
    for i in range(2,value):
        while value%i==0:
            value/=i
            mult_list.append(i)
    return mult_list

N = randrange(50, 5000)
print(N)
print(simple_multiplier(N))

