class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.ref
            print("None")  # To signify the end of the linked list

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == x:  # If first node is the given node
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

def menu():
    ll = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Add an element at the beginning")
        print("2. Add an element before a given node")
        print("3. Print Linked List")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the element to add at the beginning: "))
            ll.add_begin(data)
        elif choice == 2:
            data = int(input("Enter the element to add: "))
            x = int(input("Enter the node before which to add the element: "))
            ll.add_before(data, x)
        elif choice == 3:
            ll.print_LL()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Start the menu-driven interface
menu()
