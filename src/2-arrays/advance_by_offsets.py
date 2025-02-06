# Write a program which takes an array of n integers, where A[i] denotes the maximum you can advance from index i, and returns whether it is possible to advance to the last index starting from the beginning of the array.

from typing import List

def can_reach_end(A: List[int]) -> bool:
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

if __name__ == "__main__":
    can_reach_end([3, 3, 1, 0, 2, 0, 1])  # Output: True
    can_reach_end([3, 2, 0, 0, 2, 0, 1])  # Output: False
    # time complexity is O(n) and space complexity is O(1)


