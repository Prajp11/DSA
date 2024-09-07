class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  # Reference to the next node
        self.pref = None  # Reference to the previous node

class DoublyLL:

    def __init__(self):
        self.head = None

    # Forward Traversal in DLL
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head 
            while n is not None: 
                print(n.data, "-->", end="")
                n = n.nref 
            print("None")

    # Backward Traversal in DLL
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head 
            while n.nref is not None:  # Traverse to the last node
                n = n.nref
            while n is not None:  # Traverse backwards
                print(n.data, "-->", end="")
                n = n.pref
            print("None")

    # Insertion in DLL at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Insertion in DLL at the end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

# Driver Code
dl1 = DoublyLL()

while True:
    print("\nMenu:")
    print("1. Insert at the beginning")
    print("2. Insert at the end")
    print("3. Display the list")
    print("4. Display the list in reverse")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        data = int(input("Enter data to insert at the beginning: "))
        dl1.add_begin(data)
    elif choice == 2:
        data = int(input("Enter data to insert at the end: "))
        dl1.add_end(data)
    elif choice == 3:
        dl1.print_LL()
    elif choice == 4:
        dl1.print_LL_reverse()
    elif choice == 5:
        break
    else:
        print("Invalid choice! Please try again.")
