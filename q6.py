def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    ERROR_NON_LIST = "Input must be a list"
    NO_NEGATIVE_STRING = "No negatives"
    if not isinstance(lst, list):
        return ERROR_NON_LIST
    index = 0
    while index < len(lst):
        value = lst[index]
        if ValidateIsNegative(value):
            return value
        index += 1
    return NO_NEGATIVE_STRING

def ValidateIsNegative(input):
    if not (isinstance(input, (int, float))):
        return False
    return input < 0

# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(f"First negative in [3, 5, -1, 7, -2, 8]: {result1}")
result2 = find_first_negative([2, 10, 7, 0])
print(f"First negative in [2, 10, 7, 0]: {result2}")
#Test with empty list
result3 = find_first_negative([])
print(f"First negative in []: {result3}")
#Test with non-list input
result4 = find_first_negative("not a list")
print(f"First negative in 'not a list': {result4}")
#Test with list of non-numeric values
result5 = find_first_negative(["a", "b", "c"])
print(f"First negative in ['a', 'b', 'c']: {result5}")