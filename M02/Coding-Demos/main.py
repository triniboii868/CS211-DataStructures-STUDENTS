"""
Project/File Name: CS 211: Module 2 Coding Demo - Lists, Arrays, Dictionaries
Author:           Zach Wilson
Date Created:     August 20, 2025
Last Modified:    August 20, 2025

Purpose:          Demo the concepts of Lists, Arrays, Dictionaries by practical application

Dependencies:     Array module
Usage:            [How to run or use this file/project]
Inputs:           [Describe expected input, if any]
Outputs:          [Describe output, if any]
Notes:            [Any additional important information]
"""

# Lists: store a sequence of items, can be of mixed data types, and are mutable
print("List Demo")  # Prints a header to indicate the start of the list demonstration.

my_list = [10, "Hello World!", 3.75]  # Creates a list named 'my_list' containing an integer, a string, and a float. Lists in Python can hold mixed data types and are mutable, meaning their contents can be changed [[2]][[7]].

print(my_list)  # Outputs the current contents of 'my_list' to the console.

my_list.append("Hello Class!")  # Adds a new string element to the end of 'my_list' using the append() method, demonstrating the mutability of lists [[8]].

print("This is the second version of the list", my_list)  # Prints a message along with the updated list to show the effect of the append operation.

print(my_list[1])  # Accesses and prints the element at index 1 of 'my_list', which is the second item ("Hello World!"). List indices start at 0.

my_list.pop(0)  # Removes and returns the element at index 0 (the first item, 10) from 'my_list'. This demonstrates how lists can be modified by removing elements.

print(my_list)  # Prints the list after the removal, showing the updated contents.



# Arrays: Store items of the same type, more efficient for large sets of numeric data
import array  # Imports the 'array' module, which provides an array data structure for storing elements of the same type more efficiently than lists.

print("Array Demo")  # Prints a header to indicate the start of the array demonstration.

my_array = array.array('i', [1, 2, 3])  # Creates an array of integers ('i' type code) with initial values 1, 2, and 3. Arrays are more memory-efficient for large numeric data sets.

print(my_array)  # Outputs the current contents of 'my_array' to the console.

my_array.append(4)  # Adds the integer 4 to the end of 'my_array', demonstrating that arrays can be expanded like lists, but only with elements of the same type.

print("This is the second version of the array", my_array)  # Prints a message and the updated array to show the effect of the append operation.

my_array_index_2 = my_array[2]  # Retrieves the element at index 2 (the third item, which is 3) from 'my_array' and stores it in the variable 'my_array_index_2'.

print(my_array_index_2)  # Prints the value stored in 'my_array_index_2', which is 3.



# Dictionaries: Store key-value pairs, great for fast lookups
print("Dictionary Demo")  # Prints a header to indicate the start of the dictionary demonstration.

user = {"name": "Alice", "age": 25, "is_Student": True}  # Creates a dictionary named 'user' with three key-value pairs: a string, an integer, and a boolean. Dictionaries allow for fast lookups by key.

print(user)  # Outputs the entire 'user' dictionary to the console.

print(user["name"])  # Accesses and prints the value associated with the key "name" in the 'user' dictionary, which is "Alice".

print(user["age"])  # Accesses and prints the value associated with the key "age", which is 25.

print(user["is_Student"])  # Accesses and prints the value associated with the key "is_Student", which is True.

user["age"] = 26  # Updates the value associated with the key "age" in the 'user' dictionary from 25 to 26, demonstrating that dictionaries are mutable.

print(user)  # Prints the updated 'user' dictionary to show the change in the "age" value.

username = user["name"]  # Retrieves the value associated with the key "name" and stores it in the variable 'username'.

print(username)  # Prints the value of 'username', which is "Alice".