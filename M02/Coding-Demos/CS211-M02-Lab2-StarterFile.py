"""
Lab: Arrays vs. Dictionaries

Key Methods and Concepts:

- .append(x): Adds an element x to the end of a list or array.
- .insert(i, x): Inserts element x at index i, shifting subsequent elements right.
- .pop(): Removes and returns the last element. .pop(i) removes and returns the element at index i.
- del arr[i]: Deletes the element at index i from a list or array.
- arr.index(x): Returns the index of the first occurrence of x in the list or array.
- arr.remove(x): Removes the first occurrence of x from the list or array.
- Dictionaries use keys to store and retrieve values quickly.
- dict[key] = value: Inserts or updates a key-value pair.
- del dict[key]: Deletes the key-value pair with the specified key.
- dict.get(key): Returns the value for key if key is in the dictionary, else None.
- dict.keys(), dict.values(), dict.items(): Useful for iterating over keys, values, or key-value pairs.

Arrays (using Python's array module) are more efficient for large sets of numeric data and require all elements to be of the same type.
Dictionaries are great for fast lookups using keys.

"""

import array
import time

# -------------------------------
# Arrays Section
# -------------------------------

def array_demo():
    print("Array Demo")
    # Create an array of integers
    arr = array.array('i', [10, 20, 30])
    print("Initial array:", arr)

    # Insert at the end
    arr.append(40)
    print("After appending 40:", arr)

    # Insert at the beginning (index 0)
    arr.insert(0, 5)
    print("After inserting 5 at the beginning:", arr)

    # Insert in the middle (index 2)
    arr.insert(2, 15)
    print("After inserting 15 at index 2:", arr)

    # Delete from the end
    arr.pop()
    print("After popping from the end:", arr)

    # Delete from the beginning
    arr.pop(0)
    print("After popping from the beginning:", arr)

    # Delete from the middle (index 1)
    arr.pop(1)
    print("After popping from the middle (index 1):", arr)

    # Search for an element
    search_value = 20
    if search_value in arr:
        print(f"{search_value} found at index {arr.index(search_value)}")
    else:
        print(f"{search_value} not found in array")

    # Display the array
    print("Final array:", arr)

# -------------------------------
# Dictionaries Section
# -------------------------------

def dictionary_demo():
    print("\nDictionary Demo")
    # Create a dictionary
    d = {}

    # Insert key-value pairs
    d["name"] = "Alice"
    d["age"] = 25
    d["is_student"] = True
    print("Initial dictionary:", d)

    # Update the value for an existing key
    d["age"] = 26
    print("After updating age:", d)

    # Delete a key-value pair
    del d["is_student"]
    print("After deleting 'is_student':", d)

    # Search for a value by key
    key = "name"
    if key in d:
        print(f"Value for key '{key}':", d[key])
    else:
        print(f"Key '{key}' not found.")

    # Display the dictionary
    print("Final dictionary:", d)

# -------------------------------
# Comparison Exercise
# -------------------------------

def compare_array_vs_list():
    print("\nComparison: Array vs. List (for insertion and deletion)")

    # Setup
    arr = array.array('i', range(10000))
    lst = list(range(10000))

    # Time insertion at the beginning
    start = time.time()
    arr.insert(0, -1)
    arr_insert_time = time.time() - start

    start = time.time()
    lst.insert(0, -1)
    list_insert_time = time.time() - start

    print(f"Array insert at beginning: {arr_insert_time:.6f} seconds")
    print(f"List insert at beginning: {list_insert_time:.6f} seconds")

    # Time deletion from the beginning
    start = time.time()
    arr.pop(0)
    arr_delete_time = time.time() - start

    start = time.time()
    lst.pop(0)
    list_delete_time = time.time() - start

    print(f"Array delete from beginning: {arr_delete_time:.6f} seconds")
    print(f"List delete from beginning: {list_delete_time:.6f} seconds")

# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    array_demo()
    dictionary_demo()
    compare_array_vs_list()