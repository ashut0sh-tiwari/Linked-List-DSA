"""Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null."""
#function to check the intersecting common node of the linked lists 
class Solution:
    def getIntersectionNode(self, headA, headB):
        #initialising the variables
        llist1 = headA
        llist2 = headB
        #if one of the linked list is none
        if headA is None or headB is None:
            return None
        
        #using while loop until values of the linked lists does not match 
        #even if they dont match they intersect at end point as they both pointing to null
        while llist1 != llist2:
            #if linked list 1 reaches the end node
            if llist1 == None:
                llist1 = headB
            else:
                llist1 = llist1.next
            #if linked list 2 reaches the end node
            if llist2 == None:
                llist2 = headA
            else:
                llist2 = llist2.next
                
        return llist1
            