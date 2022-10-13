# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k

from random import randrange, choice


def polynomial_formation(new_dict):
    rezult_str='=0'
    for key in new_dict:
        if new_dict[key]>0 and key>1:
            rezult_str=f"{choice(['-', '+'])}{new_dict[key]}x^{key}"+rezult_str
        elif key==1:
            rezult_str=f"{choice(['-', '+'])}{new_dict[key]}x"+rezult_str
        elif key==0:
            rezult_str=f"{choice(['-', '+'])}{new_dict[key]}"+rezult_str
    else:
        return rezult_str


with open("file_019.txt", "w") as f:
    for i in range(2, 10):
        k_dict = {i:randrange(0,100) for i in range(randrange(i, 10))}
        write_str = f"{polynomial_formation(k_dict)}\n"
        f.write(write_str)


