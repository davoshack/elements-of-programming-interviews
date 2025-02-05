

def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

if __name__ == "__main__":
    x = 0b1101
    print(count_bits(x))  # Output: 3