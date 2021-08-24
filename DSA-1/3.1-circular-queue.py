# circular queue

class CircularQueue():
    # initiailize variable
    def __init__(self, k):
        # no of element in our queue
        self.k = k
        # our queue base on k
        self.queue = [None] * k
        # head & tail to keep track of our CQ index
        self.head = self.tail = -1

    # insert an element into the circular queue
    def enqueue(self, data):

        # check if the circular queue is full
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")
        
        # the first initialize of our data
        elif (self.head == -1):
            # after the first initialize
            # both head and tail to 0
            self.head = 0
            self.tail = 0
            
            # append the first data to our circular queue with tail index
            self.queue[self.tail] = data
        
        # after that we initialize until the 1st cond is true
        else:
            # it doesn't look that complicated
            # it's only get the index of tail :)
            self.tail = (self.tail+1) % self.k
            
            # append data to our circular queue with tail index
            self.queue[self.tail] = data

    # remove element from queue
    def dequeue(self):
        
        # check if queue is empty?
        if self.head == -1:
            print("No element in circular queue\n")
        
        # check if head & tail is at the same index
        # which mean it only has one index left in queue
        # that's why it is at the same index
        elif self.head == self.tail:

            # create temp for element we dequeue from queue using head index
            temp = self.queue[self.head]
            
            # initialize both head & tail to -1
            self.head = -1
            self.tail = -1
            return temp
        
        # if more than one element is in our queue
        else:
            # create temp for element we dequeue from queue using head index
            temp = self.queue[self.head]
            # increment our head by 1 index using modulos
            self.head = (self.head + 1) % self.k
            return temp
        
    # print circular queue
    def printCQueue(self):
        # if there is no element in our queue
        if (self.head == -1):
            print("There is no element in circular queue")
        
        # if tail index >= head index 
        # we return from head index to tail index
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        
        # otherwise, tail index < head index
        else: 
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            print()
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

# create obj
obj = CircularQueue(3)

# enqueue
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
print("Initial queue")
obj.printCQueue()

# dequeue
obj.dequeue()

print("After removing an element from the queue")
obj.printCQueue()