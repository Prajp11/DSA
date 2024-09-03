# Implementation of traverlsal operation in  Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:

    def init (self):
        self.head = None

# Forward Traversal in DLL
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            n = self.head 
            while n is not None: 
                print(n.data, "-->",end="") 
                n = n.nref 

# Backward Traversal in DLL
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty!")

        else:
            n = self.head 
            while n.ref is not None:
                n = n.ref
            while n is not None:
                print(n.data, "-->",end="") 
                n = n.pref 
        
dl1  = doublyLL()
dl1.print_LL_reverse()    
