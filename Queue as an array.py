class Queue:
    def __init__(self, capacity):
        # Initialize the queue with a fixed capacity
        self.capacity = capacity
        self.queue = [None] * capacity  # Array to store queue elements
        self.front = 0  # Index of the front of the queue
        self.rear = -1  # Index of the rear of the queue
        self.size = 0   # Current number of elements in the queue

    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0

    def is_full(self):
        # Check if the queue is full
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.queue[self.rear] = data
        self.size += 1
        print(f"Enqueued {data} to queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        data = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot
        self.front = (self.front + 1) % self.capacity  # Circular increment
        self.size -= 1
        print(f"Dequeued {data} from queue.")
        return data

    def get_front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        print(f"Front of queue is {self.queue[self.front]}")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements are:")
        i = self.front
        for _ in range(self.size):
            print(self.queue[i], end=" -> ")
            i = (i + 1) % self.capacity  # Circular increment
        print("None")

def main():
    capacity = int(input("Enter the capacity of the queue: "))
    queue = Queue(capacity)

    while True:
        print("\n1. Enqueue\n2. Dequeue\n3. Get Front\n4. Display\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter value to enqueue: ")
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.get_front()
        elif choice == '4':
            queue.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
