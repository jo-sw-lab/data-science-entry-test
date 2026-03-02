def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    ERROR_NON_STRING = "Input must be a string"
    if not isinstance(s, str):
        return ERROR_NON_STRING
    reversed_string = s[::-1]
    return reversed_string


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
result = string_reverse("Hello World")
print(f"Reversed string: {result}")
result = string_reverse("Python")
print(f"Reversed string: {result}")
#Test with empty string
result = string_reverse("")
print(f"Reversed string: {result}")
#Test with non-string input
result = string_reverse(12345)
print(f"Reversed string: {result}")