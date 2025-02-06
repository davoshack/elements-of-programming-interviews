# Implement an integer to string conversion function, and a string to integer conversion function. For example, if the input to the first function is the integer 314, it should return the string "314" and if the input to the second function is the string "314" it should return the integer 314. You may not use any library functions for this problem.

import functools
import string


def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    # Add the negative sign back if it was negative
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if s[i] == '-':
            continue
        digit = ord(s[i]) - ord('0')
        result = result * 10 + digit
    return -result if s[0] == '-' else result

def string_to_int_pythonic(s: str) -> int:
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

    
if __name__ == "__main__":
    print(int_to_string(314))  # Output: "314"
    print(string_to_int("314"))  # Output: 314
    print(string_to_int_pythonic("314"))  # Output: 314
    print(int_to_string(-314))  # Output: "-314"
    print(string_to_int("-314"))  # Output: -314
    print(string_to_int_pythonic("-314"))  # Output: -314
   