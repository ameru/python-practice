# Name: Amy Ru
# Course: FinTech Python Workshop
# Term: Winter 2020

import math

def math_func1(x, y):
    one = x ** 2
    # one = x * x
    two = y * y
    top = one + two

    three = 3 * x
    bottom = three + 5
    result = top / bottom
    return result

def math_func2(a, b, c):
    one = -b
    two = math.sqrt((b**2) - 4 * a * c)
    top = one + two

    three = 2 * a
    bottom = three
    result = top / bottom
    return result

def math_func_d(x1, y1, x2, y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

def math_func_is_negative (x):
    return x < 0
