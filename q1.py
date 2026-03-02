def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (ValidateIsInputNumeric(x) and ValidateIsInputNumeric(y)):   
        return -1
    
    x , y = y, x
    print(f"Swapped values: x = {x}, y = {y}")

    return

def ValidateIsInputNumeric(input):
    if not (isinstance(input, (int, float))):
        return False
    return True

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple", 10)
swap(9, 17)
#Test with float values
swap(3.5, 2.1)
#Test with negative values
swap(-5, -10)
#Test with zero values
swap(0, 0)
#Test with mixed numeric types
swap(5, 3.14)
#Test with non-numeric types
swap([1, 2, 3], "Hello")