from typing import List

def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # There is a carry-out, so we need one more digit to store the result.
        # A slick way to do this is to append a 0 at the end of the array, and update the first entry to 1.
        A[0] = 1
        A.append(0)
    return A

if __name__ == "__main__":
    print(plus_one([1, 2, 9]))  # Output: [1, 3, 0]
    print(plus_one([9, 9, 9]))  # Output: [1, 0, 0, 0]
    print(plus_one([1, 9, 9]))  # Output: [2, 0, 0]
    print(plus_one([9, 8, 9]))  # Output: [9, 9, 0]
    print(plus_one([9]))  # Output: [1, 0]
    print(plus_one([0]))  # Output: [1]
    print(plus_one([1]))  # Output: [2]