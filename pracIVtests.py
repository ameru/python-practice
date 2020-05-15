import pset4

# testing mul(x: int, y: int) -> int:
assert pset4.mul(9, 8) == 72
assert pset4.mul(6, 7) == 42
assert pset4.mul(9, 9) == 81

# testing exp(x: int, y: int) -> int:
assert pset4.exp(3, 1) == 3
assert pset4.exp(5, 2) == 25
assert pset4.exp(2, 4) == 16

# testing div(x: int, y: int) -> int:
assert pset4.div(3, 1) == 3
assert pset4.div(10, 5) == 2
assert pset4.div(60, 10) == 6

# testing mod(x: int, y: int) -> int:
assert pset4.mod(3, 1) == 3
assert pset4.mod(-2, 0) == 0
assert pset4.mod(25, 25) == 25

# testing gcd(x: int, y: int) -> int:
assert pset4.gcd(3, 1) == 3
assert pset4.gcd(12, 4) == 12
assert pset4.gcd(5, 10) == 10

# testing is_prime(x: int) -> bool:
assert pset4.is_prime(3)
assert not pset4.is_prime(10)
assert not pset4.is_prime(20)

# testing sum_ints(start: int, stop: int, step: int) -> int:


# testing sum_mul_table(max_int: int) -> int:


# testing rotate_string(chars: str, n_rot: int) -> str:


# testing weave_strings(s1: str, s2: str) -> str:


# testing to_pig_latin(word: str) -> str:
assert pset4.to_pig_latin("ALPHABET") == "ALPHABETYAY"
assert pset4.to_pig_latin("EARTH") == "EARTHYAY"
assert pset4.to_pig_latin("CALPOLY") == "AOCLPLYAY"
