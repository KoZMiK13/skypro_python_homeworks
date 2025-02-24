import math


a = float(input("Сторона квадрата = "))


def square(a):
    square = a*a
    ceil_square = math.ceil(square)
    return ceil_square

print(f"Площадь квадрата = {square(a)} см2")
