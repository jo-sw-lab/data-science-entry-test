def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return -1
    modified_lst = [replace_val if item == find_val else item for item in lst]
    print(f"Modified list: {modified_lst}")
    return modified_lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
find_and_replace(["apple", "banana", "apple"], "apple", "orange")
#Test with no occurrences of find_val
find_and_replace([1, 3, 4, 5], 2, 10)
#Test with empty list
find_and_replace([], 1, 10)
#Test with non-list input
find_and_replace("not a list", 1, 10)
