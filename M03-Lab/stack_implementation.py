# stack_implementation.py

# Internal stack storage (hidden from users)
_stack = []

def push(item):
    """
    Add an item to the top of the stack.
    """
    _stack.append(item)

def pop():
    """
    Remove and return the item from the top of the stack.
    Raises IndexError if the stack is empty.
    """
    if is_empty():
        raise IndexError("pop from empty stack")
    return _stack.pop()

def peek():
    """
    Return the item at the top of the stack without removing it.
    Raises IndexError if the stack is empty.
    """
    if is_empty():
        raise IndexError("peek from empty stack")
    return _stack[-1]

def is_empty():
    """
    Return True if the stack is empty, otherwise False.
    """
    return len(_stack) == 0

def size():
    """
    Return the number of items in the stack.
    """
    return len(_stack)