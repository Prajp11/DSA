# Implementation of queue with user input

def main():
    queue = []

    while True:
        print("\nMenu:")
        print("1. Enqueue an element")
        print("2. Dequeue an element")
        print("3. Display the queue")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the value to enqueue: ")
            queue.append(data)
            print(f"Enqueued '{data}' to queue.")
        
        elif choice == '2':
            if len(queue) == 0:
                print("Queue is empty. Nothing to dequeue.")
            else:
                dequeued_element = queue.pop(0)
                print(f"Dequeued '{dequeued_element}' from queue.")
        
        elif choice == '3':
            if len(queue) == 0:
                print("Queue is empty.")
            else:
                print("Current queue:", queue)
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
