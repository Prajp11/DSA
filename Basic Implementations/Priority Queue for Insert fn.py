class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # Check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # Insert an element in the queue
    def insert(self, data):
        # If the queue is empty, simply append the data
        if self.isEmpty():
            self.queue.append(data)
        else:
            # Find the right place to insert the data
            for i in range(len(self.queue)):
                if data > self.queue[i]:
                    self.queue.insert(i, data)
                    break
            else:
                # If the loop completes, append the data at the end
                self.queue.append(data)
 
    # Delete and return the element with the highest priority (front of the queue)
    def delete(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            print("The queue is empty")
            exit()
 
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(5)
    myQueue.insert(50)
    myQueue.insert(21)
    myQueue.insert(41)
    print(myQueue)  # Should print the queue with elements in descending order
    while not myQueue.isEmpty():
        print(myQueue.delete())
