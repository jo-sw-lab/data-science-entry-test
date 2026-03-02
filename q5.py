def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (ValidateIsInputNumeric(num) and ValidateIsInputNumeric(divisor)):
        return -1
    if divisor == 0:
        print("Divisor cannot be zero.")
        return -1
    is_divisible = (num % divisor == 0)
    return is_divisible

 
def ValidateIsInputNumeric(input):
    if not (isinstance(input, (int, float))):
        return False
    return True


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
is_divisible = check_divisibility(10, 2)
print(f"Is 10 divisible by 2? {is_divisible}")
is_divisible = check_divisibility(7, 3)
print(f"Is 7 divisible by 3? {is_divisible}")
#Test with zero divisor
is_divisible = check_divisibility(10, 0)
print(f"Is 10 divisible by 0? {is_divisible}")
#Test with non-numeric inputs
is_divisible = check_divisibility("ten", 2)
print(f"Is 'ten' divisible by 2? {is_divisible}")
is_divisible = check_divisibility(10, "two")
print(f"Is 10 divisible by 'two'? {is_divisible}")
#Test with negative numbers
is_divisible = check_divisibility(-7, 2)
print(f"Is -7 divisible by 2? {is_divisible}")
is_divisible = check_divisibility(10, -2)
print(f"Is 10 divisible by -2? {is_divisible}")
#Test with float numbers
is_divisible = check_divisibility(2.5, 1.5)
print(f"Is 2.5 divisible by 1.5? {is_divisible}")
is_divisible = check_divisibility(0.2, 0.2)
print(f"Is 0.2 divisible by 0.2? {is_divisible}")
