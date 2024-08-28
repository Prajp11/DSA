# Deletion at starting node

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

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("LL is empty unable to delete nodes")
        else:
            self.head = self.head.ref

# Diver Code

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.add_end(50)
LL1.delete_begin()     # Head node 30 will get deleted
LL1.print_LL()
