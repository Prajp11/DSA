class Node:  # Creation of an individual node
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):  # Initializes an empty linked list
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

# Driver Code

LL1 = LinkedList()

while True:
    print("\nOptions:")
    print("1. Add node at the beginning")
    print("2. Print the linked list")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        LL1.add_begin(data)
    elif choice == 2:
        LL1.print_LL()
    elif choice == 3:
        break
    else:
        print("Invalid choice! Please try again.")
