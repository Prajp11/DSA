class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None  # Reference to the next node
        self.pref = None  # Reference to the previous node

class doublyLL:

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

    # Insertion operation when DLL is empty
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("DLL is not empty")

# Example usage
dl1 = doublyLL()
dl1.insert_empty(10)
dl1.insert_empty(20)



dl1.print_LL()
dl1.print_LL_reverse()