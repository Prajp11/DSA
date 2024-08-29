class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {data} to queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {dequeued_node.data} from queue.")
        return dequeued_node.data

    def get_front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        print(f"Front of queue is {self.front.data}")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        print("Queue elements are:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    queue = Queue()

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
