# two kind of heaps
# min heaps & max heaps
#-----------operation-------------
# insertion: there are 2 ways to create or insert a heap:
# 1- top down approach & bottom up approach
# top down approach:
# 1. insert the element to the first available space
# 2. rearrange until heap properties is satisfy based on
# what types of heap you use
# if it is min heap: the children have to be greater than
# it's parent, otherwise we need to rearrange
# the way we swap children with it's parent called UPHEAP BUBBLING

# deletion: we can only delete the root
# replace root with the last element
# rearrange if the heap properties is not satisfiy calld DOWNHEAP BUBBLING
 
# create class MinHeap
class MinHeap: 
    #----------------- constructors ---------------------
    def __init__(self, capacity):
        # capacity: maximum of element we want to store in heap
        self.capacity = capacity
        self.storage = [0]*capacity
    
        # current no. of elements in the heap
        self.size = 0
    
    #---------------- helper methods --------------------
    ##### return index of parent, left child, and right child
    # getParentIndex: to return the parent index
    def getParentIndex(self, index):
        return ((index-1) // 2)

    # getLeftChildIndex: to return the left child index
    def getLeftChildIndex(self, index):
        return ((index*2) + 1)
    
    # getRightChildIndex: to return the right child index
    def getRightChildIndex(self, index):
        return ((index*2) + 2)

    ##### check if a node has a parent, left child, right child
    def hasParent(self, index):
        # index is a node that we want to know whether it
        # has a parent or not
        # we return a boolean whether it has or not
        return self.getParentIndex(index) >= 0
    
    # check if the node have child or not
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    ##### get data from parent, left child, and right child
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    ##### check if the heap is full
    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp


    #------------------ inserting ----------------------
    def insert(self, data):
        # check if heap is full
        if(self.isFull()):
            raise("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        # call heapifyUp function to make sure our data is in right position
        self.heapifyUp(self.size - 1)

    # heapifyUp
    def heapifyUp(self, index):
        # last element of heap
        
        # use while loop to keep walking up the tree
        # we can keep going up the tree as long as we have 
        # parent node hasParent(index)
        # and current parent element is > our current node element
        if (self.hasParent(index) and self.parent(index > self.storage[index])):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

