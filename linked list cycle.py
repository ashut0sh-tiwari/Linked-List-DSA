"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false."""

#function to check if the linked list repeat itself in the loop
class Solution:

    def hasCycle(self, head):
        #initialising the variables 
        slow = fast = head
        #using while loop until fast pointer have the next value
        while fast and fast.next:
            #slow pointer moving one node while fast pointer moving two nodes
            slow = slow.next
            fast = fast.next.next
            #if the values of slow and fast pointers equals then the linked list is repeating itself
            if slow==fast:
                break
        else:
            return None

        #code to know the position of the node from where cycle is repeating
        #making a variable pointing at head
        pointer = head
        #looping until pointer and head are not at the same position
        #fast pointer position is stored from the previous code
        #both pointer moving one step 
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next
        return pointer
        