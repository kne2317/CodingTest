import math


def function_1(a):
    if a >= 0:
        return a
    else:
        return -a


def function_2(a):
    b = a * a
    return math.sqrt(b)


print(function_1(3))
print(function_1(-2))
print(function_2(3))
print(function_2(-2))
