
# Given an array A of numbers, rearrange the array so that all even numbers come before odd numbers. 

from typing import List

def even_odd(A: List[int]) -> List[int]:
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

if __name__ == "__main__":
    print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [8, 2, 6, 4, 5, 3, 7, 1, 9] O(n) time and O(1) space