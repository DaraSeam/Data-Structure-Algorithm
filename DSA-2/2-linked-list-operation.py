# linked list operations

#-----------------------create Node-----------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#--------------------create LinkedList--------------------
class LinkedList:
    # create first node which is head ot None
    def __init__(self):
        self.head = None
    
#------------------------insertion------------------------
    # insert element in the beginning
    def insertAtBeginning(self, new_data):
        # allocate memory for new node and store data
        new_node = Node(new_data)
        
        # change next of new node to point to head
        new_node.next = self.head
        
        # change head to point to recently created new_node
        self.head = new_node
    
    # insert at the end
    def insertAtEnd(self, new_data):
        # allocate memory for new_node and store data
        new_node = Node(new_data)

        # check if list is empty, if empty display
        # display data of new_node we just created
        if self.head is None:
            self.head = new_node
            return
        
        # traverse till we reach last node
        # traverse through list by starting from head
        last = self.head
        while (last.next):
            last = last.next
        
        last.next = new_node

#-------------------------Deletion-------------------------
    def deleteNode(self, position):
        # check if there is element in list
        if self.head is None:
            return
        
        temp = self.head
        # check if position is 0
        if position == 0:
            # point head to next node
            self.head = temp.next
            # delete current node
            temp = None
            return
        
        # find the key to be deleted
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
        
        # if the key is not present
        if temp is None:
            return

        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next

#----------------------Search Element----------------------
    def search(self, key):
        # make head as current node
        current = self.head
        while current != None:
            if current.data == key:
                return True
            current = current.next
        
        return False

#----------------------Sort LinkedList---------------------
    def sortLinkedList(self, head):
        # make the head as the current
        current = head
        # create node index for later use
        index = Node(None)
        # if head is None quit 
        if head is None:
            return
        # else loop till we reach last node
        else:
            while current != None:
                # index points to the node next to current
                index = current.next

                while index != None:
                    if current.data > index.data:
                        # swap position
                        current.data, index.data = index.data, current.data
                    # quit while loop
                    index = index.next
                # quit while loop
                current = current.next

#------------------------Print List------------------------
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        # new line
        print()


# create obj
obj = LinkedList()

# insert Node in LinkedList
obj.insertAtBeginning(3)
obj.insertAtBeginning(2)
obj.insertAtBeginning(4)
obj.insertAtBeginning(1)
obj.insertAtEnd(5)
print()
print("Before delete a node: ")
obj.printList()
print()

# delete node in LinkedList
obj.deleteNode(4)
print("After delete a node: ")
obj.printList()
print()

# search LinkedList
itemToFind = 11
print("Item to find is: " +str(itemToFind))
print()

if obj.search(itemToFind):
    print(str(itemToFind)+ " is found in list!")
else:
    print(str(itemToFind)+ " can't be found in list!")
print()

# sort LinkedList
print("Linked List before sort:")
obj.printList()
print()

print("Linked List after sort: ")
obj.sortLinkedList(obj.head)
obj.printList()
