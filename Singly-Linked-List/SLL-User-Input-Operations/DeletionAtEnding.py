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

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty, unable to delete nodes.")
        elif self.head.ref is None:
            print(f"Deleting the only node with data: {self.head.data}")
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            print(f"Deleting node with data: {n.ref.data}")
            n.ref = None

# Driver Code
LL1 = LinkedList()

while True:
    print("\nMenu:")
    print("1. Insert at the beginning")
    print("2. Insert at the end")
    print("3. Delete the last node")
    print("4. Display the linked list")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data to insert at the beginning: "))
        LL1.add_begin(data)
    elif choice == 2:
        data = int(input("Enter data to insert at the end: "))
        LL1.add_end(data)
    elif choice == 3:
        LL1.delete_end()
    elif choice == 4:
        LL1.print_LL()
    elif choice == 5:
        break
    else:
        print("Invalid choice! Please try again.")
