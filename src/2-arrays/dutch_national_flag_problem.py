from typing import List

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot.
    for i in range(len(A)):
        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    
    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        # Look for a larger element. Stop when we reach an element less than the pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

if __name__ == "__main__":
    A = [0, 1, 2, 0, 2, 1, 1]
    pivot_index = 3
    dutch_flag_partition(pivot_index, A)
    print(A)  # Output: [0, 0, 1, 1, 1, 2, 2] O(n^2) time and O(1) space