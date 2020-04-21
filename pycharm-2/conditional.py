import math

def math_func_max_101 (x, y):
    if x > y:
        return x
    if y > x:
        return y

def math_func_max_of_three (a, b, c):
    if c >= a and c >= b:
        return c
    elif b >= a:
        return b
    else:
        return a

def math_func_rental_late_fee (x):
    if x <= 0:
        return 0
    if x <= 9:
        return 5
    if x <= 15:
        return 7
    if x <= 24:
        return 19
    if x > 24:
        return 100