"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""

#function to initialise the node object
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next =next
    
class Solution:
    #function to merge two linked list in ascending order
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        #initialising the variables with objects
        curr = dummy = ListNode()
        #using while loop until atleast on of the linked list exist
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        #after one of the linked list reaches the end node
        if not l1:
            curr.next = l2
        else:
            curr.next = l1

    def print(self):
        itr = self.head
        while itr:
            print(itr.val)
            itr = itr.next
        

