# how to use modulus
# '%' number denotes remainder
# '//' operator denotes how many times a number can go into another number
# 0 % 2 == 0
# 1 % 2 == 1
# 2 % 2 == 0
# 3 % 2 == 1
# 4 % 2 == 0

# 0 // 2 == 0
# 1 // 2 == 0
# 2 // 2 == 1
# 3 // 2 == 1
# 4 // 2 == 2

def is_even(x):
    if x % 2 == 0:
        return True
    if x % 2 == 1:
        return False

def in_an_interval(x):
    if x >= 2 and x < 9:
        return True
    if x > 47 and x < 92:
        return True
    if x > 12 and x <=19:
        return True
    if x >= 101 and x <= 103:
        return True
    else:
        return False

# when making individual functions, I had to change the numbers to all be paranthesis/inclusive

# for in_an_interval, make a separate bracket test for each
# a square bracket indicates inclusivity, a paranthesis indicates exclusivity
# for optimizing code, double equal operator automatically sets equation to boolean type