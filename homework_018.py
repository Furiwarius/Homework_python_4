# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

from random import randrange


def creating_originality(new_list):
    rezult_list = []
    for val in new_list:
        if val not in rezult_list: rezult_list.append(val)
    return rezult_list


random_list = [randrange(1,10) for _ in range(20)]
print(*random_list)
print(*creating_originality(random_list))

# или 


#print(*random_list, sep='\n')

random_list = set(random_list)
print(*random_list)