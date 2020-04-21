def print_hello(name: str) -> None:
    print("Hello " + name)


def get_numbers() -> int:
    input_1 = int(input("Enter a number: "))
    input_2 = int(input("Enter another number: "))
    return input_1 + input_2


def exp(x: int, y: int) -> int:
    return int(x**y)


def sum_to(n: int) -> float:
    return (n*(n+1))/2


def get_hypotenuse(a: int, b: int) -> float:
    return ((a**2) + (b**2)) ** (1/2)


def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return get_hypotenuse(x2-x1, y2-y1)


def get_perimeter(x1: int, y1: int,
                  x2: int, y2: int,
                  x3: int, y3: int) -> float:
    return (get_distance(x1, y1, x2, y2) +
            get_distance(x2, y2, x3, y3) +
            get_distance(x3, y3, x1, y1))
