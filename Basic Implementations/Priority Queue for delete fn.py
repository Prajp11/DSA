class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    def isEmpty(self):
        return len(self.queue) == 0
 
    def insert(self, data):
        self.queue.append(data)
 
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()
 
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(10)
    myQueue.insert(5)
    myQueue.insert(20)
    myQueue.insert(15)
    print(myQueue)            
    while not myQueue.isEmpty():
        print(myQueue.delete())
