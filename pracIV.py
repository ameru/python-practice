def all_input() -> str:
    user_input = input("Please enter your input: ")
    while len(user_input) != 0:
        total += user_input
        user_input = input("Please enter your input: ")
    return total

def mul(x: int, y: int) -> int:
    n = 0
    sum = 0
    while n < y:
        sum = sum + x 
        n = n + 1
    return sum


def exp(x: int, y: int) -> int:
    n = 0
    product = 0
    while n < y:
        product = product + mul(x, x)
        n += 1
    return product


def div(x: int, y: int) -> int:
    n = 0
    quotient = 0
    while n < y:
        quotient = quotient - x
        n = n - 1
    return quotient
    

def mod(x: int, y: int) -> int:


def gcd(x: int, y: int) -> int:


def is_prime(x: int) -> bool:
user_input = int (input("Please enter a number: "))
x = 0
total = 0
while user_input % x = 0
    return False


def sum_ints(start: int, stop: int, step: int) -> int:


def sum_mul_table(max_int: int) -> int:


def rotate_string(chars: str, n_rot: int) -> str:


def weave_strings(s1: str, s2: str) -> str:


def to_pig_latin(word: str) -> str:
input_1 = str (input("Please enter a word: "))
while i = "A", "E", "I", "O", "U":
    print input + "YAY"
else:
    print input + "AY"


sum = 0
i = 0
while i < 10:
    sum = sum + i
    print sum
    i = i + 1
