"""Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head."""


#function to make linked list node object
class ListNode:
    def __init__(self,head,data):
        self.head = head
        self.data = data

# function to remove the node with target value
class Solution:
    def removeElements(self, head:ListNode, val):
        #initialising the variables
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        #using while loop until the curr value exist
        while curr.next:
            #if curr value matches the target value then skip the node
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next