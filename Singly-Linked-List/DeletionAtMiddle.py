#Delete any node in-between/Middle of the linked list

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

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def delete_by_value(self, x):
        if self.head is None:
            print("Can't delete node as LL is empty.")
            return

        if x == self.head.data:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref

        if n.ref is None:
            print("Node is not present.")
        else:
            n.ref = n.ref.ref

# Creating the linked list and testing the functions
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.delete_by_value(20)
LL1.print_LL()