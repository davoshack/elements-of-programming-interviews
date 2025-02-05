# Brute-force approach to compute the parity of a binary number.

def parity(x: int) -> int:
    result = 0
    count = 0
    while x:
        result ^= x & 1
        x >>= 1
        count += 1
    return result

# A better approach to compute the parity of a binary number.
def better_parity(x: int) -> int:
    result = 0
    count = 0
    while x:
        result ^= 1
        x &= x - 1
        count += 1
    return result
    
if __name__ == "__main__":
    print(parity(0b1101))  # Output: 1
    print(better_parity(0b1101))  # Output: 1
