import math


a = b = float(input("Сторона квадрата = "))
c = math.ceil(a)*math.ceil(b)


def square():
    print(f"Площадь квадрата = {c} см2")


square()
