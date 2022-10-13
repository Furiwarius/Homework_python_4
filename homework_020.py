# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

from random import randrange

from homework_019 import polynomial_formation


def create_file(file_number):
    # генерация файла с заданным номером

    with open(f"file_020_{file_number}.txt", "w") as f:
        for i in range(2, 10):
            k_dict = {i:randrange(0,100) for i in range(randrange(i, 10))}
            write_str = f"{polynomial_formation(k_dict)}\n"
            f.write(write_str)


def assembly_line(new_dict):
    # формирование строки для последующей записи в файл

    rezult_str='=0'
    for key in new_dict:
        if new_dict[key]>0 and key>1:
            rezult_str=f"+{new_dict[key]}x^{key}"+rezult_str
        elif new_dict[key]<0 and key>1:
            rezult_str=f"{new_dict[key]}x^{key}"+rezult_str
        elif key==1 and new_dict[key]>0:
            rezult_str=f"+{new_dict[key]}x"+rezult_str
        elif key==1 and new_dict[key]<0:
            rezult_str=f"{new_dict[key]}x"+rezult_str
        elif key==0 and new_dict[key]>0:
            rezult_str=f"+{new_dict[key]}"+rezult_str
        elif key==0 and new_dict[key]<0:
            rezult_str=f"{new_dict[key]}"+rezult_str
    else:
        return rezult_str


def polynomial_parsing(new_str):
    # нахождение коэффициентов и степени из строки

    rezult_dict = {} # degree: coefficient
    str_list = list(new_str[:-2])
    for i, val in enumerate(str_list):
        if val=="^":
            rezult_dict[int(str_list.pop(i+1))] = 0
            str_list.pop(i)
    else: 
        rezult_dict[1], rezult_dict[0] = 0, 0

    sign, number = 0 ,len(rezult_dict)-1
    for i, val in enumerate(str_list[:-2]):
        if val.isalpha():
            rezult_dict[number] = int(''.join(str_list[sign:i]))
            number-=1
            sign=i+1
    else:
        rezult_dict[number] = int(''.join(str_list[sign:]))

    return rezult_dict


def polynomial_sum(polynomial_1, polynomial_2):
    #сложение коэффициентов двух уравнений

    rezult_dict={}
    for key in range(max(len(polynomial_1), len(polynomial_2))):
        if key in polynomial_1 and key in polynomial_2:
            rezult_dict[key] = polynomial_1[key]+polynomial_2[key]
            polynomial_1.pop(key)
            polynomial_2.pop(key)
    else:
        rezult_dict.update(polynomial_1)
        rezult_dict.update(polynomial_2)

    return rezult_dict

# генерация файлов с многочленами
for number in range(1,3):
    create_file(number)
else:
    file_list=[]
    for number in range(1,3):
        with open(f"file_020_{number}.txt", "r") as f:
            file_list.append([line[:-1] for line in f.readlines()])
    component_list = [[polynomial_parsing(line) for line in file] for file in file_list] 

# сумма многочленов построчно из двух файлов в 1
rezult_list = []

for value_1, value_2 in zip(component_list[0], component_list[1]):
    rezult_list.append(polynomial_sum(value_1, value_2))
else:
    for i, elem in enumerate(rezult_list):
        rezult_list[i] = {i:elem[i] for i in sorted(elem)}

with open(f"file_020_final.txt", "w") as f:
    for equation in rezult_list:
        write_str = f"{assembly_line(equation)}\n"
        f.write(write_str)
