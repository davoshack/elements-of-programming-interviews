def add_binary_strings(s: str, t: str) -> str:
    """
    Add two binary numbers represented as strings.
    
    Args:
        s: First binary number as a string of '0' and '1'
        t: Second binary number as a string of '0' and '1'
    
    Returns:
        String representing the sum of the two binary numbers
    
    Raises:
        ValueError: If either input contains characters other than '0' or '1'
    """
    # Input validation
    if not (all(bit in '01' for bit in s) and all(bit in '01' for bit in t)):
        raise ValueError("Input strings must contain only '0' and '1' characters")

    # Initialize variables
    carry = 0
    result = []
    
    # Make strings same length by padding with zeros
    max_len = max(len(s), len(t))
    s = s.zfill(max_len)
    t = t.zfill(max_len)
    
    # Process bits from right to left
    for i in range(max_len - 1, -1, -1):
        bit_sum = carry + int(s[i]) + int(t[i])
        result.append(str(bit_sum % 2))
        carry = bit_sum // 2
    
    # Add final carry if exists
    if carry:
        result.append('1')
    
    # Reverse and join the result
    return ''.join(result[::-1])


def main():
    # Example usage
    test_cases = [
        ('1010', '1011'),    # 10 + 11 = 21 (10101)
        ('111', '1'),        # 7 + 1 = 8 (1000)
        ('0', '0'),          # 0 + 0 = 0
        ('1111', '1'),       # 15 + 1 = 16 (10000)
    ]
    
    for s, t in test_cases:
        try:
            result = add_binary_strings(s, t)
            print(f"{s} + {t} = {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()