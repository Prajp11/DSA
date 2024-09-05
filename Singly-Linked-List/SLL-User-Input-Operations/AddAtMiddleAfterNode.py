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
            print("None")

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print(f"Node {x} is not present in the linked list.")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

# Menu-driven logic
def menu():
    ll = LinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Add at Beginning")
        print("2. Add After a Given Node")
        print("3. Print Linked List")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter the value to add at the beginning: "))
            ll.add_begin(data)
        elif choice == 2:
            data = int(input("Enter the value to add: "))
            node_value = int(input("Enter the node after which to add: "))
            ll.add_after(data, node_value)
        elif choice == 3:
            ll.print_LL()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Driver Code
menu()
