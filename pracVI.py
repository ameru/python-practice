from typing import List

def poly_add(poly1: List[int], poly2: List[int]) -> List[int]:
    poly_add = List[poly1] + List[poly2]
    return poly_add


def poly_mul(poly1: List[int], poly2: List[int]) -> List[int]:
    poly_mul = (poly1[List[1]] * poly2[List[1]]) + (poly1[List[1]] 
    * poly2[List[-1]]) + (poly1[List[-1]] * poly2[List[1]]) 
    + (poly1[List[-1]] * poly2[List[-1]])
    return poly_mul

def get_mode(ints: List[int]) -> int:
     get_mode = ([1, 2, 3, 1, 2, 3, 1])
     num_one = get_mode.count(1)
     num_two = get_mode.count(List[2])
     num_three = get_mode.count(List[3])
     if num_one > num_two and num_one > num_three:
         return num_one
     elif num_two > num_one and num_two > num_three:
         return num_two
     elif num_three > num_one and num_three > num_two:
         return num_three
     elif num_one == num_two or num_one == num_three:
         return num_one
     else:
         return num_two

def has_duplicates(ints: List[int]) -> bool:
    has_duplicates = ([1, 0, 2, 0, 3])
    if has_duplicates.index(0) > 1:
        return True
    else:
        return False
