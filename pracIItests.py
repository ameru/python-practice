import pset2

# testing print_hello()
pset2.print_hello("Amy")
pset2.print_hello("World")
pset2.print_hello("darkness my old friend")

# testing get_numbers()


# testing exp(x,y)
assert pset2.exp(2, 2) == 4
assert pset2.exp(2, 0) == 1
assert pset2.exp(2, 3) == 8

# testing sum_to(1,n)
assert pset2.sum_to(3) == 6
assert pset2.sum_to(1) == 1
assert pset2.sum_to(2) == 3

# testing get_hypotenuse(a,b)
assert pset2.get_hypotenuse(0, 0) == 0
assert pset2.get_hypotenuse(1, 1) == 2 ** (1/2)
assert pset2.get_hypotenuse(3, 4) == 5

# testing get_distance(x1,y1,x2,y2)
assert pset2.get_distance(2, 1, 4, 3) == 8 ** (1/2)
assert pset2.get_distance(1, 4, 3, 5) == 5 ** (1/2)
assert pset2.get_distance(2, 3, 6, 4) == 17 ** (1/2)

# testing get_perimeter(x1,y1,x2,y2,x3,y3)
assert pset2.get_perimeter(0, 0, 3, 0, 0, 4) == 12
assert pset2.get_perimeter(0, 0, 0, 8, -6, 0) == 24
assert pset2.get_perimeter(0, 0, -9, 0, 0, -12) == 36
