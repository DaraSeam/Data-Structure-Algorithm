# linked list 

# creating Node
class Node:
    def __init__(self, item): # construtor of class Node
        self.item = item
        self.next = None

# creating linked list
class LinkedList:

    # create address of first node which is head = None
    def __init__(self): # constructor of class LinkedList
        self.head = None


# create obj linked_list
linked_list = LinkedList()


# assign item values
linked_list.head = Node(1)
second = Node(2)
third = Node(3)



# connect each Node together
linked_list.head.next = second
second.next = third


# print out linked list item
temp = linked_list.head
while temp != None:
    print(temp.item)
    temp = temp.next

