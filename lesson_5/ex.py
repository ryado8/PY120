"""
P
Given an input list and two optional strings, return a string with the list elements concatenated with given delimiter, otherwise
default to a comma. The last element should have an 'or' prepended unless an 'and' is provided as an argument.

E
- if the list has two elements, the elements should be joined by a single 'or'
- if the list has one element, return the single element
- default delimiter is a comma and the default conjunction is 'or'

D
input: list, two strings
output: string

A
- if list has single element, return element. if list has two elements, return elements joined by conjunction. if list has
greater than two elements, convert elements to strings and prepend conjunction with a space to the last element. return
stringified list joined by delimiter.

1. if len of list == 1, return element
2. if len of list == 2, return list joined by 'or'
3. if len of list > 2, initialize a new empty list 'result'
4. iterate through enumerate list, append element converted to a string to 'result'
5. if index + 1 == len of list, prepend conjunction with a space to element before appending
6. return 'result' joined by delimiter
"""

def join_or(squares, delimiter = ", ", conjunction = "or"):
    length = len(squares)

    if length == 1:
        return squares[0]

    if length == 2:
        return f"{squares[0]} or {squares[1]}"

    result = []

    for idx, square in enumerate(squares):
        if idx + 1 == length:
            result.append(f"{conjunction} {square}")
        else:
            result.append(str(square))

    return delimiter.join(result)


print(join_or([8]))                      # => "8"
print(join_or([1, 2]))                   # => "1 or 2"
print(join_or([1, 2, 3]))                # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))          # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"