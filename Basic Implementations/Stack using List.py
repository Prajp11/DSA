# Python program to demonstrate stack implementation using list with user input

def main():
    stack = []

    while True:
        print("\nMenu:")
        print("1. Push an element onto the stack")
        print("2. Pop an element from the stack")
        print("3. Display the current stack")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the value to push onto the stack: ")
            stack.append(data)
            print(f"Pushed '{data}' onto the stack.")
        
        elif choice == '2':
            if len(stack) == 0:
                print("Stack is empty. Nothing to pop.")
            else:
                popped_element = stack.pop()
                print(f"Popped '{popped_element}' from the stack.")
        
        elif choice == '3':
            if len(stack) == 0:
                print("Stack is empty.")
            else:
                print("Current stack:", stack)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()



#Basic Code ---comment

# Python program to demonstrate stack implementation using list ---comment

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