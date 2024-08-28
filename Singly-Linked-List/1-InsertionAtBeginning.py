# Insertion of node at beginning

class Node:                       # Creation of a individual node
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):          # Here self self represent object of class itself
        self.head = None         # self.head is empty as linkedlist is empty

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

# Diver Code

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.print_LL()