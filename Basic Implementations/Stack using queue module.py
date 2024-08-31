# Stack implementation using queue module with user input

from queue import LifoQueue

# Initialize a stack using LifoQueue
stack = LifoQueue()

while True:
    print("\n--- Stack Menu ---")
    print("1. Push element onto the stack")
    print("2. Pop element from the stack")
    print("3. View stack")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Push element onto the stack
        element = input("Enter element to push onto the stack: ")
        stack.put(element)
        print(f'Element "{element}" pushed onto the stack.')

    elif choice == 2:
        # Pop element from the stack
        if not stack.empty():
            popped_element = stack.get()
            print(f'Element "{popped_element}" popped from the stack.')
        else:
            print("Stack is empty, no element to pop.")

    elif choice == 3:
        if stack.empty():
            print("Stack is empty.")
        else:
            print("\nCurrent stack (top to bottom):")
            temp_stack = list(stack.queue)
            print(temp_stack[::-1])  # Reverse to show the top of the stack first

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.")


#Basic Code ---comment

# Python program to demonstrate stack implementation using list ---comment

# from collections import deque

# stack = deque()

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