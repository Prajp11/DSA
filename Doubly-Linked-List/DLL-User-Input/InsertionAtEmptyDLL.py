class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  # Reference to the next node
        self.pref = None  # Reference to the previous node

class doublyLL:
    def __init__(self):
        self.head = None

    # Insertion operation when DLL is empty
    def insert_empty(self):
        if self.head is None:
            data = int(input("Enter the element to insert in an empty DLL: "))
            new_node = Node(data)
            self.head = new_node
            print(f"Inserted {data} into the empty Linked List.")
        else:
            print("Linked List is not empty")

    # Forward Traversal in DLL (for verification purposes)
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head 
            while n is not None: 
                print(n.data, "-->", end="")
                n = n.nref 
            print("None")
            print("Linked List is not empty.")

# Example usage
dll = doublyLL()
dll.insert_empty()  # Inserts only one element based on user input
dll.print_LL()  # Prints the linked list
