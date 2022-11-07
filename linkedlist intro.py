# node class
class Node:
    #function to initialise the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
# linked list contain node object
class LinkedList:
    #function to initialise head
    def __init__(self):
        self.head = None

    #function to insert new node at the begining
    def shift(self, data):
        #allocate the node and put in the new data
        new_node = Node(data)
        #make next of the new node as head
        new_node.next = self.head
        #move the head to point to new node
        self.head = new_node

    #function to return the length of the node list
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    #function to insert new node at particular index
    def inserAt(self, index, data):
        #check if the given index exist in node list
        if index<0 or index > self.getLength():
            raise Exception('invalid index')
        #if index is 0
        if index == 0:
            self.shift(data)
            return
        
        #initialising the variables
        itr = self.head
        count = 0
        while itr:
            #stopping index at -1 value to insert new node
            if count == index-1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break
            itr = itr.next
            count +=1

    #function to insert new node at the end
    def append(self, data):
        new_node = Node(data)

        #checking if node list is empty then making new node as head
        if self.head is None:
            self.head = new_node
            return
        
        #transversing till the last node
        itr =self.head
        while itr.next:
            itr = itr.next

        #change the next of last node
        itr.next = new_node

    #function to insert multiple values 
    def insertValues(self, list):
        for data in list:
            self.append(data)

    def deleteNode(self, key):
        #store head node
        itr = self.head

        #if head node itself holds the key to be deleted
        if itr is not None:
            if itr.data == key:
                self.head = itr.next
                itr = None
                return

        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while itr is not None:
            if itr.data == key:
                break
            prev = itr
            itr = itr.next

        # if key was not present in linked list
        if itr == None:
            return

        prev.next = itr.next

        itr = None


    
    #printing the list
    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
    
    

        
#code execution
if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(4)

    llist.head.next = second
    second.next = third

    llist.shift(0)
    # llist.insertAfter(llist.head.next,4)
    llist.inserAt(3,3)
    llist.append(5)
    llist.print()
    print(llist.getLength())
    llist.deleteNode(5)
    llist.print()
    llist.insertValues([5,6,7,8,9,10])
    llist.print()
    
