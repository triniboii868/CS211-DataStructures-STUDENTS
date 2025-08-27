# main.py

# Import stack functions from stack_implementation.py
from stack_implementation import push, pop, peek, is_empty, size

def demonstrate_stack():
    """
    Demonstrate stack operations.
    """
    print("Pushing items: 1, 2, 3")
    push(1)
    print(f"Stack size: {size()}")
    push(2)
    print(f"Stack size: {size()}")
    push(3)
    print(f"Stack size: {size()}")

    print("\nPopping two items:")
    print(f"Popped: {pop()}")
    print(f"Stack size: {size()}")
    print(f"Popped: {pop()}")
    print(f"Stack size: {size()}")

    print("\nCurrent top item (peek):")
    print(f"Top item: {peek()}")

    print(f"\nIs stack empty? {is_empty()}")
    print(f"Final stack size: {size()}")

def is_parentheses_balanced(s):
    """
    Check if the parentheses in the string s are balanced.
    Returns True if balanced, False otherwise.
    """
    # Clear the stack before use (if needed)
    while not is_empty():
        pop()
    for char in s:
        if char == '(':
            push(char)
        elif char == ')':
            if is_empty():
                return False
            pop()
    return is_empty()

if __name__ == "__main__":
    demonstrate_stack()
    print("\nParentheses Matching Examples:")
    test_cases = ["((()))", "(()", "())(", "()", ""]
    for expr in test_cases:
        print(f"{expr!r} is balanced? {is_parentheses_balanced(expr)}")