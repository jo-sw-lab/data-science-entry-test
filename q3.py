def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    #Defensive coding
    if not isinstance(dct, dict):
        return -1
    
    #Check if key exists in order to determine if it's an update or a new entry
    isNew = False
    if key in dct:
        print(f"Original value for key '{key}': {dct[key]}")
    else:
        isNew = True
    dct[key] = value
    if not isNew:
        print(f"Updated value for key '{key}': {dct[key]}")
    else:
        print(f"New key-value pair added: '{key}': {value}")
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
result = update_dictionary({}, "name", "Alice")
print(f"Result of updating empty dict: {result}")
result = update_dictionary({"age": 25}, "age", 26)
print(f"Result of updating existing key: {result}")
#Test with additional key-value pairs
result = update_dictionary({"name": "Bob", "age": 30}, "name", "Charlie")
print(f"Result of updating name key: {result}")
result = update_dictionary({"name": "Bob", "age": 30}, "city", "New York")
print(f"Result of adding city key: {result}")
#Test with non-string keys and values
result = update_dictionary({1: "one", 2: "two"}, 1, "yi")
print(f"Result of updating integer key: {result}")
result = update_dictionary({1: "one", 2: "two"}, 3, "three")
print(f"Result of adding new integer key: {result}")