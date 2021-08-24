class Queue:

    # create empty list
    def __init__(self):
        self.queue = []
 
    # add element to queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove element from queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
    
    # display queue
    def display(self):
        print(self.queue)

# create obj
q = Queue()

# add element to queue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

# display element before dequeue
print("Item before dequeue: ")
q.display()

# remove element
q.dequeue()
#display element after dequeue
print("Item after dequeue: ")
q.display()

