# Implementation using queue.Queue

from queue import Queue

def main():
    # Set the max size of the queue
    max_size = int(input("Enter the maximum size of the queue: "))
    q = Queue(maxsize=max_size)

    while True:
        print("\nMenu:")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. Check if the queue is full")
        print("4. Check if the queue is empty")
        print("5. Display the current queue size")
        print("6. Exit")
        
        choice = input("Enter your choice: ")


        if choice == '1':
            if q.full():
                print("Queue is full. Cannot enqueue more elements.")
            else:
                data = input("Enter the value to enqueue: ")
                q.put(data)
                print(f"Enqueued '{data}' to the queue.")
        
        elif choice == '2':
            if q.empty():
                print("Queue is empty. Nothing to dequeue.")
            else:
                dequeued_element = q.get()
                print(f"Dequeued '{dequeued_element}' from the queue.")
        
        elif choice == '3':
            if q.full():
                print("The queue is full.")
            else:
                print("The queue is not full.")
        
        elif choice == '4':
            if q.empty():
                print("The queue is empty.")
            else:
                print("The queue is not empty.")
        
        elif choice == '5':
            print(f"The current queue size is: {q.qsize()}")
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()



# from queue import Queue

# Create a queue with a maximum size of 3 --- comment
# q = Queue(maxsize=3)

# Print the current size of the queue (should be 0 initially) --- comment
# print("Initial queue size:", q.qsize())  # Output: 0

# Enqueue (put) elements into the queue --- comment
# q.put('a')
# q.put('b')
# q.put('c')1


# Check if the queue is full --- comment
# print("\nFull:", q.full())  # Output: True

# Dequeue (get) elements from the queue --- comment
# print("\nElements dequeued from the queue:")
# print(q.get())  # Output: 'a'
# print(q.get())  # Output: 'b'
# print(q.get())  # Output: 'c'

# Check if the queue is empty after dequeuing all elements --- comment
# print("\nEmpty:", q.empty())  
# # Output: True --- comment

# Enqueue another element into the queue --- comment
# q.put(1)

# Check if the queue is empty and full after adding one element --- comment
# print("\nEmpty:", q.empty())  # Output: False
# print("Full:", q.full())  # Output: False
