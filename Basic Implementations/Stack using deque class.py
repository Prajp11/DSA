# Implementation of Stack using collections.deque
from collections import deque

# Initialize an empty stack
stack = deque()

def menu():
    print("\n--- Stack Menu ---")
    print("1. Push element onto the stack")
    print("2. Pop element from the stack")
    print("3. Display stack")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    return choice

while True:
    choice = menu()

    if choice == 1:
        # Push element onto the stack
        element = input("Enter element to push onto the stack: ")
        stack.append(element)
        print(f'Element "{element}" pushed onto the stack.')

    elif choice == 2:
        # Pop element from the stack
        if stack:
            popped_element = stack.pop()
            print(f'Element "{popped_element}" popped from the stack.')
        else:
            print("Stack is empty, no element to pop.")

    elif choice == 3:
        #Display
        print("\nCurrent stack:")
        if stack:
            print(stack)
        else:
            print("Stack is empty.")

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please enter correct choice.")




#Basic Code ---comment

# Python program to demonstrate stack implementation using list ---comment

# from collections import deque
# stack = []

# append() function to push element in the stack --- comment

# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('Initial stack')
# print(stack)

# pop() function to pop element from stack in LIFO order --- comment
# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\nStack after elements are popped:')
# print(stack)