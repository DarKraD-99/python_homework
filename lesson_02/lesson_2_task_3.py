import math


def square(side):
    if side != int(side):
        return math.ceil(side * side)
    else:
        return (side * side)


num_side = float(input("Сторона: "))
print(f"Площадь квадрата: {square(num_side)}")
