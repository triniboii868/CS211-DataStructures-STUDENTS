#Stack Notepad Exercise
# ----------------------
# Building a simple command-line notepad using a stack
# - Type a word to add it to your document (push onto the stack)
# - Type 'UNDO' to remove the last word (pop from the stack) 
# - Type 'SHOW' to display the current document contents (display stack contents)
# Implementation methods from the stack_implementatin.py file. Do not use your own method.
# Complete the function below to make the stack work.
#-----------------------


from stack_implementation import push, pop, peek, is_empty, size

def add_word(word):
    push(word)

def show():
    # Display the stack in order of items being added
    # We can't access the internal stack directly, so we use a temporary stack

    # Temporary list to hold words as we pop them to the stack
    temp = []
    while not is_empty():
        temp.append(pop())

    # Reverse temp to restore original insertion order
    temp.reverse()

    # Prints space separated sentence
    print(" ".join(temp))

    # Print items back into stack
    for word in temp:
        push(word)

