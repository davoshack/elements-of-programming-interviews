# The program checks if a string is palindromic. A palindromic string is one that reads the same forwards and backwards. For example, "level" and "radar" are palindromic strings. The program uses two pointers, one starting from the beginning of the string and the other starting from the end of the string. It compares the characters at these two positions and moves the pointers towards each other until they meet in the middle of the string. If all characters match, the string is palindromic.

def is_palindromic(s: str) -> bool:
    # Note that s[~i] for i in [0, len(s) - 1] is equivalent to s[-(i + 1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))
    # Time complexity is O(n) and space complexity is O(1)

    
if __name__ == "__main__":
    print(is_palindromic("level"))  # Output: True