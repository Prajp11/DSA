# Implementation of queue using collections.deque 

from collections import deque

def main():
    q = deque()

    while True:
        print("\nMenu:")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. Display the queue")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the value to enqueue: ")
            q.append(data)
            print(f"Enqueued '{data}' to the queue.")
        
        elif choice == '2':
            if len(q) == 0:
                print("Queue is empty. Nothing to dequeue.")
            else:
                dequeued_element = q.popleft()
                print(f"Dequeued '{dequeued_element}' from the queue.")
        
        elif choice == '3':
            if len(q) == 0:
                print("Queue is empty.")
            else:
                print("Current queue:", list(q))
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()



# Basic Implementation using collections.deque


# from collections import deque
# q = deque()
# q.append('a')
# q.append('b')
# q.append('c')
# print("Initial queue")
# print(q)
# print("\nElements dequeued from the queue")
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())

# print("\nQueue after removing elements")
# print(q)