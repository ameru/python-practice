from typing import Optional


def is_positive(x: int) -> bool:
    return x > 0


def both_positive(x: int, y: int) -> bool:
    return is_positive(x) and is_positive(y)


def is_triangle(a: int, b: int, c: int) -> bool:
    return c < (a + b) and b < (a + c) and a < (b + c)


def is_isosceles_triangle(a: int, b: int, c: int) -> bool:
    return is_triangle(a, b, c) and ((a == b) or (b == c) or (a == c))


def is_rotation(rotated: str, word: str) -> bool:
    str_1 = word + word
    return rotated in str_1


def max_of_two(x: int, y: int) -> int:
    if x > y:
        return x
    if y > x:
        return y
    else:
        return x


def max_of_three(x: int, y: int, z: int) -> int:
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > y and z > x:
        return z
    else:
        return x


def mix_colors(a: str, b: str) -> str:
    if ((a == "red" and b == "yellow")
            or (a == "yellow" and b == "red")):
        return "orange"
    elif ((a == "yellow" and b == "blue")
            or (a == "blue" and b == "yellow")):
        return "green"
    elif a == "blue" and b == "red":
        return "purple"
    elif a == b:
        return a
    else:
        return "none"


def find_discriminant(a: int, b: int, c: int) -> Optional[float]:
    if (b ** 2) - (4 * a * c) > 0:
        return (b ** 2) - (4 * a * c)
    else:
        return None


def solve_poly(a: int, b: int, c: int) -> Optional[float]:
    if ((-b + (find_discriminant(a, b, c) ** (1/2))) / 2*a) > 0:
        return (-b + (find_discriminant(a, b, c) ** (1/2))) / 2*a
    else:
        return None
