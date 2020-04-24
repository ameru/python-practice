# Amy Ru
# Lab 5

poly1 = [2.3, 4.7, 1.0]
poly2 = [1.2, 2.1, -3.2]


def poly_add21(lone, ltwo):
    return [lone[0] + ltwo[0], + lone[1] + ltwo[1], + lone[2] + ltwo[2]]

def poly_add22(lone, ltwo):
    out = []
    for i in range(len(lone)):
        out.append(lone[i] + ltwo[i])
    return out

def poly_add23(lone, ltwo):
    out = []
    for i in range(len(lone)):
        out += [lone[i] + ltwo[i]]
    return out

def poly_add24(lone, ltwo):
    out = []
    for i in range(len(lone)):
        out = out + [lone[i] + ltwo[i]]
    return out

def poly_mult21(lone, ltwo):
    return [lone[0] * ltwo[0], lone[1] * ltwo[1], lone[2] * ltwo[2]]

def poly_square_allfor(lone):
    out = []
    for i in lone:
        out.append(i**2)
    return out

def poly_square_allwhile(lone):
    out = []
    i = 0
    while i < len(lone):
        out.append(lone[i]**2)
    return out

def poly_square_alllistcomp(lone):
    return ([i**2 for i in lone])

def poly_all_n_all21(lone, ltwo):
    sum1 = 0
    for i in lone:
        sum1 += i
    sum2 = 0
    for i in ltwo:
        sum2 += i
    return [sum1, sum2]

def poly_even_or_odd_all21(lone):
    out = []
    i = 0
    while i < len(lone):
        if lone[i] % 2 == 0:
            out.append(True)
        else:
            out.append(False)
    return out

# use a "for" loop when you know the length of a list/how many times you are iterating, use a "while" loop when you don't know
# use [] when you're indexing on list, use () for functions