# Вычислить число c заданной точностью d

from decimal import Decimal

from random import uniform

def obtaining_accuracy():
    while True:
        try:
            value = float(input("Задайте необходимую точность для случайного числа: "))
        except ValueError:
            print("Введенное число не подходит, попробуйте заново")
            continue
        break
    return str(value)

random_number = float(uniform(1,100))
print(random_number)

value = obtaining_accuracy()

rezult_value = Decimal(random_number).quantize(Decimal(value))
print(rezult_value)

