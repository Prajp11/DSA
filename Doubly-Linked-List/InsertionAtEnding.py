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

    # Insertion in DLL at beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Insertion in DLL at end
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
dl1 = doublyLL()
dl1.add_begin(10)
dl1.add_end(20)
dl1.add_end(30)

dl1.print_LL()
dl1.print_LL_reverse()
