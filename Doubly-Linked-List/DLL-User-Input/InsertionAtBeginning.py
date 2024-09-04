# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.nref = None  # Reference to the next node
#         self.pref = None  # Reference to the previous node

# class doublyLL:
#     def __init__(self):
#         self.head = None

#     # Forward Traversal in DLL
#     def print_LL(self):
#         if self.head is None:
#             print("Linked List is empty!")
#         else:
#             n = self.head 
#             while n is not None: 
#                 print(n.data, "-->", end="")
#                 n = n.nref 
#             print("None")

#     # Backward Traversal in DLL
#     def print_LL_reverse(self):
#         print()
#         if self.head is None:
#             print("Linked List is empty!")
#         else:
#             n = self.head 
#             while n.nref is not None:  # Traverse to the last node
#                 n = n.nref
#             while n is not None:  # Traverse backwards
#                 print(n.data, "-->", end="")
#                 n = n.pref
#             print("None")

#     # Insertion in DLL at the beginning
#     def add_begin(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.nref = self.head
#             self.head.pref = new_node
#             self.head = new_node

# # Main program to interact with the user
# dl1 = doublyLL()

# while True:
#     print("\nOptions:")
#     print("1. Add at the beginning")
#     print("2. Print the list (forward)")
#     print("3. Print the list (backward)")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         data = int(input("Enter data: "))
#         dl1.add_begin(data)
#     elif choice == 2:
#         dl1.print_LL()
#     elif choice == 3:
#         dl1.print_LL_reverse()
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice! Please try again.")



# Another Method for adding multiple values at a time
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

    # Insertion in DLL at the beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

# Main program to interact with the user
dl1 = doublyLL()

while True:
    print("\nOptions:")
    print("1. Add at the beginning")
    print("2. Print the list (forward)")
    print("3. Print the list (backward)")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data_input = input("Enter data (comma-separated for multiple values): ")
        data_list = [int(item) for item in data_input.split(',')]
        for data in data_list:
            dl1.add_begin(data)
    elif choice == 2:
        dl1.print_LL()
    elif choice == 3:
        dl1.print_LL_reverse()
    elif choice == 4:
        break
    else:
        print("Invalid choice! Please try again.")