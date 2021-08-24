# dequeue: double ended queue
class Dequeue:
    def __init__(self):
        self.items = []

    # check if list is empty 
    def isEmpty(self):
        return self.items == []
        
    # add item to Rear
    def addRear(self, item):
        # add item from rear 
        self.items.append(item)
    
    # add item to Front
    def addFront(self, item):
        # add item to index 0 if there is item in front
        # it will push to the next index
        self.items.insert(0, item)

    # remove item from Rear
    def removeRear(self):
        self.items.pop()
    
    # remove item from Front
    def removeFront(self):
        self.items.pop(0)

    # display list of items 
    def display(self):
        print(self.items)

# create obj
q = Dequeue()

# add item to Rear
q.addRear(3)
q.addRear(4)
print("Items after add to rear: ")
q.display()

# add item to Front
q.addFront(2)
q.addFront(1)
print("Items after add to front: ")
q.display()

# remove from rear
q.removeRear()
print("Items after remove from rear: ")
q.display()

# remove from front
q.removeFront()
print("Items after remove from front: ")
q.display()