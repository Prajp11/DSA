class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Popped {popped_node.data} from stack.")
        return popped_node.data

    def get_top(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        print(f"Top of stack is {self.top.data}")
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        print("Stack elements are:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
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
