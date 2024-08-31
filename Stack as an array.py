class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        print(f"Pushed {data} onto stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped_data = self.stack.pop()
        print(f"Popped {popped_data} from stack.")
        return popped_data

    def get_top(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        top_data = self.stack[-1]
        print(f"Top of stack is {top_data}")
        return top_data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements are:")
        for data in reversed(self.stack):
            print(data, end=" -> ")
        print("None")


def main():
    stack = Stack()

    while True:
        print("\n1. Push\n2. Pop\n3. Get Top\n4. Display\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter value to push: ")
            stack.push(data)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.get_top()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
