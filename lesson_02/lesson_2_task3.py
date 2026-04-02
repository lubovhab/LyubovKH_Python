import math


def square(a):
    x = math.ceil(a)
    return x * x


side = float(input("Чему равна длина стороны квадрата?: "))
print(f"Тогда площадь квадрата равна: {square(side)}")
