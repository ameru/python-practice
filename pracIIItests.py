import pset3

# testing is_positive(a)
assert not pset3.is_positive(-5)
assert pset3.is_positive(3)
assert pset3.is_positive(10)


# testing both_positive(a, b)
assert not pset3.both_positive(-5, 0)
assert pset3.both_positive(3, 90)
assert not pset3.both_positive(-11, -64)


# testing is_triangle(a: int, b: int, c: int) -> bool:
assert pset3.is_triangle(3, 4, 5)
assert not pset3.is_triangle(1, 1, 1)
assert not pset3.is_triangle(2, 6, 19)


# testing is_isosceles_triangle(a: int, b: int, c: int) -> bool:
assert not pset3.is_isosceles_triangle(0, 3, 5)
assert pset3.is_isosceles_triangle(3, 3, 4)
assert pset3.is_isosceles_triangle(6, 6, 8)


# testing is_rotation(rotated: str, word: str) -> bool:
assert pset3.is_rotation("putercom", "computer")
assert not pset3.is_rotation("computre", "computer")
assert not pset3.is_rotation("comterpu", "computer")


# testing max_of_two(x: int, y: int)
assert pset3.max_of_two(3, 1) == 3
assert pset3.max_of_two(-2, 0) == 0
assert pset3.max_of_two(25, 25) == 25


# testing max_of_three(x: int, y: int, z: int)
assert pset3.max_of_three(3, 2, 10) == 10
assert pset3.max_of_three(5, 19, 21) == 21
assert pset3.max_of_three(2, 2, 2) == 2


# testing mix_colors()
assert pset3.mix_colors("red", "red") == "red"
assert pset3.mix_colors("blue", "yellow") == "green"
assert pset3.mix_colors("blue", "red") == "purple"


# testing find_discriminant(a: int, b: int, c: int) -> Optional[float]:
assert pset3.find_discriminant(5, 1, 2) is None
assert pset3.find_discriminant(10, 2, 15) is None
assert pset3.find_discriminant(1, 5, 3) == 13

# testing solve_poly(a: int, b: int, c: int) -> Optional[float]:
assert pset3.solve_poly(1, 5, 0) == 0
assert pset3.solve_poly(1, 2, -3) == 1
assert pset3.solve_poly(-1, 2, 3) is None
