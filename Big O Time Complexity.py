# Example 1
def sum_char_codes(string: str) -> int:
    # Definitely it is O(N), because the number of operations
    # increases linearly with the size of the input.
    result = 0
    for i in string:
        result += ord(i)
    
    return result


# Example 2
def sum_char_codes(string: str) -> int:
    # Definitely it is O(N), because the number of operations
    # increases linearly with the size of the input.

    # If the loops aren't nested, the number of operations increases
    # linearly with the size of the input. Constants are ignored.
    result = 0
    for i in string:
        result += ord(i)
    
    for i in string:
        result += ord(i)
    

    return result

# Example 3
def sum_char_codes(string: str) -> int:
    # Despite the fact that this function could end earlier,
    # we often consider the worst case. So this is still O(N).

    result = 0
    for i in string:
        char_code =  ord(i)
        if (char_code == 69):
            return result    
        result += char_code

    return result

# Example 4
def sum_char_codes(string: str) -> int:
    # This is O(N^2) because for each element in the string
    # we are going to go for each element in the string.
    result = 0
    for i in string:
        for j in string:
            char_code = ord(j)
            result += char_code
    return result

def sum_char_codes(string: str) -> int:
    # A bit ridiculous, but again for every single character we go for
    # every single character and then every single character AGAIN.

    # It's like multiplying a matrix.
    result = 0
    for i in string:
        for j in string:
            for k in string:
                char_code = ord(j)
                result += char_code
    return result


