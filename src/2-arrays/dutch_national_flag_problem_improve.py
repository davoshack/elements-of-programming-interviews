from typing import List

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    
    # Second pass: group elements larger than pivot.
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

if __name__ == "__main__":
    A = [0, 1, 2, 0, 2, 1, 1]
    pivot_index = 2
    dutch_flag_partition(pivot_index, A)
    print(A)  # Output: [0, 0, 1, 1, 1, 2, 2] O(n) time and O(1) space

    